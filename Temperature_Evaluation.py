#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:36:31 2020

@author: wenninger
"""
import datetime #to be able to define x limits in plots
import matplotlib.pyplot as plt
import pandas as pd
import sys

sys.path.insert(0, '../Helper')
from plotxy import newfig,pltsettings,lbl,plot

filename = '/Users/wenninger/OneDrive - Nexus365/PhD_Oxford/Lab/Jakob_2020_02_18/Temperature_logger/Temperature_Data/2020_02_18_Debug_Warm.txt'

class TemperatureEvaluation():
    '''This class is written to handle and especially plot temperature data from the lakeshore unit.
    '''
    def __init__(self,filename,thermometer_labels = ['T1','T2','T3','T4']):
        '''The initialisation of the class.
        The data is read from the file into a pandas dataset and the first column is converted to a timestamp
        
        inputs
        ------
        filename: string or array
            The name of the file containing the dataset.
        thermometer_labels: array of strings
            The labels of the single thermometers
        '''
        #preserve parameters
        self.filename = filename 
        self.thermometer_labels = thermometer_labels
        
        self.timefmt = "%d/%m/%Y;%H:%M:%S"
        
        #Pandas raw data
        self.data = pd.read_csv(self.filename, sep='\t',engine='python',header=None,skiprows=4,skipfooter=0)
                
        #convert first column to timestamp
        self.data[0] = pd.to_datetime(self.data[0],format=self.timefmt)
        
    def plot_single(self,thermometer_index):
        '''This function plots the temperature of a single thermometer.
        
        inputs
        ------
        thermometer_index: int
            The index of the thermometer to be plotted.
            Note that the first thermometer has the index 1. So the counting starts at 1.
        '''
        try:
            label = self.thermometer_labels[thermometer_index-1]
        except:
            label = None
        # plot
        plt.plot(self.data[0],self.data[thermometer_index],label=label)
        
    def plot_all(self):
        '''This function plots the temperature for all thermometer datasets.
        '''
        for i in range(1,len(self.data.columns)):
            self.plot_single(i)
        
        
    def pltsettings(self,save=None,fileformat='.pdf',disp = True,close=False, xlabel='',ylabel='', xlim=None,
                    ylim=None,title=None,yscale=None,legendColumns=1,skip_legend=False):
        '''This function is a wrapper for the plot settings function imported from the Helper function.
        The wrapper is necessary to format the date axis.
    
        inputs
        ------
        See plotxy.
        Note that the x-limits are required to be of the form
            [datetime.date(2014, 1, 26), datetime.date(2014, 2, 1)]
        '''
        # beautify the x-labels
        plt.gcf().autofmt_xdate()
        pltsettings(save=save,fileformat=fileformat,disp = disp,close=close, xlabel=xlabel,ylabel=ylabel, 
                    xlim=xlim,ylim=ylim,title=title,yscale=yscale,legendColumns=legendColumns,skip_legend=skip_legend)
        
    