#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 22:09:50 2017

@author: Nengen
"""

#Data preprocessing

#Importing the libraries
import numpy as numpy
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,:3].values

#taking care of missing data
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer.fit(x[: , 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])
numpy.set_printoptions(threshold=numpy.nan)