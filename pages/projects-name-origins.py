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
import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from dash import html,dcc,Input,Output,callback,State
import plotly.express as px
import math
import requests
from bs4 import BeautifulSoup
import json

print(os.listdir('assets'))

def listNames(path): 
    names = []
    x = requests.get(path)
    soup = BeautifulSoup(x.content, 'html.parser')
    print(soup.get_text())
    texts = json.loads(soup.get_text())
    
    for i in range(len(list(texts.items())[0][1]['tree']['items'])):
        lists = list(texts.items())[0][1]['tree']['items'][i]['name']
        names.append(lists)
        
    return names

path = 'https://github.com/kpark11/Our-website/tree/main/assets/data/data/names/'
model_path = 'assets/char-rnn-classification.pht'


all_letters = string.ascii_letters + " .,;'"
n_letters = len(all_letters)


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
    filename = path + filename
    x = requests.get(filename)
    soup = BeautifulSoup(x.content, 'html.parser')
    texts = json.loads(soup.get_text())
    lines = texts['payload']['blob']['rawLines']
    return lines #[unicodeToAscii(texts) for line in texts]

for filename in listNames(path):
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


# Just return an output given a line
def evaluate(line_tensor):
    hidden = rnn.initHidden()

    for i in range(line_tensor.size()[0]):
        output, hidden = rnn(line_tensor[i], hidden)

    return output


def predict(line, n_predictions=3):
    output = evaluate(lineToTensor(line))

    # Get top N categories
    topv, topi = output.data.topk(n_predictions, 1, True)
    predictions = []

    for i in range(n_predictions):
        value = topv[0][i]
        category_index = topi[0][i]
        print('(%.2f) %s' % (value, all_categories[category_index]))
        predictions.append([value, all_categories[category_index]])

    return predictions




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
            type='text')],
            style={'textAlign':'center'}),
    html.Div(html.Button('Predict', id='predict', n_clicks=0),style={'textAlign':'center'}),
    html.Div([
       dcc.Loading(id="ls-loading1",
                   children=[
                       html.Div(id='output-file1',children='Origin',style={'textAlign':'center'})
                   ],
                   type="circle"),]),
])



@callback(
    Output(component_id='ls-loading1',component_property='children'),
    Input('predict_button',component_property='value'),
    State('name',component_property='value'),
    prevent_initial_call=True
)

def update_input_container(value,name):    
    origin = predict(name)
    return origin


