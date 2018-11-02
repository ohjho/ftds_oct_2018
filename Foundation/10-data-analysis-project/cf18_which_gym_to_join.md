
# Python And Data Analysis Project
Day 10 of Xccelerate Full-time Data Science Cohort 03  
Date: 29th Oct 2018

Presentated in class on Day 14: 2nd Nov 2018

The Markdown version is created using:
```
jupyter nbconvert 02-crossfit-best-affliate-topublish.ipynb --to markdown --output=cf18_which_gym_to_join.md
```

## What is the Crossfit Open?

Or just simply what is Crossfit???

[![Youtube link to 'Story of the Open'](https://img.youtube.com/vi/skUxFsTzZ4Q/0.jpg)](https://www.youtube.com/watch?v=skUxFsTzZ4Q)


## 1. Define the Business Need
People from around the world enters their scores into [Games.Crossfit.com](https://games.crossfit.com/) and there's already some filtering functions offered in the [leaderboard](https://games.crossfit.com/leaderboard/onlinequalifiers/2018) for people to interact with the data.

_**Aside from finding the world's best athletes or creating bragging rights, how can we use the data to create value for the community???**_

To those new to crossfit, **Could we use the data to determine which gym to join?**

>the three most important and interdependent facets of any fitness program, can be supported only by measurable, observable, repeatable facts, i.e., data.
>
> Greg Glassman

With Coach Glassman's quote in mind, we can all agree that the ultimate objective of the sport is if can we improve our measurable performance? For that the open is the ultimate performance test that's hosted by HQ once a year.

>The magic is in the movement, the art is in the programming, the science is in the explanation, and the fun is in the community
>
>Greg Glassman

And if you have been doing Crossfit for a while, you'd ultimately know that performance aside, the reason that keeps you coming back is the community! Having coached for the last three years at [Asphodel](https://crossfitasphodel.com), it is my opinion that one objective way to measure the health of an affiliate is it's members participation in the Open. Members who participate in the open tend to be those who come consistently (i.e. active in the community) and those who support and cheer on other members (i.e. contribute positively to the community).

Therefore, with the Open data from 2018 and 2017, we want to find which affliate serves its member in the best way. One indication of a great affliate is the community. Another is the quality of coaching. So in short we want to answer two questions:  

**1. For a given `Region` which affliate improved its members' participation the most, from 2017 to 2018?**  

**2. For a given `Region` which affliate's athlete performance improved the most from 2017 to 2018?**


## 2. Explore the Data

>If I have seen further it is only by standing on the shoulders of giants.
>
>Sir Isaac Newton

Over the years, [the leaderboard site](https://games.crossfit.com/leaderboard/onlinequalifiers/) actually has gone thru a few changes. It's not the most straight forward to scrape and there's no public API available.  

Luckily, Jean-Michel Daignan wrote a [great piece](http://jmdaignan.com/2018/03/30/crossfitopen/) on how to scrape the Crossfit Game website as of 2018 and even made the tool available on [github](https://github.com/jeanmidevacc/crossfit_webscraping). In short, he made use of a hidden API. [Click here](https://ianlondon.github.io/blog/web-scraping-discovering-hidden-apis/) if you wish to learn how to do that with other sites.

[Ray Bell](https://github.com/raybellwaves/cfanalytics) actually did the heavy lifting and made the Crossfit Open 2018 and 2017 dataset available on [Github](https://github.com/raybellwaves/cfanalytics/tree/master/Data). 

### Side Notes:
* Sam Swift is the real OG in this and was one of the first to work with [open data](http://swift.pw/crossfit-games-data-2012-2015/)
* Jonathan Kinnick from BTWB wrote [a great piece](https://btwb.blog/2018/02/24/crossfit-open-18-1-preliminary-analysis/) as well analyzing athlete's performance.

### Data Retrieval:
Let the fun begin, we are gonna use `pandas` to manage the data and `seaborn` + `matplotlib` for visualize



```python
import pandas as pd
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

sns.set(color_codes=True) #overide maplot libs ugly colours.
mpl.rcParams['figure.figsize'] = [13, 8] #default figure size
```

Let's define the data links.


```python
url_head = 'https://raw.githubusercontent.com/raybellwaves/cfanalytics/master/Data/'

l_18url = [
    url_head + 'Women_Rx_2018.csv',
    url_head + 'Men_Rx_2018.csv'
]

l_17url = [
    url_head + 'Women_Rx_2017.csv',
    url_head + 'Men_Rx_2017.csv'
]

gyms_url = url_head + 'Affiliate_list.csv'
```

<aside class="notice">
Let's download the data. This might take a while
</aside>


```python
l_d17 = [pd.read_csv(iurl) for iurl in l_17url]
l_d18 = [pd.read_csv(iurl) for iurl in l_18url]
dgyms = pd.read_csv(gyms_url)
```

    /Users/JHO/.virtualenvs/accelerateHK3/lib/python3.6/site-packages/IPython/core/interactiveshell.py:2850: DtypeWarning: Columns (13,20) have mixed types. Specify dtype option on import or set low_memory=False.
      if self.run_code(code, result):
    /Users/JHO/.virtualenvs/accelerateHK3/lib/python3.6/site-packages/IPython/core/interactiveshell.py:2850: DtypeWarning: Columns (16,18,29) have mixed types. Specify dtype option on import or set low_memory=False.
      if self.run_code(code, result):
    /Users/JHO/.virtualenvs/accelerateHK3/lib/python3.6/site-packages/IPython/core/interactiveshell.py:2850: DtypeWarning: Columns (24,29) have mixed types. Specify dtype option on import or set low_memory=False.
      if self.run_code(code, result):


### How many people completed in 2017 and 2018?


```python
print(f'# of Open Athletes \n2017: {"{:,}".format(len(l_d17[0]) + len(l_d17[1]))} \n2018: {"{:,}".format(len(l_d18[0]) + len(l_d18[1]))}')
```

    # of Open Athletes 
    2017: 273,670 
    2018: 303,956


#### We need to apply some basic data cleaning:
* 2017 and 2018 data column names are different, so we need to rename them


```python
col_map = {'Userid':'User_id', 
           'Height (m)': 'Height_(m)', 
           'Weight (kg)':'Weight_(kg)',
           'Regionid':'Region_id',
           'Regionname':'Region_name',
           'Affiliateid':'Affiliate_id',
           'Overallrank':'Overall_rank'}
l_d17 = [d.rename(columns = col_map) for d in l_d17]
```

* In the data frame that we want, we just want to have **region data**, **Overall_rank**, and a new column for **sex**


```python
def JoinAllAthletes( df_ladies, df_men):
    l_columns = ['User_id', 'Name', 'Height_(m)', 'Weight_(kg)','Age',
                 'Region_id','Region_name','Affiliate_id','Overall_rank']
    dfl = df_ladies.loc[:, l_columns].set_index('User_id')
    dfm = df_men.loc[:, l_columns].set_index('User_id')
    dfl['Sex'] = 'F'
    dfm['Sex'] = 'M'
    
    return pd.concat([dfl, dfm])

df_18 = JoinAllAthletes( l_d18[0], l_d18[1])
df_17 = JoinAllAthletes( l_d17[0], l_d17[1])
```

* we also want to remove missing data


```python
from functools import reduce

def GetMissing(in_df):
    missing_filter = [in_df.Overall_rank.isna(),
                     in_df.Affiliate_id.isna(),
                     in_df.Affiliate_id == 0,
                     in_df.Region_id.isna(),
                     in_df.Region_id ==0]
    
    dfilter = reduce( lambda x, y : x | y, missing_filter)
    return dfilter

df18 = df_18[~(GetMissing(df_18))] # '~' is for filter negation
df17 = df_17[~(GetMissing(df_17))]

print(f'For 2018: {len(df_18)} total athletes, {len(df18)} athletes have the crucial data. That is {"{:.2%}".format(len(df18)/ len(df_18))}\n')
print(f'For 2017: {len(df_17)} total athletes, {len(df17)} athletes have the crucial data. That is {"{:.2%}".format(len(df17)/ len(df_17))}')
```

    For 2018: 303956 total athletes, 287564 athletes have the crucial data. That is 94.61%
    
    For 2017: 273670 total athletes, 261126 athletes have the crucial data. That is 95.42%


## 3. Analyse the Data

Since the data set is pretty big, we are going to select a `Region` or maybe even a city first for speed of computation

### Question I: For the `Asia/Hong Kong`, which affiliate has the best Open participation?

To do that we need to combine the 2017 and 2018 data frame as well as getting affiliate information from the `dgyms` dataframe.  

* Let's create two new dataframes for the 2017 and 2018 data by `Affiliate_id` and filter only for `Region_name== "Asia"`


```python
df18_ = df18[df18.Region_name=='Asia'].groupby('Affiliate_id')['Name'].agg({'Athlete_count_2018': 'count'})
df17_ = df17[df17.Region_name=='Asia'].groupby('Affiliate_id')['Name'].agg({'Athlete_count': 'count'})

```

    /Users/JHO/.virtualenvs/accelerateHK3/lib/python3.6/site-packages/ipykernel_launcher.py:1: FutureWarning: using a dict on a Series for aggregation
    is deprecated and will be removed in a future version
      """Entry point for launching an IPython kernel.
    /Users/JHO/.virtualenvs/accelerateHK3/lib/python3.6/site-packages/ipykernel_launcher.py:2: FutureWarning: using a dict on a Series for aggregation
    is deprecated and will be removed in a future version
      


* We are going to store the 2017 athletes count number in the 2018 dataframe


```python
def GetACount(in_df, a_id):
    nfilter = in_df.index == a_id
    if sum( nfilter ) == 0:
        return np.nan
    else:
        return int(in_df[ nfilter ]['Athlete_count'].values)
df18_['Athlete_count_2017'] = df18_.index.map(lambda x: GetACount(df17_, x))
df18_['change'] = df18_['Athlete_count_2018'] - df18_['Athlete_count_2017']
df18_['pct_change'] = df18_['Athlete_count_2018'] / df18_['Athlete_count_2017'] -1
```

* And let's fill in the affiliates data as well. The `GetAffiliateDet()` function will be useful again later.


```python
def GetAffiliateDet( a_id, colname):
    dfilter = dgyms.Affiliate_id == a_id
    if sum(dfilter) == 0:
        return np.nan
    else:
        return dgyms[dfilter][colname].values[0]

df18_['Affiliate_name'] = df18_.index.map(lambda x: GetAffiliateDet(x, 'Affiliate_name'))
df18_['Country'] = df18_.index.map(lambda x: GetAffiliateDet(x, 'Country'))
```

#### The Top 10 `Asia` Affiliates by Open Participation are:


```python
l_display_a_col = ['Affiliate_name','Country','Athlete_count_2018', 'Athlete_count_2017']
df18_.sort_values(by= 'Athlete_count_2018', ascending=False).head(10).loc[: , l_display_a_col]
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
      <th>Affiliate_name</th>
      <th>Country</th>
      <th>Athlete_count_2018</th>
      <th>Athlete_count_2017</th>
    </tr>
    <tr>
      <th>Affiliate_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1971</th>
      <td>CrossFit Gangnam</td>
      <td>Korea, Republic of</td>
      <td>192</td>
      <td>138.0</td>
    </tr>
    <tr>
      <th>10506</th>
      <td>CrossFit Apgujeong</td>
      <td>Korea, Republic of</td>
      <td>120</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>12640</th>
      <td>CrossFit Redyar</td>
      <td>Russian Federation</td>
      <td>82</td>
      <td>113.0</td>
    </tr>
    <tr>
      <th>4574</th>
      <td>CrossFit EKB</td>
      <td>Russian Federation</td>
      <td>80</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>13557</th>
      <td>CrossFit 6221</td>
      <td>Indonesia</td>
      <td>78</td>
      <td>37.0</td>
    </tr>
    <tr>
      <th>9402</th>
      <td>East West CrossFit</td>
      <td>Thailand</td>
      <td>73</td>
      <td>59.0</td>
    </tr>
    <tr>
      <th>5724</th>
      <td>Reebok CrossFit MeWellness</td>
      <td>China</td>
      <td>72</td>
      <td>59.0</td>
    </tr>
    <tr>
      <th>6582</th>
      <td>CrossFit Teddygym</td>
      <td>Korea, Republic of</td>
      <td>67</td>
      <td>82.0</td>
    </tr>
    <tr>
      <th>5827</th>
      <td>CrossFit Gof Metgot</td>
      <td>Guam</td>
      <td>66</td>
      <td>56.0</td>
    </tr>
    <tr>
      <th>10774</th>
      <td>CrossFit Bukit Timah</td>
      <td>Singapore</td>
      <td>64</td>
      <td>45.0</td>
    </tr>
  </tbody>
</table>
</div>



#### The Top 10 `Asia` Affiliates by INCREASE in Open Participation:


```python
l_display_a_col = ['Affiliate_name','Country','Athlete_count_2018', 'Athlete_count_2017','change','pct_change']
df18_.sort_values(by= 'change', ascending=False).head(10).loc[:,l_display_a_col]
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
      <th>Affiliate_name</th>
      <th>Country</th>
      <th>Athlete_count_2018</th>
      <th>Athlete_count_2017</th>
      <th>change</th>
      <th>pct_change</th>
    </tr>
    <tr>
      <th>Affiliate_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1971</th>
      <td>CrossFit Gangnam</td>
      <td>Korea, Republic of</td>
      <td>192</td>
      <td>138.0</td>
      <td>54.0</td>
      <td>0.391304</td>
    </tr>
    <tr>
      <th>13557</th>
      <td>CrossFit 6221</td>
      <td>Indonesia</td>
      <td>78</td>
      <td>37.0</td>
      <td>41.0</td>
      <td>1.108108</td>
    </tr>
    <tr>
      <th>4947</th>
      <td>CrossFit Senayan</td>
      <td>Indonesia</td>
      <td>41</td>
      <td>4.0</td>
      <td>37.0</td>
      <td>9.250000</td>
    </tr>
    <tr>
      <th>17422</th>
      <td>Elite Zone CrossFit</td>
      <td>Malaysia</td>
      <td>43</td>
      <td>7.0</td>
      <td>36.0</td>
      <td>5.142857</td>
    </tr>
    <tr>
      <th>87</th>
      <td>Humphreys CrossFit</td>
      <td>Korea, Republic of</td>
      <td>42</td>
      <td>6.0</td>
      <td>36.0</td>
      <td>6.000000</td>
    </tr>
    <tr>
      <th>15879</th>
      <td>CrossFit Loga</td>
      <td>Taiwan</td>
      <td>44</td>
      <td>18.0</td>
      <td>26.0</td>
      <td>1.444444</td>
    </tr>
    <tr>
      <th>18157</th>
      <td>Reebok CrossFit Asphodel</td>
      <td>Hong Kong</td>
      <td>36</td>
      <td>11.0</td>
      <td>25.0</td>
      <td>2.272727</td>
    </tr>
    <tr>
      <th>10722</th>
      <td>CrossFit Hakata</td>
      <td>Japan</td>
      <td>49</td>
      <td>24.0</td>
      <td>25.0</td>
      <td>1.041667</td>
    </tr>
    <tr>
      <th>3170</th>
      <td>CrossFit Himalaya</td>
      <td>India</td>
      <td>38</td>
      <td>15.0</td>
      <td>23.0</td>
      <td>1.533333</td>
    </tr>
    <tr>
      <th>18438</th>
      <td>CrossFit Vyom</td>
      <td>India</td>
      <td>24</td>
      <td>3.0</td>
      <td>21.0</td>
      <td>7.000000</td>
    </tr>
  </tbody>
</table>
</div>



#### `Hong Kong` Affiliate Open Participation ranked:


```python
l_display_a_col = ['Affiliate_name','Country','Athlete_count_2018', 'Athlete_count_2017','change']
df18_[df18_.Country =='Hong Kong'].sort_values(by= 'Athlete_count_2018', ascending=False).head(10).loc[:,l_display_a_col]
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
      <th>Affiliate_name</th>
      <th>Country</th>
      <th>Athlete_count_2018</th>
      <th>Athlete_count_2017</th>
      <th>change</th>
      <th>pct_change</th>
    </tr>
    <tr>
      <th>Affiliate_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6874</th>
      <td>CrossFit CFPT</td>
      <td>Hong Kong</td>
      <td>62</td>
      <td>66.0</td>
      <td>-4.0</td>
      <td>-0.060606</td>
    </tr>
    <tr>
      <th>5725</th>
      <td>CrossFit 852</td>
      <td>Hong Kong</td>
      <td>59</td>
      <td>63.0</td>
      <td>-4.0</td>
      <td>-0.063492</td>
    </tr>
    <tr>
      <th>15225</th>
      <td>CrossFit Quarry Bay</td>
      <td>Hong Kong</td>
      <td>51</td>
      <td>47.0</td>
      <td>4.0</td>
      <td>0.085106</td>
    </tr>
    <tr>
      <th>18157</th>
      <td>Reebok CrossFit Asphodel</td>
      <td>Hong Kong</td>
      <td>36</td>
      <td>11.0</td>
      <td>25.0</td>
      <td>2.272727</td>
    </tr>
    <tr>
      <th>11248</th>
      <td>CrossFit Cavaliers</td>
      <td>Hong Kong</td>
      <td>32</td>
      <td>35.0</td>
      <td>-3.0</td>
      <td>-0.085714</td>
    </tr>
    <tr>
      <th>6960</th>
      <td>CrossFit Typhoon</td>
      <td>Hong Kong</td>
      <td>29</td>
      <td>19.0</td>
      <td>10.0</td>
      <td>0.526316</td>
    </tr>
    <tr>
      <th>17460</th>
      <td>CrossFit FPG</td>
      <td>Hong Kong</td>
      <td>29</td>
      <td>25.0</td>
      <td>4.0</td>
      <td>0.160000</td>
    </tr>
    <tr>
      <th>15287</th>
      <td>Lion Rock CrossFit</td>
      <td>Hong Kong</td>
      <td>14</td>
      <td>3.0</td>
      <td>11.0</td>
      <td>3.666667</td>
    </tr>
  </tbody>
</table>
</div>



#### And who's open participation dropped the most in `Asia`?
* Is this a sign of a struggling affiliate?
* Does these location indicate a difficult market in the region?


```python
l_display_a_col = ['Affiliate_name','Country','Athlete_count_2018', 'Athlete_count_2017','change', 'pct_change']
df18_.sort_values(by= 'pct_change', ascending=True).head(10).loc[:,l_display_a_col]
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
      <th>Affiliate_name</th>
      <th>Country</th>
      <th>Athlete_count_2018</th>
      <th>Athlete_count_2017</th>
      <th>change</th>
      <th>pct_change</th>
    </tr>
    <tr>
      <th>Affiliate_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10569</th>
      <td>CrossFit Choigang</td>
      <td>Korea, Republic of</td>
      <td>2</td>
      <td>41.0</td>
      <td>-39.0</td>
      <td>-0.951220</td>
    </tr>
    <tr>
      <th>16155</th>
      <td>Tsunami Elite CrossFit</td>
      <td>China</td>
      <td>1</td>
      <td>19.0</td>
      <td>-18.0</td>
      <td>-0.947368</td>
    </tr>
    <tr>
      <th>15446</th>
      <td>CrossFit Pangyo Avenue</td>
      <td>Korea, Republic of</td>
      <td>9</td>
      <td>110.0</td>
      <td>-101.0</td>
      <td>-0.918182</td>
    </tr>
    <tr>
      <th>9337</th>
      <td>CrossFit Genome</td>
      <td>India</td>
      <td>1</td>
      <td>10.0</td>
      <td>-9.0</td>
      <td>-0.900000</td>
    </tr>
    <tr>
      <th>8987</th>
      <td>CrossFit 1229</td>
      <td>Philippines</td>
      <td>9</td>
      <td>61.0</td>
      <td>-52.0</td>
      <td>-0.852459</td>
    </tr>
    <tr>
      <th>9097</th>
      <td>CrossFit WeMax</td>
      <td>China</td>
      <td>1</td>
      <td>6.0</td>
      <td>-5.0</td>
      <td>-0.833333</td>
    </tr>
    <tr>
      <th>8994</th>
      <td>CrossFit Primero</td>
      <td>India</td>
      <td>4</td>
      <td>23.0</td>
      <td>-19.0</td>
      <td>-0.826087</td>
    </tr>
    <tr>
      <th>16527</th>
      <td>CrossFit IDOL 2</td>
      <td>Kazakhstan</td>
      <td>6</td>
      <td>34.0</td>
      <td>-28.0</td>
      <td>-0.823529</td>
    </tr>
    <tr>
      <th>14015</th>
      <td>CrossFit Iron Fitness</td>
      <td>Singapore</td>
      <td>2</td>
      <td>11.0</td>
      <td>-9.0</td>
      <td>-0.818182</td>
    </tr>
    <tr>
      <th>14480</th>
      <td>HNXT CrossFit</td>
      <td>Korea, Republic of</td>
      <td>5</td>
      <td>25.0</td>
      <td>-20.0</td>
      <td>-0.800000</td>
    </tr>
  </tbody>
</table>
</div>



### Question II: For the `Asia/Hong Kong` Region, which affiliate improved their Open Athletes' performance the most?
Where the improve in preformance is the total number of rank improved for all athletes who completed both in 2017 and 2018.  
* First lets create another new dataframe with only `Asia` athletes where we also store their 2017 over ranking

<aside class="notice">
Note that this data frame lookup operation will take a while
</aside>


```python
col_to_keep = ['Name','Age','Affiliate_id','Overall_rank','Sex']
df18all = df18[df18.Region_name=='Asia'].loc[:, col_to_keep]
df18all = df18all.rename(columns= {'Overall_rank':'rank18'})

def GetRank(in_df, strName):
    nfilter = in_df.Name == strName
    if sum( nfilter ) == 0:
        return np.nan
    else:
        return in_df[ nfilter ]['Overall_rank'].values[0]

df18all['rank17'] = df18all.Name.apply(lambda x: GetRank(df17, x))
```

#### In `Asia` how many percent are repeat athletes (Survivability)?


```python
print(f'{sum(df18all.rank17.isna())} of {len(df18all)} athletes are missing 2017 data.\n')
print(f'Therefore, only {"{:.2%}".format(1- (sum(df18all.rank17.isna())/ len(df18all)))} are repeat athletes.')
```

    3973 of 7142 athletes are missing 2017 data.
    
    Therefore, only 44.37% are repeat athletes.


* here we create the rank `improvement` column and a normalization of it: `imp_z`


```python
df18a = df18all.dropna(subset=['rank17'])
df18a['improvement']= df18a['rank17'] - df18a['rank18']
df18a['Affiliate_name'] = df18a.Affiliate_id.map(lambda x: GetAffiliateDet(x, 'Affiliate_name'))
df18a['Country'] = df18a.Affiliate_id.map(lambda x: GetAffiliateDet(x, 'Country'))
imp_mean = df18a.improvement.mean()
imp_std = df18a.improvement.std()
df18a['imp_z'] = df18a.improvement.apply( lambda x: (x - imp_mean)/ imp_std)

print(f'Average improvement is {"{:,.0f}".format(imp_mean)} ranks')
print(f'that is a {"{:.2%}".format(imp_mean/len(df18))} improvement over the entire population! \n')
print(f'with a standard deviation of {"{:,.0f}".format(imp_std)} ranks\n')
```

    /Users/JHO/.virtualenvs/accelerateHK3/lib/python3.6/site-packages/ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    /Users/JHO/.virtualenvs/accelerateHK3/lib/python3.6/site-packages/ipykernel_launcher.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      This is separate from the ipykernel package so we can avoid doing imports until


    Average improvement is 2,956 ranks
    that is a 1.03% improvement over the entire population! 
    
    with a standard deviation of 38,443 ranks
    


    /Users/JHO/.virtualenvs/accelerateHK3/lib/python3.6/site-packages/ipykernel_launcher.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      after removing the cwd from sys.path.
    /Users/JHO/.virtualenvs/accelerateHK3/lib/python3.6/site-packages/ipykernel_launcher.py:7: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      import sys


#### This means that on average, repeat athletes in `Asia` improve their global ranking by nearly 3,000 spots! The prize of consistency!

#### What's the distribution of the normalized performance?


```python
plt.figure(figsize=(20,10))
sns.set(font_scale = 1.5, context = 'notebook')
sns.distplot(df18a.imp_z)
```

    /Users/JHO/.virtualenvs/accelerateHK3/lib/python3.6/site-packages/scipy/stats/stats.py:1706: FutureWarning: Using a non-tuple sequence for multidimensional indexing is deprecated; use `arr[tuple(seq)]` instead of `arr[seq]`. In the future this will be interpreted as an array index, `arr[np.array(seq)]`, which will result either in an error or a different result.
      return np.add.reduce(sorted[indexer] * weights, axis=axis) / sumval
    /Users/JHO/.virtualenvs/accelerateHK3/lib/python3.6/site-packages/matplotlib/axes/_axes.py:6462: UserWarning: The 'normed' kwarg is deprecated, and has been replaced by the 'density' kwarg.
      warnings.warn("The 'normed' kwarg is deprecated, and has been "





    <matplotlib.axes._subplots.AxesSubplot at 0x1138d16a0>




![png](cf18_which_gym_to_join_files/cf18_which_gym_to_join_40_2.png)


Ranking improvement, quite normally distributed!

#### Just for fun, let's see the top 10 most improved `male` athletes in `Asia`


```python
l_display_a_col = ['Name','Age','Affiliate_name','Country','rank18', 'rank17','improvement', 'imp_z']
df18a.sort_values(by ='improvement', ascending = False)[df18a.Sex=='M'].head(10).loc[:,l_display_a_col]
```

    /Users/JHO/.virtualenvs/accelerateHK3/lib/python3.6/site-packages/ipykernel_launcher.py:2: UserWarning: Boolean Series key will be reindexed to match DataFrame index.
      





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
      <th>Name</th>
      <th>Age</th>
      <th>Affiliate_name</th>
      <th>Country</th>
      <th>rank18</th>
      <th>rank17</th>
      <th>improvement</th>
      <th>imp_z</th>
    </tr>
    <tr>
      <th>User_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>319745</th>
      <td>Keith Stillman</td>
      <td>27</td>
      <td>Port Tower CrossFit</td>
      <td>Japan</td>
      <td>2763</td>
      <td>151198.0</td>
      <td>148435.0</td>
      <td>3.784274</td>
    </tr>
    <tr>
      <th>57487</th>
      <td>Kim Jwa-Nyeon</td>
      <td>43</td>
      <td>CrossFit LOL</td>
      <td>Korea, Republic of</td>
      <td>34873</td>
      <td>179933.0</td>
      <td>145060.0</td>
      <td>3.696482</td>
    </tr>
    <tr>
      <th>1363804</th>
      <td>Timofey Bakhurinskiy</td>
      <td>25</td>
      <td>CrossFit Astana</td>
      <td>Kazakhstan</td>
      <td>3815</td>
      <td>148447.0</td>
      <td>144632.0</td>
      <td>3.685349</td>
    </tr>
    <tr>
      <th>733891</th>
      <td>Zachary Thibodaux</td>
      <td>24</td>
      <td>Fight Tonight CrossFit</td>
      <td>Korea, Republic of</td>
      <td>13953</td>
      <td>155611.0</td>
      <td>141658.0</td>
      <td>3.607988</td>
    </tr>
    <tr>
      <th>967176</th>
      <td>Eunwoong Lee</td>
      <td>24</td>
      <td>CrossFit MATE</td>
      <td>Korea, Republic of</td>
      <td>41171</td>
      <td>182305.0</td>
      <td>141134.0</td>
      <td>3.594358</td>
    </tr>
    <tr>
      <th>752725</th>
      <td>Lee Byeong Su</td>
      <td>27</td>
      <td>CrossFit Shout</td>
      <td>Korea, Republic of</td>
      <td>48961</td>
      <td>189840.0</td>
      <td>140879.0</td>
      <td>3.587724</td>
    </tr>
    <tr>
      <th>278578</th>
      <td>JiMoo Son</td>
      <td>27</td>
      <td>CrossFit Limelight</td>
      <td>Korea, Republic of</td>
      <td>291</td>
      <td>139217.0</td>
      <td>138926.0</td>
      <td>3.536922</td>
    </tr>
    <tr>
      <th>879011</th>
      <td>Xingchen Li</td>
      <td>30</td>
      <td>Attitude CrossFit</td>
      <td>China</td>
      <td>12561</td>
      <td>149311.0</td>
      <td>136750.0</td>
      <td>3.480319</td>
    </tr>
    <tr>
      <th>1097087</th>
      <td>Paolo Volpe</td>
      <td>30</td>
      <td>CrossFit 6221</td>
      <td>Indonesia</td>
      <td>41938</td>
      <td>178364.0</td>
      <td>136426.0</td>
      <td>3.471891</td>
    </tr>
    <tr>
      <th>496740</th>
      <td>Hogun Hwang</td>
      <td>28</td>
      <td>CrossFit Teddygym</td>
      <td>Korea, Republic of</td>
      <td>6292</td>
      <td>141781.0</td>
      <td>135489.0</td>
      <td>3.447517</td>
    </tr>
  </tbody>
</table>
</div>



#### Where are these insane improvement from?
![picture of keith](img/kstillman.jpg "Keith and I at Bangkok Throwdown 2018")
* Injuries?
* New to the sport?
* Actual Improvements?
* Something else?

#### Back to our topic
* let's group the dataframe by `Affiliate_id` again and rank them by `Total_rank_improved`


```python
df18ag = df18a.groupby('Affiliate_id')['improvement'].agg({'athletes_count': 'count', 
                                                           'Total_rank_improved': 'sum', 
                                                           'Avg_rank_improved': 'mean',
                                                           'Median_rank_improved': 'median'})
df18ag['Affiliate_name'] = df18ag.index.map(lambda x: GetAffiliateDet(x, 'Affiliate_name'))
df18ag['Country'] = df18ag.index.map(lambda x: GetAffiliateDet(x, 'Country'))
```

    /Users/JHO/.virtualenvs/accelerateHK3/lib/python3.6/site-packages/ipykernel_launcher.py:4: FutureWarning: using a dict on a Series for aggregation
    is deprecated and will be removed in a future version
      after removing the cwd from sys.path.


#### Which gym improved their repeat athletes the most in `Asia`?


```python
l_display_a_col = ['Affiliate_name','Country','athletes_count','Total_rank_improved','Avg_rank_improved','Median_rank_improved']
df18ag.sort_values( by = 'Total_rank_improved', ascending = False).head(10).loc[:, l_display_a_col]
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
      <th>Affiliate_name</th>
      <th>Country</th>
      <th>athletes_count</th>
      <th>Total_rank_improved</th>
      <th>Avg_rank_improved</th>
      <th>Median_rank_improved</th>
    </tr>
    <tr>
      <th>Affiliate_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4574</th>
      <td>CrossFit EKB</td>
      <td>Russian Federation</td>
      <td>39</td>
      <td>590534.0</td>
      <td>15141.897436</td>
      <td>9924.0</td>
    </tr>
    <tr>
      <th>14574</th>
      <td>Actualize CrossFit</td>
      <td>Singapore</td>
      <td>23</td>
      <td>515447.0</td>
      <td>22410.739130</td>
      <td>13294.0</td>
    </tr>
    <tr>
      <th>18507</th>
      <td>CrossFit RK Olympicpark</td>
      <td>Korea, Republic of</td>
      <td>12</td>
      <td>501346.0</td>
      <td>41778.833333</td>
      <td>30873.0</td>
    </tr>
    <tr>
      <th>12640</th>
      <td>CrossFit Redyar</td>
      <td>Russian Federation</td>
      <td>51</td>
      <td>443793.0</td>
      <td>8701.823529</td>
      <td>5486.0</td>
    </tr>
    <tr>
      <th>16276</th>
      <td>Singa CrossFit</td>
      <td>Korea, Republic of</td>
      <td>27</td>
      <td>423556.0</td>
      <td>15687.259259</td>
      <td>17580.0</td>
    </tr>
    <tr>
      <th>17256</th>
      <td>CrossFit Daikanyama</td>
      <td>Japan</td>
      <td>16</td>
      <td>387475.0</td>
      <td>24217.187500</td>
      <td>13047.0</td>
    </tr>
    <tr>
      <th>13853</th>
      <td>CrossFit 4TP</td>
      <td>Korea, Republic of</td>
      <td>25</td>
      <td>375524.0</td>
      <td>15020.960000</td>
      <td>9531.0</td>
    </tr>
    <tr>
      <th>18581</th>
      <td>CrossFit GangDong</td>
      <td>Korea, Republic of</td>
      <td>11</td>
      <td>370516.0</td>
      <td>33683.272727</td>
      <td>20964.0</td>
    </tr>
    <tr>
      <th>6582</th>
      <td>CrossFit Teddygym</td>
      <td>Korea, Republic of</td>
      <td>35</td>
      <td>366844.0</td>
      <td>10481.257143</td>
      <td>11125.0</td>
    </tr>
    <tr>
      <th>4947</th>
      <td>CrossFit Senayan</td>
      <td>Indonesia</td>
      <td>18</td>
      <td>359358.0</td>
      <td>19964.333333</td>
      <td>14386.5</td>
    </tr>
  </tbody>
</table>
</div>



#### Which gym improved their repeat athletes the most in `Asia/Hong Kong`?


```python
df18ag[df18ag.Country == 'Hong Kong'].sort_values( by = 'Total_rank_improved', ascending = False).loc[:,l_display_a_col]
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
      <th>Affiliate_name</th>
      <th>Country</th>
      <th>athletes_count</th>
      <th>Total_rank_improved</th>
      <th>Avg_rank_improved</th>
      <th>Median_rank_improved</th>
    </tr>
    <tr>
      <th>Affiliate_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6874</th>
      <td>CrossFit CFPT</td>
      <td>Hong Kong</td>
      <td>41</td>
      <td>205201.0</td>
      <td>5004.902439</td>
      <td>290.0</td>
    </tr>
    <tr>
      <th>15287</th>
      <td>Lion Rock CrossFit</td>
      <td>Hong Kong</td>
      <td>6</td>
      <td>-11716.0</td>
      <td>-1952.666667</td>
      <td>8303.0</td>
    </tr>
    <tr>
      <th>6960</th>
      <td>CrossFit Typhoon</td>
      <td>Hong Kong</td>
      <td>10</td>
      <td>-26480.0</td>
      <td>-2648.000000</td>
      <td>-4648.5</td>
    </tr>
    <tr>
      <th>18157</th>
      <td>Reebok CrossFit Asphodel</td>
      <td>Hong Kong</td>
      <td>22</td>
      <td>-77357.0</td>
      <td>-3516.227273</td>
      <td>-5222.0</td>
    </tr>
    <tr>
      <th>11248</th>
      <td>CrossFit Cavaliers</td>
      <td>Hong Kong</td>
      <td>22</td>
      <td>-93719.0</td>
      <td>-4259.954545</td>
      <td>162.5</td>
    </tr>
    <tr>
      <th>5725</th>
      <td>CrossFit 852</td>
      <td>Hong Kong</td>
      <td>44</td>
      <td>-155654.0</td>
      <td>-3537.590909</td>
      <td>765.5</td>
    </tr>
    <tr>
      <th>17460</th>
      <td>CrossFit FPG</td>
      <td>Hong Kong</td>
      <td>17</td>
      <td>-170945.0</td>
      <td>-10055.588235</td>
      <td>6581.0</td>
    </tr>
    <tr>
      <th>15225</th>
      <td>CrossFit Quarry Bay</td>
      <td>Hong Kong</td>
      <td>30</td>
      <td>-684962.0</td>
      <td>-22832.066667</td>
      <td>-4756.0</td>
    </tr>
  </tbody>
</table>
</div>



#### How do those improvement in `Asia/Hong Kong` compare by distribution in a boxplot (to account for outliners)


```python
plt.figure(figsize=(15,10))
sns.set(font_scale = 1.5, context = 'talk')
g = sns.boxplot( data = df18a[ df18a.Country == 'Hong Kong'], 
            x = 'Affiliate_name', y = 'imp_z')
g.set_xticklabels(g.get_xticklabels(), rotation=45)
mean_z = df18a.imp_z.mean()
g.hlines(mean_z, g.get_xlim()[0], g.get_xlim()[1], color = 'r')
```




    <matplotlib.collections.LineCollection at 0x113da27f0>




![png](cf18_which_gym_to_join_files/cf18_which_gym_to_join_51_1.png)


#### Are there noticeable improvement differences between Male and Female athletes in `Asia/Hong Kong`?


```python
plt.figure(figsize=(15,10))
sns.set(font_scale = 1, context = 'talk')
g = sns.violinplot( data = df18a[ df18a.Country == 'Hong Kong'], 
            x = 'Affiliate_name', y = 'imp_z', hue = 'Sex', split=True,
            palette = ['r','b'])
g.set_xticklabels(g.get_xticklabels(), rotation=90)
mean_z = df18a.imp_z.mean()
g.hlines(mean_z, g.get_xlim()[0], g.get_xlim()[1], color = 'r')
```

    /Users/JHO/.virtualenvs/accelerateHK3/lib/python3.6/site-packages/scipy/stats/stats.py:1706: FutureWarning: Using a non-tuple sequence for multidimensional indexing is deprecated; use `arr[tuple(seq)]` instead of `arr[seq]`. In the future this will be interpreted as an array index, `arr[np.array(seq)]`, which will result either in an error or a different result.
      return np.add.reduce(sorted[indexer] * weights, axis=axis) / sumval





    <matplotlib.collections.LineCollection at 0x11464edd8>




![png](cf18_which_gym_to_join_files/cf18_which_gym_to_join_53_2.png)


#### Also what's the survivibility of the 'Open Athlete' by gyms in `Asia/Hong Kong`?


```python
def dfGet(in_df, keyCol, inkey, getcol):
    dfilter = in_df[keyCol]== inkey
    if sum(dfilter)==0:
        return np.nan
    else:
        return in_df[dfilter][getcol].values[0]

df18s = df18_
df18s['Athlete_2018_repeat_count'] = df18s.Affiliate_name.apply(lambda x: dfGet(df18ag, 'Affiliate_name',x,'athletes_count'))
df18s['survival_rate'] = df18s['Athlete_2018_repeat_count']/ df18s['Athlete_count_2018']

l_display_a_col = ['Affiliate_name','Country','Athlete_count_2018','Athlete_2018_repeat_count','survival_rate']
df18s[df18s.Country == 'Hong Kong'].sort_values( by = 'survival_rate', ascending = False).loc[:, l_display_a_col]
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
      <th>Affiliate_name</th>
      <th>Country</th>
      <th>Athlete_count_2018</th>
      <th>Athlete_2018_repeat_count</th>
      <th>survival_rate</th>
    </tr>
    <tr>
      <th>Affiliate_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5725</th>
      <td>CrossFit 852</td>
      <td>Hong Kong</td>
      <td>59</td>
      <td>44.0</td>
      <td>0.745763</td>
    </tr>
    <tr>
      <th>11248</th>
      <td>CrossFit Cavaliers</td>
      <td>Hong Kong</td>
      <td>32</td>
      <td>22.0</td>
      <td>0.687500</td>
    </tr>
    <tr>
      <th>6874</th>
      <td>CrossFit CFPT</td>
      <td>Hong Kong</td>
      <td>62</td>
      <td>41.0</td>
      <td>0.661290</td>
    </tr>
    <tr>
      <th>18157</th>
      <td>Reebok CrossFit Asphodel</td>
      <td>Hong Kong</td>
      <td>36</td>
      <td>22.0</td>
      <td>0.611111</td>
    </tr>
    <tr>
      <th>15225</th>
      <td>CrossFit Quarry Bay</td>
      <td>Hong Kong</td>
      <td>51</td>
      <td>30.0</td>
      <td>0.588235</td>
    </tr>
    <tr>
      <th>17460</th>
      <td>CrossFit FPG</td>
      <td>Hong Kong</td>
      <td>29</td>
      <td>17.0</td>
      <td>0.586207</td>
    </tr>
    <tr>
      <th>15287</th>
      <td>Lion Rock CrossFit</td>
      <td>Hong Kong</td>
      <td>14</td>
      <td>6.0</td>
      <td>0.428571</td>
    </tr>
    <tr>
      <th>6960</th>
      <td>CrossFit Typhoon</td>
      <td>Hong Kong</td>
      <td>29</td>
      <td>10.0</td>
      <td>0.344828</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize=(15,10))
sns.set(font_scale = 1.5, context = 'talk')
g = sns.barplot( data = df18s[ df18s.Country == 'Hong Kong'], 
            x = 'Affiliate_name', y = 'survival_rate')
g.set_xticklabels(g.get_xticklabels(), rotation=45)
g.set_title('Open Athlete Survival Rate')
```




    Text(0.5,1,'Open Athlete Survival Rate')




![png](cf18_which_gym_to_join_files/cf18_which_gym_to_join_56_1.png)


## What does this all mean?
* Keep at it! Repeat athletes found 1% global ranking improvement on average! And [one percent](https://jamesclear.com/marginal-gains) goes a long way!

* With this analysis, we can help someone identify where's a good gym to join if they are visiting or moving to a new city (maybe even write a Plot.ly interactive web app??)

### What's Next?
Using the same dataset we will answer
* which country to move to if you want to become a [2019 Crossfit Game](https://morningchalkup.com/2018/08/23/how-greg-glassman-is-reshaping-the-crossfit-games/) athlete? Taking into account the competitiveness of the country, quality of life, and coaching jobs available.
* Analyze performance by Weight Class! To answer the question, what if Crossfit have weight categories?
