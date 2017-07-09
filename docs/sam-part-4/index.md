
<a id="header"></a>
# Part 4: levels 62-70

[Return home](../)


```python
from samurai import *
from plotting import *

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
from IPython.display import display
%matplotlib inline

pd.options.display.max_rows = None
```

These last nine levels are truly the formative levels for Samurai. They add the fundamental traits and actions that give the job its complexity. Up to this point, most decision making was obvious and any alternate decision paths often led to virtually indistinguishable results under ideal conditions. The Kenki mechanic was relatively low pressure as it accumulated slowly and the choices for its spenders were rather limited. We'll see how this changes rapidly over the final leveling stretch.

## lvl 62-67

Level 62 is indeed a gamechanger. The trait Kenki Mastery II adds a Kenki bonus to almost every weaponskill (barring Iaijutsu), significantly increasing our Kenki accrual rate to 10 for combo finishers plus 5 for non finishers, or a net 55 Kenki per 8 GCD rotation (going through all Sen combos). The Kenki Mastery II trait grants Kenki for the following actions:


```python
kenki_table_II = [('Hakaze', 5), ('Shifu', 5), ('Jinpu', 5), ('Enpi', 10),
                 ('Gekko', 5), ('Gekko (rear combo)', 5), 
                 ('Kasha', 5), ('Kasha (side combo)', 5),
                 ('Yukikaze (combo)', 10),
                 ('Fuga', 5), ('Mangetsu (combo)', 5), ('Oka (combo)', 5), ]

kenki_table_df = pd.DataFrame(kenki_table_II, columns=['Weaponskill', 'Kenki granted'])
kenki_table_df.set_index('Weaponskill')
display(kenki_table_df)
```


<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Weaponskill</th>
      <th>Kenki granted</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Hakaze</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Shifu</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jinpu</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Enpi</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Gekko</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Gekko (rear combo)</td>
      <td>5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Kasha</td>
      <td>5</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kasha (side combo)</td>
      <td>5</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Yukikaze (combo)</td>
      <td>10</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Fuga</td>
      <td>5</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Mangetsu (combo)</td>
      <td>5</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Oka (combo)</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>


This will net a substantial surplus if we reserve Kenki solely for Hissatsu: Kaiten on our Iaijutsu. Coincidentally, level 62 also grants the ability Hissatsu: Shinten, dealing 300 potency off the GCD at a cost of 25 Kenki on a 1s recast. This is significantly more value than spending on Hissatsu: Kaiten on Kasha/Gekko and only ~16.6% less value than spending Hissatsu: Kaiten on Higanbana or Midare Setsugekka. See part 5 for an in-depth discussion on Kenki spenders.

Level 66 grants the Hissatsu: Seigan ability. Formerly known as Starry Eyes, this ability is only usable under the Open Eyes status, which is granted by successfully reducing damage received while Third Eye is active. At 200 potency with a cost of 15 Kenki, Hissatsu: Seigan is more efficient in potency per Kenki spent than Hissatsu: Shinten and is worth trying to use as much as possible. See part 5 for an in-depth discussion on Third Eye and Kenki spenders.

With the massively increased Kenki generation, let's revisit our single target situations.

### Example Kenki usage only using Hissatsu: Kaiten


```python
sam = Samurai(kenki_mastery=2)

actions = [('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Jinpu', 'Hissatsu: Kaiten'), ('Higanbana'), ('Gekko'), ('Hakaze'),
           ('Yukikaze'), ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Kaiten', 'Meikyo Shisui'),
           ('Midare Setsugekka'), ('Gekko'), ('Yukikaze'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'), ('Hakaze'), ('Jinpu'), ('Gekko'),
           ('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Yukikaze', 'Hissatsu: Kaiten'), ('Midare Setsugekka'), ('Hakaze'),
           ('Jinpu'), ('Gekko'), ('Hakaze'), ('Shifu', 'Hissatsu: Kaiten'),
           ('Higanbana'), ('Kasha'), ('Hakaze'), ('Yukikaze'),
           ('Hakaze'), ('Jinpu'), ('Gekko', 'Hissatsu: Kaiten'), ('Midare Setsugekka'),
           ]
```


```python
df0, average_potency, pps = sam.parse_rotation(actions)
display(df0)
```

    average potency per GCD = 486.5776923076921
    average potency per second = 224.627485795
    


<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Time</th>
      <th>Weaponskill</th>
      <th>Abilities</th>
      <th>Potency</th>
      <th>Jinpu</th>
      <th>Shifu</th>
      <th>Yukikaze</th>
      <th>Higanbana</th>
      <th>Kenki</th>
      <th>Total Potency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>0</td>
      <td>150.000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>5</td>
      <td>430.000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Kasha</td>
      <td></td>
      <td>400.000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>830.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>20</td>
      <td>980.000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Jinpu</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>280.000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>25</td>
      <td>1260.000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Higanbana</td>
      <td></td>
      <td>323.470</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>1583.470</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Gekko</td>
      <td></td>
      <td>503.470</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>10</td>
      <td>2086.940</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Hakaze</td>
      <td></td>
      <td>215.970</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>20</td>
      <td>2302.910</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Yukikaze</td>
      <td></td>
      <td>434.470</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>25</td>
      <td>2737.380</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>2972.325</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Shifu</td>
      <td></td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>40</td>
      <td>3373.215</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Kasha</td>
      <td>(Hissatsu: Kaiten, Meikyo Shisui)</td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>45</td>
      <td>3927.285</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1422.090</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>5349.375</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Gekko</td>
      <td></td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>5903.445</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Yukikaze</td>
      <td></td>
      <td>477.480</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>45</td>
      <td>6380.925</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Kasha</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>55</td>
      <td>6934.995</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1422.090</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>45</td>
      <td>8357.085</td>
    </tr>
    <tr>
      <th>17</th>
      <td>36.96</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>45</td>
      <td>8592.030</td>
    </tr>
    <tr>
      <th>18</th>
      <td>39.12</td>
      <td>Jinpu</td>
      <td></td>
      <td>400.890</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>50</td>
      <td>8992.920</td>
    </tr>
    <tr>
      <th>19</th>
      <td>41.28</td>
      <td>Gekko</td>
      <td></td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>55</td>
      <td>9546.990</td>
    </tr>
    <tr>
      <th>20</th>
      <td>43.44</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>9781.935</td>
    </tr>
    <tr>
      <th>21</th>
      <td>45.60</td>
      <td>Shifu</td>
      <td></td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>70</td>
      <td>10182.825</td>
    </tr>
    <tr>
      <th>22</th>
      <td>47.76</td>
      <td>Kasha</td>
      <td></td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>10736.895</td>
    </tr>
    <tr>
      <th>23</th>
      <td>49.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>85</td>
      <td>10971.840</td>
    </tr>
    <tr>
      <th>24</th>
      <td>52.08</td>
      <td>Yukikaze</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>477.480</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>90</td>
      <td>11449.320</td>
    </tr>
    <tr>
      <th>25</th>
      <td>54.24</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1422.090</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>12871.410</td>
    </tr>
    <tr>
      <th>26</th>
      <td>56.40</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>13106.355</td>
    </tr>
    <tr>
      <th>27</th>
      <td>58.56</td>
      <td>Jinpu</td>
      <td></td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>85</td>
      <td>13507.245</td>
    </tr>
    <tr>
      <th>28</th>
      <td>60.72</td>
      <td>Gekko</td>
      <td></td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>90</td>
      <td>14061.315</td>
    </tr>
    <tr>
      <th>29</th>
      <td>62.88</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>14296.260</td>
    </tr>
    <tr>
      <th>30</th>
      <td>65.04</td>
      <td>Shifu</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>14697.150</td>
    </tr>
    <tr>
      <th>31</th>
      <td>67.20</td>
      <td>Higanbana</td>
      <td></td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>15098.040</td>
    </tr>
    <tr>
      <th>32</th>
      <td>69.36</td>
      <td>Kasha</td>
      <td></td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>15652.110</td>
    </tr>
    <tr>
      <th>33</th>
      <td>71.52</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>90</td>
      <td>15887.055</td>
    </tr>
    <tr>
      <th>34</th>
      <td>73.68</td>
      <td>Yukikaze</td>
      <td></td>
      <td>477.480</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>95</td>
      <td>16364.535</td>
    </tr>
    <tr>
      <th>35</th>
      <td>75.84</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>16599.480</td>
    </tr>
    <tr>
      <th>36</th>
      <td>78.00</td>
      <td>Jinpu</td>
      <td></td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>17000.370</td>
    </tr>
    <tr>
      <th>37</th>
      <td>80.16</td>
      <td>Gekko</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>17554.440</td>
    </tr>
    <tr>
      <th>38</th>
      <td>82.32</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1422.090</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>18976.530</td>
    </tr>
  </tbody>
</table>
</div>


As you can see, we capped Kenki about a minute into the encounter. Let's add in Hissatsu: Shinten to dump some Kenki.


```python
sam = Samurai(kenki_mastery=2)

actions = [('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Jinpu', 'Hissatsu: Kaiten'), ('Higanbana'), ('Gekko'), ('Hakaze'),
           ('Yukikaze'), ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Kaiten', 'Meikyo Shisui'),
           ('Midare Setsugekka'), ('Gekko'), ('Yukikaze'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'), ('Hakaze'), ('Jinpu'), ('Gekko'),
           ('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Yukikaze', 'Hissatsu: Kaiten'), ('Midare Setsugekka'), ('Hakaze'),
           ('Jinpu'), ('Gekko', 'Hissatsu: Shinten'), ('Hakaze'), ('Shifu', 'Hissatsu: Kaiten'),
           ('Higanbana'), ('Kasha'), ('Hakaze'), ('Yukikaze', 'Hissatsu: Shinten'),
           ('Hakaze', 'Hissatsu: Shinten'), ('Jinpu', 'Hissatsu: Shinten'), ('Gekko', 'Hissatsu: Kaiten'), ('Midare Setsugekka'),
           ]
```


```python
df1, average_potency, pps = sam.parse_rotation(actions)
display(df1)
```

    average potency per GCD = 525.8546153846153
    average potency per second = 242.759588068
    


<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Time</th>
      <th>Weaponskill</th>
      <th>Abilities</th>
      <th>Potency</th>
      <th>Jinpu</th>
      <th>Shifu</th>
      <th>Yukikaze</th>
      <th>Higanbana</th>
      <th>Kenki</th>
      <th>Total Potency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>0</td>
      <td>150.000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>5</td>
      <td>430.000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Kasha</td>
      <td></td>
      <td>400.000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>830.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>20</td>
      <td>980.000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Jinpu</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>280.000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>25</td>
      <td>1260.000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Higanbana</td>
      <td></td>
      <td>323.470</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>1583.470</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Gekko</td>
      <td></td>
      <td>503.470</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>10</td>
      <td>2086.940</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Hakaze</td>
      <td></td>
      <td>215.970</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>20</td>
      <td>2302.910</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Yukikaze</td>
      <td></td>
      <td>434.470</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>25</td>
      <td>2737.380</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>2972.325</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Shifu</td>
      <td></td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>40</td>
      <td>3373.215</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Kasha</td>
      <td>(Hissatsu: Kaiten, Meikyo Shisui)</td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>45</td>
      <td>3927.285</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1422.090</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>5349.375</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Gekko</td>
      <td></td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>5903.445</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Yukikaze</td>
      <td></td>
      <td>477.480</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>45</td>
      <td>6380.925</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Kasha</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>55</td>
      <td>6934.995</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1422.090</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>45</td>
      <td>8357.085</td>
    </tr>
    <tr>
      <th>17</th>
      <td>36.96</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>45</td>
      <td>8592.030</td>
    </tr>
    <tr>
      <th>18</th>
      <td>39.12</td>
      <td>Jinpu</td>
      <td></td>
      <td>400.890</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>50</td>
      <td>8992.920</td>
    </tr>
    <tr>
      <th>19</th>
      <td>41.28</td>
      <td>Gekko</td>
      <td></td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>55</td>
      <td>9546.990</td>
    </tr>
    <tr>
      <th>20</th>
      <td>43.44</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>9781.935</td>
    </tr>
    <tr>
      <th>21</th>
      <td>45.60</td>
      <td>Shifu</td>
      <td></td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>70</td>
      <td>10182.825</td>
    </tr>
    <tr>
      <th>22</th>
      <td>47.76</td>
      <td>Kasha</td>
      <td></td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>10736.895</td>
    </tr>
    <tr>
      <th>23</th>
      <td>49.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>85</td>
      <td>10971.840</td>
    </tr>
    <tr>
      <th>24</th>
      <td>52.08</td>
      <td>Yukikaze</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>477.480</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>90</td>
      <td>11449.320</td>
    </tr>
    <tr>
      <th>25</th>
      <td>54.24</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1422.090</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>12871.410</td>
    </tr>
    <tr>
      <th>26</th>
      <td>56.40</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>13106.355</td>
    </tr>
    <tr>
      <th>27</th>
      <td>58.56</td>
      <td>Jinpu</td>
      <td></td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>85</td>
      <td>13507.245</td>
    </tr>
    <tr>
      <th>28</th>
      <td>60.72</td>
      <td>Gekko</td>
      <td>(Hissatsu: Shinten,)</td>
      <td>937.020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>90</td>
      <td>14444.265</td>
    </tr>
    <tr>
      <th>29</th>
      <td>62.88</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>14679.210</td>
    </tr>
    <tr>
      <th>30</th>
      <td>65.04</td>
      <td>Shifu</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>15080.100</td>
    </tr>
    <tr>
      <th>31</th>
      <td>67.20</td>
      <td>Higanbana</td>
      <td></td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>15480.990</td>
    </tr>
    <tr>
      <th>32</th>
      <td>69.36</td>
      <td>Kasha</td>
      <td></td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>16035.060</td>
    </tr>
    <tr>
      <th>33</th>
      <td>71.52</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>16270.005</td>
    </tr>
    <tr>
      <th>34</th>
      <td>73.68</td>
      <td>Yukikaze</td>
      <td>(Hissatsu: Shinten,)</td>
      <td>860.430</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>17130.435</td>
    </tr>
    <tr>
      <th>35</th>
      <td>75.84</td>
      <td>Hakaze</td>
      <td>(Hissatsu: Shinten,)</td>
      <td>617.895</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>17748.330</td>
    </tr>
    <tr>
      <th>36</th>
      <td>78.00</td>
      <td>Jinpu</td>
      <td>(Hissatsu: Shinten,)</td>
      <td>783.840</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>45</td>
      <td>18532.170</td>
    </tr>
    <tr>
      <th>37</th>
      <td>80.16</td>
      <td>Gekko</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>25</td>
      <td>19086.240</td>
    </tr>
    <tr>
      <th>38</th>
      <td>82.32</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1422.090</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>20508.330</td>
    </tr>
  </tbody>
</table>
</div>


I made the conscious effort to try to spend all the Kenki generated by the end. We have the flexibility of spending Kenki whenever with the 1s recast time on Hissatsu: Shinten. We could even use it every GCD like I did towards the end for increased burst provided we have enough Kenki. 

With the acquisition of Kenki Mastery II and Hissatsu: Shinten at level 62, we net an over 10% increase in potency per second. 


```python
compare_potencies([df0, df1], ['No Hissatsu: Shinten', 'With Hissatsu: Shinten'])
```


![png](output_15_0.png)


The first 60 seconds or so are identical because I made the decision to not use Hissatsu: Shinten until I nearly capped on Kenki.

### Example Kenki usage with AoE rotations

Hissatsu: Kyuten is learned at level 64 and is the AoE analog of Hissatsu: Shinten, matching it in potency at two targets. However, its value needs to be compared to spending Hissatsu: Kaiten on Tenka Goken. Hissatsu: Kyuten does 150 potency to all targets without AoE downscaling at the cost of 25 Kenki whereas Hissatsu: Kaiten increases the potency of the next weaponskill, in our case Tenka Goken, by 50% at the cost of 20 Kenki. Additionally, Tenka Goken experiences decreased potency per target as target numbers goes up down to a minimum 180 potency for the fifth target and beyond. Let's see each compares as a function of number of targets.

#### Only Hissatsu: Kaiten on Tenka Goken


```python
dfs_aoe_kaiten_only = []
pps_aoe_kaiten_only = []
labels = []

n_target_range = range(2, 8)

for n_targets in n_target_range:
    sam = Samurai(kenki_mastery=2, kenki_gauge=50)
    
    actions = [('Fuga'), ('Oka'), ('Fuga'), ('Mangetsu', 'Hissatsu: Kaiten'), ('Tenka Goken'), 
               ('Fuga'), ('Mangetsu'), ('Fuga'), ('Oka', 'Hissatsu: Kaiten'), 
               ('Tenka Goken'), ('Fuga'), ('Mangetsu'), ('Fuga'),
               ('Oka', 'Hissatsu: Kaiten'), ('Tenka Goken')]
    
    print('number of targets = %s' % n_targets)
    df_temp, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
    dfs_aoe_kaiten_only.append(df_temp)
    pps_aoe_kaiten_only.append(pps)
    
    labels.append('%s targets' % n_targets)
    print('\n')

display(dfs_aoe_kaiten_only[-1])
```

    number of targets = 2
    average potency per GCD = 437.2
    average potency per second = 182.166666667
    
    
    number of targets = 3
    average potency per GCD = 627.6
    average potency per second = 261.5
    
    
    number of targets = 4
    average potency per GCD = 799.2
    average potency per second = 333.0
    
    
    number of targets = 5
    average potency per GCD = 952.0
    average potency per second = 396.666666667
    
    
    number of targets = 6
    average potency per GCD = 1086.0
    average potency per second = 452.5
    
    
    number of targets = 7
    average potency per GCD = 1220.0
    average potency per second = 508.333333333
    
    
    


<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Time</th>
      <th>Weaponskill</th>
      <th>Abilities</th>
      <th>Potency</th>
      <th>Jinpu</th>
      <th>Shifu</th>
      <th>Yukikaze</th>
      <th>Higanbana</th>
      <th>Kenki</th>
      <th>Total Potency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>Fuga</td>
      <td></td>
      <td>700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>50</td>
      <td>700.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.4</td>
      <td>Oka</td>
      <td></td>
      <td>1000.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>55</td>
      <td>1700.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.8</td>
      <td>Fuga</td>
      <td></td>
      <td>700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>65</td>
      <td>2400.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.2</td>
      <td>Mangetsu</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>1000.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>70</td>
      <td>3400.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.6</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>2700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>60</td>
      <td>6100.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>12.0</td>
      <td>Fuga</td>
      <td></td>
      <td>700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>60</td>
      <td>6800.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>14.4</td>
      <td>Mangetsu</td>
      <td></td>
      <td>1000.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>65</td>
      <td>7800.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16.8</td>
      <td>Fuga</td>
      <td></td>
      <td>700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>75</td>
      <td>8500.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>19.2</td>
      <td>Oka</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>1000.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>80</td>
      <td>9500.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>21.6</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>2700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>70</td>
      <td>12200.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>24.0</td>
      <td>Fuga</td>
      <td></td>
      <td>700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>70</td>
      <td>12900.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>26.4</td>
      <td>Mangetsu</td>
      <td></td>
      <td>1000.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>75</td>
      <td>13900.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>28.8</td>
      <td>Fuga</td>
      <td></td>
      <td>700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>85</td>
      <td>14600.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>31.2</td>
      <td>Oka</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>1000.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>90</td>
      <td>15600.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>33.6</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>2700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>80</td>
      <td>18300.0</td>
    </tr>
  </tbody>
</table>
</div>



```python
compare_n_potencies(dfs_aoe_kaiten_only, labels)
```


![png](output_21_0.png)


#### Only Hissatsu: Kyuten


```python
dfs_aoe_kyuten_only = []
pps_aoe_kyuten_only = []
labels = []

n_target_range = range(2, 8)

for n_targets in n_target_range:
    sam = Samurai(kenki_mastery=2, kenki_gauge=50)
    
    actions = [('Fuga'), ('Oka'), ('Fuga'), ('Mangetsu', 'Hissatsu: Kyuten'), ('Tenka Goken'), 
               ('Fuga'), ('Mangetsu'), ('Fuga'), ('Oka', 'Hissatsu: Kyuten'), 
               ('Tenka Goken'), ('Fuga', 'Hissatsu: Kyuten'), ('Mangetsu', 'Hissatsu: Kyuten'), ('Fuga'),
               ('Oka', 'Hissatsu: Kyuten'), ('Tenka Goken')]
    
    print('number of targets = %s' % n_targets)
    df_temp, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
    dfs_aoe_kyuten_only.append(df_temp)
    pps_aoe_kyuten_only.append(pps)
    
    labels.append('%s targets' % n_targets)
    print('\n')

display(dfs_aoe_kyuten_only[-1])
```

    number of targets = 2
    average potency per GCD = 468.8
    average potency per second = 195.333333333
    
    
    number of targets = 3
    average potency per GCD = 680.4
    average potency per second = 283.5
    
    
    number of targets = 4
    average potency per GCD = 876.8
    average potency per second = 365.333333333
    
    
    number of targets = 5
    average potency per GCD = 1058.0
    average potency per second = 440.833333333
    
    
    number of targets = 6
    average potency per GCD = 1224.0
    average potency per second = 510.0
    
    
    number of targets = 7
    average potency per GCD = 1390.0
    average potency per second = 579.166666667
    
    
    


<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Time</th>
      <th>Weaponskill</th>
      <th>Abilities</th>
      <th>Potency</th>
      <th>Jinpu</th>
      <th>Shifu</th>
      <th>Yukikaze</th>
      <th>Higanbana</th>
      <th>Kenki</th>
      <th>Total Potency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>Fuga</td>
      <td></td>
      <td>700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>50</td>
      <td>700.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.4</td>
      <td>Oka</td>
      <td></td>
      <td>1000.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>55</td>
      <td>1700.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.8</td>
      <td>Fuga</td>
      <td></td>
      <td>700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>65</td>
      <td>2400.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.2</td>
      <td>Mangetsu</td>
      <td>(Hissatsu: Kyuten,)</td>
      <td>2050.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>70</td>
      <td>4450.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.6</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>1800.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>55</td>
      <td>6250.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>12.0</td>
      <td>Fuga</td>
      <td></td>
      <td>700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>55</td>
      <td>6950.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>14.4</td>
      <td>Mangetsu</td>
      <td></td>
      <td>1000.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>60</td>
      <td>7950.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16.8</td>
      <td>Fuga</td>
      <td></td>
      <td>700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>70</td>
      <td>8650.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>19.2</td>
      <td>Oka</td>
      <td>(Hissatsu: Kyuten,)</td>
      <td>2050.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>75</td>
      <td>10700.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>21.6</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>1800.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>60</td>
      <td>12500.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>24.0</td>
      <td>Fuga</td>
      <td>(Hissatsu: Kyuten,)</td>
      <td>1750.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>60</td>
      <td>14250.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>26.4</td>
      <td>Mangetsu</td>
      <td>(Hissatsu: Kyuten,)</td>
      <td>2050.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>40</td>
      <td>16300.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>28.8</td>
      <td>Fuga</td>
      <td></td>
      <td>700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>25</td>
      <td>17000.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>31.2</td>
      <td>Oka</td>
      <td>(Hissatsu: Kyuten,)</td>
      <td>2050.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>30</td>
      <td>19050.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>33.6</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>1800.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>15</td>
      <td>20850.0</td>
    </tr>
  </tbody>
</table>
</div>



```python
compare_n_potencies(dfs_aoe_kyuten_only, labels)
```


![png](output_24_0.png)


Now it would be wasteful to use Kenki on Hissatsu: Kaiten with Tenka Goken exclusively as we have a net surplus of Kenki so let's fill in the gaps with Hissatsu: Kyuten.

#### Using Hissatsu: Kaiten on Tenka Goken and Hissatsu: Kyuten with excess Kenki


```python
dfs_aoe_both = []
pps_aoe_both = []
labels = []

n_target_range = range(2, 8)

for n_targets in n_target_range:
    sam = Samurai(kenki_mastery=2, kenki_gauge=50)
    
    actions = [('Fuga'), ('Oka', 'Hissatsu: Kyuten'), ('Fuga'), ('Mangetsu', 'Hissatsu: Kaiten'), ('Tenka Goken'), 
               ('Fuga', 'Hissatsu: Kyuten'), ('Mangetsu'), ('Fuga'), ('Oka', 'Hissatsu: Kaiten'), 
               ('Tenka Goken'), ('Fuga', 'Hissatsu: Kyuten'), ('Mangetsu'), ('Fuga'),
               ('Oka', 'Hissatsu: Kaiten'), ('Tenka Goken')]
    
    print('number of targets = %s' % n_targets)
    df_temp, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
    dfs_aoe_both.append(df_temp)
    pps_aoe_both.append(pps)
    
    labels.append('%s targets' % n_targets)
    print('\n')

display(dfs_aoe_both[-1])
```

    number of targets = 2
    average potency per GCD = 497.2
    average potency per second = 207.166666667
    
    
    number of targets = 3
    average potency per GCD = 717.6
    average potency per second = 299.0
    
    
    number of targets = 4
    average potency per GCD = 919.2
    average potency per second = 383.0
    
    
    number of targets = 5
    average potency per GCD = 1102.0
    average potency per second = 459.166666667
    
    
    number of targets = 6
    average potency per GCD = 1266.0
    average potency per second = 527.5
    
    
    number of targets = 7
    average potency per GCD = 1430.0
    average potency per second = 595.833333333
    
    
    


<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Time</th>
      <th>Weaponskill</th>
      <th>Abilities</th>
      <th>Potency</th>
      <th>Jinpu</th>
      <th>Shifu</th>
      <th>Yukikaze</th>
      <th>Higanbana</th>
      <th>Kenki</th>
      <th>Total Potency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>Fuga</td>
      <td></td>
      <td>700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>50</td>
      <td>700.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.4</td>
      <td>Oka</td>
      <td>(Hissatsu: Kyuten,)</td>
      <td>2050.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>55</td>
      <td>2750.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.8</td>
      <td>Fuga</td>
      <td></td>
      <td>700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>40</td>
      <td>3450.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.2</td>
      <td>Mangetsu</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>1000.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>45</td>
      <td>4450.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.6</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>2700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>35</td>
      <td>7150.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>12.0</td>
      <td>Fuga</td>
      <td>(Hissatsu: Kyuten,)</td>
      <td>1750.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>35</td>
      <td>8900.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>14.4</td>
      <td>Mangetsu</td>
      <td></td>
      <td>1000.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>15</td>
      <td>9900.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16.8</td>
      <td>Fuga</td>
      <td></td>
      <td>700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>25</td>
      <td>10600.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>19.2</td>
      <td>Oka</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>1000.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>30</td>
      <td>11600.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>21.6</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>2700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>20</td>
      <td>14300.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>24.0</td>
      <td>Fuga</td>
      <td>(Hissatsu: Kyuten,)</td>
      <td>1750.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>20</td>
      <td>16050.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>26.4</td>
      <td>Mangetsu</td>
      <td></td>
      <td>1000.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>0</td>
      <td>17050.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>28.8</td>
      <td>Fuga</td>
      <td></td>
      <td>700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>17750.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>31.2</td>
      <td>Oka</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>1000.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>15</td>
      <td>18750.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>33.6</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>2700.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>5</td>
      <td>21450.0</td>
    </tr>
  </tbody>
</table>
</div>



```python
compare_n_potencies(dfs_aoe_both, labels)
```


![png](output_28_0.png)


#### Potency per Kenki spent as a function of targets


```python
potency_one_tenka = []
labels = []

n_target_range = range(2, 8)

for n_targets in n_target_range:
    sam = Samurai(kenki_mastery=2, kenki_gauge=50)
    sam.has_getsu = True
    sam.has_ka = True
    sam.has_hissatsu_kaiten = True
    
    df, _, _ = sam.parse_rotation([('Tenka Goken')], n_targets=n_targets)
    
    potency_one_tenka.append(df['Potency']/20)
```

    average potency per GCD = 1026.0
    average potency per second = 427.5
    average potency per GCD = 1458.0000000000002
    average potency per second = 607.5
    average potency per GCD = 1836.0000000000005
    average potency per second = 765.0
    average potency per GCD = 2160.0
    average potency per second = 900.0
    average potency per GCD = 2430.0
    average potency per second = 1012.5
    average potency per GCD = 2700.0
    average potency per second = 1125.0
    


```python
fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, figsize=(12,4))
fig.tight_layout(pad=2)

axes.plot(n_target_range, potency_one_tenka, '-o', label='Hissatsu: Kaiten and Tenka Goken')
axes.plot(n_target_range, [n*150/25 for n in n_target_range], '-^', label='Hissatsu: Kyuten')
axes.set_ylabel('Potency per Kenki')
axes.set_xlabel('Number of Targets')
axes.legend(loc='upper left', framealpha=0.5)

fig.suptitle('Total Potency per Kenki')
```




    <matplotlib.text.Text at 0x18c24dd33c8>




![png](output_31_1.png)


Expending Kenki on Hissatsu: Kaiten for Tenka Goken is the best bang for your buck, no question. When you only have enough Kenki for Hissatsu: Kaiten or Hissatsu: Kyuten, choose Hissatsu: Kaiten, hands down.

However, as we saw in the two previous examples, using Kenki exclusively on Hissatsu: Kyuten is extremely competitive with using Kenki on both. Additionally, it is superior to using Hissatsu: Kaiten exclusively. We can credit this to the minimal prerequisites for using Hissatsu: Kyuten; even though it costs more Kenki, you do not have to build Sen to use it, unlike Tenka Goken (with Hissatsu: Kaiten).

## Level 68-70

Level 68 is a pivotal shift in how Samurai plays. It grants you Hagakure, an ability on a short 40s cooldown that converts open Sen to Kenki at a 1 to 20 rate. Initially, this came as a headscratcher to many folks: b-but muh Iaijutsu? Samurai post-50 driven by Kenki more than Sen. The addition of powerful Kenki spenders like Hissatsu: Shinten and the level 70 capstone Hissatsu: Guren adds significant potency to the samurai rotation off the GCD. Iaijutsu, while powerful in their own right, cost a GCD and delay Kenki generation from the other weaponskills.

Consider Midare Setsugekka. At the cost of three Sen, it deals 720 potency. If instead of using those three Sen on Iaijutsu, what if we used Hagakure to generate 60 Kenki?

We could spend it on...
- Hissatsu: Guren, for 800+ potency for 50 Kenki.
- Hissatsu: Shinten (x2.4), for 720 potency for 60 Kenki.
- Hissatsu: Kyuten (x2.4), for burst AoE opportunities.

Essentially, Hagakure converts damage potential from being on the GCD to being off the GCD. This grants flexibility in how you produce damage, streamlines the weaponskill rotation, increases Kenki generation, and overall fills out the samurai rotation. See part 5 for in-depth discussion on Hagakure usage.

### Example Hagakure usage


```python
sam = Samurai(kenki_mastery=2)

actions = [('Hakaze'), ('Shifu'), ('Kasha'), 
           ('Hakaze'), ('Jinpu', 'Hissatsu: Kaiten'), ('Higanbana'), ('Gekko', 'Meikyo Shisui'), 
           ('Yukikaze'), ('Kasha', 'Hagakure'), ('Gekko', 'Hissatsu: Guren'),
           ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Shinten'),
           ('Hakaze', 'Hissatsu: Shinten'), ('Yukikaze', 'Hissatsu: Shinten'),
           ('Hakaze'), ('Jinpu'), ('Gekko', 'Hissatsu: Kaiten'), ('Midare Setsugekka'),
           ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Shinten'),
           ('Hakaze'), ('Yukikaze'),
           ('Hakaze'), ('Jinpu'), ('Gekko', 'Hissatsu: Shinten'),
           ('Hakaze', 'Hagakure'), ('Shifu', 'Hissatsu: Shinten'), ('Kasha', 'Hissatsu: Shinten'),
           ('Hakaze'), ('Jinpu', 'Hissatsu: Kaiten'), ('Higanbana'), ('Gekko', 'Hissatsu: Shinten'),
           ('Hakaze'), ('Yukikaze', 'Hissatsu: Shinten'),
           ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Kaiten'), ('Midare Setsugekka')
           ]
```


```python
df2, average_potency, pps = sam.parse_rotation(actions)
display(df2)
```

    average potency per GCD = 545.2244999999999
    average potency per second = 251.719529086
    


<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Time</th>
      <th>Weaponskill</th>
      <th>Abilities</th>
      <th>Potency</th>
      <th>Jinpu</th>
      <th>Shifu</th>
      <th>Yukikaze</th>
      <th>Higanbana</th>
      <th>Kenki</th>
      <th>Total Potency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>0</td>
      <td>150.000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>5</td>
      <td>430.000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Kasha</td>
      <td></td>
      <td>400.000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>830.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>20</td>
      <td>980.000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Jinpu</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>280.000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>25</td>
      <td>1260.000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Higanbana</td>
      <td></td>
      <td>323.470</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>1583.470</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Gekko</td>
      <td>(Meikyo Shisui,)</td>
      <td>503.470</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>10</td>
      <td>2086.940</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Yukikaze</td>
      <td></td>
      <td>434.470</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>20</td>
      <td>2521.410</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Kasha</td>
      <td>(Hagakure,)</td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>30</td>
      <td>3075.480</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Gekko</td>
      <td>(Hissatsu: Guren,)</td>
      <td>1575.270</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>4650.750</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>50</td>
      <td>4885.695</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Shifu</td>
      <td></td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>55</td>
      <td>5286.585</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Kasha</td>
      <td>(Hissatsu: Shinten,)</td>
      <td>937.020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>60</td>
      <td>6223.605</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Hakaze</td>
      <td>(Hissatsu: Shinten,)</td>
      <td>617.895</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>45</td>
      <td>6841.500</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Yukikaze</td>
      <td>(Hissatsu: Shinten,)</td>
      <td>860.430</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>25</td>
      <td>7701.930</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10</td>
      <td>7936.875</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Jinpu</td>
      <td></td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>8337.765</td>
    </tr>
    <tr>
      <th>17</th>
      <td>36.96</td>
      <td>Gekko</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>8891.835</td>
    </tr>
    <tr>
      <th>18</th>
      <td>39.12</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1422.090</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10</td>
      <td>10313.925</td>
    </tr>
    <tr>
      <th>19</th>
      <td>41.28</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10</td>
      <td>10548.870</td>
    </tr>
    <tr>
      <th>20</th>
      <td>43.44</td>
      <td>Shifu</td>
      <td></td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>10949.760</td>
    </tr>
    <tr>
      <th>21</th>
      <td>45.60</td>
      <td>Kasha</td>
      <td>(Hissatsu: Shinten,)</td>
      <td>937.020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>11886.780</td>
    </tr>
    <tr>
      <th>22</th>
      <td>47.76</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5</td>
      <td>12121.725</td>
    </tr>
    <tr>
      <th>23</th>
      <td>49.92</td>
      <td>Yukikaze</td>
      <td></td>
      <td>477.480</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10</td>
      <td>12599.205</td>
    </tr>
    <tr>
      <th>24</th>
      <td>52.08</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>12834.150</td>
    </tr>
    <tr>
      <th>25</th>
      <td>54.24</td>
      <td>Jinpu</td>
      <td></td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>25</td>
      <td>13235.040</td>
    </tr>
    <tr>
      <th>26</th>
      <td>56.40</td>
      <td>Gekko</td>
      <td>(Hissatsu: Shinten,)</td>
      <td>937.020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>30</td>
      <td>14172.060</td>
    </tr>
    <tr>
      <th>27</th>
      <td>58.56</td>
      <td>Hakaze</td>
      <td>(Hagakure,)</td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>14407.005</td>
    </tr>
    <tr>
      <th>28</th>
      <td>60.72</td>
      <td>Shifu</td>
      <td>(Hissatsu: Shinten,)</td>
      <td>783.840</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>15190.845</td>
    </tr>
    <tr>
      <th>29</th>
      <td>62.88</td>
      <td>Kasha</td>
      <td>(Hissatsu: Shinten,)</td>
      <td>937.020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>60</td>
      <td>16127.865</td>
    </tr>
    <tr>
      <th>30</th>
      <td>65.04</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>45</td>
      <td>16362.810</td>
    </tr>
    <tr>
      <th>31</th>
      <td>67.20</td>
      <td>Jinpu</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>50</td>
      <td>16763.700</td>
    </tr>
    <tr>
      <th>32</th>
      <td>69.36</td>
      <td>Higanbana</td>
      <td></td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>17164.590</td>
    </tr>
    <tr>
      <th>33</th>
      <td>71.52</td>
      <td>Gekko</td>
      <td>(Hissatsu: Shinten,)</td>
      <td>937.020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>18101.610</td>
    </tr>
    <tr>
      <th>34</th>
      <td>73.68</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>18336.555</td>
    </tr>
    <tr>
      <th>35</th>
      <td>75.84</td>
      <td>Yukikaze</td>
      <td>(Hissatsu: Shinten,)</td>
      <td>860.430</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>25</td>
      <td>19196.985</td>
    </tr>
    <tr>
      <th>36</th>
      <td>78.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.945</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10</td>
      <td>19431.930</td>
    </tr>
    <tr>
      <th>37</th>
      <td>80.16</td>
      <td>Shifu</td>
      <td></td>
      <td>400.890</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>19832.820</td>
    </tr>
    <tr>
      <th>38</th>
      <td>82.32</td>
      <td>Kasha</td>
      <td>(Hissatsu: Kaiten,)</td>
      <td>554.070</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>20386.890</td>
    </tr>
    <tr>
      <th>39</th>
      <td>84.48</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1422.090</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10</td>
      <td>21808.980</td>
    </tr>
  </tbody>
</table>
</div>



```python
compare_n_potencies([df0, df1, df2], ['No Hissatsu: Shinten', 'With Hissatsu: Shinten', 'lvl 70'])
```


![png](output_38_0.png)


We can easily observe the impact of increased Kenki generation and spending from level 67 and up. The addition of the devastating Hissatsu: Guren plus the Kenki generated with Hagakure allow us to rapidly pile on damage with an early onslaught of Hissatsu: Shinten. 

Developing an intuition for Kenki management and planning out your weaponskill rotation as each encounter demands are the keys to playing Samurai well.

<a href="#header">back to the top...</a>
