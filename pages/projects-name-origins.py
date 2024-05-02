# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 22:39:11 2023

@author: brian
"""

#import sys
import torch
import dash
import torch.nn as nn
import os
import glob
import unicodedata
import string
from dash import html,dcc,Input,Output,callback,State




name_path = 'assets/data/data/names/*.txt'
model_path = 'assets/char-rnn-classification.pht'


all_letters = string.ascii_letters + " .,;'"
n_letters = len(all_letters)

def findFiles(name_path): return glob.glob(name_path)
# Turn a Unicode string to plain ASCII, thanks to https://stackoverflow.com/a/518232/2809427

def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in all_letters
    )

# Build the category_lines dictionary, a list of names per language
category_lines = {}
all_categories = []

# Read a file and split into lines
def readLines(filename):
    lines = open(filename, encoding='utf-8').read().strip().split('\n')
    return [unicodeToAscii(line) for line in lines]

for filename in findFiles(name_path):
    category = filename
    all_categories.append(category)
    lines = readLines(filename)
    category_lines[category] = lines

n_categories = len(all_categories)

# Find letter index from all_letters, e.g. "a" = 0
def letterToIndex(letter):
    return all_letters.find(letter)

# Just for demonstration, turn a letter into a <1 x n_letters> Tensor
def letterToTensor(letter):
    tensor = torch.zeros(1, n_letters)
    tensor[0][letterToIndex(letter)] = 1
    return tensor

# Turn a line into a <line_length x 1 x n_letters>,
# or an array of one-hot letter vectors
def lineToTensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)
    for li, letter in enumerate(line):
        tensor[li][0][letterToIndex(letter)] = 1
    return tensor



    

class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()

        self.hidden_size = hidden_size

        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        self.h2o = nn.Linear(hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, input, hidden):
        combined = torch.cat((input, hidden), 1)
        hidden = self.i2h(combined)
        output = self.h2o(hidden)
        output = self.softmax(output)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, self.hidden_size)
    
    
criterion = nn.NLLLoss()
    
n_hidden = 128
rnn = RNN(n_letters, n_hidden, n_categories)

rnn.load_state_dict(torch.load(model_path))
rnn.eval()
print(rnn)


# Just return an output given a line
def evaluate(line_tensor):
    hidden = rnn.initHidden()

    for i in range(line_tensor.size()[0]):
        output, hidden = rnn(line_tensor[i], hidden)

    return output


def predict(line, n_predictions=3):
    with torch.no_grad():
        output = evaluate(lineToTensor(line))
    
        # Get top N categories
        topv, topi = output.topk(n_predictions, 1, True)
        predictions = []
        values = []
        for i in range(n_predictions):
            value = topv[0][i].item()
            category_index = topi[0][i].item()
            print('(%.2f) %s' % (value, all_categories[category_index]))
            values.append(value)
            predictions.append(all_categories[category_index])

    return values,predictions




dash.register_page(__name__)


layout = html.Div([
    html.H2('This predicts the origin of the name',style={'textAlign': 'center', 'color': '#FF8903'}),
    html.Br(),
    html.Div('This is based on Sean Robert',style={'textAlign':'center'}),
    html.Div('https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html',style={'textAlign':'center'}),
    html.Br(),
    html.Br(),
    html.Div([html.Label("Type your name: "),
             dcc.Input(
             id='name',
             #children='Park',
            value='First or last name')],
            style={'textAlign':'center',"margin-left": "15px"}),
    html.Div(html.Button('Predict', id='predict', n_clicks=0),style={'textAlign':'center'}),
    html.Br(),
    html.Div([
       dcc.Loading(id="ls-loading1",
                   children='Type your first or last name and press Enter',
                   type="circle"),],
       style={'textAlign':'center'}),
])



@callback(
    Output(component_id='ls-loading1',component_property='children'),
    Input('predict','n_clicks'),
    State('name',component_property='value'),
    prevent_initial_call=True
)

def update_input_container(n_clicks,value):
    score,pred = predict(value)
    out = ''
    for i in len(pred):
        out = str(score[i]) + ', ' + out + str(pred[i]) + '\n'
    print(out)
    print(type(out))
    return out


