# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 17:03:01 2018

@author: Alfonso Sanchez
"""
'''*********************************************************************************
Importing libraries
*********************************************************************************'''
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FuncFormatter
from matplotlib import rcParams
import pandas as pd
import numpy as np

'''*********************************************************************************
Local functions
*********************************************************************************'''

#Defines format for millions
def millions(x, pos):
    'The two args are the value and tick position'
    return '%1.1fM' % (x*1e-6)

#Defines format for billions
def billions(x, pos):
    'The two args are the value and tick position'
    return '%1.1fB' % (x*1e-9)

#Defines format for trillions
def trillions(x, pos):
    'The two args are the value and tick position'
    return '%1.1fT' % (x*1e-12)


'''*********************************************************************************
Functions to be imported
*********************************************************************************'''

#-----------------------------------------------------------------------------------
#Function to reduce the number of rows of a dataset
#-----------------------------------------------------------------------------------

def ReducingRows(Dataframe, ColumnRef, RowsCondition):
    
    #Finding the indexs to reduce the number of rows, the ones that fullfill
    #the RowsCondition
    RowsSelected = []
    
    for Indice in range(len(RowsCondition)):

        for Index in Dataframe[ColumnRef].index:
        
            if Dataframe[ColumnRef].iloc[Index] == RowsCondition[Indice]:
            
                RowsSelected.append(Index)
                
    Dataframe = Dataframe.iloc[RowsSelected]
    Dataframe.index = range(1,len(Dataframe.index)+1)
            
    return Dataframe


#-----------------------------------------------------------------------------------
#Function to reduce the number of columns in a dataset
#-----------------------------------------------------------------------------------

def ReducingColumns(Dataframe, ColsCondition):
    
    #Finding the indexs to reduce the number of rows, the ones that fullfill
    #the RowsCondition
    DataframeCopy = Dataframe.copy
    
    for Column in DataframeCopy.columns:
        
            if Column == ColsCondition[Col]:
            
                ColumnsSelected.append(Column)
                
    Dataframe = ColumnsSelected 
            
    return Dataframe


#-----------------------------------------------------------------------------------
#Function to plot the NaN values in the selected datasets
#-----------------------------------------------------------------------------------

def PlottingNaN(GDP, Ener_prod, Oil_prod, Gas_prod, NaNIndexs, Columns):
    
    ColsInt = [int(k) for k in Columns[1:]]

    fig = plt.figure(figsize=(15,10))
    ax = fig.add_subplot(221)
    columnas = {}
    for n in NaNIndexs[0]:
        columnas[n+1] = GDP['geo'].iloc[n]
    GDPTemp = GDP.iloc[NaNIndexs[0]].T[1:]        
    GDPTemp.rename(columns=columnas, inplace=True)
    GDPTemp.index = ColsInt
    GDPTemp.plot(ax=plt.gca());
    plt.xlabel('Time')
    plt.ylabel('Dollars')
    plt.title('NaN values in the GDP dataframe')
    plt.grid()

    ax = fig.add_subplot(222)
    columnas = {}    
    for n in NaNIndexs[1]:
        columnas[n+1] = Ener_prod['geo'].iloc[n]
    EnerTemp = Ener_prod.iloc[NaNIndexs[1]].T[1:]
    EnerTemp.rename(columns=columnas, inplace=True)    
    EnerTemp.index = ColsInt
    EnerTemp.plot(ax=plt.gca());
    plt.xlabel('Time')
    plt.ylabel('BOE')
    plt.title('NaN values in the Ener_prod dataframe')
    plt.grid()    

    ax = fig.add_subplot(223)
    columnas = {}    
    for n in NaNIndexs[2]:
        columnas[n+1] = Oil_prod['geo'].iloc[n]
    OilTemp = Oil_prod.iloc[NaNIndexs[2]].T[1:]
    OilTemp.rename(columns=columnas, inplace=True)      
    OilTemp.index = ColsInt
    OilTemp.plot(ax=plt.gca());
    plt.xlabel('Time')
    plt.ylabel('BOE')
    plt.title('NaN values in the Oil_prod dataframe')
    plt.grid()    

    if len(NaNIndexs) > 3:
        ax = fig.add_subplot(224)
        columnas = {}    
        for n in NaNIndexs[3]:
            columnas[n+1] = Gas_prod['geo'].iloc[n]        
        GasTemp = Gas_prod.iloc[NaNIndexs[3]].T[1:]
        GasTemp.rename(columns=columnas, inplace=True)         
        GasTemp.index = ColsInt
        GasTemp.plot(ax=plt.gca());
        plt.xlabel('Time')
        plt.ylabel('BOE')
        plt.title('NaN values in the Gas_prod dataframe')
        plt.grid()        
    

#-----------------------------------------------------------------------------------
#Function to plot the depencencies on hydrocarbons of the north american countries
#-----------------------------------------------------------------------------------

def NorthAmeComparison(GDP, Population, Oil_prod, Ener_prod, Gas_prod, Countries):

    fig = plt.figure(figsize=(15,14))
    formatter = FuncFormatter(millions)
    formatter2 = FuncFormatter(billions)
    formatter3 = FuncFormatter(trillions)
    
    ax = fig.add_subplot(331)
    ax.yaxis.set_major_formatter(formatter)
    A = ax.plot(Population.index.astype('int'),Ener_prod[Countries[0]].values, color='b', label='Energy');
    ax.set_ylabel('Energy (BOE)', fontsize=10);
    axb = ax.twinx()
    axb.yaxis.set_major_formatter(formatter3)
    B = axb.plot(Population.index.astype('int'),GDP[Countries[0]].values, color='r', label='GDP');
    axb.set_ylabel('GDP (Dollars)', fontsize=10);
    C = A + B
    labs = [l.get_label() for l in C]
    axb.legend(C, labs, fontsize=12, loc='upper left')
    plt.title(Countries[0] + ' GDP and Energy relation')
    plt.grid()
    
    ax2 = fig.add_subplot(332)
    ax2.yaxis.set_major_formatter(formatter)
    A = ax2.plot(Population.index.astype('int'),Ener_prod[Countries[0]].values, color='b', label='Energy');
    ax2.set_ylabel('Energy (BOE)', fontsize=10);
    ax2b = ax2.twinx()
    ax2b.yaxis.set_major_formatter(formatter)
    B = ax2b.plot(Population.index.astype('int'),Oil_prod[Countries[0]].values, color='g', label='Oil');
    ax2b.set_ylabel('Oil (BOE)', fontsize=10);
    C = A + B
    labs = [l.get_label() for l in C]
    ax2b.legend(C, labs, fontsize=12, loc='upper left')
    plt.title(Countries[0] + ' Energy and Oil relation')
    plt.grid()
    
    ax2c = fig.add_subplot(333)
    ax2c.yaxis.set_major_formatter(formatter)
    A = ax2c.plot(Population.index.astype('int'),Ener_prod[Countries[0]].values, color='b', label='Energy');
    ax2c.set_ylabel('Energy (BOE)', fontsize=10);
    ax2bc = ax2c.twinx()
    ax2bc.yaxis.set_major_formatter(formatter)
    B = ax2bc.plot(Population.index.astype('int'),Gas_prod[Countries[0]].values, color='m', label='Gas');
    ax2bc.set_ylabel('Gas (BOE)', fontsize=10);
    C = A + B
    labs = [l.get_label() for l in C]
    ax2bc.legend(C, labs, fontsize=12, loc='upper left')
    plt.title(Countries[0] + ' Energy and Gas relation')
    plt.grid()
    
    ax = fig.add_subplot(334)
    ax.yaxis.set_major_formatter(formatter)
    A = ax.plot(Population.index.astype('int'),Ener_prod[Countries[1]].values, color='b', label='Energy');
    ax.set_ylabel('Energy (BOE)', fontsize=10);
    axb = ax.twinx()
    axb.yaxis.set_major_formatter(formatter3)
    B = axb.plot(Population.index.astype('int'),GDP[Countries[1]].values, color='r', label='GDP');
    axb.set_ylabel('GDP (Dollars)', fontsize=10);
    C = A + B
    labs = [l.get_label() for l in C]
    axb.legend(C, labs, fontsize=12, loc='upper left')
    plt.title(Countries[0] + ' GDP and Energy relation')
    plt.grid()
    
    ax2 = fig.add_subplot(335)
    ax2.yaxis.set_major_formatter(formatter)
    A = ax2.plot(Population.index.astype('int'),Ener_prod[Countries[1]].values, color='b', label='Energy');
    ax2.set_ylabel('Energy (BOE)', fontsize=10);
    ax2b = ax2.twinx()
    ax2b.yaxis.set_major_formatter(formatter)
    B = ax2b.plot(Population.index.astype('int'),Oil_prod[Countries[1]].values, color='g', label='Oil');
    ax2b.set_ylabel('Oil (BOE)', fontsize=10);
    C = A + B
    labs = [l.get_label() for l in C]
    ax2b.legend(C, labs, fontsize=12, loc='upper left')
    plt.title(Countries[0] + ' Energy and Oil relation')
    plt.grid()
    
    ax2c = fig.add_subplot(336)
    ax2c.yaxis.set_major_formatter(formatter)
    A = ax2c.plot(Population.index.astype('int'),Ener_prod[Countries[1]].values, color='b', label='Energy');
    ax2c.set_ylabel('Energy (BOE)', fontsize=10);
    ax2bc = ax2c.twinx()
    ax2bc.yaxis.set_major_formatter(formatter)
    B = ax2bc.plot(Population.index.astype('int'),Gas_prod[Countries[1]].values, color='m', label='Gas');
    ax2bc.set_ylabel('Gas (BOE)', fontsize=10);
    C = A + B
    labs = [l.get_label() for l in C]
    ax2bc.legend(C, labs, fontsize=12, loc='upper left')
    plt.title(Countries[0] + ' Energy and Gas relation')
    plt.grid()
    
    ax = fig.add_subplot(337)
    ax.yaxis.set_major_formatter(formatter)
    A = ax.plot(Population.index.astype('int'),Ener_prod[Countries[2]].values, color='b', label='Energy');
    ax.set_ylabel('Energy (BOE)', fontsize=10);
    axb = ax.twinx()
    axb.yaxis.set_major_formatter(formatter3)
    B = axb.plot(Population.index.astype('int'),GDP[Countries[2]].values, color='r', label='GDP');
    axb.set_ylabel('GDP (Dollars)', fontsize=10);
    C = A + B
    labs = [l.get_label() for l in C]
    axb.legend(C, labs, fontsize=12, loc='upper left')
    plt.title(Countries[2]+ ' GDP and Energy relation')
    plt.grid()
    
    ax2 = fig.add_subplot(338)
    ax2.yaxis.set_major_formatter(formatter)
    A = ax2.plot(Population.index.astype('int'),Ener_prod[Countries[2]].values, color='b', label='Energy');
    ax2.set_ylabel('Energy (BOE)', fontsize=10);
    ax2b = ax2.twinx()
    ax2b.yaxis.set_major_formatter(formatter)
    B = ax2b.plot(Population.index.astype('int'),Oil_prod[Countries[2]].values, color='g', label='Oil');
    ax2b.set_ylabel('Oil (BOE)', fontsize=10);
    C = A + B
    labs = [l.get_label() for l in C]
    ax2b.legend(C, labs, fontsize=12, loc='upper left')
    plt.title(Countries[2] + ' Energy and Oil relation')
    plt.grid()
    
    ax2c = fig.add_subplot(339)
    ax2c.yaxis.set_major_formatter(formatter)
    A = ax2c.plot(Population.index.astype('int'),Ener_prod[Countries[2]].values, color='b', label='Energy');
    ax2c.set_ylabel('Energy (BOE)', fontsize=10);
    ax2bc = ax2c.twinx()
    ax2bc.yaxis.set_major_formatter(formatter)
    B = ax2bc.plot(Population.index.astype('int'),Gas_prod[Countries[2]].values, color='m', label='Gas');
    ax2bc.set_ylabel('Gas (BOE)', fontsize=10);
    C = A + B
    labs = [l.get_label() for l in C]
    ax2bc.legend(C, labs, fontsize=12, loc='upper left')
    plt.title(Countries[2] + ' Energy and Gas relation')
    plt.grid()
    
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=.65, hspace=.3)
    

#-----------------------------------------------------------------------------------
#Function create merged pd df for the NA countries correlations
#-----------------------------------------------------------------------------------

def CorreDataFrames(Dataframes, FramesLab):
    
    DataDict = {}
    for n in range(len(Dataframes)):
        DataDict[FramesLab[n]] = Dataframes[n]
        
    return pd.DataFrame(DataDict)

#-----------------------------------------------------------------------------------
#Function to plot North american countries correlations
#-----------------------------------------------------------------------------------

def CountriesNortAmeCorr(CorrUS, CorrCA, CorrMX, FramesLab):

    rcParams['axes.titlepad'] = 8
    
    fig = plt.figure(figsize=(15,15))
    
    ax = fig.add_subplot(321)
    ax = plt.imshow(np.abs(np.corrcoef(CorrUS.T.values)), cmap='jet')
    plt.yticks(range(4), FramesLab, color='k')
    plt.xticks(range(4), FramesLab, color='k')
    plt.xticks(rotation=90);
    plt.title('Correlations for US', fontsize=12);
    plt.clim(0,1)
    plt.colorbar()
    
    ax = fig.add_subplot(322)
    ax = plt.imshow(np.abs(np.corrcoef(CorrCA.T.values)), cmap='jet')
    plt.yticks(range(4), FramesLab, color='k')
    plt.xticks(range(4), FramesLab, color='k')
    plt.xticks(rotation=90);
    plt.title('Correlations for CA', fontsize=12);
    plt.clim(0,1)
    plt.colorbar()
    
    ax = fig.add_subplot(323)
    ax = plt.imshow(np.abs(np.corrcoef(CorrMX.T.values)), cmap='jet')
    plt.yticks(range(4), FramesLab, color='k')
    plt.xticks(range(4), FramesLab, color='k')
    plt.xticks(rotation=90);
    plt.title('Correlations for MX', fontsize=12);
    plt.clim(0,1)
    plt.colorbar()
    
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=.5)
    
#-----------------------------------------------------------------------------------
#Function to visualiza relation between the GDP per capita and the Energy per capita
#-----------------------------------------------------------------------------------

def NorthAmeComparisonPC(GDPpc, Population, Ener_prodpc, Countries):

    rcParams['axes.titlepad'] = 30 

    fig = plt.figure(figsize=(15,5))
    formatter = FuncFormatter(millions)

    
    ax = fig.add_subplot(131)
    A = ax.plot(GDPpc[Countries[0]],Ener_prodpc[Countries[0]], '*g', label='GDP vs Energy');
    ax.set_ylabel('Energy (TOE)', fontsize=10);
    ax.set_xlabel('GDP (Dollars)', fontsize=10);
    axb = ax.twiny().twinx()
    axb.yaxis.set_major_formatter(formatter)
    B = axb.plot(Population.index.astype('int'),Population[Countries[0]].values, 'r', label='Population');
    axb.set_ylabel('Population', fontsize=10);
    axb.set_xlabel('Time', fontsize=10);
    C = A + B
    labs = [l.get_label() for l in C]
    axb.legend(C, labs, fontsize=12, loc='upper left')
    plt.title(Countries[0] + ' GDP and Energy relation')
    plt.grid()
    
    ax2 = fig.add_subplot(132)
    A = ax2.plot(GDPpc[Countries[1]],Ener_prodpc[Countries[1]].values, '*g', label='GDP vs Energy');
    ax2.set_ylabel('Energy (TOE)', fontsize=10);
    ax2.set_xlabel('GDP (Dollars)', fontsize=10);
    ax2b = ax2.twiny().twinx()
    ax2b.yaxis.set_major_formatter(formatter)
    B = ax2b.plot(Population.index.astype('int'),Population[Countries[1]].values, color='r', label='Population');
    ax2b.set_ylabel('Population', fontsize=10);
    C = A + B
    labs = [l.get_label() for l in C]
    ax2b.legend(C, labs, fontsize=12, loc='upper left')
    plt.title(Countries[1] + ' GDP and Energy relation')
    plt.grid()
    
    ax2c = fig.add_subplot(133)
    A = ax2c.plot(GDPpc[Countries[2]],Ener_prodpc[Countries[2]].values, '*g', label='GDP vs Energy');
    ax2c.set_ylabel('Energy (TOE)', fontsize=10);
    ax2c.set_xlabel('GDP (Dollars)', fontsize=10);
    ax2bc = ax2c.twiny().twinx()
    ax2bc.yaxis.set_major_formatter(formatter)
    B = ax2bc.plot(Population.index.astype('int'),Population[Countries[2]].values, color='r', label='Population');
    ax2bc.set_ylabel('Population', fontsize=10);
    C = A + B
    labs = [l.get_label() for l in C]
    ax2bc.legend(C, labs, fontsize=12, loc='upper left')
    plt.title(Countries[2] + ' GDP and Energy relation')
    plt.grid()
    
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=.65, hspace=.5)
    
#-----------------------------------------------------------------------------------
#Function plot the GDO pc and the Ener pc considering the hydrocarbons produced
#-----------------------------------------------------------------------------------

def NorthAmeComparisonPC_Oil(GDPpc, Oil_prod, Ener_prodpc, Countries):

    rcParams['axes.titlepad'] = 30 

    fig = plt.figure(figsize=(15,5))
    formatter = FuncFormatter(millions)

    
    ax = fig.add_subplot(131)
    A = ax.plot(GDPpc[Countries[0]],Ener_prodpc[Countries[0]], '*g', label='GDP vs Energy');
    ax.set_ylabel('Energy (TOE)', fontsize=10);
    ax.set_xlabel('GDP (Dollars)', fontsize=10);
    axb = ax.twiny().twinx()
    axb.yaxis.set_major_formatter(formatter)
    B = axb.plot(Oil_prod.index.astype('int'),Oil_prod[Countries[0]].values, 'b', label='Hydrocarbons');
    axb.set_ylabel('Hydrocarbons (TOE)', fontsize=10);
    axb.set_xlabel('Time', fontsize=10);
    C = A + B
    labs = [l.get_label() for l in C]
    axb.legend(C, labs, fontsize=12, loc='upper left')
    plt.title(Countries[0] + ' GDP and Energy relation')
    plt.grid()
    
    ax2 = fig.add_subplot(132)
    A = ax2.plot(GDPpc[Countries[1]],Ener_prodpc[Countries[1]].values, '*g', label='GDP vs Energy');
    ax2.set_ylabel('Energy (TOE)', fontsize=10);
    ax2.set_xlabel('GDP (Dollars)', fontsize=10);
    ax2b = ax2.twiny().twinx()
    ax2b.yaxis.set_major_formatter(formatter)
    B = ax2b.plot(Oil_prod.index.astype('int'),Oil_prod[Countries[1]].values, color='b', label='Hydrocarbons');
    ax2b.set_ylabel('Hydrocarbons (TOE)', fontsize=10);
    C = A + B
    labs = [l.get_label() for l in C]
    ax2b.legend(C, labs, fontsize=12, loc='upper left')
    plt.title(Countries[1] + ' GDP and Energy relation')
    plt.grid()
    
    ax2c = fig.add_subplot(133)
    A = ax2c.plot(GDPpc[Countries[2]],Ener_prodpc[Countries[2]].values, '*g', label='GDP vs Energy');
    ax2c.set_ylabel('Energy (TOE)', fontsize=10);
    ax2c.set_xlabel('GDP (Dollars)', fontsize=10);
    ax2bc = ax2c.twiny().twinx()
    ax2bc.yaxis.set_major_formatter(formatter)
    B = ax2bc.plot(Oil_prod.index.astype('int'),Oil_prod[Countries[2]].values, color='b', label='Hydrocarbons');
    ax2bc.set_ylabel('Hydrocarbons (TOE)', fontsize=10);
    C = A + B
    labs = [l.get_label() for l in C]
    ax2bc.legend(C, labs, fontsize=12, loc='upper left')
    plt.title(Countries[2] + ' GDP and Energy relation')
    plt.grid()
    
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=.65, hspace=.5)    

    
'''*********************************************************************************
Fin
*********************************************************************************'''    