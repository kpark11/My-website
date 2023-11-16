# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 22:39:11 2023

@author: brian
"""

#import sys
import torch
import dash
import torch.nn as nn
import unicodedata
import string

from dash import html,dcc,Input,Output,callback




dash.register_page(__name__)




layout = html.Div([
    html.H2('This predicts the origin of the name',style={'textAlign': 'center', 'color': '#FF8903'}),
    html.Br(),
    html.Div('This is based on Sean Robert https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html',style={'textAlign':'center'}),
    html.Br(),
    html.Div([html.Label("Type your name: "),
             dcc.Input(
             id='input',
            value=0,
            placeholder=0)],
            style={'textAlign':'center'}),
     html.Div([
        dcc.Loading(id="ls-loading",
                    children=[
                        html.Div(id='output-file',className='file',style={'display':'flex'})
                    ],
                    type="circle"),]),
])

@callback(
    Output(component_id='ls-loading',component_property='children'),
    Input('input',component_property='value')
)

def update_input_container(name):    
    origin = predict(name)
    return origin


rnn = torch.load(r'https://github.com/kpark11/Our-website/tree/main/assets/char-rnn-classification.pt?raw=true')


all_letters = string.ascii_letters + " .,;'"
n_letters = len(all_letters)
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


category_lines = {}
all_categories = []
n_categories = len(all_categories)
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
'''
if __name__ == '__main__':
    predict(sys.argv[1])
'''


