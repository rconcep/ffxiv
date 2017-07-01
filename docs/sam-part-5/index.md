
<a id="header"></a>
# Part 5: miscellaneous topics


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

## Table of contents
- <a href="#buff-priority">On buff priority</a>
- <a href="#meikyo-shisui">On Meikyo Shisui</a>
- <a href="#kenki-spending">On Kenki spending</a>
- <a href="#hissatsu-mobility">On Hissatsu: Gyoten / Yaten</a>
- <a href="#third-eye">On Third Eye</a>
- <a href="#hagakure">On Hagakure</a>

<a id="buff-priority"></a>
## On buff priority

SAM has two self buffs and one target debuff to apply. The slashing resistance down debuff may be applied by WAR and NIN within 2-3 GCDs, letting you defer Yukikaze. What order should you apply your buffs and debuffs from a fresh start? Let's examine some rotations that differ only in the buff/debuff application order.

### Shifu, Jinpu, Yukikaze


```python
sam = Samurai(kenki_mastery=True)

actions = [('Hakaze'), ('Shifu'), ('Kasha'),
           ('Higanbana'),
           ('Hakaze'), ('Jinpu'), ('Gekko'),
           ('Hakaze'), ('Yukikaze'),
           ('Hakaze', 'Hissatsu: Shinten'), ('Shifu', 'Hissatsu: Shinten'), ('Kasha', 'Hagakure'),
           ('Hakaze', 'Hissatsu: Guren'), ('Yukikaze', 'Hissatsu: Shinten'),
           ('Hakaze', 'Hissatsu: Shinten'), ('Jinpu'), ('Gekko'),
           ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka')]
```


```python
df_buffs_0, average_potency, pps = sam.parse_rotation(actions)
display(df_buffs_0)
```

    average potency per GCD = 511.8080952380951
    average potency per second = 235.701096491
    


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
      <th>Ability</th>
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
      <td>Higanbana</td>
      <td></td>
      <td>240.000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>20</td>
      <td>1070.000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Hakaze</td>
      <td></td>
      <td>175.200</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>20</td>
      <td>1245.200</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Jinpu</td>
      <td></td>
      <td>308.980</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>25</td>
      <td>1554.180</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Gekko</td>
      <td></td>
      <td>488.980</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>30</td>
      <td>2043.160</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Hakaze</td>
      <td></td>
      <td>201.480</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>40</td>
      <td>2244.640</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Yukikaze</td>
      <td></td>
      <td>419.980</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>45</td>
      <td>2664.620</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Hakaze</td>
      <td>Hissatsu: Shinten</td>
      <td>603.405</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>55</td>
      <td>3268.025</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Shifu</td>
      <td>Hissatsu: Shinten</td>
      <td>769.350</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>4037.375</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Kasha</td>
      <td>Hagakure</td>
      <td>539.580</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>4576.955</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Hakaze</td>
      <td>Hissatsu: Guren</td>
      <td>1241.655</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>85</td>
      <td>5818.610</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Shinten</td>
      <td>845.940</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>40</td>
      <td>6664.550</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Hakaze</td>
      <td>Hissatsu: Shinten</td>
      <td>603.405</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>25</td>
      <td>7267.955</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Jinpu</td>
      <td></td>
      <td>386.400</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5</td>
      <td>7654.355</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Gekko</td>
      <td></td>
      <td>539.580</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10</td>
      <td>8193.935</td>
    </tr>
    <tr>
      <th>17</th>
      <td>36.96</td>
      <td>Hakaze</td>
      <td></td>
      <td>220.455</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>8414.390</td>
    </tr>
    <tr>
      <th>18</th>
      <td>39.12</td>
      <td>Shifu</td>
      <td></td>
      <td>386.400</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>25</td>
      <td>8800.790</td>
    </tr>
    <tr>
      <th>19</th>
      <td>41.28</td>
      <td>Kasha</td>
      <td>Hissatsu: Kaiten</td>
      <td>539.580</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>30</td>
      <td>9340.370</td>
    </tr>
    <tr>
      <th>20</th>
      <td>43.44</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1407.600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>10747.970</td>
    </tr>
  </tbody>
</table>
</div>


### Jinpu, Shifu, Yukikaze


```python
sam = Samurai(kenki_mastery=True)

actions = [('Hakaze'), ('Jinpu'), ('Gekko'),
           ('Higanbana'),
           ('Hakaze'), ('Shifu'), ('Kasha'),           
           ('Hakaze'), ('Yukikaze'),
           ('Hakaze', 'Hissatsu: Shinten'), ('Jinpu', 'Hissatsu: Shinten'), ('Gekko', 'Hagakure'),
           ('Hakaze', 'Hissatsu: Guren'), ('Yukikaze', 'Hissatsu: Shinten'),
           ('Hakaze', 'Hissatsu: Shinten'), ('Shifu'), ('Kasha'),
           ('Hakaze'), ('Jinpu'), ('Gekko', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka')]
```


```python
df_buffs_1, average_potency, pps = sam.parse_rotation(actions)
display(df_buffs_1)
```

    average potency per GCD = 523.5026190476191
    average potency per second = 236.115871993
    


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
      <th>Ability</th>
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
      <td>Jinpu</td>
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
      <td>4.80</td>
      <td>Gekko</td>
      <td></td>
      <td>460.000</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>890.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.20</td>
      <td>Higanbana</td>
      <td></td>
      <td>276.000</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>20</td>
      <td>1166.000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.60</td>
      <td>Hakaze</td>
      <td></td>
      <td>209.530</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>1</td>
      <td>20</td>
      <td>1375.530</td>
    </tr>
    <tr>
      <th>5</th>
      <td>12.00</td>
      <td>Shifu</td>
      <td></td>
      <td>359.030</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>1</td>
      <td>25</td>
      <td>1734.560</td>
    </tr>
    <tr>
      <th>6</th>
      <td>14.16</td>
      <td>Kasha</td>
      <td></td>
      <td>493.327</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>30</td>
      <td>2227.887</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16.32</td>
      <td>Hakaze</td>
      <td></td>
      <td>205.827</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>40</td>
      <td>2433.714</td>
    </tr>
    <tr>
      <th>8</th>
      <td>18.48</td>
      <td>Yukikaze</td>
      <td></td>
      <td>424.327</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>45</td>
      <td>2858.041</td>
    </tr>
    <tr>
      <th>9</th>
      <td>20.64</td>
      <td>Hakaze</td>
      <td>Hissatsu: Shinten</td>
      <td>607.752</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>55</td>
      <td>3465.793</td>
    </tr>
    <tr>
      <th>10</th>
      <td>22.80</td>
      <td>Jinpu</td>
      <td>Hissatsu: Shinten</td>
      <td>773.697</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>4239.490</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.96</td>
      <td>Gekko</td>
      <td>Hagakure</td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>4783.417</td>
    </tr>
    <tr>
      <th>12</th>
      <td>27.12</td>
      <td>Hakaze</td>
      <td>Hissatsu: Guren</td>
      <td>1246.002</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>85</td>
      <td>6029.419</td>
    </tr>
    <tr>
      <th>13</th>
      <td>29.28</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Shinten</td>
      <td>850.287</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>40</td>
      <td>6879.706</td>
    </tr>
    <tr>
      <th>14</th>
      <td>31.44</td>
      <td>Hakaze</td>
      <td>Hissatsu: Shinten</td>
      <td>607.752</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>25</td>
      <td>7487.458</td>
    </tr>
    <tr>
      <th>15</th>
      <td>33.60</td>
      <td>Shifu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5</td>
      <td>7878.205</td>
    </tr>
    <tr>
      <th>16</th>
      <td>35.76</td>
      <td>Kasha</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10</td>
      <td>8422.132</td>
    </tr>
    <tr>
      <th>17</th>
      <td>37.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>8646.934</td>
    </tr>
    <tr>
      <th>18</th>
      <td>40.08</td>
      <td>Jinpu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>25</td>
      <td>9037.681</td>
    </tr>
    <tr>
      <th>19</th>
      <td>42.24</td>
      <td>Gekko</td>
      <td>Hissatsu: Kaiten</td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>30</td>
      <td>9581.608</td>
    </tr>
    <tr>
      <th>20</th>
      <td>44.40</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1411.947</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>10993.555</td>
    </tr>
  </tbody>
</table>
</div>


### Yukikaze, Jinpu, Shifu


```python
sam = Samurai(kenki_mastery=True)

actions = [('Hakaze'), ('Yukikaze'),
           ('Higanbana'),
           ('Hakaze'), ('Jinpu'), ('Gekko'),
           ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Shinten'),           
           ('Hakaze', 'Hissatsu: Shinten'), ('Yukikaze', 'Hagakure'),
           ('Hakaze', 'Hissatsu: Guren'), ('Jinpu', 'Hissatsu: Shinten'), ('Gekko', 'Hissatsu: Shinten'),
           ('Hakaze'), ('Yukikaze'),
           ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'),
           ('Hakaze')]
```


```python
df_buffs_2, average_potency, pps = sam.parse_rotation(actions)
display(df_buffs_2)
```

    average potency per GCD = 515.7328571428571
    average potency per second = 230.237882653
    


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
      <th>Ability</th>
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
      <td>Yukikaze</td>
      <td></td>
      <td>340.000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>5</td>
      <td>490.000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.80</td>
      <td>Higanbana</td>
      <td></td>
      <td>266.400</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>0</td>
      <td>15</td>
      <td>756.400</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.20</td>
      <td>Hakaze</td>
      <td></td>
      <td>194.500</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>950.900</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.60</td>
      <td>Jinpu</td>
      <td></td>
      <td>343.000</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>1293.900</td>
    </tr>
    <tr>
      <th>5</th>
      <td>12.00</td>
      <td>Gekko</td>
      <td></td>
      <td>542.800</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>1</td>
      <td>25</td>
      <td>1836.700</td>
    </tr>
    <tr>
      <th>6</th>
      <td>14.40</td>
      <td>Hakaze</td>
      <td></td>
      <td>223.675</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>2060.375</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16.80</td>
      <td>Shifu</td>
      <td></td>
      <td>389.620</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>1</td>
      <td>40</td>
      <td>2449.995</td>
    </tr>
    <tr>
      <th>8</th>
      <td>18.96</td>
      <td>Kasha</td>
      <td>Hissatsu: Shinten</td>
      <td>922.530</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>45</td>
      <td>3372.525</td>
    </tr>
    <tr>
      <th>9</th>
      <td>21.12</td>
      <td>Hakaze</td>
      <td>Hissatsu: Shinten</td>
      <td>603.405</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>30</td>
      <td>3975.930</td>
    </tr>
    <tr>
      <th>10</th>
      <td>23.28</td>
      <td>Yukikaze</td>
      <td>Hagakure</td>
      <td>462.990</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10</td>
      <td>4438.920</td>
    </tr>
    <tr>
      <th>11</th>
      <td>25.44</td>
      <td>Hakaze</td>
      <td>Hissatsu: Guren</td>
      <td>1241.655</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>5680.575</td>
    </tr>
    <tr>
      <th>12</th>
      <td>27.60</td>
      <td>Jinpu</td>
      <td>Hissatsu: Shinten</td>
      <td>769.350</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>6449.925</td>
    </tr>
    <tr>
      <th>13</th>
      <td>29.76</td>
      <td>Gekko</td>
      <td>Hissatsu: Shinten</td>
      <td>922.530</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>7372.455</td>
    </tr>
    <tr>
      <th>14</th>
      <td>31.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>220.455</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>0</td>
      <td>7592.910</td>
    </tr>
    <tr>
      <th>15</th>
      <td>34.08</td>
      <td>Yukikaze</td>
      <td></td>
      <td>462.990</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5</td>
      <td>8055.900</td>
    </tr>
    <tr>
      <th>16</th>
      <td>36.24</td>
      <td>Hakaze</td>
      <td></td>
      <td>220.455</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>8276.355</td>
    </tr>
    <tr>
      <th>17</th>
      <td>38.40</td>
      <td>Shifu</td>
      <td></td>
      <td>386.400</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>8662.755</td>
    </tr>
    <tr>
      <th>18</th>
      <td>40.56</td>
      <td>Kasha</td>
      <td>Hissatsu: Kaiten</td>
      <td>539.580</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>25</td>
      <td>9202.335</td>
    </tr>
    <tr>
      <th>19</th>
      <td>42.72</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1407.600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>10609.935</td>
    </tr>
    <tr>
      <th>20</th>
      <td>44.88</td>
      <td>Hakaze</td>
      <td></td>
      <td>220.455</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>10830.390</td>
    </tr>
  </tbody>
</table>
</div>


### Yukikaze, Shifu, Jinpu


```python
sam = Samurai(kenki_mastery=True)

actions = [('Hakaze'), ('Yukikaze'),
           ('Higanbana'),
           ('Hakaze'), ('Shifu'), ('Kasha'),
           ('Hakaze'), ('Jinpu'), ('Gekko', 'Hissatsu: Shinten'),           
           ('Hakaze', 'Hissatsu: Shinten'), ('Yukikaze', 'Hagakure'),
           ('Hakaze', 'Hissatsu: Guren'), ('Jinpu', 'Hissatsu: Shinten'), ('Gekko', 'Hissatsu: Shinten'),
           ('Hakaze'), ('Yukikaze'),
           ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'),
           ('Hakaze')]
```


```python
df_buffs_3, average_potency, pps = sam.parse_rotation(actions)
display(df_buffs_3)
```

    average potency per GCD = 508.13214285714287
    average potency per second = 230.370790155
    


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
      <th>Ability</th>
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
      <td>Yukikaze</td>
      <td></td>
      <td>340.000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>5</td>
      <td>490.000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.80</td>
      <td>Higanbana</td>
      <td></td>
      <td>266.400</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>0</td>
      <td>15</td>
      <td>756.400</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.20</td>
      <td>Hakaze</td>
      <td></td>
      <td>194.500</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>950.900</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.60</td>
      <td>Shifu</td>
      <td></td>
      <td>338.800</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>1289.700</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.76</td>
      <td>Kasha</td>
      <td></td>
      <td>469.200</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>25</td>
      <td>1758.900</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>191.700</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>1950.600</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16.08</td>
      <td>Jinpu</td>
      <td></td>
      <td>339.780</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>40</td>
      <td>2290.380</td>
    </tr>
    <tr>
      <th>8</th>
      <td>18.24</td>
      <td>Gekko</td>
      <td>Hissatsu: Shinten</td>
      <td>922.530</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>45</td>
      <td>3212.910</td>
    </tr>
    <tr>
      <th>9</th>
      <td>20.40</td>
      <td>Hakaze</td>
      <td>Hissatsu: Shinten</td>
      <td>603.405</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>30</td>
      <td>3816.315</td>
    </tr>
    <tr>
      <th>10</th>
      <td>22.56</td>
      <td>Yukikaze</td>
      <td>Hagakure</td>
      <td>462.990</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10</td>
      <td>4279.305</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.72</td>
      <td>Hakaze</td>
      <td>Hissatsu: Guren</td>
      <td>1241.655</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>5520.960</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.88</td>
      <td>Jinpu</td>
      <td>Hissatsu: Shinten</td>
      <td>769.350</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>6290.310</td>
    </tr>
    <tr>
      <th>13</th>
      <td>29.04</td>
      <td>Gekko</td>
      <td>Hissatsu: Shinten</td>
      <td>922.530</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>7212.840</td>
    </tr>
    <tr>
      <th>14</th>
      <td>31.20</td>
      <td>Hakaze</td>
      <td></td>
      <td>220.455</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>0</td>
      <td>7433.295</td>
    </tr>
    <tr>
      <th>15</th>
      <td>33.36</td>
      <td>Yukikaze</td>
      <td></td>
      <td>462.990</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5</td>
      <td>7896.285</td>
    </tr>
    <tr>
      <th>16</th>
      <td>35.52</td>
      <td>Hakaze</td>
      <td></td>
      <td>220.455</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>8116.740</td>
    </tr>
    <tr>
      <th>17</th>
      <td>37.68</td>
      <td>Shifu</td>
      <td></td>
      <td>386.400</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>8503.140</td>
    </tr>
    <tr>
      <th>18</th>
      <td>39.84</td>
      <td>Kasha</td>
      <td>Hissatsu: Kaiten</td>
      <td>539.580</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>25</td>
      <td>9042.720</td>
    </tr>
    <tr>
      <th>19</th>
      <td>42.00</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1407.600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>10450.320</td>
    </tr>
    <tr>
      <th>20</th>
      <td>44.16</td>
      <td>Hakaze</td>
      <td></td>
      <td>220.455</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>10670.775</td>
    </tr>
  </tbody>
</table>
</div>



```python
compare_n_potencies([df_buffs_0, df_buffs_1, df_buffs_2, df_buffs_3], ['Shifu, Jinpu, Yukikaze', 'Jinpu, Shifu, Yukikaze', 'Yukikaze, Jinpu, Shifu', 'Yukikaze, Shifu, Jinpu'])
```


![png](output_16_0.png)


The results are quite close but Jinpu > Shifu > Yukikaze appears to be the highest priority. For total party DPS, contributions due to (~16s) earlier application of the slashing resistance down debuff should be accounted for, assuming no WAR or NIN in the party. How do priorities differ if someone else, e.g., WAR, can applythe debuff instead?


```python
sam = Samurai(kenki_mastery=True)
sam.applied_yukikaze = True

actions = [('Hakaze'), ('Shifu'), ('Kasha'),
           ('Higanbana'),
           ('Hakaze'), ('Jinpu'), ('Gekko'),
           ('Hakaze'), ('Yukikaze'),
           ('Hakaze', 'Hissatsu: Shinten'), ('Shifu', 'Hissatsu: Shinten'), ('Kasha', 'Hagakure'),
           ('Hakaze', 'Hissatsu: Guren'), ('Yukikaze', 'Hissatsu: Shinten'),
           ('Hakaze', 'Hissatsu: Shinten'), ('Jinpu'), ('Gekko'),
           ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka')]

df_buffs_0_sl, average_potency, pps = sam.parse_rotation(actions)

sam = Samurai(kenki_mastery=True)
sam.applied_yukikaze = True

actions = [('Hakaze'), ('Jinpu'), ('Gekko'),
           ('Higanbana'),
           ('Hakaze'), ('Shifu'), ('Kasha'),           
           ('Hakaze'), ('Yukikaze'),
           ('Hakaze', 'Hissatsu: Shinten'), ('Jinpu', 'Hissatsu: Shinten'), ('Gekko', 'Hagakure'),
           ('Hakaze', 'Hissatsu: Guren'), ('Yukikaze', 'Hissatsu: Shinten'),
           ('Hakaze', 'Hissatsu: Shinten'), ('Shifu'), ('Kasha'),
           ('Hakaze'), ('Jinpu'), ('Gekko', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka')]

df_buffs_1_sl, average_potency, pps = sam.parse_rotation(actions)

sam = Samurai(kenki_mastery=True)
sam.applied_yukikaze = True

actions = [('Hakaze'), ('Yukikaze'),
           ('Higanbana'),
           ('Hakaze'), ('Jinpu'), ('Gekko'),
           ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Shinten'),           
           ('Hakaze', 'Hissatsu: Shinten'), ('Yukikaze', 'Hagakure'),
           ('Hakaze', 'Hissatsu: Guren'), ('Jinpu', 'Hissatsu: Shinten'), ('Gekko', 'Hissatsu: Shinten'),
           ('Hakaze'), ('Yukikaze'),
           ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'),
           ('Hakaze')]

df_buffs_2_sl, average_potency, pps = sam.parse_rotation(actions)

sam = Samurai(kenki_mastery=True)
sam.applied_yukikaze = True

actions = [('Hakaze'), ('Yukikaze'),
           ('Higanbana'),
           ('Hakaze'), ('Shifu'), ('Kasha'),
           ('Hakaze'), ('Jinpu'), ('Gekko', 'Hissatsu: Shinten'),           
           ('Hakaze', 'Hissatsu: Shinten'), ('Yukikaze', 'Hagakure'),
           ('Hakaze', 'Hissatsu: Guren'), ('Jinpu', 'Hissatsu: Shinten'), ('Gekko', 'Hissatsu: Shinten'),
           ('Hakaze'), ('Yukikaze'),
           ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'),
           ('Hakaze')]

df_buffs_3_sl, average_potency, pps = sam.parse_rotation(actions)
```

    average potency per GCD = 522.7740476190475
    average potency per second = 240.75120614
    average potency per GCD = 535.3092857142858
    average potency per second = 241.441043814
    average potency per GCD = 515.7328571428571
    average potency per second = 230.237882653
    average potency per GCD = 508.13214285714287
    average potency per second = 230.370790155
    


```python
compare_n_potencies([df_buffs_0_sl, df_buffs_1_sl, df_buffs_2_sl, df_buffs_3_sl], ['Shifu, Jinpu, Yukikaze', 'Jinpu, Shifu, Yukikaze', 'Yukikaze, Jinpu, Shifu', 'Yukikaze, Shifu, Jinpu'])
```


![png](output_19_0.png)


Here I made the assumption that the slashing resistance down debuff was already applied at the beginning of each rotation. We see that the value of deferring Yukikaze increases if someone else can apply the debuff instead. Although the average potency per GCD is much higher when applying Jinpu before Shifu while the delta in pps is much smaller, the results are likely to change as your skill speed changes.

<a href="#header">back to the top...</a>

<a id="meikyo-shisui"></a>
## On Meikyo Shisui
Some of the initial questions of Meikyo Shisui were if Iaijutsu would consume charges of it and if combo actions initiated during it would continue after the buff expired. Testing on the live server showed:

- Iaijutsu does not consume charges
- Combo actions do not continue after the buff expires

The first revelation increases the flexibility of Meikyo Shisui. With the buff's 10s duration, it is possible to spend your three charges while using an Iaijutsu sometime in between. The implications of that are immense:

1) High, raw damage in 3-4 GCDs
    - e.g., with Setsu already open, do Kasha, Gekko+Hissatsu: Kaiten, Midare Setsugekka, Kasha. That's 1200+1080=2280 potency in 4 GCDs plus 30 Kenki.

2) Up to 30 Kenki generated in 3-4 GCDs

3) Expedited Sen opening for rapid Iaijutsu and/or Kenki generation via Hagakure

The sheer potency and utility of Kasha, Gekko, and (to a lesser extent) Yukikaze exemplify how powerful Meikyo Shisui is. At 400 potency (340 for Yukikaze) and 10 Kenki generated for each, the opportunity to skip the lower potency and Kenki production of Hakaze, Shifu, and Jinpu is immense. From a damage and potential damage perspective, it is optimal to use Meikyo Shisui to do some combination of Kasha, Gekko, and Yukikaze with an Iaijutsu in between.

### Example 1: Two of Kasha or Gekko, one of the other


```python
sam = Samurai(kenki_mastery=True)

actions = [('Hakaze'), ('Jinpu'), ('Gekko'),
           ('Hakaze'), ('Shifu'), ('Kasha'),
           ('Hakaze'), ('Yukikaze', 'Hissatsu: Guren'),
           ('Hakaze', 'Hagakure'), ('Yukikaze', 'Meikyo Shisui'),
           ('Gekko', 'Hissatsu: Shinten'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'),
           ('Kasha', 'Hissatsu: Shinten'),
           ('Hakaze', 'Hissatsu: Shinten'), ('Jinpu'), ('Gekko'),
           ('Hakaze'), ('Yukikaze'),
           ('Hakaze'), ('Shifu', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'),
           ('Kasha', 'Hissatsu: Shinten')]

df_ms, average_potency, pps = sam.parse_rotation(actions)
display(df_ms)
```

    average potency per GCD = 532.045652173913
    average potency per second = 241.647906793
    


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
      <th>Ability</th>
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
      <td>Jinpu</td>
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
      <td>4.80</td>
      <td>Gekko</td>
      <td></td>
      <td>460.000</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>890.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.20</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.500</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>20</td>
      <td>1062.500</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.60</td>
      <td>Shifu</td>
      <td></td>
      <td>322.000</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>25</td>
      <td>1384.500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.76</td>
      <td>Kasha</td>
      <td></td>
      <td>460.000</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>30</td>
      <td>1844.500</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.500</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>40</td>
      <td>2017.000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16.08</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Guren</td>
      <td>1412.200</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>45</td>
      <td>3429.200</td>
    </tr>
    <tr>
      <th>8</th>
      <td>18.24</td>
      <td>Hakaze</td>
      <td>Hagakure</td>
      <td>191.475</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>5</td>
      <td>3620.675</td>
    </tr>
    <tr>
      <th>9</th>
      <td>20.40</td>
      <td>Yukikaze</td>
      <td>Meikyo Shisui</td>
      <td>434.010</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>70</td>
      <td>4054.685</td>
    </tr>
    <tr>
      <th>10</th>
      <td>22.56</td>
      <td>Gekko</td>
      <td>Hissatsu: Shinten</td>
      <td>893.550</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>80</td>
      <td>4948.235</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.72</td>
      <td>Kasha</td>
      <td>Hissatsu: Kaiten</td>
      <td>510.600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>65</td>
      <td>5458.835</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.88</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1378.620</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>55</td>
      <td>6837.455</td>
    </tr>
    <tr>
      <th>13</th>
      <td>29.04</td>
      <td>Kasha</td>
      <td>Hissatsu: Shinten</td>
      <td>510.600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>55</td>
      <td>7348.055</td>
    </tr>
    <tr>
      <th>14</th>
      <td>31.20</td>
      <td>Hakaze</td>
      <td>Hissatsu: Shinten</td>
      <td>574.425</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>30</td>
      <td>7922.480</td>
    </tr>
    <tr>
      <th>15</th>
      <td>33.36</td>
      <td>Jinpu</td>
      <td></td>
      <td>357.420</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>10</td>
      <td>8279.900</td>
    </tr>
    <tr>
      <th>16</th>
      <td>35.52</td>
      <td>Gekko</td>
      <td></td>
      <td>510.600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>15</td>
      <td>8790.500</td>
    </tr>
    <tr>
      <th>17</th>
      <td>37.68</td>
      <td>Hakaze</td>
      <td></td>
      <td>191.475</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>25</td>
      <td>8981.975</td>
    </tr>
    <tr>
      <th>18</th>
      <td>39.84</td>
      <td>Yukikaze</td>
      <td></td>
      <td>434.010</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>0</td>
      <td>30</td>
      <td>9415.985</td>
    </tr>
    <tr>
      <th>19</th>
      <td>42.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>191.475</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>0</td>
      <td>40</td>
      <td>9607.460</td>
    </tr>
    <tr>
      <th>20</th>
      <td>44.16</td>
      <td>Shifu</td>
      <td>Hissatsu: Kaiten</td>
      <td>357.420</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>0</td>
      <td>45</td>
      <td>9964.880</td>
    </tr>
    <tr>
      <th>21</th>
      <td>46.32</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1378.620</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>30</td>
      <td>11343.500</td>
    </tr>
    <tr>
      <th>22</th>
      <td>48.48</td>
      <td>Kasha</td>
      <td>Hissatsu: Shinten</td>
      <td>893.550</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>30</td>
      <td>12237.050</td>
    </tr>
  </tbody>
</table>
</div>



```python
plot_potency(df_ms)
```


![png](output_24_0.png)


By using some combination of Kasha and Gekko only for our Meikyo Shisui charges, we end up with the situation where one of our Shifu or Jinpu buffs will fall off. This is due to us avoiding combos that terminate in opening a Sen that has already been opened; in this example, it was the Kasha combo leading to Shifu being dropped for about 4-5 seconds. In this instance, we moved the final Midare Setsugekka to after Hakaze -> Shifu to minimize Shifu downtime.

The penalty for dropping the Shifu or Jinpu buff is in the neighborhood of 9-15% potency per GCD. For example, dropping Jinpu for 4-5 seconds is about two GCDs plus auto attacks; Hakaze -> Jinpu is 150+280=430 potency plus maybe 2 auto attacks. This puts the raw potency lost due to a dropped buff in the order of 90-100 (auto attacks not accounted for in my modeling). This is larger than the difference between Yukikaze and Kasha or Gekko.

### Example: One Yukikaze, two of Kasha and/or Gekko


```python
sam = Samurai(kenki_mastery=True)

actions = [('Hakaze'), ('Jinpu'), ('Gekko'),
           ('Hakaze'), ('Shifu'), ('Kasha'),
           ('Hakaze'), ('Yukikaze', 'Hissatsu: Guren'),
           ('Hakaze', 'Hagakure'), ('Jinpu'), ('Gekko', 'Meikyo Shisui'),
           ('Yukikaze', 'Hissatsu: Shinten'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'),
           ('Gekko', 'Hissatsu: Shinten'),
           ('Hakaze', 'Hissatsu: Shinten'), ('Shifu'), ('Kasha'),
           ('Hakaze'), ('Yukikaze'),
           ('Hakaze', 'Hissatsu: Shinten'), ('Jinpu', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'),
           ('Gekko', 'Hissatsu: Shinten')]

df_ms2, average_potency, pps = sam.parse_rotation(actions)
display(df_ms2)
```

    average potency per GCD = 556.6820833333333
    average potency per second = 253.037310606
    


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
      <th>Ability</th>
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
      <td>Jinpu</td>
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
      <td>4.80</td>
      <td>Gekko</td>
      <td></td>
      <td>460.000</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>890.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.20</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.500</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>20</td>
      <td>1062.500</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.60</td>
      <td>Shifu</td>
      <td></td>
      <td>322.000</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>25</td>
      <td>1384.500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.76</td>
      <td>Kasha</td>
      <td></td>
      <td>460.000</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>30</td>
      <td>1844.500</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.500</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>40</td>
      <td>2017.000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16.08</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Guren</td>
      <td>1412.200</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>45</td>
      <td>3429.200</td>
    </tr>
    <tr>
      <th>8</th>
      <td>18.24</td>
      <td>Hakaze</td>
      <td>Hagakure</td>
      <td>191.475</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>5</td>
      <td>3620.675</td>
    </tr>
    <tr>
      <th>9</th>
      <td>20.40</td>
      <td>Jinpu</td>
      <td></td>
      <td>357.420</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>70</td>
      <td>3978.095</td>
    </tr>
    <tr>
      <th>10</th>
      <td>22.56</td>
      <td>Gekko</td>
      <td>Meikyo Shisui</td>
      <td>510.600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>75</td>
      <td>4488.695</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.72</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Shinten</td>
      <td>816.960</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>85</td>
      <td>5305.655</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.88</td>
      <td>Kasha</td>
      <td>Hissatsu: Kaiten</td>
      <td>510.600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>70</td>
      <td>5816.255</td>
    </tr>
    <tr>
      <th>13</th>
      <td>29.04</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1378.620</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>60</td>
      <td>7194.875</td>
    </tr>
    <tr>
      <th>14</th>
      <td>31.20</td>
      <td>Gekko</td>
      <td>Hissatsu: Shinten</td>
      <td>893.550</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>60</td>
      <td>8088.425</td>
    </tr>
    <tr>
      <th>15</th>
      <td>33.36</td>
      <td>Hakaze</td>
      <td>Hissatsu: Shinten</td>
      <td>574.425</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>45</td>
      <td>8662.850</td>
    </tr>
    <tr>
      <th>16</th>
      <td>35.52</td>
      <td>Shifu</td>
      <td></td>
      <td>357.420</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>25</td>
      <td>9020.270</td>
    </tr>
    <tr>
      <th>17</th>
      <td>37.68</td>
      <td>Kasha</td>
      <td></td>
      <td>510.600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>30</td>
      <td>9530.870</td>
    </tr>
    <tr>
      <th>18</th>
      <td>39.84</td>
      <td>Hakaze</td>
      <td></td>
      <td>191.475</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>40</td>
      <td>9722.345</td>
    </tr>
    <tr>
      <th>19</th>
      <td>42.00</td>
      <td>Yukikaze</td>
      <td></td>
      <td>434.010</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>45</td>
      <td>10156.355</td>
    </tr>
    <tr>
      <th>20</th>
      <td>44.16</td>
      <td>Hakaze</td>
      <td>Hissatsu: Shinten</td>
      <td>574.425</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>55</td>
      <td>10730.780</td>
    </tr>
    <tr>
      <th>21</th>
      <td>46.32</td>
      <td>Jinpu</td>
      <td>Hissatsu: Kaiten</td>
      <td>357.420</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>35</td>
      <td>11088.200</td>
    </tr>
    <tr>
      <th>22</th>
      <td>48.48</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1378.620</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>20</td>
      <td>12466.820</td>
    </tr>
    <tr>
      <th>23</th>
      <td>50.64</td>
      <td>Gekko</td>
      <td>Hissatsu: Shinten</td>
      <td>893.550</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>20</td>
      <td>13360.370</td>
    </tr>
  </tbody>
</table>
</div>



```python
plot_potency(df_ms2)
```


![png](output_28_0.png)



```python
compare_n_potencies([df_ms, df_ms2], ['Gekko/Kasha only', 'Yukikaze + Gekko/Kasha'])
```


![png](output_29_0.png)


The advantage of using Yukikaze in your Meikyo Shisui window ensures you don't need to worry about dropping a buff. The final weaponskill you use on Meikyo Shisui should be the one of Kasha or Gekko corresponding to the buff with the longest remaining duration. For example, if Shifu has more duration than Jinpu, finish the window with Kasha then follow up with the Gekko combo. The auto-attack penalty from dropping a buff isn't accounted for here but regardless, the second policy comes out on top. (Generating extra Kenki for Hissatsu: Shinten doesn't hurt either.)

<a href="#header">back to the top...</a>

<a id="kenki-spending"></a>
## On Kenki spending
As I've iterated, Kenki grants access to just about all of your damage-dealing abilities which are, cumulatively, an enormous share of your potential DPS. Economical spending of Kenki is therefore essential to maximizing your DPS.

Throughout the leveling process, we gain a number of Kenki spenders. We examine their value by their potency per Kenki (ppK) in order to evaluate their usefulness.

### For single target situations:

1) Hissatsu: Guren (16 ppK)
    - Although at a lower ppK than 2), its potency is from the ability and not a weaponskill. It does not directly compete with Midare Setsugekka; it only competes via Hagakure usage.
    
2) Hissatsu: Kaiten on Midare Setsugekka (18 ppK)

3) Hissatsu: Seigan (~13 ppK)

4) Hissatsu: Shinten (12 ppK)

5) Hissatsu: Gyoten / Yaten (10 ppK)

5) Hissatsu: Kaiten on Gekko / Kasha (10 ppK)

### For multiple target situations:

1) Hissatsu: Guren (>16 ppK)

2) Hissatsu: Kaiten on Tenka Goken (>9 ppK)

3) Hissatsu: Kyuten (6*n* ppK, where *n* is the number of targets)
    - We examined the tradeoff between 2) and 3) in Part 4. In short, always have Kenki to use on Hissatsu: Kaiten for Tenka Goken. Excess Kenki goes to Hissatsu: Kyuten. With the Fuga, Oka, Fuga, Mangetsu combo generating 30 Kenki total, this should always be possible.

### Wasted Kenki
Kenki capping is a risk especially when using Hagakure to convert three Sen. The penalty for doing so may be determined via the ppK values above. Since Kenki is quantized in units of 5, the potency losses are not insignificant. These losses are, however, only realized if they would have been spendable in the first place. For example, if you overflowed Kenki by 5 but ended the encounter with 0 Kenki, then you haven't lost anything because that 5 Kenki could not have been spent anyway. However, if you instead ended with 5 Kenki, it is a loss of 100 potency because you could have spent the 10 Kenki on Hissatsu: Gyoten / Yaten.

Along those lines, while we strive to convert all Kenki into Hissatsu: Seigan / Shinten (in single target situations), ending an encounter with Kenki left on the table is a definite loss. Although typically less than ideal, dump Kenki into Hissatsu: Gyoten if it means Kenki goes unused otherwise. Alternatively, if you have 20 Kenki to spend, use it on Hissatsu: Kaiten for Gekko or Kasha.

<a href="#header">back to the top...</a>

<a id="hissatsu-mobility"></a>
## On Hissatsu: Gyoten / Yaten
The difference in ppK between Hissatsu: Shinten and Hissatsu: Gyoten is miniscule but there. The utility of a gap closer is increasing uptime via reduction of transit time. The increase in auto attacks from using Hissatsu: Gyoten should alone make it worth it; the increased weaponskill uptime for Sen and Kenki generation seals the deal. Use Hissatsu: Gyoten whenever you need the gap closer.

Hissatsu: Yaten is a little more subtle. The Enhanced Enpi proc granted increases the potency of the next Enpi you use to 300. Using this Enhanced Enpi gives you time to move back into range and refunds the Kenki cost of using Hissatsu: Yaten. Furthermore, the increased potency offsets the loss from not being able to do your weaponskill combos. (The Gekko/Kasha combos average ~276 potency per GCD plus the Kenki generated.) You may also argue that if you use Hissatsu: Yaten to stay active longer before disengaging to dodge adds benefit from increased uptime.

If our goal is to not take damage from point blank AoE attacks, then our options are:

1) Disengage early to dodge, then:

    1) Run back into range
    
    2) Hissatsu: Gyoten back into range

2) Use Hissatsu: Yaten to dodge, then:

    1) Run back into range
    
    2) Enpi, then run back into range
    
    3) Enpi, then Hissatsu: Gyoten back into range

Disengaging early and running back into range saves Kenki at the cost of reduced uptime. If that saved Kenki is instead spent on Hissatsu: Shinten, that is a gain of 2 ppK. If we lost weaponskills due to lost uptime, e.g., we lost between 5 and 10 Kenki in addition to the weaponskill potency and auto attacks. It is difficult to imagine a scenario where we would want to take the loss in uptime.

Using Hissatsu: Yaten to dodge incurs the cost of the reduced ppK but not of reduced uptime or related weaponskill losses (since it is off the GCD). The next decision is if you use the Enhanced Enpi proc or not. As stated, the increased potency plus Kenki refund is more than sufficient to make it worth using, especially if the alternative is doing nothing. Doing nothing in lieu of Enpi may be attractive if you are mid-combo since Enpi breaks combo. Breaking combo delays Sen opening, Kenki generation, and devalues the combo actions already taken.

If you backstep mid-combo prior to Kasha or Gekko, you may preserve your combo by doing nothing and waiting to reengage. The outcome is 400 potency, an open Sen, and the 10 Kenki cost of Hissatsu: Yaten refunded. The opened Sen may be valued by its Kenki equivalent (via Hagakure) of 20 -- a value of 240 potency if converted into Hissatsu: Shinten. Alternatively, it may be valued for its progress towards Midare Setsugekka -- a value of 240 or 360 potency. Compare this to the 300 potency of Enhanced Enpi plus refunded Kenki cost with a broken combo. When faced with these two options, preserving your combo by doing nothing is the attractive option.

Breaking combo after only Hakaze appears to lean differently. It is a similar value proposition as the previous scenario if the intended combo path were Yukikaze. In this case, you should elect to preserve your combo for Yukikaze. However, if the intended combo paths end in Kasha or Gekko, breaking combo with Enhanced Enpi looks more attractive:

- The next combo step after Hakaze is 280 potency plus 5 Kenki and the opportunity to finish the combo.
- There is less of a sunk cost if the combo is broken (only Hakaze will be "wasted"). Essentially, you defer the combo by two GCDs and write off the Hakaze. 

The Enhanced Enpi covers the immediate next GCD (Jinpu or Shifu) with its increased potency and higher Kenki generated. It also covers the cost of doing nothing instead. So while you ideally should not use Hissatsu: Yaten to disengage while in the middle of a combo, you should not use Enhanced Enpi unless you're only on the Hakaze step of the combo and intend to finish the combo with Kasha or Gekko. In that case, you should break combo with Enhanced Enpi.

The final decision is if you use Hissatsu: Gyoten to get back into range. Once again, the tradeoff is reduced Kenki efficiency versus increased uptime. If the dodge maneuver is executed efficienctly, then the GCD after using Enpi will most likely be enough to return to the target without clipping the following GCD. Therefore, the tension is between auto attack uptime and Kenki savings. If auto attacks are approximately 100 potency, then using Hissatsu: Gyoten to close the gap is worth it if at least one auto attack is gained as a result. However, if the Kenki spent on Hissatsu: Gyoten prevents you from using a Hissatsu: Shinten later on, then running back into range would have been the better option. The payoff in using the gap closer is minimal compared to the potential penalty for inefficient Kenki use (~100 potency for a gained auto attack versus 200 potency loss for insufficient Kenki for Hissatsu: Shinten). I would imagine that the expected payoff is optimal if you elect to run back into range instead of using Hissatsu : Gyoten.

<a href="#header">back to the top...</a>

<a id="third-eye"></a>
## On Third Eye
This defensive ability with a short cooldown offers a modest one time damage taken reduction. Additionally, it grants the Open Eyes status, enabling the use of either Merciful Eyes or Hissatsu: Seigan. 

Merciful Eyes's healing potency was reduced since the media tour tool tip release by a factor of 3. What was once a frequently available Second Wind alternative has been reduced to a pitiful 200 potency heal. In my experience, this is enough to offset an auto attack while, for example, face-tanking a FATE boss. As such, use Open Eyes for Merciful Eyes if you are desparate.

On the other hand, the ability formerly known as Starry Eyes, Hissatsu: Seigan, which was useless due to its high Kenki cost according to the media tour tool tips, has since found its calling along with its renaming to be inline with the other Kenki spenders. At a potency of 200 with a Kenki cost of 15, its potency per Kenki ratio of ~13 ranks it third among Kenki spenders, beating out the gold standard of Hissatsu: Shinten (at a potency per Kenki ratio of 12).

This grants an avenue of optimization in which you try to make sure you activate Third Eye before as many (unavoidable) damage situations as you can. Kenki that would have gone to a Hissatsu: Shinten dump may then be used on Hissatsu: Seigan instead for a theoretical DPS gain. The modest duration of the Open Eyes status (15s) enables you to spend the Open Eyes at your convenience (e.g., you currently only have enough Kenki for an upcoming Hissatsu: Kaiten for Midare Setsugekka, which takes priority).

Of course, this theoretical DPS gain means nothing if the Kenki difference is not made up by the end of the encounter; if you end the encounter with 10 spare Kenki, then a Hissatsu: Shinten should've been used instead.

Try taking advantage of Third Eye on fights like Susano EX! There's raidwide damage with cast bars (Unkehi), targeted damage (stack after knockback, targeted lightning), raidwide damage without cast bars (during the parry active time maneuver).

<a href="#header">back to the top...</a>

<a id="hagakure"></a>
## On Hagakure
As discussed in part 4, Hagakure is a subtly vital cooldown. By converting open Sen into Kenki, it essentially is shifting damage potential from being on the GCD (via Iaijutsu weaponskills) to being off the GCD (via Kenki spenders). This effectively makes the damage potential "free" because it's no longer constrained to the GCD. This pushes your rotation up a GCD because you no longer need to cast the Iaijutsu to realize that potential. 

Besides Higanbana, Midare Setsugekka is our most powerful Iaijutsu at 720 potency for three Sen. If Hagakure is used to convert this three Sen into Kenki, 60 Kenki is generated. If this Kenki is used for Hissatsu: Shinten at 12 ppK, the equivalent 720 potency is there. Thus, with our "gold standard" of Kenki spenders, all the potency is accounted for. In fact, one does not need to exclusively convert three Sen using Hagakure because it would still be efficient to convert one or two Sen due to the exchange rate. If the generated Kenki is used on Hissatsu: Seigan or other higher efficiency Kenki spenders, the value of Hagakure increases further.

When might it be useful to use Hagakure on one or two Sen?

- Getting Hagakure on cooldown sooner

- Adjusting your Midare Setsugekka timing to align with encounter mechanics and/or party buffs

- Fast loans of Kenki for on-demand burst potential (e.g., add phase)

The value of Hagakure depends on being able to convert the Kenki back into potency. You may look at the ppK list and say, "Hissatsu: Kaiten plus Midare Setsugekka is the highest efficiency use of Kenki. Why should we ever convert three Sen into Kenki?" While it's true that Hissatsu: Kaiten + Midare Setsugekka is the best bang for your buck in terms of ppK, the ability to move the damage from Midare Setsugekka off the GCD provides the actual gains in pps, which is what actually matters.

### Example


```python
sam = Samurai(kenki_mastery=True)

actions = [('Hakaze'), ('Jinpu'), ('Gekko'),
           ('Hakaze'), ('Shifu'), ('Kasha'),
           ('Hakaze'), ('Yukikaze', 'Hissatsu: Guren'),
           ('Hakaze', 'Hagakure'), ('Jinpu', 'Hissatsu: Shinten'), ('Gekko', 'Meikyo Shisui'),
           ('Yukikaze', 'Hissatsu: Shinten'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'),
           ('Hakaze', 'Hissatsu: Shinten'), ('Yukikaze', 'Hissatsu: Shinten')]

df_hgk1, average_potency, pps = sam.parse_rotation(actions)
display(df_hgk1)
```

    average potency per GCD = 560.5756250000001
    average potency per second = 252.511542793
    


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
      <th>Ability</th>
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
      <td>Jinpu</td>
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
      <td>4.80</td>
      <td>Gekko</td>
      <td></td>
      <td>460.000</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>890.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.20</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.500</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>20</td>
      <td>1062.500</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.60</td>
      <td>Shifu</td>
      <td></td>
      <td>322.000</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>25</td>
      <td>1384.500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.76</td>
      <td>Kasha</td>
      <td></td>
      <td>460.000</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>30</td>
      <td>1844.500</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.500</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>40</td>
      <td>2017.000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16.08</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Guren</td>
      <td>1412.200</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>45</td>
      <td>3429.200</td>
    </tr>
    <tr>
      <th>8</th>
      <td>18.24</td>
      <td>Hakaze</td>
      <td>Hagakure</td>
      <td>191.475</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>5</td>
      <td>3620.675</td>
    </tr>
    <tr>
      <th>9</th>
      <td>20.40</td>
      <td>Jinpu</td>
      <td>Hissatsu: Shinten</td>
      <td>740.370</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>70</td>
      <td>4361.045</td>
    </tr>
    <tr>
      <th>10</th>
      <td>22.56</td>
      <td>Gekko</td>
      <td>Meikyo Shisui</td>
      <td>510.600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>50</td>
      <td>4871.645</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.72</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Shinten</td>
      <td>816.960</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>60</td>
      <td>5688.605</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.88</td>
      <td>Kasha</td>
      <td>Hissatsu: Kaiten</td>
      <td>510.600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>45</td>
      <td>6199.205</td>
    </tr>
    <tr>
      <th>13</th>
      <td>29.04</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1378.620</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>35</td>
      <td>7577.825</td>
    </tr>
    <tr>
      <th>14</th>
      <td>31.20</td>
      <td>Hakaze</td>
      <td>Hissatsu: Shinten</td>
      <td>574.425</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>35</td>
      <td>8152.250</td>
    </tr>
    <tr>
      <th>15</th>
      <td>33.36</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Shinten</td>
      <td>816.960</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>15</td>
      <td>8969.210</td>
    </tr>
  </tbody>
</table>
</div>



```python
sam = Samurai(kenki_mastery=True)

actions = [('Hakaze'), ('Jinpu'), ('Gekko'),
           ('Hakaze'), ('Shifu'), ('Kasha'),
           ('Hakaze'), ('Yukikaze', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'),
           ('Hakaze'), ('Jinpu'), ('Gekko', 'Meikyo Shisui'),
           ('Yukikaze', 'Hissatsu: Guren'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'), ('Gekko')]

df_hgk2, average_potency, pps = sam.parse_rotation(actions)
display(df_hgk2)
```

    average potency per GCD = 543.8215625
    average potency per second = 244.964667793
    


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
      <th>Ability</th>
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
      <td>Jinpu</td>
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
      <td>4.80</td>
      <td>Gekko</td>
      <td></td>
      <td>460.000</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>890.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.20</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.500</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>20</td>
      <td>1062.500</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.60</td>
      <td>Shifu</td>
      <td></td>
      <td>322.000</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>25</td>
      <td>1384.500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.76</td>
      <td>Kasha</td>
      <td></td>
      <td>460.000</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>30</td>
      <td>1844.500</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.500</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>40</td>
      <td>2017.000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16.08</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Kaiten</td>
      <td>391.000</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>45</td>
      <td>2408.000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>18.24</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1378.620</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>35</td>
      <td>3786.620</td>
    </tr>
    <tr>
      <th>9</th>
      <td>20.40</td>
      <td>Hakaze</td>
      <td></td>
      <td>191.475</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>35</td>
      <td>3978.095</td>
    </tr>
    <tr>
      <th>10</th>
      <td>22.56</td>
      <td>Jinpu</td>
      <td></td>
      <td>357.420</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>40</td>
      <td>4335.515</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.72</td>
      <td>Gekko</td>
      <td>Meikyo Shisui</td>
      <td>510.600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>45</td>
      <td>4846.115</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.88</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Guren</td>
      <td>1455.210</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>55</td>
      <td>6301.325</td>
    </tr>
    <tr>
      <th>13</th>
      <td>29.04</td>
      <td>Kasha</td>
      <td>Hissatsu: Kaiten</td>
      <td>510.600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>15</td>
      <td>6811.925</td>
    </tr>
    <tr>
      <th>14</th>
      <td>31.20</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1378.620</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>5</td>
      <td>8190.545</td>
    </tr>
    <tr>
      <th>15</th>
      <td>33.36</td>
      <td>Gekko</td>
      <td></td>
      <td>510.600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>5</td>
      <td>8701.145</td>
    </tr>
  </tbody>
</table>
</div>



```python
compare_n_potencies([df_hgk1, df_hgk2], ['Using Hagakure', 'No Hagakure'])
```


![png](output_37_0.png)


The two policies diverge in a number of spots:

- Deferring the first Midare Setsugekka lets us spend Kenki on Hissatsu: Guren earlier. This basically already covers the difference of using Hagakure instead of Midare Setsugekka.

- Using Hagakure gave us four Hissatsu: Shinten compared to not using it at the expense of one Midare Setsugekka. This is essentially where the cumulative potency was derived from. In addition to the Kenki converted using Hagakure, we were able to generate more Kenki from weaponskills alone.

- At the end of these simulations, the one with the policy of using Hagakure ends with more Kenki (=> potential damage) and at a higher pps.

To sum up:

- Hagakure converts damage potential from being on the GCD with Iaijutsu to being off the GCD with Kenki spenders.
    - More specifically, it essentially turns Midare Setsugekka into Kenki. Higanbana, given its full duration, is unmatched in its value per Sen/GCD.

- The value in the conversion is only realized if the Kenki is actually spent. While the conversion gives you flexibility in when/how you spend it (i.e., you can bank the Kenki for opportunistic burst phases), the payoff period takes a little longer. For example, you would need to use Hissatsu: Shinten 3-4 times over 3-4 GCDs. This has the potential to lead to wasted Kenki if you're not careful.

- Hagakure does not need to always be spent on three Sen for maximum benefit.

- You can use Hagakure to adjust your rotation timings by clearing open Sen.


<a href="#header">back to the top...</a>
