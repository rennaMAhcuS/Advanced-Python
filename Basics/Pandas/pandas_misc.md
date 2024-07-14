# Pandas Tutorial - KeithGalli

## Intro to Dataframes


```python
import pandas as pd
import numpy as np
```


```python
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], columns=["A", "B", "C"], index=["x","y","z",'zz'])
```


```python
df.head()
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>x</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>y</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>z</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>zz</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail(2)
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>z</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>zz</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.columns
```




    Index(['A', 'B', 'C'], dtype='object')




```python
df.index.tolist()
```




    ['x', 'y', 'z', 'zz']




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 4 entries, x to zz
    Data columns (total 3 columns):
     #   Column  Non-Null Count  Dtype
    ---  ------  --------------  -----
     0   A       4 non-null      int64
     1   B       4 non-null      int64
     2   C       4 non-null      int64
    dtypes: int64(3)
    memory usage: 128.0+ bytes



```python
df.describe()
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.500000</td>
      <td>6.500000</td>
      <td>7.500000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3.872983</td>
      <td>3.872983</td>
      <td>3.872983</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>3.250000</td>
      <td>4.250000</td>
      <td>5.250000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.500000</td>
      <td>6.500000</td>
      <td>7.500000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>7.750000</td>
      <td>8.750000</td>
      <td>9.750000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>10.000000</td>
      <td>11.000000</td>
      <td>12.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.nunique()
```




    A    4
    B    4
    C    4
    dtype: int64




```python
df['A'].unique()
```




    array([ 1,  4,  7, 10])




```python
df.shape
```




    (4, 3)




```python
df.size
```




    12




```python
df
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>x</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>y</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>z</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>zz</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



## Loading in Dataframes from Files


```python
coffee = pd.read_csv('./warmup-data/coffee.csv')
```


```python
results = pd.read_parquet('./data/results.parquet')
bios = pd.read_csv('./data/bios.csv')
```


```python
## To read an excel spreadsheet
olympics_data = pd.read_excel('./data/olympics-data.xlsx', sheet_name="results")
```

## Accessing Data with Pandas


```python
print(coffee)
```

              Day Coffee Type  Units Sold
    0      Monday    Espresso          25
    1      Monday       Latte          15
    2     Tuesday    Espresso          30
    3     Tuesday       Latte          20
    4   Wednesday    Espresso          35
    5   Wednesday       Latte          25
    6    Thursday    Espresso          40
    7    Thursday       Latte          30
    8      Friday    Espresso          45
    9      Friday       Latte          35
    10   Saturday    Espresso          45
    11   Saturday       Latte          35
    12     Sunday    Espresso          45
    13     Sunday       Latte          35



```python
display(coffee)
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
      <th>Day</th>
      <th>Coffee Type</th>
      <th>Units Sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Monday</td>
      <td>Espresso</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Monday</td>
      <td>Latte</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tuesday</td>
      <td>Espresso</td>
      <td>30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tuesday</td>
      <td>Latte</td>
      <td>20</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wednesday</td>
      <td>Espresso</td>
      <td>35</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wednesday</td>
      <td>Latte</td>
      <td>25</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Thursday</td>
      <td>Espresso</td>
      <td>40</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Thursday</td>
      <td>Latte</td>
      <td>30</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Friday</td>
      <td>Espresso</td>
      <td>45</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Friday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Saturday</td>
      <td>Espresso</td>
      <td>45</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Saturday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Sunday</td>
      <td>Espresso</td>
      <td>45</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Sunday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>



```python
coffee.head()
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
      <th>Day</th>
      <th>Coffee Type</th>
      <th>Units Sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Monday</td>
      <td>Espresso</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Monday</td>
      <td>Latte</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tuesday</td>
      <td>Espresso</td>
      <td>30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tuesday</td>
      <td>Latte</td>
      <td>20</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wednesday</td>
      <td>Espresso</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>




```python
coffee.tail(10)
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
      <th>Day</th>
      <th>Coffee Type</th>
      <th>Units Sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>Wednesday</td>
      <td>Espresso</td>
      <td>35</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wednesday</td>
      <td>Latte</td>
      <td>25</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Thursday</td>
      <td>Espresso</td>
      <td>40</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Thursday</td>
      <td>Latte</td>
      <td>30</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Friday</td>
      <td>Espresso</td>
      <td>45</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Friday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Saturday</td>
      <td>Espresso</td>
      <td>45</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Saturday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Sunday</td>
      <td>Espresso</td>
      <td>45</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Sunday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>




```python
coffee.sample(5) # Pass in random_state to make deterministic
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
      <th>Day</th>
      <th>Coffee Type</th>
      <th>Units Sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11</th>
      <td>Saturday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Monday</td>
      <td>Espresso</td>
      <td>25</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Thursday</td>
      <td>Espresso</td>
      <td>40</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Thursday</td>
      <td>Latte</td>
      <td>30</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Sunday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>




```python
# loc
# coffee.loc[Rows, Columns]

coffee.loc[0]
```




    Day              Monday
    Coffee Type    Espresso
    Units Sold           25
    Name: 0, dtype: object




```python
coffee.loc[[0,1,5]]
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
      <th>Day</th>
      <th>Coffee Type</th>
      <th>Units Sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Monday</td>
      <td>Espresso</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Monday</td>
      <td>Latte</td>
      <td>15</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wednesday</td>
      <td>Latte</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>




```python
coffee.loc[5:9, ["Day", "Units Sold"]]
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
      <th>Day</th>
      <th>Units Sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>Wednesday</td>
      <td>25</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Thursday</td>
      <td>40</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Thursday</td>
      <td>30</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Friday</td>
      <td>45</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Friday</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>



#### iloc


```python
coffee.iloc[:, [0,2]]
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
      <th>Day</th>
      <th>Units Sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Monday</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Monday</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tuesday</td>
      <td>30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tuesday</td>
      <td>20</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wednesday</td>
      <td>35</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wednesday</td>
      <td>25</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Thursday</td>
      <td>40</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Thursday</td>
      <td>30</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Friday</td>
      <td>45</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Friday</td>
      <td>35</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Saturday</td>
      <td>45</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Saturday</td>
      <td>35</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Sunday</td>
      <td>45</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Sunday</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>



#### Other Stuff


```python
coffee.index = coffee["Day"]
```


```python
coffee.loc["Monday":"Wednesday"]
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
      <th>Day</th>
      <th>Coffee Type</th>
      <th>Units Sold</th>
    </tr>
    <tr>
      <th>Day</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Monday</th>
      <td>Monday</td>
      <td>Espresso</td>
      <td>25</td>
    </tr>
    <tr>
      <th>Monday</th>
      <td>Monday</td>
      <td>Latte</td>
      <td>15</td>
    </tr>
    <tr>
      <th>Tuesday</th>
      <td>Tuesday</td>
      <td>Espresso</td>
      <td>30</td>
    </tr>
    <tr>
      <th>Tuesday</th>
      <td>Tuesday</td>
      <td>Latte</td>
      <td>20</td>
    </tr>
    <tr>
      <th>Wednesday</th>
      <td>Wednesday</td>
      <td>Espresso</td>
      <td>35</td>
    </tr>
    <tr>
      <th>Wednesday</th>
      <td>Wednesday</td>
      <td>Latte</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>




```python
coffee = pd.read_csv('./warmup-data/coffee.csv')
```

#### Setting Values


```python
coffee.loc[1:3, "Units Sold"] = 10
```

#### Optimized way to get single values (.at & .iat)


```python
coffee.at[0,"Units Sold"]
```




    25




```python
coffee.iat[3,1]
```




    'Latte'



#### Getting Columns


```python
coffee.Day
```




    0        Monday
    1        Monday
    2       Tuesday
    3       Tuesday
    4     Wednesday
    5     Wednesday
    6      Thursday
    7      Thursday
    8        Friday
    9        Friday
    10     Saturday
    11     Saturday
    12       Sunday
    13       Sunday
    Name: Day, dtype: object




```python
coffee["Day"]
```




    0        Monday
    1        Monday
    2       Tuesday
    3       Tuesday
    4     Wednesday
    5     Wednesday
    6      Thursday
    7      Thursday
    8        Friday
    9        Friday
    10     Saturday
    11     Saturday
    12       Sunday
    13       Sunday
    Name: Day, dtype: object



#### Sort Values


```python
coffee.sort_values(["Units Sold"], ascending=False)
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
      <th>Day</th>
      <th>Coffee Type</th>
      <th>Units Sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>Friday</td>
      <td>Espresso</td>
      <td>45</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Saturday</td>
      <td>Espresso</td>
      <td>45</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Sunday</td>
      <td>Espresso</td>
      <td>45</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Thursday</td>
      <td>Espresso</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wednesday</td>
      <td>Espresso</td>
      <td>35</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Friday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Saturday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Sunday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Thursday</td>
      <td>Latte</td>
      <td>30</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Monday</td>
      <td>Espresso</td>
      <td>25</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wednesday</td>
      <td>Latte</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Monday</td>
      <td>Latte</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tuesday</td>
      <td>Espresso</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tuesday</td>
      <td>Latte</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
coffee.sort_values(["Units Sold", "Coffee Type"], ascending=[0,1])
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
      <th>Day</th>
      <th>Coffee Type</th>
      <th>Units Sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>Friday</td>
      <td>Espresso</td>
      <td>45</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Saturday</td>
      <td>Espresso</td>
      <td>45</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Sunday</td>
      <td>Espresso</td>
      <td>45</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Thursday</td>
      <td>Espresso</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wednesday</td>
      <td>Espresso</td>
      <td>35</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Friday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Saturday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Sunday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Thursday</td>
      <td>Latte</td>
      <td>30</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Monday</td>
      <td>Espresso</td>
      <td>25</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wednesday</td>
      <td>Latte</td>
      <td>25</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tuesday</td>
      <td>Espresso</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Monday</td>
      <td>Latte</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tuesday</td>
      <td>Latte</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>



#### Iterate over dataframe with for loop


```python
for index, row in coffee.iterrows():
    print(index)
    print(row)
    print("Coffee Type of Row:", row["Coffee Type"])
```

    0
    Day              Monday
    Coffee Type    Espresso
    Units Sold           25
    Name: 0, dtype: object
    Coffee Type of Row: Espresso
    1
    Day            Monday
    Coffee Type     Latte
    Units Sold         10
    Name: 1, dtype: object
    Coffee Type of Row: Latte
    2
    Day             Tuesday
    Coffee Type    Espresso
    Units Sold           10
    Name: 2, dtype: object
    Coffee Type of Row: Espresso
    3
    Day            Tuesday
    Coffee Type      Latte
    Units Sold          10
    Name: 3, dtype: object
    Coffee Type of Row: Latte
    4
    Day            Wednesday
    Coffee Type     Espresso
    Units Sold            35
    Name: 4, dtype: object
    Coffee Type of Row: Espresso
    5
    Day            Wednesday
    Coffee Type        Latte
    Units Sold            25
    Name: 5, dtype: object
    Coffee Type of Row: Latte
    6
    Day            Thursday
    Coffee Type    Espresso
    Units Sold           40
    Name: 6, dtype: object
    Coffee Type of Row: Espresso
    7
    Day            Thursday
    Coffee Type       Latte
    Units Sold           30
    Name: 7, dtype: object
    Coffee Type of Row: Latte
    8
    Day              Friday
    Coffee Type    Espresso
    Units Sold           45
    Name: 8, dtype: object
    Coffee Type of Row: Espresso
    9
    Day            Friday
    Coffee Type     Latte
    Units Sold         35
    Name: 9, dtype: object
    Coffee Type of Row: Latte
    10
    Day            Saturday
    Coffee Type    Espresso
    Units Sold           45
    Name: 10, dtype: object
    Coffee Type of Row: Espresso
    11
    Day            Saturday
    Coffee Type       Latte
    Units Sold           35
    Name: 11, dtype: object
    Coffee Type of Row: Latte
    12
    Day              Sunday
    Coffee Type    Espresso
    Units Sold           45
    Name: 12, dtype: object
    Coffee Type of Row: Espresso
    13
    Day            Sunday
    Coffee Type     Latte
    Units Sold         35
    Name: 13, dtype: object
    Coffee Type of Row: Latte


## Filtering Data


```python
bios.head()
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
      <th>athlete_id</th>
      <th>name</th>
      <th>born_date</th>
      <th>born_city</th>
      <th>born_region</th>
      <th>born_country</th>
      <th>NOC</th>
      <th>height_cm</th>
      <th>weight_kg</th>
      <th>died_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Jean-François Blanchy</td>
      <td>1886-12-12</td>
      <td>Bordeaux</td>
      <td>Gironde</td>
      <td>FRA</td>
      <td>France</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1960-10-02</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Arnaud Boetsch</td>
      <td>1969-04-01</td>
      <td>Meulan</td>
      <td>Yvelines</td>
      <td>FRA</td>
      <td>France</td>
      <td>183.0</td>
      <td>76.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Jean Borotra</td>
      <td>1898-08-13</td>
      <td>Biarritz</td>
      <td>Pyrénées-Atlantiques</td>
      <td>FRA</td>
      <td>France</td>
      <td>183.0</td>
      <td>76.0</td>
      <td>1994-07-17</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Jacques Brugnon</td>
      <td>1895-05-11</td>
      <td>Paris VIIIe</td>
      <td>Paris</td>
      <td>FRA</td>
      <td>France</td>
      <td>168.0</td>
      <td>64.0</td>
      <td>1978-03-20</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Albert Canet</td>
      <td>1878-04-17</td>
      <td>Wandsworth</td>
      <td>England</td>
      <td>GBR</td>
      <td>France</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1930-07-25</td>
    </tr>
  </tbody>
</table>
</div>




```python
bios.loc[bios["height_cm"] > 215]
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
      <th>athlete_id</th>
      <th>name</th>
      <th>born_date</th>
      <th>born_city</th>
      <th>born_region</th>
      <th>born_country</th>
      <th>NOC</th>
      <th>height_cm</th>
      <th>weight_kg</th>
      <th>died_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5089</th>
      <td>5108</td>
      <td>Viktor Pankrashkin</td>
      <td>1957-06-19</td>
      <td>Moskva (Moscow)</td>
      <td>Moskva</td>
      <td>RUS</td>
      <td>Soviet Union</td>
      <td>220.0</td>
      <td>112.0</td>
      <td>1993-07-24</td>
    </tr>
    <tr>
      <th>5583</th>
      <td>5606</td>
      <td>Paulinho Villas Boas</td>
      <td>1963-01-26</td>
      <td>São Paulo</td>
      <td>São Paulo</td>
      <td>BRA</td>
      <td>Brazil</td>
      <td>217.0</td>
      <td>106.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5673</th>
      <td>5696</td>
      <td>Gunther Behnke</td>
      <td>1963-01-19</td>
      <td>Leverkusen</td>
      <td>Nordrhein-Westfalen</td>
      <td>GER</td>
      <td>Germany</td>
      <td>221.0</td>
      <td>114.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5716</th>
      <td>5739</td>
      <td>Uwe Blab</td>
      <td>1962-03-26</td>
      <td>München (Munich)</td>
      <td>Bayern</td>
      <td>GER</td>
      <td>Germany West Germany</td>
      <td>218.0</td>
      <td>110.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5781</th>
      <td>5804</td>
      <td>Tommy Burleson</td>
      <td>1952-02-24</td>
      <td>Crossnore</td>
      <td>North Carolina</td>
      <td>USA</td>
      <td>United States</td>
      <td>223.0</td>
      <td>102.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5796</th>
      <td>5819</td>
      <td>Andy Campbell</td>
      <td>1956-07-21</td>
      <td>Melbourne</td>
      <td>Victoria</td>
      <td>AUS</td>
      <td>Australia</td>
      <td>218.0</td>
      <td>93.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6223</th>
      <td>6250</td>
      <td>Lars Hansen</td>
      <td>1954-09-27</td>
      <td>København (Copenhagen)</td>
      <td>Hovedstaden</td>
      <td>DEN</td>
      <td>Canada</td>
      <td>216.0</td>
      <td>105.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6270</th>
      <td>6298</td>
      <td>Hu Zhangbao</td>
      <td>1963-04-05</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>People's Republic of China</td>
      <td>216.0</td>
      <td>135.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6409</th>
      <td>6440</td>
      <td>Sergey Kovalenko</td>
      <td>1947-08-11</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Soviet Union</td>
      <td>216.0</td>
      <td>111.0</td>
      <td>2004-11-18</td>
    </tr>
    <tr>
      <th>6420</th>
      <td>6451</td>
      <td>Jānis Krūmiņš</td>
      <td>1930-01-30</td>
      <td>Cēsis</td>
      <td>Cēsu novads</td>
      <td>LAT</td>
      <td>Soviet Union</td>
      <td>218.0</td>
      <td>141.0</td>
      <td>1994-11-20</td>
    </tr>
    <tr>
      <th>6504</th>
      <td>6537</td>
      <td>Luc Longley</td>
      <td>1969-01-19</td>
      <td>Melbourne</td>
      <td>Victoria</td>
      <td>AUS</td>
      <td>Australia</td>
      <td>220.0</td>
      <td>135.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6722</th>
      <td>6755</td>
      <td>Shaquille O'Neal</td>
      <td>1972-03-06</td>
      <td>Newark</td>
      <td>New Jersey</td>
      <td>USA</td>
      <td>United States</td>
      <td>216.0</td>
      <td>137.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6937</th>
      <td>6972</td>
      <td>David Robinson</td>
      <td>1965-08-06</td>
      <td>Key West</td>
      <td>Florida</td>
      <td>USA</td>
      <td>United States</td>
      <td>216.0</td>
      <td>107.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6978</th>
      <td>7013</td>
      <td>Arvydas Sabonis</td>
      <td>1964-12-19</td>
      <td>Kaunas</td>
      <td>Kaunas</td>
      <td>LTU</td>
      <td>Lithuania Soviet Union</td>
      <td>223.0</td>
      <td>122.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7074</th>
      <td>7111</td>
      <td>Paulo da Silva</td>
      <td>1963-07-21</td>
      <td>São Paulo</td>
      <td>São Paulo</td>
      <td>BRA</td>
      <td>Brazil</td>
      <td>217.0</td>
      <td>106.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7188</th>
      <td>7226</td>
      <td>Vladimir Tkachenko</td>
      <td>1957-09-20</td>
      <td>Golovinka</td>
      <td>Krasnodar Kray</td>
      <td>RUS</td>
      <td>Soviet Union</td>
      <td>220.0</td>
      <td>110.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7281</th>
      <td>7320</td>
      <td>Stojko Vranković</td>
      <td>1964-01-22</td>
      <td>Drniš</td>
      <td>Šibensko-kninska županija</td>
      <td>CRO</td>
      <td>Croatia Yugoslavia</td>
      <td>217.0</td>
      <td>115.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7376</th>
      <td>7416</td>
      <td>Eurelijus Žukauskas</td>
      <td>1973-08-22</td>
      <td>Klaipėda</td>
      <td>Klaipėda</td>
      <td>LTU</td>
      <td>Lithuania</td>
      <td>218.0</td>
      <td>115.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>52608</th>
      <td>52983</td>
      <td>Aleksey Kazakov</td>
      <td>1976-03-18</td>
      <td>Naberezhnye Chelny</td>
      <td>Respublika Tatarstan</td>
      <td>RUS</td>
      <td>Russian Federation</td>
      <td>217.0</td>
      <td>102.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>82100</th>
      <td>82753</td>
      <td>Frédéric Weis</td>
      <td>1977-06-22</td>
      <td>Thionville</td>
      <td>Moselle</td>
      <td>FRA</td>
      <td>France</td>
      <td>218.0</td>
      <td>110.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>89070</th>
      <td>89782</td>
      <td>Yao Ming</td>
      <td>1980-09-12</td>
      <td>Xuhui District</td>
      <td>Shanghai</td>
      <td>CHN</td>
      <td>People's Republic of China</td>
      <td>226.0</td>
      <td>141.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>89075</th>
      <td>89787</td>
      <td>Roberto Dueñas</td>
      <td>1975-11-01</td>
      <td>Madrid</td>
      <td>Madrid</td>
      <td>ESP</td>
      <td>Spain</td>
      <td>221.0</td>
      <td>137.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>107408</th>
      <td>108533</td>
      <td>Peter John Ramos</td>
      <td>1985-05-23</td>
      <td>Fajardo</td>
      <td>Puerto Rico</td>
      <td>PUR</td>
      <td>Puerto Rico</td>
      <td>219.0</td>
      <td>113.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>112312</th>
      <td>113568</td>
      <td>Stanko Barać</td>
      <td>1986-08-13</td>
      <td>Mostar</td>
      <td>Hercegovačko-neretvanski kanton</td>
      <td>BIH</td>
      <td>Croatia</td>
      <td>217.0</td>
      <td>110.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>112332</th>
      <td>113588</td>
      <td>Andreas Glyniadakis</td>
      <td>1981-08-26</td>
      <td>Chania</td>
      <td>Kriti</td>
      <td>GRE</td>
      <td>Greece</td>
      <td>216.0</td>
      <td>115.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>112337</th>
      <td>113593</td>
      <td>Hamed Haddadi</td>
      <td>1985-05-19</td>
      <td>Ahvaz</td>
      <td>Khuzestan</td>
      <td>IRI</td>
      <td>Islamic Republic of Iran</td>
      <td>218.0</td>
      <td>110.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>118663</th>
      <td>120400</td>
      <td>Timofey Mozgov</td>
      <td>1986-07-16</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Russian Federation</td>
      <td>216.0</td>
      <td>113.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>118676</th>
      <td>120415</td>
      <td>Dmitry Musersky</td>
      <td>1988-10-29</td>
      <td>Makiïvka</td>
      <td>Donetsk</td>
      <td>UKR</td>
      <td>Russian Federation</td>
      <td>219.0</td>
      <td>104.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>120266</th>
      <td>122147</td>
      <td>Zhang Zhaoxu</td>
      <td>1987-11-18</td>
      <td>Binzhou</td>
      <td>Shandong</td>
      <td>CHN</td>
      <td>People's Republic of China</td>
      <td>221.0</td>
      <td>110.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>121694</th>
      <td>123709</td>
      <td>Salah Mejri</td>
      <td>1986-06-15</td>
      <td>Jendouba</td>
      <td>Jendouba</td>
      <td>TUN</td>
      <td>Tunisia</td>
      <td>216.0</td>
      <td>110.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>123850</th>
      <td>126093</td>
      <td>Tyson Chandler</td>
      <td>1982-10-02</td>
      <td>Hanford</td>
      <td>California</td>
      <td>USA</td>
      <td>United States</td>
      <td>216.0</td>
      <td>107.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>130460</th>
      <td>133147</td>
      <td>Li Muhao</td>
      <td>1992-06-02</td>
      <td>Guiyang</td>
      <td>Guizhou</td>
      <td>CHN</td>
      <td>People's Republic of China</td>
      <td>218.0</td>
      <td>115.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>130461</th>
      <td>133148</td>
      <td>Zhou Qi</td>
      <td>1996-01-16</td>
      <td>Xinxiang</td>
      <td>Henan</td>
      <td>CHN</td>
      <td>People's Republic of China</td>
      <td>217.0</td>
      <td>95.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>138671</th>
      <td>142084</td>
      <td>Ondřej Balvín</td>
      <td>1992-09-20</td>
      <td>Ústí nad Labem</td>
      <td>Ústecký kraj</td>
      <td>CZE</td>
      <td>Czechia</td>
      <td>216.0</td>
      <td>107.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>139365</th>
      <td>142836</td>
      <td>Moustapha Fall</td>
      <td>1992-02-23</td>
      <td>Paris</td>
      <td>Paris</td>
      <td>FRA</td>
      <td>France</td>
      <td>218.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
bios.loc[bios["height_cm"] > 215, ["name", "height_cm"]]
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
      <th>name</th>
      <th>height_cm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5089</th>
      <td>Viktor Pankrashkin</td>
      <td>220.0</td>
    </tr>
    <tr>
      <th>5583</th>
      <td>Paulinho Villas Boas</td>
      <td>217.0</td>
    </tr>
    <tr>
      <th>5673</th>
      <td>Gunther Behnke</td>
      <td>221.0</td>
    </tr>
    <tr>
      <th>5716</th>
      <td>Uwe Blab</td>
      <td>218.0</td>
    </tr>
    <tr>
      <th>5781</th>
      <td>Tommy Burleson</td>
      <td>223.0</td>
    </tr>
    <tr>
      <th>5796</th>
      <td>Andy Campbell</td>
      <td>218.0</td>
    </tr>
    <tr>
      <th>6223</th>
      <td>Lars Hansen</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>6270</th>
      <td>Hu Zhangbao</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>6409</th>
      <td>Sergey Kovalenko</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>6420</th>
      <td>Jānis Krūmiņš</td>
      <td>218.0</td>
    </tr>
    <tr>
      <th>6504</th>
      <td>Luc Longley</td>
      <td>220.0</td>
    </tr>
    <tr>
      <th>6722</th>
      <td>Shaquille O'Neal</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>6937</th>
      <td>David Robinson</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>6978</th>
      <td>Arvydas Sabonis</td>
      <td>223.0</td>
    </tr>
    <tr>
      <th>7074</th>
      <td>Paulo da Silva</td>
      <td>217.0</td>
    </tr>
    <tr>
      <th>7188</th>
      <td>Vladimir Tkachenko</td>
      <td>220.0</td>
    </tr>
    <tr>
      <th>7281</th>
      <td>Stojko Vranković</td>
      <td>217.0</td>
    </tr>
    <tr>
      <th>7376</th>
      <td>Eurelijus Žukauskas</td>
      <td>218.0</td>
    </tr>
    <tr>
      <th>52608</th>
      <td>Aleksey Kazakov</td>
      <td>217.0</td>
    </tr>
    <tr>
      <th>82100</th>
      <td>Frédéric Weis</td>
      <td>218.0</td>
    </tr>
    <tr>
      <th>89070</th>
      <td>Yao Ming</td>
      <td>226.0</td>
    </tr>
    <tr>
      <th>89075</th>
      <td>Roberto Dueñas</td>
      <td>221.0</td>
    </tr>
    <tr>
      <th>107408</th>
      <td>Peter John Ramos</td>
      <td>219.0</td>
    </tr>
    <tr>
      <th>112312</th>
      <td>Stanko Barać</td>
      <td>217.0</td>
    </tr>
    <tr>
      <th>112332</th>
      <td>Andreas Glyniadakis</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>112337</th>
      <td>Hamed Haddadi</td>
      <td>218.0</td>
    </tr>
    <tr>
      <th>118663</th>
      <td>Timofey Mozgov</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>118676</th>
      <td>Dmitry Musersky</td>
      <td>219.0</td>
    </tr>
    <tr>
      <th>120266</th>
      <td>Zhang Zhaoxu</td>
      <td>221.0</td>
    </tr>
    <tr>
      <th>121694</th>
      <td>Salah Mejri</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>123850</th>
      <td>Tyson Chandler</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>130460</th>
      <td>Li Muhao</td>
      <td>218.0</td>
    </tr>
    <tr>
      <th>130461</th>
      <td>Zhou Qi</td>
      <td>217.0</td>
    </tr>
    <tr>
      <th>138671</th>
      <td>Ondřej Balvín</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>139365</th>
      <td>Moustapha Fall</td>
      <td>218.0</td>
    </tr>
  </tbody>
</table>
</div>



#### Short-hand syntax (without .loc)


```python
bios[bios['height_cm'] > 215][["name","height_cm"]]
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
      <th>name</th>
      <th>height_cm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5089</th>
      <td>Viktor Pankrashkin</td>
      <td>220.0</td>
    </tr>
    <tr>
      <th>5583</th>
      <td>Paulinho Villas Boas</td>
      <td>217.0</td>
    </tr>
    <tr>
      <th>5673</th>
      <td>Gunther Behnke</td>
      <td>221.0</td>
    </tr>
    <tr>
      <th>5716</th>
      <td>Uwe Blab</td>
      <td>218.0</td>
    </tr>
    <tr>
      <th>5781</th>
      <td>Tommy Burleson</td>
      <td>223.0</td>
    </tr>
    <tr>
      <th>5796</th>
      <td>Andy Campbell</td>
      <td>218.0</td>
    </tr>
    <tr>
      <th>6223</th>
      <td>Lars Hansen</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>6270</th>
      <td>Hu Zhangbao</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>6409</th>
      <td>Sergey Kovalenko</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>6420</th>
      <td>Jānis Krūmiņš</td>
      <td>218.0</td>
    </tr>
    <tr>
      <th>6504</th>
      <td>Luc Longley</td>
      <td>220.0</td>
    </tr>
    <tr>
      <th>6722</th>
      <td>Shaquille O'Neal</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>6937</th>
      <td>David Robinson</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>6978</th>
      <td>Arvydas Sabonis</td>
      <td>223.0</td>
    </tr>
    <tr>
      <th>7074</th>
      <td>Paulo da Silva</td>
      <td>217.0</td>
    </tr>
    <tr>
      <th>7188</th>
      <td>Vladimir Tkachenko</td>
      <td>220.0</td>
    </tr>
    <tr>
      <th>7281</th>
      <td>Stojko Vranković</td>
      <td>217.0</td>
    </tr>
    <tr>
      <th>7376</th>
      <td>Eurelijus Žukauskas</td>
      <td>218.0</td>
    </tr>
    <tr>
      <th>52608</th>
      <td>Aleksey Kazakov</td>
      <td>217.0</td>
    </tr>
    <tr>
      <th>82100</th>
      <td>Frédéric Weis</td>
      <td>218.0</td>
    </tr>
    <tr>
      <th>89070</th>
      <td>Yao Ming</td>
      <td>226.0</td>
    </tr>
    <tr>
      <th>89075</th>
      <td>Roberto Dueñas</td>
      <td>221.0</td>
    </tr>
    <tr>
      <th>107408</th>
      <td>Peter John Ramos</td>
      <td>219.0</td>
    </tr>
    <tr>
      <th>112312</th>
      <td>Stanko Barać</td>
      <td>217.0</td>
    </tr>
    <tr>
      <th>112332</th>
      <td>Andreas Glyniadakis</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>112337</th>
      <td>Hamed Haddadi</td>
      <td>218.0</td>
    </tr>
    <tr>
      <th>118663</th>
      <td>Timofey Mozgov</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>118676</th>
      <td>Dmitry Musersky</td>
      <td>219.0</td>
    </tr>
    <tr>
      <th>120266</th>
      <td>Zhang Zhaoxu</td>
      <td>221.0</td>
    </tr>
    <tr>
      <th>121694</th>
      <td>Salah Mejri</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>123850</th>
      <td>Tyson Chandler</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>130460</th>
      <td>Li Muhao</td>
      <td>218.0</td>
    </tr>
    <tr>
      <th>130461</th>
      <td>Zhou Qi</td>
      <td>217.0</td>
    </tr>
    <tr>
      <th>138671</th>
      <td>Ondřej Balvín</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>139365</th>
      <td>Moustapha Fall</td>
      <td>218.0</td>
    </tr>
  </tbody>
</table>
</div>



#### Multiple filter conditions


```python
bios[(bios['height_cm'] > 215) & (bios['born_country']=='USA')]
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
      <th>athlete_id</th>
      <th>name</th>
      <th>born_date</th>
      <th>born_city</th>
      <th>born_region</th>
      <th>born_country</th>
      <th>NOC</th>
      <th>height_cm</th>
      <th>weight_kg</th>
      <th>died_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5781</th>
      <td>5804</td>
      <td>Tommy Burleson</td>
      <td>1952-02-24</td>
      <td>Crossnore</td>
      <td>North Carolina</td>
      <td>USA</td>
      <td>United States</td>
      <td>223.0</td>
      <td>102.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6722</th>
      <td>6755</td>
      <td>Shaquille O'Neal</td>
      <td>1972-03-06</td>
      <td>Newark</td>
      <td>New Jersey</td>
      <td>USA</td>
      <td>United States</td>
      <td>216.0</td>
      <td>137.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6937</th>
      <td>6972</td>
      <td>David Robinson</td>
      <td>1965-08-06</td>
      <td>Key West</td>
      <td>Florida</td>
      <td>USA</td>
      <td>United States</td>
      <td>216.0</td>
      <td>107.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>123850</th>
      <td>126093</td>
      <td>Tyson Chandler</td>
      <td>1982-10-02</td>
      <td>Hanford</td>
      <td>California</td>
      <td>USA</td>
      <td>United States</td>
      <td>216.0</td>
      <td>107.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



#### Filter by string conditions


```python
bios[bios['name'].str.contains("keith", case=False)]
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
      <th>athlete_id</th>
      <th>name</th>
      <th>born_date</th>
      <th>born_city</th>
      <th>born_region</th>
      <th>born_country</th>
      <th>NOC</th>
      <th>height_cm</th>
      <th>weight_kg</th>
      <th>died_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1897</th>
      <td>1907</td>
      <td>Keith Hanlon</td>
      <td>1966-09-01</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Ireland</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3505</th>
      <td>3517</td>
      <td>Keith Wallace</td>
      <td>1961-03-29</td>
      <td>Preston</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>165.0</td>
      <td>51.0</td>
      <td>1999-12-31</td>
    </tr>
    <tr>
      <th>6228</th>
      <td>6255</td>
      <td>Keith Hartley</td>
      <td>1940-10-15</td>
      <td>Vancouver</td>
      <td>British Columbia</td>
      <td>CAN</td>
      <td>Canada</td>
      <td>200.0</td>
      <td>85.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8898</th>
      <td>8946</td>
      <td>Keith Mwila</td>
      <td>1966-01-01</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Zambia</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1993-01-09</td>
    </tr>
    <tr>
      <th>12053</th>
      <td>12118</td>
      <td>Keith Hervey</td>
      <td>1898-11-03</td>
      <td>Fulham</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1973-02-22</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>109900</th>
      <td>111105</td>
      <td>Keith Cumberpatch</td>
      <td>1927-08-25</td>
      <td>Christchurch</td>
      <td>Canterbury</td>
      <td>NZL</td>
      <td>New Zealand</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2013-11-15</td>
    </tr>
    <tr>
      <th>115973</th>
      <td>117348</td>
      <td>Keith Sanderson</td>
      <td>1975-02-02</td>
      <td>Plymouth</td>
      <td>Massachusetts</td>
      <td>USA</td>
      <td>United States</td>
      <td>183.0</td>
      <td>95.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>117676</th>
      <td>119195</td>
      <td>Duncan Keith</td>
      <td>1983-07-16</td>
      <td>Winnipeg</td>
      <td>Manitoba</td>
      <td>CAN</td>
      <td>Canada</td>
      <td>185.0</td>
      <td>88.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>122121</th>
      <td>124176</td>
      <td>Keith Ferguson</td>
      <td>1979-09-07</td>
      <td>Sale</td>
      <td>Victoria</td>
      <td>AUS</td>
      <td>Australia</td>
      <td>176.0</td>
      <td>78.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>127310</th>
      <td>129749</td>
      <td>Tracy Keith-Matchitt</td>
      <td>1990-03-30</td>
      <td>Palmerston North</td>
      <td>Manawatu-Wanganui</td>
      <td>NZL</td>
      <td>Cook Islands</td>
      <td>167.0</td>
      <td>60.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>70 rows × 10 columns</p>
</div>




```python
# Regex syntax
bios[bios['name'].str.contains('keith|patrick', case=False)]
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
      <th>athlete_id</th>
      <th>name</th>
      <th>born_date</th>
      <th>born_city</th>
      <th>born_region</th>
      <th>born_country</th>
      <th>NOC</th>
      <th>height_cm</th>
      <th>weight_kg</th>
      <th>died_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Patrick Chila</td>
      <td>1969-11-27</td>
      <td>Ris-Orangis</td>
      <td>Essonne</td>
      <td>FRA</td>
      <td>France</td>
      <td>180.0</td>
      <td>73.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>119</th>
      <td>120</td>
      <td>Patrick Wheatley</td>
      <td>1899-01-20</td>
      <td>Vryheid</td>
      <td>KwaZulu-Natal</td>
      <td>RSA</td>
      <td>Great Britain</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1967-11-05</td>
    </tr>
    <tr>
      <th>319</th>
      <td>320</td>
      <td>Patrick De Koning</td>
      <td>1961-04-23</td>
      <td>Dendermonde</td>
      <td>Oost-Vlaanderen</td>
      <td>BEL</td>
      <td>Belgium</td>
      <td>178.0</td>
      <td>92.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1897</th>
      <td>1907</td>
      <td>Keith Hanlon</td>
      <td>1966-09-01</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Ireland</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2115</th>
      <td>2125</td>
      <td>Patrick Jopp</td>
      <td>1962-01-08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Switzerland</td>
      <td>176.0</td>
      <td>67.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>143975</th>
      <td>147633</td>
      <td>Patrick Chinyemba</td>
      <td>2001-01-03</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Zambia</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>144172</th>
      <td>147850</td>
      <td>Patrick Jakob</td>
      <td>1996-10-17</td>
      <td>Sankt Johann in Tirol</td>
      <td>Tirol</td>
      <td>AUT</td>
      <td>Austria</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>144547</th>
      <td>148239</td>
      <td>Patrick Galbraith</td>
      <td>1986-03-11</td>
      <td>Haderslev</td>
      <td>Syddanmark</td>
      <td>DEN</td>
      <td>Denmark</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>144565</th>
      <td>148257</td>
      <td>Patrick Russell</td>
      <td>1993-01-04</td>
      <td>Gentofte</td>
      <td>Hovedstaden</td>
      <td>DEN</td>
      <td>Denmark</td>
      <td>186.0</td>
      <td>93.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145435</th>
      <td>149158</td>
      <td>Patrick Gasienica</td>
      <td>1998-11-28</td>
      <td>McHenry</td>
      <td>Illinois</td>
      <td>USA</td>
      <td>United States</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-06-12</td>
    </tr>
  </tbody>
</table>
<p>303 rows × 10 columns</p>
</div>




```python
# Other cool regex filters

# Find athletes born in cities that start with a vowel:
vowel_cities = bios[bios['born_city'].str.contains(r'^[AEIOUaeiou]', na=False)]

# Find athletes with names that contain exactly two vowels:
two_vowels = bios[bios['name'].str.contains(r'^[^AEIOUaeiou]*[AEIOUaeiou][^AEIOUaeiou]*[AEIOUaeiou][^AEIOUaeiou]*$', na=False)]

# Find athletes with names that have repeated consecutive letters (e.g., "Aaron", "Emmett"):
repeated_letters = bios[bios['name'].str.contains(r'(.)\1', na=False)]

# Find athletes with names ending in 'son' or 'sen':
son_sen_names = bios[bios['name'].str.contains(r'son$|sen$', case=False, na=False)]

# Find athletes born in a year starting with '19':
born_19xx = bios[bios['born_date'].str.contains(r'^19', na=False)]

# Find athletes with names that do not contain any vowels:
no_vowels = bios[bios['name'].str.contains(r'^[^AEIOUaeiou]*$', na=False)]

# Find athletes whose names contain a hyphen or an apostrophe:
hyphen_apostrophe = bios[bios['name'].str.contains(r"[-']", na=False)]

# Find athletes with names that start and end with the same letter:
start_end_same = bios[bios['name'].str.contains(r'^(.).*\1$', na=False, case=False)]

# Find athletes with a born_city that has exactly 7 characters:
city_seven_chars = bios[bios['born_city'].str.contains(r'^.{7}$', na=False)]

# Find athletes with names containing three or more vowels:
three_or_more_vowels = bios[bios['name'].str.contains(r'([AEIOUaeiou].*){3,}', na=False)]

```

    /var/folders/rz/zcgcqm0x1bl9cj8slq9l2s1c0000gn/T/ipykernel_10015/351328603.py:10: UserWarning: This pattern is interpreted as a regular expression, and has match groups. To actually get the groups, use str.extract.
      repeated_letters = bios[bios['name'].str.contains(r'(.)\1', na=False)]
    /var/folders/rz/zcgcqm0x1bl9cj8slq9l2s1c0000gn/T/ipykernel_10015/351328603.py:25: UserWarning: This pattern is interpreted as a regular expression, and has match groups. To actually get the groups, use str.extract.
      start_end_same = bios[bios['name'].str.contains(r'^(.).*\1$', na=False)]
    /var/folders/rz/zcgcqm0x1bl9cj8slq9l2s1c0000gn/T/ipykernel_10015/351328603.py:31: UserWarning: This pattern is interpreted as a regular expression, and has match groups. To actually get the groups, use str.extract.
      three_or_more_vowels = bios[bios['name'].str.contains(r'([AEIOUaeiou].*){3,}', na=False)]



```python
# Don't use regex search (exact match)
bios[bios['name'].str.contains('keith|patrick', case=False, regex=False)]
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
      <th>athlete_id</th>
      <th>name</th>
      <th>born_date</th>
      <th>born_city</th>
      <th>born_region</th>
      <th>born_country</th>
      <th>NOC</th>
      <th>height_cm</th>
      <th>weight_kg</th>
      <th>died_date</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
## isin method & startswith
bios[bios['born_country'].isin(["USA", "FRA", "GBR"]) & (bios['name'].str.startswith("Keith"))]
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
      <th>athlete_id</th>
      <th>name</th>
      <th>born_date</th>
      <th>born_city</th>
      <th>born_region</th>
      <th>born_country</th>
      <th>NOC</th>
      <th>height_cm</th>
      <th>weight_kg</th>
      <th>died_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3505</th>
      <td>3517</td>
      <td>Keith Wallace</td>
      <td>1961-03-29</td>
      <td>Preston</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>165.0</td>
      <td>51.0</td>
      <td>1999-12-31</td>
    </tr>
    <tr>
      <th>12053</th>
      <td>12118</td>
      <td>Keith Hervey</td>
      <td>1898-11-03</td>
      <td>Fulham</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1973-02-22</td>
    </tr>
    <tr>
      <th>14577</th>
      <td>14674</td>
      <td>Keith Harrison</td>
      <td>1933-03-28</td>
      <td>Birmingham</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16166</th>
      <td>16281</td>
      <td>Keith Reynolds</td>
      <td>1963-12-25</td>
      <td>Solihull</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>173.0</td>
      <td>68.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18734</th>
      <td>18862</td>
      <td>Keith Sinclair</td>
      <td>1945-06-26</td>
      <td>Sunderland</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>190.0</td>
      <td>79.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29897</th>
      <td>30123</td>
      <td>Keith Langley</td>
      <td>1961-06-03</td>
      <td>Aldershot</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>173.0</td>
      <td>70.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34011</th>
      <td>34275</td>
      <td>Keith Remfry</td>
      <td>1947-11-17</td>
      <td>Ealing</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>193.0</td>
      <td>114.0</td>
      <td>2015-09-16</td>
    </tr>
    <tr>
      <th>46885</th>
      <td>47234</td>
      <td>Keith Collin</td>
      <td>1937-01-18</td>
      <td>Marylebone</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>168.0</td>
      <td>63.0</td>
      <td>1991-03-06</td>
    </tr>
    <tr>
      <th>50929</th>
      <td>51288</td>
      <td>Keith Carter</td>
      <td>1924-08-30</td>
      <td>Akron</td>
      <td>Ohio</td>
      <td>USA</td>
      <td>United States</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2013-05-03</td>
    </tr>
    <tr>
      <th>51185</th>
      <td>51544</td>
      <td>Keith Russell</td>
      <td>1948-01-15</td>
      <td>Mesa</td>
      <td>Arizona</td>
      <td>USA</td>
      <td>United States</td>
      <td>188.0</td>
      <td>73.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>52913</th>
      <td>53288</td>
      <td>Keith Erickson</td>
      <td>1944-04-19</td>
      <td>San Francisco</td>
      <td>California</td>
      <td>USA</td>
      <td>United States</td>
      <td>196.0</td>
      <td>86.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>55317</th>
      <td>55712</td>
      <td>Keith Boxell</td>
      <td>1958-05-06</td>
      <td>Clapham</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>170.0</td>
      <td>87.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>57818</th>
      <td>58226</td>
      <td>Keith Peache</td>
      <td>1947-08-10</td>
      <td>Lewisham</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>180.0</td>
      <td>98.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>61748</th>
      <td>62202</td>
      <td>Keith Grogono</td>
      <td>1912-11-04</td>
      <td>Stratford</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1999-03-22</td>
    </tr>
    <tr>
      <th>62620</th>
      <td>63086</td>
      <td>Keith Musto</td>
      <td>1936-01-12</td>
      <td>Rochford</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>174.0</td>
      <td>72.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>62678</th>
      <td>63144</td>
      <td>Keith Notary</td>
      <td>1960-01-22</td>
      <td>Merritt Island</td>
      <td>Florida</td>
      <td>USA</td>
      <td>United States</td>
      <td>170.0</td>
      <td>66.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>68324</th>
      <td>68841</td>
      <td>Keith Angus</td>
      <td>1943-04-05</td>
      <td>Sheffield</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>170.0</td>
      <td>59.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>68472</th>
      <td>68989</td>
      <td>Keith Cullen</td>
      <td>1972-06-13</td>
      <td>Ilford</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>177.0</td>
      <td>61.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>68997</th>
      <td>69514</td>
      <td>Keith Stock</td>
      <td>1957-03-18</td>
      <td>Woolwich</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>176.0</td>
      <td>73.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>77550</th>
      <td>78141</td>
      <td>Keith Brantly</td>
      <td>1962-05-23</td>
      <td>Scott Air Force Base</td>
      <td>Illinois</td>
      <td>USA</td>
      <td>United States</td>
      <td>180.0</td>
      <td>64.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>84097</th>
      <td>84766</td>
      <td>Keith Christiansen</td>
      <td>1944-07-14</td>
      <td>International Falls</td>
      <td>Minnesota</td>
      <td>USA</td>
      <td>United States</td>
      <td>165.0</td>
      <td>69.0</td>
      <td>2018-11-05</td>
    </tr>
    <tr>
      <th>94646</th>
      <td>95413</td>
      <td>Keith Meyer</td>
      <td>1938-06-20</td>
      <td>Geneva</td>
      <td>Illinois</td>
      <td>USA</td>
      <td>United States</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2010-07-25</td>
    </tr>
    <tr>
      <th>95267</th>
      <td>96037</td>
      <td>Keith Oliver</td>
      <td>1947-10-27</td>
      <td>Liverpool</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>172.0</td>
      <td>68.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>96452</th>
      <td>97229</td>
      <td>Keith Schellenberg</td>
      <td>1929-03-13</td>
      <td>Middlesbrough</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2019-10-28</td>
    </tr>
    <tr>
      <th>97499</th>
      <td>98286</td>
      <td>Keith Tkachuk</td>
      <td>1972-03-28</td>
      <td>Melrose</td>
      <td>Massachusetts</td>
      <td>USA</td>
      <td>United States</td>
      <td>188.0</td>
      <td>102.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>98068</th>
      <td>98860</td>
      <td>Keith Wegeman</td>
      <td>1929-08-28</td>
      <td>Denver</td>
      <td>Colorado</td>
      <td>USA</td>
      <td>United States</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1974-08-22</td>
    </tr>
    <tr>
      <th>99921</th>
      <td>100722</td>
      <td>Keith Carney</td>
      <td>1970-02-03</td>
      <td>Providence</td>
      <td>Rhode Island</td>
      <td>USA</td>
      <td>United States</td>
      <td>188.0</td>
      <td>93.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>115973</th>
      <td>117348</td>
      <td>Keith Sanderson</td>
      <td>1975-02-02</td>
      <td>Plymouth</td>
      <td>Massachusetts</td>
      <td>USA</td>
      <td>United States</td>
      <td>183.0</td>
      <td>95.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
print("Make sure to smash that like button & subscribe tehehehe")
```

    Make sure to smash that like button & subscribe tehehehe


#### Query functions


```python
bios.query('born_country == "USA" and born_city == "Seattle"')
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
      <th>athlete_id</th>
      <th>name</th>
      <th>born_date</th>
      <th>born_city</th>
      <th>born_region</th>
      <th>born_country</th>
      <th>NOC</th>
      <th>height_cm</th>
      <th>weight_kg</th>
      <th>died_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11030</th>
      <td>11088</td>
      <td>David Halpern</td>
      <td>1955-08-18</td>
      <td>Seattle</td>
      <td>Washington</td>
      <td>USA</td>
      <td>United States</td>
      <td>178.0</td>
      <td>79.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12800</th>
      <td>12870</td>
      <td>Todd Trewin</td>
      <td>1958-04-20</td>
      <td>Seattle</td>
      <td>Washington</td>
      <td>USA</td>
      <td>United States</td>
      <td>180.0</td>
      <td>75.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15476</th>
      <td>15583</td>
      <td>Scott McKinley</td>
      <td>1968-10-15</td>
      <td>Seattle</td>
      <td>Washington</td>
      <td>USA</td>
      <td>United States</td>
      <td>183.0</td>
      <td>75.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29079</th>
      <td>29293</td>
      <td>Joyce Tanac</td>
      <td>1950-09-27</td>
      <td>Seattle</td>
      <td>Washington</td>
      <td>USA</td>
      <td>United States</td>
      <td>156.0</td>
      <td>49.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>31135</th>
      <td>31371</td>
      <td>Bill Kuhlemeier</td>
      <td>1908-01-14</td>
      <td>Seattle</td>
      <td>Washington</td>
      <td>USA</td>
      <td>United States</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2001-07-08</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>133392</th>
      <td>136331</td>
      <td>Hans Struzyna</td>
      <td>1989-03-31</td>
      <td>Seattle</td>
      <td>Washington</td>
      <td>USA</td>
      <td>United States</td>
      <td>188.0</td>
      <td>91.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>135448</th>
      <td>138662</td>
      <td>Maude Davis Crossland</td>
      <td>2003-03-19</td>
      <td>Seattle</td>
      <td>Washington</td>
      <td>USA</td>
      <td>Colombia</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>136993</th>
      <td>140229</td>
      <td>Jenell Berhorst</td>
      <td>2003-12-13</td>
      <td>Seattle</td>
      <td>Washington</td>
      <td>USA</td>
      <td>United States</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>143507</th>
      <td>147159</td>
      <td>Nevin Harrison</td>
      <td>2002-06-02</td>
      <td>Seattle</td>
      <td>Washington</td>
      <td>USA</td>
      <td>United States</td>
      <td>175.0</td>
      <td>73.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145446</th>
      <td>149169</td>
      <td>Corinne Stoddard</td>
      <td>2001-08-15</td>
      <td>Seattle</td>
      <td>Washington</td>
      <td>USA</td>
      <td>United States</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>102 rows × 10 columns</p>
</div>



## Adding / Removing Columns


```python
coffee.head()
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
      <th>Day</th>
      <th>Coffee Type</th>
      <th>Units Sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Monday</td>
      <td>Espresso</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Monday</td>
      <td>Latte</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tuesday</td>
      <td>Espresso</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tuesday</td>
      <td>Latte</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wednesday</td>
      <td>Espresso</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>




```python
coffee['price'] = 4.99
```


```python
coffee['new_price'] = np.where(coffee['Coffee Type']=='Espresso', 3.99, 5.99) 
```


```python
coffee
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
      <th>Day</th>
      <th>Coffee Type</th>
      <th>Units Sold</th>
      <th>price</th>
      <th>new_price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Monday</td>
      <td>Espresso</td>
      <td>25.0</td>
      <td>3.99</td>
      <td>3.99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Monday</td>
      <td>Latte</td>
      <td>10.0</td>
      <td>5.99</td>
      <td>5.99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tuesday</td>
      <td>Espresso</td>
      <td>NaN</td>
      <td>3.99</td>
      <td>3.99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tuesday</td>
      <td>Latte</td>
      <td>NaN</td>
      <td>5.99</td>
      <td>5.99</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wednesday</td>
      <td>Espresso</td>
      <td>35.0</td>
      <td>3.99</td>
      <td>3.99</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wednesday</td>
      <td>Latte</td>
      <td>25.0</td>
      <td>5.99</td>
      <td>5.99</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Thursday</td>
      <td>Espresso</td>
      <td>40.0</td>
      <td>3.99</td>
      <td>3.99</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Thursday</td>
      <td>Latte</td>
      <td>30.0</td>
      <td>5.99</td>
      <td>5.99</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Friday</td>
      <td>Espresso</td>
      <td>45.0</td>
      <td>3.99</td>
      <td>3.99</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Friday</td>
      <td>Latte</td>
      <td>35.0</td>
      <td>5.99</td>
      <td>5.99</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Saturday</td>
      <td>Espresso</td>
      <td>45.0</td>
      <td>3.99</td>
      <td>3.99</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Saturday</td>
      <td>Latte</td>
      <td>35.0</td>
      <td>5.99</td>
      <td>5.99</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Sunday</td>
      <td>Espresso</td>
      <td>45.0</td>
      <td>3.99</td>
      <td>3.99</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Sunday</td>
      <td>Latte</td>
      <td>35.0</td>
      <td>5.99</td>
      <td>5.99</td>
    </tr>
  </tbody>
</table>
</div>




```python
coffee.drop(columns=['price'], inplace=True)

# the below would also have worked
# coffee = coffee.drop(columns=['price'])
```


```python
coffee = coffee[['Day', 'Coffee Type', 'Units Sold', 'new_price']]
```


```python
coffee['revenue'] = coffee['Units Sold'] * coffee['new_price']
```


```python
coffee
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
      <th>Day</th>
      <th>Coffee Type</th>
      <th>Units Sold</th>
      <th>new_price</th>
      <th>revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Monday</td>
      <td>Espresso</td>
      <td>25.0</td>
      <td>3.99</td>
      <td>99.75</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Monday</td>
      <td>Latte</td>
      <td>10.0</td>
      <td>5.99</td>
      <td>59.90</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tuesday</td>
      <td>Espresso</td>
      <td>NaN</td>
      <td>3.99</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tuesday</td>
      <td>Latte</td>
      <td>NaN</td>
      <td>5.99</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wednesday</td>
      <td>Espresso</td>
      <td>35.0</td>
      <td>3.99</td>
      <td>139.65</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wednesday</td>
      <td>Latte</td>
      <td>25.0</td>
      <td>5.99</td>
      <td>149.75</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Thursday</td>
      <td>Espresso</td>
      <td>40.0</td>
      <td>3.99</td>
      <td>159.60</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Thursday</td>
      <td>Latte</td>
      <td>30.0</td>
      <td>5.99</td>
      <td>179.70</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Friday</td>
      <td>Espresso</td>
      <td>45.0</td>
      <td>3.99</td>
      <td>179.55</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Friday</td>
      <td>Latte</td>
      <td>35.0</td>
      <td>5.99</td>
      <td>209.65</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Saturday</td>
      <td>Espresso</td>
      <td>45.0</td>
      <td>3.99</td>
      <td>179.55</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Saturday</td>
      <td>Latte</td>
      <td>35.0</td>
      <td>5.99</td>
      <td>209.65</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Sunday</td>
      <td>Espresso</td>
      <td>45.0</td>
      <td>3.99</td>
      <td>179.55</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Sunday</td>
      <td>Latte</td>
      <td>35.0</td>
      <td>5.99</td>
      <td>209.65</td>
    </tr>
  </tbody>
</table>
</div>




```python
coffee.rename(columns={'new_price': 'price'}, inplace=True)
```


```python
bios_new = bios.copy()
```


```python
bios_new['first_name'] = bios_new['name'].str.split(' ').str[0]
```


```python
bios_new.query('first_name == "Keith"')
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
      <th>athlete_id</th>
      <th>name</th>
      <th>born_date</th>
      <th>born_city</th>
      <th>born_region</th>
      <th>born_country</th>
      <th>NOC</th>
      <th>height_cm</th>
      <th>weight_kg</th>
      <th>died_date</th>
      <th>first_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1897</th>
      <td>1907</td>
      <td>Keith Hanlon</td>
      <td>1966-09-01</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Ireland</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Keith</td>
    </tr>
    <tr>
      <th>3505</th>
      <td>3517</td>
      <td>Keith Wallace</td>
      <td>1961-03-29</td>
      <td>Preston</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>165.0</td>
      <td>51.0</td>
      <td>1999-12-31</td>
      <td>Keith</td>
    </tr>
    <tr>
      <th>6228</th>
      <td>6255</td>
      <td>Keith Hartley</td>
      <td>1940-10-15</td>
      <td>Vancouver</td>
      <td>British Columbia</td>
      <td>CAN</td>
      <td>Canada</td>
      <td>200.0</td>
      <td>85.0</td>
      <td>NaN</td>
      <td>Keith</td>
    </tr>
    <tr>
      <th>8898</th>
      <td>8946</td>
      <td>Keith Mwila</td>
      <td>1966-01-01</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Zambia</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1993-01-09</td>
      <td>Keith</td>
    </tr>
    <tr>
      <th>12053</th>
      <td>12118</td>
      <td>Keith Hervey</td>
      <td>1898-11-03</td>
      <td>Fulham</td>
      <td>England</td>
      <td>GBR</td>
      <td>Great Britain</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1973-02-22</td>
      <td>Keith</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>99921</th>
      <td>100722</td>
      <td>Keith Carney</td>
      <td>1970-02-03</td>
      <td>Providence</td>
      <td>Rhode Island</td>
      <td>USA</td>
      <td>United States</td>
      <td>188.0</td>
      <td>93.0</td>
      <td>NaN</td>
      <td>Keith</td>
    </tr>
    <tr>
      <th>102227</th>
      <td>103168</td>
      <td>Keith Beavers</td>
      <td>1983-02-09</td>
      <td>London</td>
      <td>Ontario</td>
      <td>CAN</td>
      <td>Canada</td>
      <td>185.0</td>
      <td>75.0</td>
      <td>NaN</td>
      <td>Keith</td>
    </tr>
    <tr>
      <th>109900</th>
      <td>111105</td>
      <td>Keith Cumberpatch</td>
      <td>1927-08-25</td>
      <td>Christchurch</td>
      <td>Canterbury</td>
      <td>NZL</td>
      <td>New Zealand</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2013-11-15</td>
      <td>Keith</td>
    </tr>
    <tr>
      <th>115973</th>
      <td>117348</td>
      <td>Keith Sanderson</td>
      <td>1975-02-02</td>
      <td>Plymouth</td>
      <td>Massachusetts</td>
      <td>USA</td>
      <td>United States</td>
      <td>183.0</td>
      <td>95.0</td>
      <td>NaN</td>
      <td>Keith</td>
    </tr>
    <tr>
      <th>122121</th>
      <td>124176</td>
      <td>Keith Ferguson</td>
      <td>1979-09-07</td>
      <td>Sale</td>
      <td>Victoria</td>
      <td>AUS</td>
      <td>Australia</td>
      <td>176.0</td>
      <td>78.0</td>
      <td>NaN</td>
      <td>Keith</td>
    </tr>
  </tbody>
</table>
<p>64 rows × 11 columns</p>
</div>




```python
bios_new['born_datetime'] = pd.to_datetime(bios_new['born_date'])
```


```python
bios_new['born_year'] = bios_new['born_datetime'].dt.year
```


```python
bios_new[['name','born_year']]
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
      <th>name</th>
      <th>born_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jean-François Blanchy</td>
      <td>1886.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Arnaud Boetsch</td>
      <td>1969.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jean Borotra</td>
      <td>1898.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jacques Brugnon</td>
      <td>1895.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Albert Canet</td>
      <td>1878.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>145495</th>
      <td>Polina Luchnikova</td>
      <td>2002.0</td>
    </tr>
    <tr>
      <th>145496</th>
      <td>Valeriya Merkusheva</td>
      <td>1999.0</td>
    </tr>
    <tr>
      <th>145497</th>
      <td>Yuliya Smirnova</td>
      <td>1998.0</td>
    </tr>
    <tr>
      <th>145498</th>
      <td>André Foussard</td>
      <td>1899.0</td>
    </tr>
    <tr>
      <th>145499</th>
      <td>Bill Phillips</td>
      <td>1913.0</td>
    </tr>
  </tbody>
</table>
<p>145500 rows × 2 columns</p>
</div>




```python
bios_new.to_csv('./data/bios_new.csv', index=False)
```


```python
bios['height_category'] = bios['height_cm'].apply(lambda x: 'Short' if x < 165 else ('Average' if x < 185 else 'Tall'))
```


```python
def categorize_athlete(row):
    if row['height_cm'] < 175 and row['weight_kg'] < 70:
        return 'Lightweight'
    elif row['height_cm'] < 185 or row['weight_kg'] <= 80:
        return 'Middleweight'
    
    else:
        return 'Heavyweight'
    
bios['Category'] = bios.apply(categorize_athlete, axis=1)
```


```python
bios.head()
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
      <th>athlete_id</th>
      <th>name</th>
      <th>born_date</th>
      <th>born_city</th>
      <th>born_region</th>
      <th>born_country</th>
      <th>NOC</th>
      <th>height_cm</th>
      <th>weight_kg</th>
      <th>died_date</th>
      <th>height_category</th>
      <th>Category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Jean-François Blanchy</td>
      <td>1886-12-12</td>
      <td>Bordeaux</td>
      <td>Gironde</td>
      <td>FRA</td>
      <td>France</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1960-10-02</td>
      <td>Tall</td>
      <td>Heavyweight</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Arnaud Boetsch</td>
      <td>1969-04-01</td>
      <td>Meulan</td>
      <td>Yvelines</td>
      <td>FRA</td>
      <td>France</td>
      <td>183.0</td>
      <td>76.0</td>
      <td>NaN</td>
      <td>Average</td>
      <td>Middleweight</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Jean Borotra</td>
      <td>1898-08-13</td>
      <td>Biarritz</td>
      <td>Pyrénées-Atlantiques</td>
      <td>FRA</td>
      <td>France</td>
      <td>183.0</td>
      <td>76.0</td>
      <td>1994-07-17</td>
      <td>Average</td>
      <td>Middleweight</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Jacques Brugnon</td>
      <td>1895-05-11</td>
      <td>Paris VIIIe</td>
      <td>Paris</td>
      <td>FRA</td>
      <td>France</td>
      <td>168.0</td>
      <td>64.0</td>
      <td>1978-03-20</td>
      <td>Average</td>
      <td>Lightweight</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Albert Canet</td>
      <td>1878-04-17</td>
      <td>Wandsworth</td>
      <td>England</td>
      <td>GBR</td>
      <td>France</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1930-07-25</td>
      <td>Tall</td>
      <td>Heavyweight</td>
    </tr>
  </tbody>
</table>
</div>



## Merging & Concatenating Data


```python
nocs = pd.read_csv('./data/noc_regions.csv')
```


```python
bios_new = pd.merge(bios, nocs, left_on='born_country', right_on='NOC', how='left')
```


```python
bios_new.rename(columns={'region': 'born_country_full'}, inplace=True)
```


```python
usa = bios[bios['born_country']=='USA'].copy()
gbr = bios[bios['born_country']=='GBR'].copy()
```


```python
new_df = pd.concat([usa,gbr])
```


```python
new_df.tail()
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
      <th>athlete_id</th>
      <th>name</th>
      <th>born_date</th>
      <th>born_city</th>
      <th>born_region</th>
      <th>born_country</th>
      <th>NOC</th>
      <th>height_cm</th>
      <th>weight_kg</th>
      <th>died_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>144811</th>
      <td>148512</td>
      <td>Benjamin Alexander</td>
      <td>1983-05-08</td>
      <td>London</td>
      <td>England</td>
      <td>GBR</td>
      <td>Jamaica</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>144815</th>
      <td>148517</td>
      <td>Ashley Watson</td>
      <td>1993-10-28</td>
      <td>Peterborough</td>
      <td>England</td>
      <td>GBR</td>
      <td>Jamaica</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145005</th>
      <td>148716</td>
      <td>Peder Kongshaug</td>
      <td>2001-08-13</td>
      <td>Wimbledon</td>
      <td>England</td>
      <td>GBR</td>
      <td>Norway</td>
      <td>184.0</td>
      <td>86.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145319</th>
      <td>149041</td>
      <td>Axel Brown</td>
      <td>1992-04-02</td>
      <td>Harrogate</td>
      <td>England</td>
      <td>GBR</td>
      <td>Trinidad and Tobago</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145388</th>
      <td>149111</td>
      <td>Jean-Luc Baker</td>
      <td>1993-10-07</td>
      <td>Burnley</td>
      <td>England</td>
      <td>GBR</td>
      <td>United States</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
combined_df = pd.merge(results, bios, on='athlete_id', how='left')
```


```python
combined_df.head()
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
      <th>year</th>
      <th>type</th>
      <th>discipline</th>
      <th>event</th>
      <th>as</th>
      <th>athlete_id</th>
      <th>noc</th>
      <th>team</th>
      <th>place</th>
      <th>tied</th>
      <th>medal</th>
      <th>name</th>
      <th>born_date</th>
      <th>born_city</th>
      <th>born_region</th>
      <th>born_country</th>
      <th>NOC</th>
      <th>height_cm</th>
      <th>weight_kg</th>
      <th>died_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1912.0</td>
      <td>Summer</td>
      <td>Tennis</td>
      <td>Singles, Men (Olympic)</td>
      <td>Jean-François Blanchy</td>
      <td>1</td>
      <td>FRA</td>
      <td>None</td>
      <td>17.0</td>
      <td>True</td>
      <td>None</td>
      <td>Jean-François Blanchy</td>
      <td>1886-12-12</td>
      <td>Bordeaux</td>
      <td>Gironde</td>
      <td>FRA</td>
      <td>France</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1960-10-02</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1912.0</td>
      <td>Summer</td>
      <td>Tennis</td>
      <td>Doubles, Men (Olympic)</td>
      <td>Jean-François Blanchy</td>
      <td>1</td>
      <td>FRA</td>
      <td>Jean Montariol</td>
      <td>NaN</td>
      <td>False</td>
      <td>None</td>
      <td>Jean-François Blanchy</td>
      <td>1886-12-12</td>
      <td>Bordeaux</td>
      <td>Gironde</td>
      <td>FRA</td>
      <td>France</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1960-10-02</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1920.0</td>
      <td>Summer</td>
      <td>Tennis</td>
      <td>Singles, Men (Olympic)</td>
      <td>Jean-François Blanchy</td>
      <td>1</td>
      <td>FRA</td>
      <td>None</td>
      <td>32.0</td>
      <td>True</td>
      <td>None</td>
      <td>Jean-François Blanchy</td>
      <td>1886-12-12</td>
      <td>Bordeaux</td>
      <td>Gironde</td>
      <td>FRA</td>
      <td>France</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1960-10-02</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1920.0</td>
      <td>Summer</td>
      <td>Tennis</td>
      <td>Doubles, Mixed (Olympic)</td>
      <td>Jean-François Blanchy</td>
      <td>1</td>
      <td>FRA</td>
      <td>Jeanne Vaussard</td>
      <td>8.0</td>
      <td>True</td>
      <td>None</td>
      <td>Jean-François Blanchy</td>
      <td>1886-12-12</td>
      <td>Bordeaux</td>
      <td>Gironde</td>
      <td>FRA</td>
      <td>France</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1960-10-02</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1920.0</td>
      <td>Summer</td>
      <td>Tennis</td>
      <td>Doubles, Men (Olympic)</td>
      <td>Jean-François Blanchy</td>
      <td>1</td>
      <td>FRA</td>
      <td>Jacques Brugnon</td>
      <td>4.0</td>
      <td>False</td>
      <td>None</td>
      <td>Jean-François Blanchy</td>
      <td>1886-12-12</td>
      <td>Bordeaux</td>
      <td>Gironde</td>
      <td>FRA</td>
      <td>France</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1960-10-02</td>
    </tr>
  </tbody>
</table>
</div>



## Handling Null Values


```python
coffee.loc[[2,3], 'Units Sold'] = np.nan
```


```python
# Make sure to set this to your Units Sold column if you want these changes to stick
coffee['Units Sold'].fillna(coffee['Units Sold'].mean()) 
```




    0     25.00
    1     10.00
    2     33.75
    3     33.75
    4     35.00
    5     25.00
    6     40.00
    7     30.00
    8     45.00
    9     35.00
    10    45.00
    11    35.00
    12    45.00
    13    35.00
    Name: Units Sold, dtype: float64




```python
# coffee['Units Sold'] = coffee['Units Sold'].interpolate()
coffee['Units Sold'].interpolate()
```




    0     25.000000
    1     10.000000
    2     18.333333
    3     26.666667
    4     35.000000
    5     25.000000
    6     40.000000
    7     30.000000
    8     45.000000
    9     35.000000
    10    45.000000
    11    35.000000
    12    45.000000
    13    35.000000
    Name: Units Sold, dtype: float64




```python
coffee.dropna(subset=['Units Sold']) # Use inplace=True if you want to update the coffee df
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
      <th>Day</th>
      <th>Coffee Type</th>
      <th>Units Sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Monday</td>
      <td>Espresso</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Monday</td>
      <td>Latte</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wednesday</td>
      <td>Espresso</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wednesday</td>
      <td>Latte</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Thursday</td>
      <td>Espresso</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Thursday</td>
      <td>Latte</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Friday</td>
      <td>Espresso</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Friday</td>
      <td>Latte</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Saturday</td>
      <td>Espresso</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Saturday</td>
      <td>Latte</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Sunday</td>
      <td>Espresso</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Sunday</td>
      <td>Latte</td>
      <td>35.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
coffee[coffee['Units Sold'].notna()]
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
      <th>Day</th>
      <th>Coffee Type</th>
      <th>Units Sold</th>
      <th>price</th>
      <th>revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Monday</td>
      <td>Espresso</td>
      <td>15.0</td>
      <td>3.99</td>
      <td>99.75</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Monday</td>
      <td>Latte</td>
      <td>15.0</td>
      <td>5.99</td>
      <td>89.85</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wednesday</td>
      <td>Espresso</td>
      <td>35.0</td>
      <td>3.99</td>
      <td>139.65</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wednesday</td>
      <td>Latte</td>
      <td>25.0</td>
      <td>5.99</td>
      <td>149.75</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Thursday</td>
      <td>Espresso</td>
      <td>40.0</td>
      <td>3.99</td>
      <td>159.60</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Thursday</td>
      <td>Latte</td>
      <td>30.0</td>
      <td>5.99</td>
      <td>179.70</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Friday</td>
      <td>Espresso</td>
      <td>45.0</td>
      <td>3.99</td>
      <td>179.55</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Friday</td>
      <td>Latte</td>
      <td>35.0</td>
      <td>5.99</td>
      <td>209.65</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Saturday</td>
      <td>Espresso</td>
      <td>45.0</td>
      <td>3.99</td>
      <td>179.55</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Saturday</td>
      <td>Latte</td>
      <td>35.0</td>
      <td>5.99</td>
      <td>209.65</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Sunday</td>
      <td>Espresso</td>
      <td>45.0</td>
      <td>3.99</td>
      <td>179.55</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Sunday</td>
      <td>Latte</td>
      <td>35.0</td>
      <td>5.99</td>
      <td>209.65</td>
    </tr>
  </tbody>
</table>
</div>




```python
coffee
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
      <th>Day</th>
      <th>Coffee Type</th>
      <th>Units Sold</th>
      <th>price</th>
      <th>revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Monday</td>
      <td>Espresso</td>
      <td>15.000000</td>
      <td>3.99</td>
      <td>99.75</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Monday</td>
      <td>Latte</td>
      <td>15.000000</td>
      <td>5.99</td>
      <td>89.85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tuesday</td>
      <td>Espresso</td>
      <td>21.666667</td>
      <td>3.99</td>
      <td>119.70</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tuesday</td>
      <td>Latte</td>
      <td>28.333333</td>
      <td>5.99</td>
      <td>119.80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wednesday</td>
      <td>Espresso</td>
      <td>35.000000</td>
      <td>3.99</td>
      <td>139.65</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wednesday</td>
      <td>Latte</td>
      <td>25.000000</td>
      <td>5.99</td>
      <td>149.75</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Thursday</td>
      <td>Espresso</td>
      <td>40.000000</td>
      <td>3.99</td>
      <td>159.60</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Thursday</td>
      <td>Latte</td>
      <td>30.000000</td>
      <td>5.99</td>
      <td>179.70</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Friday</td>
      <td>Espresso</td>
      <td>45.000000</td>
      <td>3.99</td>
      <td>179.55</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Friday</td>
      <td>Latte</td>
      <td>35.000000</td>
      <td>5.99</td>
      <td>209.65</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Saturday</td>
      <td>Espresso</td>
      <td>45.000000</td>
      <td>3.99</td>
      <td>179.55</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Saturday</td>
      <td>Latte</td>
      <td>35.000000</td>
      <td>5.99</td>
      <td>209.65</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Sunday</td>
      <td>Espresso</td>
      <td>45.000000</td>
      <td>3.99</td>
      <td>179.55</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Sunday</td>
      <td>Latte</td>
      <td>35.000000</td>
      <td>5.99</td>
      <td>209.65</td>
    </tr>
  </tbody>
</table>
</div>



## Aggregating Data


```python
bios.head()
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
      <th>athlete_id</th>
      <th>name</th>
      <th>born_date</th>
      <th>born_city</th>
      <th>born_region</th>
      <th>born_country</th>
      <th>NOC</th>
      <th>height_cm</th>
      <th>weight_kg</th>
      <th>died_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Jean-François Blanchy</td>
      <td>1886-12-12</td>
      <td>Bordeaux</td>
      <td>Gironde</td>
      <td>FRA</td>
      <td>France</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1960-10-02</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Arnaud Boetsch</td>
      <td>1969-04-01</td>
      <td>Meulan</td>
      <td>Yvelines</td>
      <td>FRA</td>
      <td>France</td>
      <td>183.0</td>
      <td>76.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Jean Borotra</td>
      <td>1898-08-13</td>
      <td>Biarritz</td>
      <td>Pyrénées-Atlantiques</td>
      <td>FRA</td>
      <td>France</td>
      <td>183.0</td>
      <td>76.0</td>
      <td>1994-07-17</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Jacques Brugnon</td>
      <td>1895-05-11</td>
      <td>Paris VIIIe</td>
      <td>Paris</td>
      <td>FRA</td>
      <td>France</td>
      <td>168.0</td>
      <td>64.0</td>
      <td>1978-03-20</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Albert Canet</td>
      <td>1878-04-17</td>
      <td>Wandsworth</td>
      <td>England</td>
      <td>GBR</td>
      <td>France</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1930-07-25</td>
    </tr>
  </tbody>
</table>
</div>




```python
bios['born_city'].value_counts()
```




    born_city
    Budapest           1378
    Moskva (Moscow)     883
    Oslo                708
    Stockholm           629
    Praha (Prague)      600
                       ... 
    Bodrogkisfalud        1
    Ternberg              1
    Klaus                 1
    Plaški                1
    Dulwich Hill          1
    Name: count, Length: 22368, dtype: int64




```python
bios[bios['born_country']=='USA']['born_region'].value_counts().head(10)
```




    born_region
    California       1634
    New York          990
    Illinois          585
    Pennsylvania      530
    Massachusetts     530
    New Jersey        381
    Texas             368
    Minnesota         365
    Ohio              328
    Michigan          319
    Name: count, dtype: int64




```python
bios[bios['born_country']=='USA']['born_region'].value_counts().tail(25)
```




    born_region
    Utah              91
    Missouri          91
    North Carolina    86
    Arizona           83
    New Hampshire     83
    Vermont           68
    Mississippi       66
    Alabama           64
    Kentucky          62
    Tennessee         62
    Nebraska          60
    Rhode Island      56
    Montana           55
    South Carolina    50
    Maine             50
    Alaska            45
    Arkansas          42
    Idaho             41
    New Mexico        38
    Nevada            36
    South Dakota      27
    West Virginia     24
    Delaware          22
    North Dakota      16
    Wyoming           14
    Name: count, dtype: int64



#### Groupby function in Pandas


```python
coffee.groupby(['Coffee Type'])['Units Sold'].sum()
```




    Coffee Type
    Espresso    235.0
    Latte       170.0
    Name: Units Sold, dtype: float64




```python
coffee.groupby(['Coffee Type'])['Units Sold'].mean()
```




    Coffee Type
    Espresso    39.166667
    Latte       28.333333
    Name: Units Sold, dtype: float64




```python
coffee.groupby(['Coffee Type', 'Day']).agg({'Units Sold': 'sum', 'price': 'mean'})
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
      <th></th>
      <th>Units Sold</th>
      <th>price</th>
    </tr>
    <tr>
      <th>Coffee Type</th>
      <th>Day</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="7" valign="top">Espresso</th>
      <th>Friday</th>
      <td>45.0</td>
      <td>3.99</td>
    </tr>
    <tr>
      <th>Monday</th>
      <td>25.0</td>
      <td>3.99</td>
    </tr>
    <tr>
      <th>Saturday</th>
      <td>45.0</td>
      <td>3.99</td>
    </tr>
    <tr>
      <th>Sunday</th>
      <td>45.0</td>
      <td>3.99</td>
    </tr>
    <tr>
      <th>Thursday</th>
      <td>40.0</td>
      <td>3.99</td>
    </tr>
    <tr>
      <th>Tuesday</th>
      <td>0.0</td>
      <td>3.99</td>
    </tr>
    <tr>
      <th>Wednesday</th>
      <td>35.0</td>
      <td>3.99</td>
    </tr>
    <tr>
      <th rowspan="7" valign="top">Latte</th>
      <th>Friday</th>
      <td>35.0</td>
      <td>5.99</td>
    </tr>
    <tr>
      <th>Monday</th>
      <td>10.0</td>
      <td>5.99</td>
    </tr>
    <tr>
      <th>Saturday</th>
      <td>35.0</td>
      <td>5.99</td>
    </tr>
    <tr>
      <th>Sunday</th>
      <td>35.0</td>
      <td>5.99</td>
    </tr>
    <tr>
      <th>Thursday</th>
      <td>30.0</td>
      <td>5.99</td>
    </tr>
    <tr>
      <th>Tuesday</th>
      <td>0.0</td>
      <td>5.99</td>
    </tr>
    <tr>
      <th>Wednesday</th>
      <td>25.0</td>
      <td>5.99</td>
    </tr>
  </tbody>
</table>
</div>



#### Pivot Tables


```python
pivot = coffee.pivot(columns='Coffee Type', index='Day', values='revenue')
```


```python
pivot.sum()
```




    Coffee Type
    Espresso     937.65
    Latte       1018.30
    dtype: float64




```python
pivot.sum(axis=1)
```




    Day
    Friday       389.20
    Monday       159.65
    Saturday     389.20
    Sunday       389.20
    Thursday     339.30
    Tuesday        0.00
    Wednesday    289.40
    dtype: float64



#### Using datetime with Groupby


```python
bios['born_date'] = pd.to_datetime(bios['born_date'])
bios['month_born'] = bios['born_date'].dt.month
bios['year_born'] = bios['born_date'].dt.year
bios.groupby([bios['year_born'],bios['month_born']])['name'].count().reset_index().sort_values('name', ascending=False)
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
      <th>year_born</th>
      <th>month_born</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1437</th>
      <td>1970.0</td>
      <td>1.0</td>
      <td>239</td>
    </tr>
    <tr>
      <th>1461</th>
      <td>1972.0</td>
      <td>1.0</td>
      <td>229</td>
    </tr>
    <tr>
      <th>1629</th>
      <td>1986.0</td>
      <td>1.0</td>
      <td>227</td>
    </tr>
    <tr>
      <th>1497</th>
      <td>1975.0</td>
      <td>1.0</td>
      <td>227</td>
    </tr>
    <tr>
      <th>1617</th>
      <td>1985.0</td>
      <td>1.0</td>
      <td>225</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>1857.0</td>
      <td>5.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>96</th>
      <td>1857.0</td>
      <td>7.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>97</th>
      <td>1857.0</td>
      <td>8.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>98</th>
      <td>1857.0</td>
      <td>9.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1884</th>
      <td>2009.0</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>1885 rows × 3 columns</p>
</div>



## Advanced Functionality


```python
# shift() rank() cumsum() rolling()
```


```python

```


```python
latte = coffee[coffee['Coffee Type']=="Latte"].copy()
latte['3day'] = latte['Units Sold'].rolling(3).sum()
```


```python
latte
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
      <th>Day</th>
      <th>Coffee Type</th>
      <th>Units Sold</th>
      <th>price</th>
      <th>revenue</th>
      <th>yesterday_revenue</th>
      <th>pct_change</th>
      <th>cumulative_revenue</th>
      <th>3day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Monday</td>
      <td>Latte</td>
      <td>15.000000</td>
      <td>5.99</td>
      <td>89.85</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>189.6</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tuesday</td>
      <td>Latte</td>
      <td>28.333333</td>
      <td>5.99</td>
      <td>119.80</td>
      <td>89.85</td>
      <td>133.333333</td>
      <td>429.1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wednesday</td>
      <td>Latte</td>
      <td>25.000000</td>
      <td>5.99</td>
      <td>149.75</td>
      <td>119.80</td>
      <td>125.000000</td>
      <td>718.5</td>
      <td>68.333333</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Thursday</td>
      <td>Latte</td>
      <td>30.000000</td>
      <td>5.99</td>
      <td>179.70</td>
      <td>149.75</td>
      <td>120.000000</td>
      <td>1057.8</td>
      <td>83.333333</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Friday</td>
      <td>Latte</td>
      <td>35.000000</td>
      <td>5.99</td>
      <td>209.65</td>
      <td>179.70</td>
      <td>116.666667</td>
      <td>1447.0</td>
      <td>90.000000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Saturday</td>
      <td>Latte</td>
      <td>35.000000</td>
      <td>5.99</td>
      <td>209.65</td>
      <td>209.65</td>
      <td>100.000000</td>
      <td>1836.2</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Sunday</td>
      <td>Latte</td>
      <td>35.000000</td>
      <td>5.99</td>
      <td>209.65</td>
      <td>209.65</td>
      <td>100.000000</td>
      <td>2225.4</td>
      <td>105.000000</td>
    </tr>
  </tbody>
</table>
</div>



```python

```

## Advanced Functionality (cont.)
These two libraries didn't actually make it into final video



```python
!pip install pyjanitor
```


```python
import janitor

coffee.clean_names()
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
      <th>day</th>
      <th>coffee_type</th>
      <th>units_sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Monday</td>
      <td>Espresso</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Monday</td>
      <td>Latte</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tuesday</td>
      <td>Espresso</td>
      <td>30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tuesday</td>
      <td>Latte</td>
      <td>20</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wednesday</td>
      <td>Espresso</td>
      <td>35</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wednesday</td>
      <td>Latte</td>
      <td>25</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Thursday</td>
      <td>Espresso</td>
      <td>40</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Thursday</td>
      <td>Latte</td>
      <td>30</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Friday</td>
      <td>Espresso</td>
      <td>45</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Friday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Saturday</td>
      <td>Espresso</td>
      <td>45</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Saturday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Sunday</td>
      <td>Espresso</td>
      <td>45</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Sunday</td>
      <td>Latte</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>




```python
!pip install skimpy
```


```python
from skimpy import skim

skim(results)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">╭──────────────────────────────────────────────── skimpy summary ─────────────────────────────────────────────────╮
│ <span style="font-style: italic">         Data Summary         </span> <span style="font-style: italic">      Data Types       </span>                                                          │
│ ┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓ ┏━━━━━━━━━━━━━┳━━━━━━━┓                                                          │
│ ┃<span style="color: #008080; text-decoration-color: #008080; font-weight: bold"> dataframe         </span>┃<span style="color: #008080; text-decoration-color: #008080; font-weight: bold"> Values </span>┃ ┃<span style="color: #008080; text-decoration-color: #008080; font-weight: bold"> Column Type </span>┃<span style="color: #008080; text-decoration-color: #008080; font-weight: bold"> Count </span>┃                                                          │
│ ┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩ ┡━━━━━━━━━━━━━╇━━━━━━━┩                                                          │
│ │ Number of rows    │ 308408 │ │ string      │ 7     │                                                          │
│ │ Number of columns │ 11     │ │ float64     │ 2     │                                                          │
│ └───────────────────┴────────┘ │ int64       │ 1     │                                                          │
│                                │ bool        │ 1     │                                                          │
│                                └─────────────┴───────┘                                                          │
│ <span style="font-style: italic">                                                    number                                                    </span>  │
│ ┏━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┓  │
│ ┃<span style="font-weight: bold"> column_name    </span>┃<span style="font-weight: bold"> NA      </span>┃<span style="font-weight: bold"> NA %  </span>┃<span style="font-weight: bold"> mean   </span>┃<span style="font-weight: bold"> sd     </span>┃<span style="font-weight: bold"> p0    </span>┃<span style="font-weight: bold"> p25    </span>┃<span style="font-weight: bold"> p50    </span>┃<span style="font-weight: bold"> p75     </span>┃<span style="font-weight: bold"> p100    </span>┃<span style="font-weight: bold"> hist    </span>┃  │
│ ┡━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━┩  │
│ │ <span style="color: #af87ff; text-decoration-color: #af87ff">year          </span> │ <span style="color: #008080; text-decoration-color: #008080">   2601</span> │ <span style="color: #008080; text-decoration-color: #008080"> 0.84</span> │ <span style="color: #008080; text-decoration-color: #008080">  2000</span> │ <span style="color: #008080; text-decoration-color: #008080">    31</span> │ <span style="color: #008080; text-decoration-color: #008080"> 1900</span> │ <span style="color: #008080; text-decoration-color: #008080">  2000</span> │ <span style="color: #008080; text-decoration-color: #008080">  2000</span> │ <span style="color: #008080; text-decoration-color: #008080">   2000</span> │ <span style="color: #008080; text-decoration-color: #008080">   2000</span> │ <span style="color: #008000; text-decoration-color: #008000">▁▂▂▅▇▇ </span> │  │
│ │ <span style="color: #af87ff; text-decoration-color: #af87ff">athlete_id    </span> │ <span style="color: #008080; text-decoration-color: #008080">      0</span> │ <span style="color: #008080; text-decoration-color: #008080">    0</span> │ <span style="color: #008080; text-decoration-color: #008080"> 73000</span> │ <span style="color: #008080; text-decoration-color: #008080"> 41000</span> │ <span style="color: #008080; text-decoration-color: #008080">    1</span> │ <span style="color: #008080; text-decoration-color: #008080"> 34000</span> │ <span style="color: #008080; text-decoration-color: #008080"> 74000</span> │ <span style="color: #008080; text-decoration-color: #008080"> 110000</span> │ <span style="color: #008080; text-decoration-color: #008080"> 150000</span> │ <span style="color: #008000; text-decoration-color: #008000">▆▇▆▇▇▅ </span> │  │
│ │ <span style="color: #af87ff; text-decoration-color: #af87ff">place         </span> │ <span style="color: #008080; text-decoration-color: #008080">  25215</span> │ <span style="color: #008080; text-decoration-color: #008080"> 8.18</span> │ <span style="color: #008080; text-decoration-color: #008080">    16</span> │ <span style="color: #008080; text-decoration-color: #008080">    19</span> │ <span style="color: #008080; text-decoration-color: #008080">    1</span> │ <span style="color: #008080; text-decoration-color: #008080">     5</span> │ <span style="color: #008080; text-decoration-color: #008080">     9</span> │ <span style="color: #008080; text-decoration-color: #008080">     20</span> │ <span style="color: #008080; text-decoration-color: #008080">    180</span> │ <span style="color: #008000; text-decoration-color: #008000">  ▇▁   </span> │  │
│ └────────────────┴─────────┴───────┴────────┴────────┴───────┴────────┴────────┴─────────┴─────────┴─────────┘  │
│ <span style="font-style: italic">                                                     bool                                                     </span>  │
│ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓  │
│ ┃<span style="font-weight: bold"> column_name                       </span>┃<span style="font-weight: bold"> true              </span>┃<span style="font-weight: bold"> true rate                    </span>┃<span style="font-weight: bold"> hist                </span>┃  │
│ ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩  │
│ │ <span style="color: #af87ff; text-decoration-color: #af87ff">tied                             </span> │ <span style="color: #008080; text-decoration-color: #008080">            45940</span> │ <span style="color: #008080; text-decoration-color: #008080">                        0.15</span> │ <span style="color: #008000; text-decoration-color: #008000">      ▇    ▁       </span> │  │
│ └───────────────────────────────────┴───────────────────┴──────────────────────────────┴─────────────────────┘  │
│ <span style="font-style: italic">                                                    string                                                    </span>  │
│ ┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓  │
│ ┃<span style="font-weight: bold"> column_name             </span>┃<span style="font-weight: bold"> NA            </span>┃<span style="font-weight: bold"> NA %        </span>┃<span style="font-weight: bold"> words per row              </span>┃<span style="font-weight: bold"> total words           </span>┃  │
│ ┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩  │
│ │ <span style="color: #af87ff; text-decoration-color: #af87ff">type                   </span> │ <span style="color: #008080; text-decoration-color: #008080">         2601</span> │ <span style="color: #008080; text-decoration-color: #008080">       0.84</span> │ <span style="color: #008080; text-decoration-color: #008080">                      0.99</span> │ <span style="color: #008080; text-decoration-color: #008080">               305807</span> │  │
│ │ <span style="color: #af87ff; text-decoration-color: #af87ff">discipline             </span> │ <span style="color: #008080; text-decoration-color: #008080">            1</span> │ <span style="color: #008080; text-decoration-color: #008080">          0</span> │ <span style="color: #008080; text-decoration-color: #008080">                         2</span> │ <span style="color: #008080; text-decoration-color: #008080">               610211</span> │  │
│ │ <span style="color: #af87ff; text-decoration-color: #af87ff">event                  </span> │ <span style="color: #008080; text-decoration-color: #008080">            0</span> │ <span style="color: #008080; text-decoration-color: #008080">          0</span> │ <span style="color: #008080; text-decoration-color: #008080">                       4.2</span> │ <span style="color: #008080; text-decoration-color: #008080">              1303323</span> │  │
│ │ <span style="color: #af87ff; text-decoration-color: #af87ff">as                     </span> │ <span style="color: #008080; text-decoration-color: #008080">            0</span> │ <span style="color: #008080; text-decoration-color: #008080">          0</span> │ <span style="color: #008080; text-decoration-color: #008080">                       2.1</span> │ <span style="color: #008080; text-decoration-color: #008080">               634574</span> │  │
│ │ <span style="color: #af87ff; text-decoration-color: #af87ff">noc                    </span> │ <span style="color: #008080; text-decoration-color: #008080">            1</span> │ <span style="color: #008080; text-decoration-color: #008080">          0</span> │ <span style="color: #008080; text-decoration-color: #008080">                         1</span> │ <span style="color: #008080; text-decoration-color: #008080">               308407</span> │  │
│ │ <span style="color: #af87ff; text-decoration-color: #af87ff">team                   </span> │ <span style="color: #008080; text-decoration-color: #008080">       186694</span> │ <span style="color: #008080; text-decoration-color: #008080">      60.53</span> │ <span style="color: #008080; text-decoration-color: #008080">                      0.62</span> │ <span style="color: #008080; text-decoration-color: #008080">               190405</span> │  │
│ │ <span style="color: #af87ff; text-decoration-color: #af87ff">medal                  </span> │ <span style="color: #008080; text-decoration-color: #008080">       264269</span> │ <span style="color: #008080; text-decoration-color: #008080">      85.69</span> │ <span style="color: #008080; text-decoration-color: #008080">                      0.14</span> │ <span style="color: #008080; text-decoration-color: #008080">                44139</span> │  │
│ └─────────────────────────┴───────────────┴─────────────┴────────────────────────────┴───────────────────────┘  │
╰────────────────────────────────────────────────────── End ──────────────────────────────────────────────────────╯
</pre>




```python
coffee.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 14 entries, 0 to 13
    Data columns (total 7 columns):
     #   Column             Non-Null Count  Dtype  
    ---  ------             --------------  -----  
     0   Day                14 non-null     object 
     1   Coffee Type        14 non-null     object 
     2   Units Sold         14 non-null     float64
     3   price              14 non-null     float64
     4   revenue            14 non-null     float64
     5   yesterday_revenue  12 non-null     float64
     6   pct_change         12 non-null     float64
    dtypes: float64(5), object(2)
    memory usage: 916.0+ bytes


## New Functionality


```python
results_numpy = pd.read_csv('./data/results.csv')
results_arrow = pd.read_csv('./data/results.csv', engine='pyarrow', dtype_backend='pyarrow')
```


```python
results_numpy.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 308408 entries, 0 to 308407
    Data columns (total 11 columns):
     #   Column      Non-Null Count   Dtype  
    ---  ------      --------------   -----  
     0   year        305807 non-null  float64
     1   type        305807 non-null  object 
     2   discipline  308407 non-null  object 
     3   event       308408 non-null  object 
     4   as          308408 non-null  object 
     5   athlete_id  308408 non-null  int64  
     6   noc         308407 non-null  object 
     7   team        121714 non-null  object 
     8   place       283193 non-null  float64
     9   tied        308408 non-null  bool   
     10  medal       44139 non-null   object 
    dtypes: bool(1), float64(2), int64(1), object(7)
    memory usage: 23.8+ MB



```python
results_arrow.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 308408 entries, 0 to 308407
    Data columns (total 11 columns):
     #   Column      Non-Null Count   Dtype          
    ---  ------      --------------   -----          
     0   year        305807 non-null  double[pyarrow]
     1   type        305807 non-null  string[pyarrow]
     2   discipline  308407 non-null  string[pyarrow]
     3   event       308408 non-null  string[pyarrow]
     4   as          308408 non-null  string[pyarrow]
     5   athlete_id  308408 non-null  int64[pyarrow] 
     6   noc         308407 non-null  string[pyarrow]
     7   team        121714 non-null  string[pyarrow]
     8   place       283193 non-null  double[pyarrow]
     9   tied        308408 non-null  bool[pyarrow]  
     10  medal       44139 non-null   string[pyarrow]
    dtypes: bool[pyarrow](1), double[pyarrow](2), int64[pyarrow](1), string[pyarrow](7)
    memory usage: 37.5 MB



```python
filtered_bios = bios[(bios['born_region'] == 'New Hampshire') | (bios['born_city'] == 'San Francisco')]

bios.head()
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
      <th>athlete_id</th>
      <th>name</th>
      <th>born_date</th>
      <th>born_city</th>
      <th>born_region</th>
      <th>born_country</th>
      <th>NOC</th>
      <th>height_cm</th>
      <th>weight_kg</th>
      <th>died_date</th>
      <th>month_born</th>
      <th>year_born</th>
      <th>height_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Jean-François Blanchy</td>
      <td>1886-12-12</td>
      <td>Bordeaux</td>
      <td>Gironde</td>
      <td>FRA</td>
      <td>France</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1960-10-02</td>
      <td>12.0</td>
      <td>1886.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Arnaud Boetsch</td>
      <td>1969-04-01</td>
      <td>Meulan</td>
      <td>Yvelines</td>
      <td>FRA</td>
      <td>France</td>
      <td>183.0</td>
      <td>76.0</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>1969.0</td>
      <td>27597.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Jean Borotra</td>
      <td>1898-08-13</td>
      <td>Biarritz</td>
      <td>Pyrénées-Atlantiques</td>
      <td>FRA</td>
      <td>France</td>
      <td>183.0</td>
      <td>76.0</td>
      <td>1994-07-17</td>
      <td>8.0</td>
      <td>1898.0</td>
      <td>27597.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Jacques Brugnon</td>
      <td>1895-05-11</td>
      <td>Paris VIIIe</td>
      <td>Paris</td>
      <td>FRA</td>
      <td>France</td>
      <td>168.0</td>
      <td>64.0</td>
      <td>1978-03-20</td>
      <td>5.0</td>
      <td>1895.0</td>
      <td>83975.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Albert Canet</td>
      <td>1878-04-17</td>
      <td>Wandsworth</td>
      <td>England</td>
      <td>GBR</td>
      <td>France</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1930-07-25</td>
      <td>4.0</td>
      <td>1878.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
import pandas as pd

# Creating a DataFrame
data = {
    'Date': ['2024-05-01', '2024-05-01', '2024-05-01', '2024-05-02', '2024-05-02', '2024-05-03', '2024-05-03', '2024-05-03'],
    'Item': ['Apple', 'Banana', 'Orange', 'Apple', 'Banana', 'Orange', 'Apple', 'Orange'],
    'Units Sold': [30, 21, 15, 40, 34, 20, 45, 25],
    'Price Per Unit': [1.0, 0.5, 0.75, 1.0, 0.5, 0.75, 1.0, 0.75],
    'Salesperson': ['John', 'John', 'John', 'Alice', 'Alice', 'John', 'Alice', 'John']
}

df = pd.DataFrame(data)

# Display the DataFrame
df

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
      <th>Date</th>
      <th>Item</th>
      <th>Units Sold</th>
      <th>Price Per Unit</th>
      <th>Salesperson</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-05-01</td>
      <td>Apple</td>
      <td>30</td>
      <td>1.00</td>
      <td>John</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-05-01</td>
      <td>Banana</td>
      <td>21</td>
      <td>0.50</td>
      <td>John</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-05-01</td>
      <td>Orange</td>
      <td>15</td>
      <td>0.75</td>
      <td>John</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-05-02</td>
      <td>Apple</td>
      <td>40</td>
      <td>1.00</td>
      <td>Alice</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-05-02</td>
      <td>Banana</td>
      <td>34</td>
      <td>0.50</td>
      <td>Alice</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-05-03</td>
      <td>Orange</td>
      <td>20</td>
      <td>0.75</td>
      <td>John</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-05-03</td>
      <td>Apple</td>
      <td>45</td>
      <td>1.00</td>
      <td>Alice</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-05-03</td>
      <td>Orange</td>
      <td>25</td>
      <td>0.75</td>
      <td>John</td>
    </tr>
  </tbody>
</table>
</div>




```python
pivot_table = pd.pivot_table(df, values='Units Sold', index='Date', columns='Item', aggfunc='sum')
pivot_table

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
      <th>Salesperson</th>
      <th>Alice</th>
      <th>John</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2024-05-01</th>
      <td>NaN</td>
      <td>66.0</td>
    </tr>
    <tr>
      <th>2024-05-02</th>
      <td>74.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2024-05-03</th>
      <td>45.0</td>
      <td>45.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
import pandas as pd
import matplotlib.pyplot as plt

# Assuming your DataFrame is named 'bios' and already loaded
# First, filter out rows where the height_cm data is missing
bios_filtered = bios.dropna(subset=['height_cm'])

# Plotting the histogram
plt.figure(figsize=(10, 6))
plt.hist(bios_filtered['height_cm'], bins=20, color='blue', edgecolor='black')

plt.title('Distribution of Athlete Heights in Olympics')
plt.xlabel('Height in cm')
plt.ylabel('Number of Athletes')
plt.grid(True)

# Using a logarithmic scale for the y-axis if the data spread is wide
plt.yscale('log')

plt.show()
```


    
![png](tutorial_files/tutorial_133_0.png)
    


## What Next???

Check out some of my other tutorials:
- [Cleaning Data w/ Pandas](https://www.youtube.com/live/oad9tVEsfI0?si=qnDOg9BSRFxcP5gZ)
- [Solving 100 Python Pandas Problems](https://youtu.be/i7v2m-ebXB4?si=VSJHnZryqMv8GW54)
- [Real-world Data Analsys Problems w/ Python Pandas](https://youtu.be/eMOA1pPVUc4)

Platforms to Try
- [Stratascratch](https://stratascratch.com/?via=keith)
- [Analyst Builder](https://www.analystbuilder.com/?via=keith)
