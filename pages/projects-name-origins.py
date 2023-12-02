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
import time
import math
import requests
from bs4 import BeautifulSoup
import json



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
    
    
    
n_hidden = 128
rnn = RNN(n_letters, n_hidden, n_categories)





def categoryFromOutput(output):
    top_n, top_i = output.topk(1)
    category_i = top_i[0].item()
    return all_categories[category_i], category_i


def randomChoice(l):
    return l[random.randint(0, len(l) - 1)]

def randomTrainingExample():
    category = randomChoice(all_categories)
    line = randomChoice(category_lines[category])
    category_tensor = torch.tensor([all_categories.index(category)], dtype=torch.long)
    line_tensor = lineToTensor(line)
    return category, line, category_tensor, line_tensor


for i in range(10):
    category, line, category_tensor, line_tensor = randomTrainingExample()
    print('category =', category, '/ line =', line)
    


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



    
    
    
learning_rate = 0.005 # If you set this too high, it might explode. If too low, it might not learn
criterion = nn.NLLLoss()


def train(category_tensor, line_tensor):
    hidden = rnn.initHidden()

    rnn.zero_grad()

    for i in range(line_tensor.size()[0]):
        output, hidden = rnn(line_tensor[i], hidden)

    loss = criterion(output, category_tensor)
    loss.backward()

    # Add parameters' gradients to their values, multiplied by learning rate
    for p in rnn.parameters():
        p.data.add_(p.grad.data, alpha=-learning_rate)

    return output, loss.item()
'''
if __name__ == '__main__':
    predict(sys.argv[1])
'''




def timeSince(since):
    now = time.time()
    s = now - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)

        




dash.register_page(__name__)


layout = html.Div([
    html.H2('This predicts the origin of the name',style={'textAlign': 'center', 'color': '#FF8903'}),
    html.Br(),
    html.Div('This is based on Sean Robert',style={'textAlign':'center'}),
    html.Div('https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html',style={'textAlign':'center'}),
    html.Br(),
    html.Br(),
    html.Div('There are few parameters needed to train: the numer of hidden layers (128 initial size) and learning rate (0.005 initial size)',style={'textAlign':'center'}),
    html.Br(),
    html.Div([html.Label("the number of hidden layers :   "),
             dcc.Input(
             id='n_hidden',
            value=128,
            placeholder=128)],
            style={'textAlign':'center'}),
    html.Div([html.Label("learning rate :   "),
             dcc.Input(
             id='learning_rate',
            value=0.005,
            placeholder=0.005)],
            style={'textAlign':'center'}),
     html.Div([html.Label("iterations :   "),
             dcc.Input(
             id='iterations',
            value=100000,
            placeholder=100000)],
            style={'textAlign':'center'}),
    html.Div(html.Button('Train', id='train', n_clicks=0),style={'textAlign':'center'}),
    html.Div([
        dcc.Loading(id="ls-loading",
                    children=[
                        html.Div(id='output-file',children='Click Train Button')
                    ],
                    type="circle"),]),
    html.Br(),
    html.Div([html.Label("Type your name: "),
             dcc.Input(
             id='name',
            type='text')],
            style={'textAlign':'center'}),
    html.Div(html.Button('Predict', id='predict', n_clicks=0),style={'textAlign':'center'}),
    html.Div([
       dcc.Loading(id="ls-loading1",
                   children=[
                       html.Div(id='output-file1',children='Origin')
                   ],
                   type="circle"),]),
])


@callback(
    Output('ls-loading', 'children'),
    Input('train', component_property='value'),
    [State('n_hidden', component_property='value'),State('learning_rate',component_property='value'),State('iterations',component_property='value')],
    prevent_initial_call=True
)


def update_output(n_clicks,val_hidden, val_rate,val_iter):
    n_hidden = val_hidden
    learning_rate = val_rate
    n_iters = val_iter
    # Keep track of losses for plotting
    current_loss = 0
    all_losses = []
    print('n_hidden: {}'.format(n_hidden))
    print('learning rate: {}'.format(learning_rate))
    print('iterations: {}'.format(n_iters))
    rnn = RNN(n_letters, n_hidden, n_categories)
    
    start = time.time()
    
    
    print_every = 5000
    plot_every = 1000
    
    
    
    for iter in range(1, n_iters + 1):
        category, line, category_tensor, line_tensor = randomTrainingExample()
        output, loss = train(category_tensor, line_tensor)
        current_loss += loss
    
        # Print ``iter`` number, loss, name and guess
        if iter % print_every == 0:
            guess, guess_i = categoryFromOutput(output)
            correct = '✓' if guess == category else '✗ (%s)' % category
            return print('%d %d%% (%s) %.4f %s / %s %s' % (iter, iter / n_iters * 100, timeSince(start), loss, line, guess, correct))
    
        # Add current loss avg to list of losses
        if iter % plot_every == 0:
            all_losses.append(current_loss / plot_every)
            current_loss = 0
            
     
    plt.figure()
    plt.plot(all_losses)

            
        
    return print('done')



@callback(
    Output(component_id='ls-loading1',component_property='children'),
    Input('predict_button',component_property='value'),
    State('name',component_property='value'),
    prevent_initial_call=True
)

def update_input_container(predict_button,name):    
    origin = predict(name)
    return origin


