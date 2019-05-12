
# Investigate a Dataset

## Hydrocarbons dependencies and purchase power for North America

### *Udacity Data Analysis Nanodegree*

## Table of Contents
<ul>
<li><a href="#Intro">Introduction</a></li>
<li><a href="#Objective">Objective</a></li>
<li><a href="#wrangling">Data Wrangling</a></li>
<li><a href="#eda">Exploratory Data Analysis</a></li>
<li><a href="#conclusions">Conclusions</a></li>
</ul>

<a id='Intro'></a>
## Introduction

For most countries, their economies growth reflects the quality of life of their citizens, in terms of their acquisition power. Nonetheless, the GDP per capita is expected to be directly related with the amount of energy that each of their citizens can use to generate capital, and therefore, with the amount of hydrocarbons produced to generate energy. This is the importance to fully understand that relationship, to analyze the dependency that remains on the hydrocarbons to increase the economic growth for most of the countries.


<a id='Objective'></a>
## Objective <a class="anchor" id="objective"></a>


The goal of this project is to present a detailed analysis of the North America countries dependencies to the use of hydrocarbons for the increment of their economies and their quality of lives. For this, data obtained from many countries were used, related with their GDPs, populations, production of hydrocarbons and use of energy. 

To be more specific, the objective of this project is to show how related are the GDP and the use of energy, based on the production of hydrocarbons, for the North America countries. Additionally, to show how much acquisition power their citizens have based on the amount of energy produced, considering the GDP per capita as their acquisition power.  

Information about the mentioned variables were obtained from the updated https://www.gapminder.org/data/ data. Data associated with the production of hydrocarbons and use of energy are presented as tones of barrels of equivalent oil (TOE), while data related with the GDP is presented as international dollars (Dollars).


<a id='wrangling'></a>
## Data Wrangling

The data is imported as Pandas dataframes, obtained from the previosly mentioned webpage. The names of files obtained can be observed when loading the data in *csv* format.

### Importing libraries and loading the data for the analysis


```python
#Importing libraries to be used in the analysis
import pandas as pd
import os
import numpy as np
import matplotlib.pylab as plt

#Finding the path were the data is stored
path = os.path.join(os.getcwd(),'Data')

#Loading data obtained for the analysis
Population = pd.read_csv(os.path.join(path,'population_total.csv'))
GDP = pd.read_csv(os.path.join(path,'total_gdp_us_inflation_adjusted.csv'))
Oil_prod = pd.read_csv(os.path.join(path,'oil_production_total.csv'))
Gas_prod = pd.read_csv(os.path.join(path,'natural_gas_production_total.csv'))
Ener_use = pd.read_csv(os.path.join(path,'energy_use_total.csv'))
```

Example of the loaded data:


```python
GDP.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>geo</th>
      <th>1960</th>
      <th>1961</th>
      <th>1962</th>
      <th>1963</th>
      <th>1964</th>
      <th>1965</th>
      <th>1966</th>
      <th>1967</th>
      <th>1968</th>
      <th>...</th>
      <th>2008</th>
      <th>2009</th>
      <th>2010</th>
      <th>2011</th>
      <th>2012</th>
      <th>2013</th>
      <th>2014</th>
      <th>2015</th>
      <th>2016</th>
      <th>2017</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>1.210000e+10</td>
      <td>1.470000e+10</td>
      <td>1.590000e+10</td>
      <td>1.690000e+10</td>
      <td>1.940000e+10</td>
      <td>2.010000e+10</td>
      <td>2.060000e+10</td>
      <td>2.090000e+10</td>
      <td>2.140000e+10</td>
      <td>2.200000e+10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>1.110000e+10</td>
      <td>1.150000e+10</td>
      <td>1.190000e+10</td>
      <td>1.220000e+10</td>
      <td>1.240000e+10</td>
      <td>1.250000e+10</td>
      <td>1.280000e+10</td>
      <td>1.300000e+10</td>
      <td>1.350000e+10</td>
      <td>1.400000e+10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Algeria</td>
      <td>2.740000e+10</td>
      <td>2.370000e+10</td>
      <td>1.900000e+10</td>
      <td>2.560000e+10</td>
      <td>2.710000e+10</td>
      <td>2.870000e+10</td>
      <td>2.740000e+10</td>
      <td>2.990000e+10</td>
      <td>3.320000e+10</td>
      <td>...</td>
      <td>1.530000e+11</td>
      <td>1.560000e+11</td>
      <td>1.610000e+11</td>
      <td>1.660000e+11</td>
      <td>1.710000e+11</td>
      <td>1.760000e+11</td>
      <td>1.830000e+11</td>
      <td>1.900000e+11</td>
      <td>1.960000e+11</td>
      <td>1.990000e+11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Andorra</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>3.680000e+09</td>
      <td>3.550000e+09</td>
      <td>3.360000e+09</td>
      <td>3.200000e+09</td>
      <td>3.150000e+09</td>
      <td>3.160000e+09</td>
      <td>3.230000e+09</td>
      <td>3.260000e+09</td>
      <td>3.320000e+09</td>
      <td>3.380000e+09</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Angola</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>7.790000e+10</td>
      <td>7.980000e+10</td>
      <td>8.250000e+10</td>
      <td>8.570000e+10</td>
      <td>9.020000e+10</td>
      <td>9.630000e+10</td>
      <td>1.010000e+11</td>
      <td>1.040000e+11</td>
      <td>1.030000e+11</td>
      <td>1.040000e+11</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Antigua and Barbuda</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>1.410000e+09</td>
      <td>1.240000e+09</td>
      <td>1.150000e+09</td>
      <td>1.130000e+09</td>
      <td>1.170000e+09</td>
      <td>1.170000e+09</td>
      <td>1.230000e+09</td>
      <td>1.280000e+09</td>
      <td>1.340000e+09</td>
      <td>1.390000e+09</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Argentina</td>
      <td>1.160000e+11</td>
      <td>1.220000e+11</td>
      <td>1.210000e+11</td>
      <td>1.140000e+11</td>
      <td>1.260000e+11</td>
      <td>1.390000e+11</td>
      <td>1.380000e+11</td>
      <td>1.430000e+11</td>
      <td>1.500000e+11</td>
      <td>...</td>
      <td>4.090000e+11</td>
      <td>3.850000e+11</td>
      <td>4.240000e+11</td>
      <td>4.490000e+11</td>
      <td>4.440000e+11</td>
      <td>4.550000e+11</td>
      <td>4.440000e+11</td>
      <td>4.560000e+11</td>
      <td>4.480000e+11</td>
      <td>4.600000e+11</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Armenia</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>1.060000e+10</td>
      <td>9.060000e+09</td>
      <td>9.260000e+09</td>
      <td>9.700000e+09</td>
      <td>1.040000e+10</td>
      <td>1.070000e+10</td>
      <td>1.110000e+10</td>
      <td>1.150000e+10</td>
      <td>1.150000e+10</td>
      <td>1.240000e+10</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Australia</td>
      <td>1.990000e+11</td>
      <td>2.040000e+11</td>
      <td>2.070000e+11</td>
      <td>2.200000e+11</td>
      <td>2.350000e+11</td>
      <td>2.490000e+11</td>
      <td>2.550000e+11</td>
      <td>2.710000e+11</td>
      <td>2.850000e+11</td>
      <td>...</td>
      <td>1.100000e+12</td>
      <td>1.120000e+12</td>
      <td>1.140000e+12</td>
      <td>1.170000e+12</td>
      <td>1.220000e+12</td>
      <td>1.250000e+12</td>
      <td>1.280000e+12</td>
      <td>1.310000e+12</td>
      <td>1.350000e+12</td>
      <td>1.380000e+12</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Austria</td>
      <td>9.180000e+10</td>
      <td>9.690000e+10</td>
      <td>9.950000e+10</td>
      <td>1.040000e+11</td>
      <td>1.100000e+11</td>
      <td>1.140000e+11</td>
      <td>1.200000e+11</td>
      <td>1.240000e+11</td>
      <td>1.290000e+11</td>
      <td>...</td>
      <td>4.000000e+11</td>
      <td>3.850000e+11</td>
      <td>3.920000e+11</td>
      <td>4.030000e+11</td>
      <td>4.060000e+11</td>
      <td>4.060000e+11</td>
      <td>4.100000e+11</td>
      <td>4.140000e+11</td>
      <td>4.200000e+11</td>
      <td>4.330000e+11</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 59 columns</p>
</div>



As can be observed, the loaded data contains more countries than the required and undefined values which increase the uncertainty of the analysis. Moreover, the loaded dataframes do not possess information for the same dates or the same countries, as can be observed by getting the shapes and the number of *nan* values for each of the generated dataframes:


```python
Dataframes = [GDP, Population, Ener_use, Oil_prod, Gas_prod]
Names = ['GDP', 'Population', 'Ener_use', 'Oil_prod', 'Gas_prod']
NanVals = [GDP.isnull().values.sum(), Population.isnull().values.sum(), Ener_use.isnull().values.sum(),
           Oil_prod.isnull().values.sum(), Gas_prod.isnull().values.sum()]

Structures = np.zeros(shape=(5,3), dtype=int)
for n in range(len(Dataframes)):
    Structures[n,:] = [Dataframes[n].shape[0], Dataframes[n].shape[1], NanVals[n]]
    
display(pd.DataFrame({'Dataframe':Names,'Countries':Structures[:,0],'Dates':Structures[:,1],'NaN':Structures[:,2]}))

```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dataframe</th>
      <th>Countries</th>
      <th>Dates</th>
      <th>NaN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GDP</td>
      <td>190</td>
      <td>59</td>
      <td>2481</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Population</td>
      <td>195</td>
      <td>220</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ener_use</td>
      <td>275</td>
      <td>53</td>
      <td>8920</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Oil_prod</td>
      <td>49</td>
      <td>53</td>
      <td>318</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Gas_prod</td>
      <td>49</td>
      <td>48</td>
      <td>90</td>
    </tr>
  </tbody>
</table>
</div>


Then, a reduction of the loaded data and the nan values is required. 

### Reducing the amount of data (rows)

The amount of data is reduced by focusing the analysis on the twenty countries with more GDP during the most recent date of the data obtained (2017), which includes the countries of interest. The countries with most GDP are found by a descending sorting of the GDP dataframe values for the 2017 date column.

Once the data was sorted, a vector with the names of the 20 countries with more GDP during 2017 is created, to be used as indices to filter the data of the rest of the created datasets.



```python
#Importing custom function to reduce the number of rows in the generated dataframes
from Functions import ReducingRows

Indices = GDP.sort_values(['2017'],axis=0,ascending=0).index[0:33]
Countries = GDP['geo'].iloc[Indices].values

Oil_prod = ReducingRows(Oil_prod, 'geo', Countries)
Population = ReducingRows(Population, 'geo', Oil_prod['geo'].values)
Gas_prod = ReducingRows(Gas_prod, 'geo', Oil_prod['geo'].values)
Ener_use = ReducingRows(Ener_use, 'geo', Oil_prod['geo'].values)
GDP = ReducingRows(GDP, 'geo', Oil_prod['geo'].values)

```

Then, the dataframes have the following structures:


```python
Dataframes = [GDP, Population, Ener_use, Oil_prod, Gas_prod]
Names = ['GDP', 'Population', 'Ener_use', 'Oil_prod', 'Gas_prod']

Structures = np.zeros(shape=(5,2), dtype=int)
for n in range(len(Dataframes)):
    Structures[n,:] = [Dataframes[n].shape[0], Dataframes[n].shape[1]]
    
display(pd.DataFrame({'Dataframe':Names,'Countries':Structures[:,0],'Dates':Structures[:,1]}))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dataframe</th>
      <th>Countries</th>
      <th>Dates</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GDP</td>
      <td>20</td>
      <td>59</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Population</td>
      <td>20</td>
      <td>220</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ener_use</td>
      <td>20</td>
      <td>53</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Oil_prod</td>
      <td>20</td>
      <td>53</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Gas_prod</td>
      <td>20</td>
      <td>48</td>
    </tr>
  </tbody>
</table>
</div>


### Reducing the amount of data (columns)

The range of columns used are reduced by discarding those which are not found in all the generated datasets.


```python
#Getting the Dataframes columns
Cols1 = np.array(GDP.columns)
Cols2 = np.array(Population.columns)
Cols3 = np.array(Oil_prod.columns)
Cols4 = np.array(Gas_prod.columns)
Cols5 = np.array(Ener_use.columns)

#Comparing columns among the dataframes and selecting the ones to be used for the analysis
Columns = [Col for Col in Cols1 if (Col in Cols2) and (Col in Cols3) and (Col in Cols4) and (Col in Cols5)]

#Reduing columns in the dataframes
GDP = GDP[Columns]
Oil_prod = Oil_prod[Columns]
Gas_prod = Gas_prod[Columns]
Ener_use = Ener_use[Columns]
Population = Population[Columns]
```

Then, the dataframes have the following structures:


```python
Dataframes = [GDP, Population, Ener_use, Oil_prod, Gas_prod]
Names = ['GDP', 'Population', 'Ener_use', 'Oil_prod', 'Gas_prod']

Structures = np.zeros(shape=(5,2), dtype=int)
for n in range(len(Dataframes)):
    Structures[n,:] = [Dataframes[n].shape[0], Dataframes[n].shape[1]]
    
display(pd.DataFrame({'Dataframe':Names,'Countries':Structures[:,0],'Dates':Structures[:,1]}))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dataframe</th>
      <th>Countries</th>
      <th>Dates</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GDP</td>
      <td>20</td>
      <td>43</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Population</td>
      <td>20</td>
      <td>43</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ener_use</td>
      <td>20</td>
      <td>43</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Oil_prod</td>
      <td>20</td>
      <td>43</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Gas_prod</td>
      <td>20</td>
      <td>43</td>
    </tr>
  </tbody>
</table>
</div>


### Managing the not defined values

The handling of the not defined values is implemented in three steps, after finding the indices of the *nan* values for each of the generated data frames.


```python
#Finding the indices of the nan values on each of the dataframes
GDPnan = GDP.index[GDP.isnull().any(axis=1)==True]-1
Popnan = Population.index[Population.isnull().any(axis=1)==True]-1
Enernan = Ener_use.index[Ener_use.isnull().any(axis=1)==True]-1
Oilnan = Oil_prod.index[Oil_prod.isnull().any(axis=1)==True]-1
Gasnan = Gas_prod.index[Gas_prod.isnull().any(axis=1)==True]-1

```

First, each of the rows containing undefined values are plotted to understand their effect. 


```python
#Importing libraries and custom functions
import matplotlib.pylab as plt
from Functions import PlottingNaN
%matplotlib inline  

NaNIndexs = [GDPnan, Enernan, Oilnan, Gasnan]

PlottingNaN(GDP, Ener_use, Oil_prod, Gas_prod, NaNIndexs, Columns)
```


![png](output_23_0.png)


Then, data related with countries that are affected greatly by the presence of *nan* values are discarded. As can be seen in the previous figure, data related with *Russia* presents not defined values in each of the dataframes. What is more important, it presents a considerable amount of not defined values in most of the dataframes. As result, data related with that country will be dropped to reduce uncertainty related with calculations using that data.


```python
#Dropping data related with Russia
GDP.drop([8], inplace=True)
Ener_use.drop([8], inplace=True)
Oil_prod.drop([8], inplace=True)
Gas_prod.drop([8], inplace=True)
Population.drop([8], inplace=True)
```

The rest of the not defined values will be replaced using adjacent data found on each of their corresponding rows. This is possible using the *pandas* *fillna* function.


```python
#Filling nan values with adjacent data in the same rows
GDP[Columns[1:]] = GDP[Columns[1:]].fillna(method='bfill',axis=1)
Oil_prod[Columns[1:]] = Oil_prod[Columns[1:]].fillna(method='bfill',axis=1)
Ener_use[Columns[1:]] = Ener_use[Columns[1:]].fillna(method='ffill',axis=1)
Ener_use[Columns[1:]] = Ener_use[Columns[1:]].fillna(method='bfill',axis=1)

```

The modified dataframes do not present *nan* values:


```python
Names = ['GDP', 'Population', 'Ener_use', 'Oil_prod', 'Gas_prod']
NanVals = [GDP.isnull().values.sum(), Population.isnull().values.sum(), Ener_use.isnull().values.sum(),
           Oil_prod.isnull().values.sum(), Gas_prod.isnull().values.sum()]

Structures = np.zeros(shape=(5,3), dtype=int)
for n in range(len(Dataframes)):
    Structures[n,:] = [Dataframes[n].shape[0], Dataframes[n].shape[1], NanVals[n]]
    
display(pd.DataFrame({'Dataframe':Names,'NaN':Structures[:,2]}))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Dataframe</th>
      <th>NaN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GDP</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Population</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ener_use</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Oil_prod</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Gas_prod</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>


### Conditioning the dataframes

Renaming the daframes Indices and Columns is important to have a better understanding of the data visualization, applied in the next section.


```python
#Renamig columns
RenamingCols = {}

index = 0   
for n in GDP['geo'].values:
    RenamingCols[GDP.index[index]] = n
    index+=1    
    
GDP = GDP[Columns[1:]].T.rename(columns=RenamingCols)
Ener_use = Ener_use[Columns[1:]].T.rename(columns=RenamingCols)
Oil_prod = Oil_prod[Columns[1:]].T.rename(columns=RenamingCols)
Gas_prod = Gas_prod[Columns[1:]].T.rename(columns=RenamingCols)
Population = Population[Columns[1:]].T.rename(columns=RenamingCols)

#Renaming rows
GDP.index = GDP.index.astype('int')
Population.index = Population.index.astype('int')
Ener_use.index = Ener_use.index.astype('int')
Oil_prod.index = Oil_prod.index.astype('int')

```

### Generating additional dataframes

Additional dataframes are required to measure the effects of the increment of the North American economies and the use of energy per citizen:


```python
#Creating additional dataframes
GDP_percap = GDP.div(Population)
Ener_percap = Ener_use.div(Population)

#Renaming their rows
Gas_prod.index = Gas_prod.index.astype('int')
GDP_percap.index = GDP_percap.index.astype('int')
```

Example of a proprocessed dataframe:

### Example


```python
GDP_percap.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>United States</th>
      <th>China</th>
      <th>United Kingdom</th>
      <th>India</th>
      <th>Brazil</th>
      <th>Italy</th>
      <th>Canada</th>
      <th>Australia</th>
      <th>Mexico</th>
      <th>Indonesia</th>
      <th>Saudi Arabia</th>
      <th>Iran</th>
      <th>Norway</th>
      <th>Argentina</th>
      <th>Nigeria</th>
      <th>Thailand</th>
      <th>United Arab Emirates</th>
      <th>Colombia</th>
      <th>Malaysia</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1970</th>
      <td>22761.904762</td>
      <td>226.666667</td>
      <td>17949.640288</td>
      <td>364.620939</td>
      <td>4711.437566</td>
      <td>17723.880597</td>
      <td>24418.604651</td>
      <td>25546.875000</td>
      <td>5384.615385</td>
      <td>770.434783</td>
      <td>22089.041096</td>
      <td>7017.543860</td>
      <td>32216.494845</td>
      <td>7041.666667</td>
      <td>1616.071429</td>
      <td>929.539295</td>
      <td>241702.127660</td>
      <td>2755.656109</td>
      <td>1916.666667</td>
    </tr>
    <tr>
      <th>1971</th>
      <td>23412.322275</td>
      <td>236.686391</td>
      <td>18458.781362</td>
      <td>362.190813</td>
      <td>5107.471853</td>
      <td>17940.630798</td>
      <td>25091.743119</td>
      <td>25954.198473</td>
      <td>5418.994413</td>
      <td>804.237288</td>
      <td>25573.770492</td>
      <td>7815.699659</td>
      <td>33759.590793</td>
      <td>7336.065574</td>
      <td>1797.556719</td>
      <td>944.736842</td>
      <td>203584.229391</td>
      <td>2853.982301</td>
      <td>2054.054054</td>
    </tr>
    <tr>
      <th>1972</th>
      <td>24413.145540</td>
      <td>240.184758</td>
      <td>19285.714286</td>
      <td>352.331606</td>
      <td>5600.000000</td>
      <td>18416.206262</td>
      <td>25990.990991</td>
      <td>26541.353383</td>
      <td>5675.675676</td>
      <td>842.975207</td>
      <td>29890.453834</td>
      <td>8704.318937</td>
      <td>35368.956743</td>
      <td>7338.709677</td>
      <td>1822.827939</td>
      <td>959.079284</td>
      <td>170570.570571</td>
      <td>3008.658009</td>
      <td>2203.539823</td>
    </tr>
    <tr>
      <th>1973</th>
      <td>25534.883721</td>
      <td>253.107345</td>
      <td>20499.108734</td>
      <td>355.817875</td>
      <td>6194.174757</td>
      <td>19561.243144</td>
      <td>27422.222222</td>
      <td>26814.814815</td>
      <td>5916.230366</td>
      <td>887.096774</td>
      <td>35469.448584</td>
      <td>9190.938511</td>
      <td>36868.686869</td>
      <td>7420.634921</td>
      <td>1880.199667</td>
      <td>1027.363184</td>
      <td>143073.047859</td>
      <td>3126.582278</td>
      <td>2396.551724</td>
    </tr>
    <tr>
      <th>1974</th>
      <td>25161.290323</td>
      <td>253.318584</td>
      <td>19928.825623</td>
      <td>352.553542</td>
      <td>6619.047619</td>
      <td>20545.454545</td>
      <td>28070.175439</td>
      <td>27518.248175</td>
      <td>6074.450085</td>
      <td>929.133858</td>
      <td>39093.484419</td>
      <td>9528.301887</td>
      <td>37844.611529</td>
      <td>7695.312500</td>
      <td>2025.931929</td>
      <td>1046.004843</td>
      <td>120594.479830</td>
      <td>3239.669421</td>
      <td>2529.411765</td>
    </tr>
    <tr>
      <th>1975</th>
      <td>24885.844749</td>
      <td>270.358306</td>
      <td>19572.953737</td>
      <td>375.201288</td>
      <td>6777.777778</td>
      <td>20072.332731</td>
      <td>28060.344828</td>
      <td>27681.159420</td>
      <td>6239.737274</td>
      <td>946.564885</td>
      <td>33916.554509</td>
      <td>9021.406728</td>
      <td>39650.872818</td>
      <td>7547.892720</td>
      <td>1876.971609</td>
      <td>1070.921986</td>
      <td>102527.075812</td>
      <td>3233.870968</td>
      <td>2491.803279</td>
    </tr>
    <tr>
      <th>1976</th>
      <td>25972.850679</td>
      <td>261.472785</td>
      <td>20106.761566</td>
      <td>372.641509</td>
      <td>7300.000000</td>
      <td>21402.877698</td>
      <td>29148.936170</td>
      <td>28000.000000</td>
      <td>6325.878594</td>
      <td>992.537313</td>
      <td>37851.662404</td>
      <td>10267.062315</td>
      <td>41687.344913</td>
      <td>7283.018868</td>
      <td>1978.527607</td>
      <td>1140.552995</td>
      <td>102318.392581</td>
      <td>3320.158103</td>
      <td>2712.000000</td>
    </tr>
    <tr>
      <th>1977</th>
      <td>26950.672646</td>
      <td>277.310924</td>
      <td>20603.907638</td>
      <td>390.769231</td>
      <td>7433.628319</td>
      <td>21863.799283</td>
      <td>29915.611814</td>
      <td>28591.549296</td>
      <td>6376.360809</td>
      <td>1051.094891</td>
      <td>38517.618469</td>
      <td>9540.229885</td>
      <td>43316.831683</td>
      <td>7657.992565</td>
      <td>2038.690476</td>
      <td>1225.225225</td>
      <td>107486.631016</td>
      <td>3378.378378</td>
      <td>2851.562500</td>
    </tr>
    <tr>
      <th>1978</th>
      <td>28177.777778</td>
      <td>304.347826</td>
      <td>21492.007105</td>
      <td>403.903904</td>
      <td>7474.137931</td>
      <td>22459.893048</td>
      <td>30708.333333</td>
      <td>28671.328671</td>
      <td>6772.727273</td>
      <td>1092.198582</td>
      <td>34677.419355</td>
      <td>7944.444444</td>
      <td>44827.586207</td>
      <td>7216.117216</td>
      <td>1861.471861</td>
      <td>1321.585903</td>
      <td>92840.375587</td>
      <td>3581.132075</td>
      <td>2977.099237</td>
    </tr>
    <tr>
      <th>1979</th>
      <td>28728.070175</td>
      <td>323.469388</td>
      <td>22380.106572</td>
      <td>374.449339</td>
      <td>7847.457627</td>
      <td>23665.480427</td>
      <td>31481.481481</td>
      <td>29448.275862</td>
      <td>7237.813885</td>
      <td>1145.833333</td>
      <td>36710.239651</td>
      <td>6863.270777</td>
      <td>46683.046683</td>
      <td>7833.935018</td>
      <td>1932.773109</td>
      <td>1362.068966</td>
      <td>100525.210084</td>
      <td>3690.036900</td>
      <td>3155.555556</td>
    </tr>
  </tbody>
</table>
</div>



<a id='eda'></a>
## Exploratory Data Analysis

As mentioned in the project objective section, the goal of this project is to understand the GDP of the North American countries in terms of their productions of hydrocarbons, while understanding their purchase power of their citizens based on their use of energy. 

### Economic growth , use of energy and production of hydrocarbons

To achieved what it was mentioned in the objective of this project, the GDP of the North American countries are plotted against their use of energy and their productions of hydrocarbons. This visualization shows how related are their GDP to their uses of energy. Furthermore, the visualization also helps us to understand how dependent the North American countries are to the use of their produced hydrocarbons for the generation of energy.


```python
#Importing custom functions
from Functions import NorthAmeComparison

#Defining north american countries
Countries = ['United States', 'Canada', 'Mexico']

#Visualization the GDP vs use of energy and energy vs produced hydrocarbons
NorthAmeComparison(GDP, Population, Oil_prod, Ener_use, Gas_prod, Countries)
```


![png](output_39_0.png)


It can be observed in the previous figure that the North American countries GDPs and their consumptions of energy have similar behaviors, having a high probability of being correlated. In the same figure can also be observed how much of the north American countries used energy are generated from their produced hydrocarbons. This tell us that some countries depend more than others on this natural resource. 

Although it appears that the behavior of the used energy for the United states is not highly correlated with the production of hydrocarbons, it remains related at some degree. On the other side, Canada and Mexico are highly dependent on their production of hydrocarbons for the generation of energy. Nonetheless, Mexico depends more on the oil produced locally, while Canada depends in similar proportions on both hydrocarbons produced, oil and natural gas.

#### Correlations

Unfortunately, the previous visualization is not enough to determine dependencies among the North American countries GDPs and their production of hydrocarbons, even when it gives a good idea of the probable relationships. To increase certainty about those dependencies, it is necessary to calculate the correlations among the two variables of interest, the countries GDPs and their production of hydrocarbons.


```python
#Importing custom functions
from Functions import CorreDataFrames

#Array to identify the datafrmes to use
FramesLab = ['GDP', 'Ener_use', 'Oil_prod', 'Gas_prod']

#Generating a dataframe for the US information
Country = 'United States'
Dataframes = [GDP[Country], Ener_use[Country], Oil_prod[Country],
                  Gas_prod[Country]]
CorrUS = CorreDataFrames(Dataframes, FramesLab)

#Generating a dataframe for the CA information
Country = 'Canada'
Dataframes = [GDP[Country], Ener_use[Country], Oil_prod[Country],
                  Gas_prod[Country]]
CorrCA = CorreDataFrames(Dataframes, FramesLab)

#Generating a dataframe for the MX information
Country = 'Mexico'
Dataframes = [GDP[Country], Ener_use[Country], Oil_prod[Country],
                  Gas_prod[Country]]
CorrMX = CorreDataFrames(Dataframes, FramesLab)

```

Visualizing correlations among the variables of interest for the North American countries:


```python
#Importing custom functions
from Functions import CountriesNortAmeCorr

#Plotting correlations
CountriesNortAmeCorr(CorrUS, CorrCA, CorrMX, FramesLab)
```


![png](output_44_0.png)


With the last visualization it can be concluded that there is a dependency of the North American countries to the production of hydrocarbons for the increment of their economies. However, that dependency is different for each type of hydrocarbon, and some countries depends more than others from each of them.

### Consumption of energy per capita and the quality of life

The economy of any country is reflected in the purchase power of their citizens, the amount of goods that they can buy with their salaries. In the previous analysis it was observed that there is a strong correlation between the GDP and the energy used, at least for the North American countries. 

Then, it is important to understand how much the availability of energy helps the citizens to produce more and as a consequence to increase its participation on the country's economy, and therefore, to the generation of the GDP. This, considering that the GDP generated from a country is generated equally from its population.

For this analysis are used the last two dataframes generated in the *Data Wrangling* section, the GDP_percap and the Ener_percap dataframes, containing information about the GDP per capita and the Energy used per capita, respectively.

#### GDP per capita (statistics)

A good description of the data information can be observed calculating the statistics of the mentioned dataframes, as follow: 


```python
#Displaying statistics related with the GDP per capita
Countries = ['United States', 'Canada', 'Mexico']
display(GDP_percap[Countries].describe())

```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>United States</th>
      <th>Canada</th>
      <th>Mexico</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>42.000000</td>
      <td>42.000000</td>
      <td>42.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>36447.623953</td>
      <td>36998.277527</td>
      <td>7742.693651</td>
    </tr>
    <tr>
      <th>std</th>
      <td>8865.427923</td>
      <td>7228.645007</td>
      <td>1141.108335</td>
    </tr>
    <tr>
      <th>min</th>
      <td>22761.904762</td>
      <td>24418.604651</td>
      <td>5384.615385</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>28475.495805</td>
      <td>31545.893720</td>
      <td>7172.354344</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>35685.138340</td>
      <td>36175.297802</td>
      <td>7745.232625</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>45004.665920</td>
      <td>44057.213408</td>
      <td>8719.245283</td>
    </tr>
    <tr>
      <th>max</th>
      <td>50166.112957</td>
      <td>48484.848485</td>
      <td>9375.000000</td>
    </tr>
  </tbody>
</table>
</div>


#### Enercy consumption per capita (statistics)


```python
#Displaying statistics related with the Energy use per capita
Countries = ['United States', 'Canada', 'Mexico']
display(Ener_percap[Countries].describe())
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>United States</th>
      <th>Canada</th>
      <th>Mexico</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>42.000000</td>
      <td>42.000000</td>
      <td>42.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>7.683479</td>
      <td>7.624900</td>
      <td>1.336337</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.305708</td>
      <td>0.466939</td>
      <td>0.221125</td>
    </tr>
    <tr>
      <th>min</th>
      <td>7.075071</td>
      <td>6.423373</td>
      <td>0.800419</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>7.527137</td>
      <td>7.383171</td>
      <td>1.341653</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>7.762511</td>
      <td>7.600003</td>
      <td>1.412366</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>7.847190</td>
      <td>7.950320</td>
      <td>1.462189</td>
    </tr>
    <tr>
      <th>max</th>
      <td>8.347831</td>
      <td>8.427171</td>
      <td>1.588498</td>
    </tr>
  </tbody>
</table>
</div>


The max parameter of the statistics shows that Mexico is the North American country with less purchase power, considering the GDP per capita as purchase power, and has the smallest max parameter for the energy used per capita. This tendency can be observed with the United states, which has the bigger purchase power per capita and their citizens use more energy than the rest of North America. There is an obvious relationship among these two variables.

The same behavior can be observed for most of the data available in the datraframes. This can be observed by analyzing the minimum values, the first quartile (Q1) values, the second quartile (Q2) values and the third quartile (Q3) values for the GDP per capita and the use of energy per capita. 

However, the minimum and the Q3 values for Canada present an interesting scenario, a scenario where people from Canada were the ones with more purchase power and with similar use of energy as the United States. This means that at certain point in time people from Canada were living better than the rest of North America. Nonetheless, the amount of citizens in which the GDP and the Energy available was divided needs to be considered.

Lastly, Mexico shows the less variability among the GDP and the use of energy per capita, while Canada shows more variability in terms of the Energy used per capita and the United states shows more variability for the GDP per capita. This means that Mexico is the North American country with the smallest growth in terms of the GDP and the use of Energy per capita. Nevertheless, it is important to consider the amount of population that each of the North American countries have.  

#### Visualizaing GDP per capita Vs Energy consumtion per capita

The following visualization helps to understand better the relationship between the GDP per capita, the Energy consumption per capita and population for each country through 1970 to 2017.


```python
#Importing custom functions
from Functions import NorthAmeComparisonPC

#Visualization
NorthAmeComparisonPC(GDP_percap, Population, Ener_percap, Countries);
```


![png](output_53_0.png)


The previous figure explains the interested scenario mentioned in the previous subsection, where Canadians were the citizens with most acquisition power in North America. That was due of its population, since the energy available was distributed among less people when compared with the rest of North America. 

It can also be observed the almost linear relationship of the GDP per capita and the Energy used per capita for Mexico and Canada, which can be used to predict its behavior in the future. United States presents a different behavior. An additional study of the data can be implemented considering the previously found relationship among the Energy used and the production of hydrocarbons, as presented next.

#### Considering the dependecy on the production of hydrocarbons

The North American countries dependencies on the production of hydrocarbons for their generation of energy and their GDP can be observed in the next figure. For the case of Mexico, it can be observed a highly dependency of the population power acquisition on the production of hydrocarbons. A similar dependency can be observed in Canada, but in less degree. United States presents a different behavior, it does not rely that much in their production of oil, at least with the available data which consider only the locally produced hydrocarbons.


```python
#importing custom functions
from Functions import NorthAmeComparisonPC_Oil

#Considering the dependecy on the production of hydrocarbons 
Hidrocar = Oil_prod.add(Gas_prod)
NorthAmeComparisonPC_Oil(GDP_percap, Hidrocar, Ener_percap, Countries);
```


![png](output_56_0.png)


<a id='conclusions'></a>
## Conclusions


As summary, it was found an obvious dependency between the GDP and the production of hydrocarbons for the North American countries, as explained in the Exploratory Data Analysis section. Additionally, it was found that the energy consumption per capita is a good metric to understand how much produce the country's population to generate the GDP, which will increase depending on how much energy is available to be used for the country’s population.

However, the data obtained for this project was limited, in terms of outdated information, the amount of hydrocarbons imported to generate energy, a realistic GDP Purchase Power Parity (PPP) and more complete information about other types of sources for the generation of energy.

The limitations affected the analysis by constraining the used hydrocarbons to those produced internally, to consider the power purchase parity as the GDP, and to understand how much other sources of energy contributed to the generation of the North American countries GDPs. It also affected to present an outdated analysis, given that not all the available csv files contain recent information.

Nonetheless, the presented analysis helps to explain, with considerable solid basis, the economy of the North American countries in terms of their GDP, Energy consumption and production of hydrocarbons through 1970 to 2010. 


```python

```
