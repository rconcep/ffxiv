
# Samurai by the numbers (lvl 50)
## by Tzuyu Chou (Cactuar)

### Update log

-06/05/2017: Finished through two extended rotations.

-06/03/2017: Updating format to be consistent with part 1. Including the new parse rotation function syntax.

-06/01/2017: Three openers and priority


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

## lvl 50

Level 50 unlocks the final weaponskill, Yukikaze, a combo finisher to open the final Sen, Setsu. It combos from Hakaze so it is a two hit combo contrary to Gekko and Kasha. Level 50 also confers the Meikyo Shisui ability, a cooldown that allows you to execute up to 3 combo abilities without meeting combo prerequisites. This may be used, for example, to quickly get Jinpu and Shifu buffs up or to open up all three Sen in a fraction of the time as normal.

Furthermore, the opening of the final Sen unlocks the final Iaijutsu, Midare Setsugekka. This powerful single target nuke gives the opportunity in single target situations to deal massive damage without having to clip Higanbana.

Let's explore opener options.

## Opener 1
Buff first: Shifu > Jinpu > Yukikaze.

Iaijutsu: Higanbana > Midare Setsugekka. 

Meikyo Shisui: generate second Midare Setsugekka. 


```python
sam = Samurai()

n_targets = 1

actions = [('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Jinpu'), ('Higanbana'), ('Gekko'), ('Hakaze'),
           ('Yukikaze'), ('Hakaze'), ('Shifu'), ('Kasha'),
           ('Midare Setsugekka', 'Meikyo Shisui'), ('Kasha'), ('Gekko'), ('Yukikaze'), 
           ('Midare Setsugekka'), ('Hakaze'), ('Jinpu')]
```


```python
df0, average_potency, pps = sam.parse_rotation(actions)
display(df0)
```

    average potency per GCD = 415.500578947
    average potency per second = 191.242999031
    


<div>
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
      <td>980.000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Jinpu</td>
      <td></td>
      <td>280.000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>1260.000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Higanbana</td>
      <td></td>
      <td>276.000</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>1536.000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Gekko</td>
      <td></td>
      <td>493.327</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>2029.327</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Hakaze</td>
      <td></td>
      <td>205.827</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>2235.154</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Yukikaze</td>
      <td></td>
      <td>424.327</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>1</td>
      <td>2659.481</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>2884.283</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Shifu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>3275.030</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Kasha</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>3818.957</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Midare Setsugekka</td>
      <td>Meikyo Shisui</td>
      <td>952.407</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>4771.364</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Kasha</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5315.291</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Gekko</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5859.218</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Yukikaze</td>
      <td></td>
      <td>467.337</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>6326.555</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>952.407</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>7278.962</td>
    </tr>
    <tr>
      <th>17</th>
      <td>36.96</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>7503.764</td>
    </tr>
    <tr>
      <th>18</th>
      <td>39.12</td>
      <td>Jinpu</td>
      <td></td>
      <td>390.747</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>7894.511</td>
    </tr>
  </tbody>
</table>
</div>



```python
plot_potency(df0)
```


![png](output_9_0.png)


## Opener 2
Similar to Opener 1, just prioritize Jinpu > Shifu > Yukikaze so that the Higanbana DoT is buffed earlier.


```python
sam = Samurai()

n_targets = 1

actions = [('Hakaze'), ('Jinpu'), ('Gekko'), ('Higanbana'),
           ('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Yukikaze'), ('Hakaze'), ('Jinpu'), ('Gekko'),
           ('Midare Setsugekka', 'Meikyo Shisui'), ('Kasha'), ('Gekko'), ('Yukikaze'),
           ('Midare Setsugekka'), ('Hakaze'), ('Jinpu')]
```


```python
df1, average_potency, pps = sam.parse_rotation(actions)
display(df1)
```

    average potency per GCD = 425.951105263
    average potency per second = 191.597324811
    


<div>
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
      <td>2858.041</td>
    </tr>
    <tr>
      <th>9</th>
      <td>20.64</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>3082.843</td>
    </tr>
    <tr>
      <th>10</th>
      <td>22.80</td>
      <td>Jinpu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>3473.590</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.96</td>
      <td>Gekko</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>4017.517</td>
    </tr>
    <tr>
      <th>12</th>
      <td>27.12</td>
      <td>Midare Setsugekka</td>
      <td>Meikyo Shisui</td>
      <td>952.407</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>4969.924</td>
    </tr>
    <tr>
      <th>13</th>
      <td>29.28</td>
      <td>Kasha</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5513.851</td>
    </tr>
    <tr>
      <th>14</th>
      <td>31.44</td>
      <td>Gekko</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>6057.778</td>
    </tr>
    <tr>
      <th>15</th>
      <td>33.60</td>
      <td>Yukikaze</td>
      <td></td>
      <td>467.337</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>6525.115</td>
    </tr>
    <tr>
      <th>16</th>
      <td>35.76</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>952.407</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>7477.522</td>
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
      <td>7702.324</td>
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
      <td>8093.071</td>
    </tr>
  </tbody>
</table>
</div>



```python
plot_potency(df1)
```


![png](output_13_0.png)


## Opener 3
Meikyo Shisui: Get buffs up ASAP. Since Iaijutsu consumes one charge of Meikyo Shisui, we must delay Higanbana.

Buffs first: Shifu > Jinpu > Yukikaze.

Iaijutsu: Midare Setsugekka > Higanbana.


```python
sam = Samurai()

n_targets = 1

actions = [('Hakaze'), ('Shifu'), ('Kasha', 'Meikyo Shisui'),
           ('Jinpu'), ('Gekko'), ('Yukikaze'), ('Midare Setsugekka'),
           ('Hakaze'), ('Yukikaze'), ('Higanbana'), ('Hakaze'),
           ('Shifu'), ('Kasha'), ('Hakaze'), ('Jinpu'),
           ('Gekko'), ('Hakaze'), ('Yukikaze'), ('Midare Setsugekka')]
```


```python
df2, average_potency, pps = sam.parse_rotation(actions)
display(df2)
```

    average potency per GCD = 410.969301579
    average potency per second = 189.157382025
    


<div>
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
      <th>Total Potency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.00000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>150.00000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.00000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>430.00000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Kasha</td>
      <td>Meikyo Shisui</td>
      <td>400.00000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>830.00000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Jinpu</td>
      <td></td>
      <td>280.00000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>1110.00000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Gekko</td>
      <td></td>
      <td>460.00000</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>1570.00000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Yukikaze</td>
      <td></td>
      <td>391.00000</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>1961.00000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>919.08000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>2880.08000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Hakaze</td>
      <td></td>
      <td>191.47500</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>3071.55500</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Yukikaze</td>
      <td></td>
      <td>434.01000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>3505.56500</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Higanbana</td>
      <td></td>
      <td>306.36000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>3811.92500</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>4040.39297</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Shifu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>4434.80594</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Kasha</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>4982.39891</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5210.86688</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Jinpu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5605.27985</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Gekko</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>6152.87282</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>6381.34079</td>
    </tr>
    <tr>
      <th>17</th>
      <td>36.96</td>
      <td>Yukikaze</td>
      <td></td>
      <td>471.00297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>6852.34376</td>
    </tr>
    <tr>
      <th>18</th>
      <td>39.12</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>956.07297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>7808.41673</td>
    </tr>
  </tbody>
</table>
</div>



```python
plot_potency(df2)
```


![png](output_17_0.png)


## Opener 4
Buffs up first: Shifu > Jinpu > Yukikaze

Iaijutsu: Midare Setsugekka > Higanbana

Meikyo Shisui: Generate second Midare Setsugekka


```python
sam = Samurai()

n_targets = 1

actions = [('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Jinpu'), ('Gekko'), ('Hakaze'), ('Yukikaze'),
           ('Midare Setsugekka'), ('Hakaze'), ('Shifu'), ('Kasha'),
           ('Higanbana', 'Meikyo Shisui'), ('Kasha'), ('Gekko'), ('Yukikaze'),
           ('Midare Setsugekka'), ('Hakaze'), ('Jinpu')]
```


```python
df3, average_potency, pps = sam.parse_rotation(actions)
display(df3)
```

    average potency per GCD = 405.97778
    average potency per second = 186.85992781
    


<div>
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
      <th>Total Potency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.00000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>150.00000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.00000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>430.00000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Kasha</td>
      <td></td>
      <td>400.00000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>830.00000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.00000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>980.00000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Jinpu</td>
      <td></td>
      <td>280.00000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>1260.00000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Gekko</td>
      <td></td>
      <td>460.00000</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>1720.00000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.50000</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>1892.50000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Yukikaze</td>
      <td></td>
      <td>391.00000</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>2283.50000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>919.08000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>3202.58000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Hakaze</td>
      <td></td>
      <td>191.47500</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>3394.05500</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Shifu</td>
      <td></td>
      <td>357.42000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>3751.47500</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Kasha</td>
      <td></td>
      <td>510.60000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>4262.07500</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Higanbana</td>
      <td>Meikyo Shisui</td>
      <td>306.36000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>4568.43500</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Kasha</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5116.02797</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Gekko</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5663.62094</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Yukikaze</td>
      <td></td>
      <td>471.00297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>6134.62391</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>956.07297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>7090.69688</td>
    </tr>
    <tr>
      <th>17</th>
      <td>36.96</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>7319.16485</td>
    </tr>
    <tr>
      <th>18</th>
      <td>39.12</td>
      <td>Jinpu</td>
      <td></td>
      <td>394.41297</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>7713.57782</td>
    </tr>
  </tbody>
</table>
</div>



```python
plot_potency(df3)
```


![png](output_21_0.png)


## Opener 5
Similar to Openers 1 and 2, but prioritizes Yukikaze > Shifu > Jinpu. This lets you put Higanbana one GCD earlier and, for parties without WAR, gets the slashing resistance down debuff up faster. A NIN may possibly get it up faster or at the same time if it opens with Shadow Fang combo due to Huton.


```python
sam = Samurai()

n_targets = 1

actions = [('Hakaze'), ('Yukikaze'), ('Higanbana'), ('Hakaze'),
           ('Shifu'), ('Kasha'), ('Hakaze'), ('Jinpu'),
           ('Gekko'), ('Hakaze'), ('Yukikaze'), ('Midare Setsugekka', 'Meikyo Shisui'),
           ('Kasha'), ('Gekko'), ('Yukikaze'), ('Midare Setsugekka'),
           ('Hakaze'), ('Shifu'), ('Kasha')]
```


```python
df4, average_potency, pps = sam.parse_rotation(actions)
display(df4)
```

    average potency per GCD = 428.845663158
    average potency per second = 194.001609524
    


<div>
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
      <th>Total Potency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.0000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>150.0000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Yukikaze</td>
      <td></td>
      <td>340.0000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>490.0000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.80</td>
      <td>Higanbana</td>
      <td></td>
      <td>266.4000</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>0</td>
      <td>756.4000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.20</td>
      <td>Hakaze</td>
      <td></td>
      <td>197.5800</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>1</td>
      <td>953.9800</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.60</td>
      <td>Shifu</td>
      <td></td>
      <td>341.8800</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>1</td>
      <td>1295.8600</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.76</td>
      <td>Kasha</td>
      <td></td>
      <td>471.9720</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>1767.8320</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>194.4720</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>1962.3040</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16.08</td>
      <td>Jinpu</td>
      <td></td>
      <td>342.9678</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>2305.2718</td>
    </tr>
    <tr>
      <th>8</th>
      <td>18.24</td>
      <td>Gekko</td>
      <td></td>
      <td>542.7678</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>2848.0396</td>
    </tr>
    <tr>
      <th>9</th>
      <td>20.40</td>
      <td>Hakaze</td>
      <td></td>
      <td>223.6428</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>3071.6824</td>
    </tr>
    <tr>
      <th>10</th>
      <td>22.56</td>
      <td>Yukikaze</td>
      <td></td>
      <td>466.1778</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>3537.8602</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.72</td>
      <td>Midare Setsugekka</td>
      <td>Meikyo Shisui</td>
      <td>951.2478</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>4489.1080</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.88</td>
      <td>Kasha</td>
      <td></td>
      <td>542.7678</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5031.8758</td>
    </tr>
    <tr>
      <th>13</th>
      <td>29.04</td>
      <td>Gekko</td>
      <td></td>
      <td>542.7678</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5574.6436</td>
    </tr>
    <tr>
      <th>14</th>
      <td>31.20</td>
      <td>Yukikaze</td>
      <td></td>
      <td>466.1778</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>6040.8214</td>
    </tr>
    <tr>
      <th>15</th>
      <td>33.36</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>951.2478</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>6992.0692</td>
    </tr>
    <tr>
      <th>16</th>
      <td>35.52</td>
      <td>Hakaze</td>
      <td></td>
      <td>223.6428</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>7215.7120</td>
    </tr>
    <tr>
      <th>17</th>
      <td>37.68</td>
      <td>Shifu</td>
      <td></td>
      <td>389.5878</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>7605.2998</td>
    </tr>
    <tr>
      <th>18</th>
      <td>39.84</td>
      <td>Kasha</td>
      <td></td>
      <td>542.7678</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>8148.0676</td>
    </tr>
  </tbody>
</table>
</div>



```python
plot_potency(df4)
```


![png](output_25_0.png)



```python
dfs = [df4, df3, df2, df1, df0]
labels = ['Opener 5', 'Opener 4', 'Opener 3', 'Opener 2', 'Opener 1']
compare_n_potencies(dfs, labels)
```


![png](output_26_0.png)


The time horizon was selected so that each opener had at least two Midare Setsugekka.

These openers have fairly similar cumulative potencies over the selected time horizon. At level 50, you have no other offensive cooldowns when considering buff alignment. Party synergies will need to be considered to determine the best placement. (Maximizing potency delivered under party buffs.) Higanbana is applied at a different time and each opener bursts at different times. Since Higanbana and Midare Setsugekka have the highest effective potency per GCD (with DoT snapshot), getting those Iaijutsu under party buffs will differentiate these openers' potency significantly.


```python
fig, ax = plt.subplots(figsize=(12, 4))

for k, df in enumerate(dfs):
    ax.plot(df['Time'], df['Potency'], label=labels[k])
    ax.set_xlabel('Time')
    ax.set_ylabel('Potency')
    ax.legend(loc='upper left', framealpha=0.5)

fig.suptitle('Opener Potency over Time')
fig.tight_layout(pad=3)
```


![png](output_29_0.png)


### Priority: Shifu > Jinpu > Yukikaze and Higanbana > Midare Setsugekka
Since Yukikaze is applied to the target, refreshing it on a dying target is lesser of a priority. However, since it is necessary to open Setsu, it cannot be neglected.

### Filler: Combos to refresh buffs, avoid wasting Sen.

### AoE: Similar as lvl 40-49... avoid using Yukikaze in large pulls due to it being a target debuff, not a self buff.
You will probably be using the AoE weaponskills -> Tenka Goken rotation anyway.

## Extended simulations

Openers are fine to look at it in a vacuum, but cooldown and buff alignment is difficult to see over short time horizons; do the buff/cooldown timings set you up nicely for the rest of the encounter? Let's look at how these openers transition into the priority system and look at an example of how a long single target encounter may go.

### With Opener 5
This opener had the highest average potency by a slim margin.


```python
sam = Samurai()

n_targets = 1

actions = [('Hakaze'), ('Yukikaze'), ('Higanbana'), ('Hakaze'),
           ('Shifu'), ('Kasha'), ('Hakaze'), ('Jinpu'),
           ('Gekko'), ('Hakaze'), ('Yukikaze'), ('Midare Setsugekka', 'Meikyo Shisui'),
           ('Kasha'), ('Gekko'), ('Yukikaze'), ('Midare Setsugekka'),
           ('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'), 
           ('Jinpu'), ('Gekko'), ('Hakaze'), ('Yukikaze'),
           ('Midare Setsugekka'), ('Hakaze'), ('Shifu'), ('Kasha'),
           ('Higanbana'), ('Hakaze'), ('Jinpu'), ('Gekko'),
           ('Hakaze'), ('Yukikaze'), ('Hakaze'), ('Shifu'),
           ('Kasha'), ('Midare Setsugekka'), ('Hakaze'), ('Jinpu'),
           ('Gekko'), ('Hakaze'), ('Yukikaze'), ('Hakaze'),
           ('Shifu'), ('Kasha'), ('Midare Setsugekka'), ('Hakaze'), # Meikyo Shisui should be coming off c/d next.
           ('Jinpu'), ('Gekko'), ('Hakaze'), ('Yukikaze'),
           ('Hakaze'), ('Shifu'), ('Kasha'), ('Midare Setsugekka'), # Higanbana DoT should be falling off...
           ('Hakaze'), ('Jinpu'), ('Gekko'), ('Higanbana', 'Meikyo Shisui'),
           ('Yukikaze'), ('Kasha'), ('Gekko'), ('Midare Setsugekka')]
```


```python
df4_ext, average_potency, pps = sam.parse_rotation(actions)
display(df4_ext)
```

    average potency per GCD = 443.035088125
    average potency per second = 203.694293391
    


<div>
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
      <th>Total Potency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.00000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>150.00000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Yukikaze</td>
      <td></td>
      <td>340.00000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>490.00000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.80</td>
      <td>Higanbana</td>
      <td></td>
      <td>266.40000</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>0</td>
      <td>756.40000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.20</td>
      <td>Hakaze</td>
      <td></td>
      <td>197.58000</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>1</td>
      <td>953.98000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.60</td>
      <td>Shifu</td>
      <td></td>
      <td>341.88000</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>1</td>
      <td>1295.86000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.76</td>
      <td>Kasha</td>
      <td></td>
      <td>471.97200</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>1767.83200</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>194.47200</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>1962.30400</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16.08</td>
      <td>Jinpu</td>
      <td></td>
      <td>342.96780</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>2305.27180</td>
    </tr>
    <tr>
      <th>8</th>
      <td>18.24</td>
      <td>Gekko</td>
      <td></td>
      <td>542.76780</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>2848.03960</td>
    </tr>
    <tr>
      <th>9</th>
      <td>20.40</td>
      <td>Hakaze</td>
      <td></td>
      <td>223.64280</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>3071.68240</td>
    </tr>
    <tr>
      <th>10</th>
      <td>22.56</td>
      <td>Yukikaze</td>
      <td></td>
      <td>466.17780</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>3537.86020</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.72</td>
      <td>Midare Setsugekka</td>
      <td>Meikyo Shisui</td>
      <td>951.24780</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>4489.10800</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.88</td>
      <td>Kasha</td>
      <td></td>
      <td>542.76780</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5031.87580</td>
    </tr>
    <tr>
      <th>13</th>
      <td>29.04</td>
      <td>Gekko</td>
      <td></td>
      <td>542.76780</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5574.64360</td>
    </tr>
    <tr>
      <th>14</th>
      <td>31.20</td>
      <td>Yukikaze</td>
      <td></td>
      <td>466.17780</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>6040.82140</td>
    </tr>
    <tr>
      <th>15</th>
      <td>33.36</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>951.24780</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>6992.06920</td>
    </tr>
    <tr>
      <th>16</th>
      <td>35.52</td>
      <td>Hakaze</td>
      <td></td>
      <td>223.64280</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>7215.71200</td>
    </tr>
    <tr>
      <th>17</th>
      <td>37.68</td>
      <td>Shifu</td>
      <td></td>
      <td>389.58780</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>7605.29980</td>
    </tr>
    <tr>
      <th>18</th>
      <td>39.84</td>
      <td>Kasha</td>
      <td></td>
      <td>542.76780</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>8148.06760</td>
    </tr>
    <tr>
      <th>19</th>
      <td>42.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>223.64280</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>8371.71040</td>
    </tr>
    <tr>
      <th>20</th>
      <td>44.16</td>
      <td>Jinpu</td>
      <td></td>
      <td>389.58780</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>8761.29820</td>
    </tr>
    <tr>
      <th>21</th>
      <td>46.32</td>
      <td>Gekko</td>
      <td></td>
      <td>542.76780</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>9304.06600</td>
    </tr>
    <tr>
      <th>22</th>
      <td>48.48</td>
      <td>Hakaze</td>
      <td></td>
      <td>223.64280</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>9527.70880</td>
    </tr>
    <tr>
      <th>23</th>
      <td>50.64</td>
      <td>Yukikaze</td>
      <td></td>
      <td>466.17780</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>9993.88660</td>
    </tr>
    <tr>
      <th>24</th>
      <td>52.80</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>951.24780</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10945.13440</td>
    </tr>
    <tr>
      <th>25</th>
      <td>54.96</td>
      <td>Hakaze</td>
      <td></td>
      <td>223.64280</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>11168.77720</td>
    </tr>
    <tr>
      <th>26</th>
      <td>57.12</td>
      <td>Shifu</td>
      <td></td>
      <td>389.58780</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>11558.36500</td>
    </tr>
    <tr>
      <th>27</th>
      <td>59.28</td>
      <td>Kasha</td>
      <td></td>
      <td>542.76780</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>12101.13280</td>
    </tr>
    <tr>
      <th>28</th>
      <td>61.44</td>
      <td>Higanbana</td>
      <td></td>
      <td>338.52780</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>12439.66060</td>
    </tr>
    <tr>
      <th>29</th>
      <td>63.60</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>12668.12857</td>
    </tr>
    <tr>
      <th>30</th>
      <td>65.76</td>
      <td>Jinpu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>13062.54154</td>
    </tr>
    <tr>
      <th>31</th>
      <td>67.92</td>
      <td>Gekko</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>13610.13451</td>
    </tr>
    <tr>
      <th>32</th>
      <td>70.08</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>13838.60248</td>
    </tr>
    <tr>
      <th>33</th>
      <td>72.24</td>
      <td>Yukikaze</td>
      <td></td>
      <td>471.00297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>14309.60545</td>
    </tr>
    <tr>
      <th>34</th>
      <td>74.40</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>14538.07342</td>
    </tr>
    <tr>
      <th>35</th>
      <td>76.56</td>
      <td>Shifu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>14932.48639</td>
    </tr>
    <tr>
      <th>36</th>
      <td>78.72</td>
      <td>Kasha</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15480.07936</td>
    </tr>
    <tr>
      <th>37</th>
      <td>80.88</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>956.07297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>16436.15233</td>
    </tr>
    <tr>
      <th>38</th>
      <td>83.04</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>16664.62030</td>
    </tr>
    <tr>
      <th>39</th>
      <td>85.20</td>
      <td>Jinpu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>17059.03327</td>
    </tr>
    <tr>
      <th>40</th>
      <td>87.36</td>
      <td>Gekko</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>17606.62624</td>
    </tr>
    <tr>
      <th>41</th>
      <td>89.52</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>17835.09421</td>
    </tr>
    <tr>
      <th>42</th>
      <td>91.68</td>
      <td>Yukikaze</td>
      <td></td>
      <td>471.00297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>18306.09718</td>
    </tr>
    <tr>
      <th>43</th>
      <td>93.84</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>18534.56515</td>
    </tr>
    <tr>
      <th>44</th>
      <td>96.00</td>
      <td>Shifu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>18928.97812</td>
    </tr>
    <tr>
      <th>45</th>
      <td>98.16</td>
      <td>Kasha</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>19476.57109</td>
    </tr>
    <tr>
      <th>46</th>
      <td>100.32</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>956.07297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20432.64406</td>
    </tr>
    <tr>
      <th>47</th>
      <td>102.48</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20661.11203</td>
    </tr>
    <tr>
      <th>48</th>
      <td>104.64</td>
      <td>Jinpu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>21055.52500</td>
    </tr>
    <tr>
      <th>49</th>
      <td>106.80</td>
      <td>Gekko</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>21603.11797</td>
    </tr>
    <tr>
      <th>50</th>
      <td>108.96</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>21831.58594</td>
    </tr>
    <tr>
      <th>51</th>
      <td>111.12</td>
      <td>Yukikaze</td>
      <td></td>
      <td>471.00297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>22302.58891</td>
    </tr>
    <tr>
      <th>52</th>
      <td>113.28</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>22531.05688</td>
    </tr>
    <tr>
      <th>53</th>
      <td>115.44</td>
      <td>Shifu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>22925.46985</td>
    </tr>
    <tr>
      <th>54</th>
      <td>117.60</td>
      <td>Kasha</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>23473.06282</td>
    </tr>
    <tr>
      <th>55</th>
      <td>119.76</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>956.07297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>24429.13579</td>
    </tr>
    <tr>
      <th>56</th>
      <td>121.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>24657.60376</td>
    </tr>
    <tr>
      <th>57</th>
      <td>124.08</td>
      <td>Jinpu</td>
      <td></td>
      <td>357.42000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>25015.02376</td>
    </tr>
    <tr>
      <th>58</th>
      <td>126.24</td>
      <td>Gekko</td>
      <td></td>
      <td>510.60000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>25525.62376</td>
    </tr>
    <tr>
      <th>59</th>
      <td>128.40</td>
      <td>Higanbana</td>
      <td>Meikyo Shisui</td>
      <td>306.36000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>25831.98376</td>
    </tr>
    <tr>
      <th>60</th>
      <td>130.56</td>
      <td>Yukikaze</td>
      <td></td>
      <td>471.00297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>26302.98673</td>
    </tr>
    <tr>
      <th>61</th>
      <td>132.72</td>
      <td>Kasha</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>26850.57970</td>
    </tr>
    <tr>
      <th>62</th>
      <td>134.88</td>
      <td>Gekko</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>27398.17267</td>
    </tr>
    <tr>
      <th>63</th>
      <td>137.04</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>956.07297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>28354.24564</td>
    </tr>
  </tbody>
</table>
</div>



```python
plot_potency(df4_ext, truncate_actions=True)
```


![png](output_36_0.png)


Interestingly enough, the average potency this long into the encounter is actually higher than after the opener. This can be attributed to the lack of stacking damage buffs that we can blow into the opener. 

One observed issue through this simulation is the timing of Higanbana's DoT and Meikyo Shisui coming off cooldown. As commented in the actions list, Meikyo Shisui comes off cooldown for quite a while before an optimal time to use it is presented. It should be off cooldown at around index 48; this is right before a Sen is opened via combo finisher. With the MO of using Meikyo Shisui exclusively to open three Sen in a row, this means we must wait until after we naturally open these Sen (at index 54). Furthermore, the third Higanbana is due to be applied at approximately index 55. Since this is when Midare Setsugekka is ready, we must delay. At this juncture, we must decide if we let Higanbana's DoT fall off for four more GCDs (about 3-4 ticks) in order to to get Meikyo Shisui back on cooldown after a double Midare Setsugekka. The other option would be to get Higanbana applied ASAP. 

The usual answer for this dilemma is constrained by the number of Meikyo Shisui uses available in the encounter. If delaying using Meikyo Shisui too long results in one less use of it, then we should lean towards letting Higanbana drop a few ticks if it lets us use Meikyo Shisui sooner.

### With Opener 3
This opener had the lowest average potency, but got buffs up faster and got Meikyo Shisui on cooldown the soonest. This difference in buff/DoT timing is worth exploring


```python
sam = Samurai()

n_targets = 1

actions = [('Hakaze'), ('Shifu'), ('Kasha', 'Meikyo Shisui'),
           ('Jinpu'), ('Gekko'), ('Yukikaze'), ('Midare Setsugekka'),
           ('Hakaze'), ('Yukikaze'), ('Higanbana'), ('Hakaze'),
           ('Shifu'), ('Kasha'), ('Hakaze'), ('Jinpu'),
           ('Gekko'), ('Hakaze'), ('Yukikaze'), ('Midare Setsugekka'),
           ('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Jinpu'), ('Gekko'), ('Hakaze'), ('Yukikaze'),
           ('Midare Setsugekka'), ('Hakaze'), ('Shifu'), ('Kasha'),
           ('Hakaze'), ('Jinpu'), ('Gekko'), ('Hakaze'),
           ('Yukikaze'), ('Midare Setsugekka'), ('Hakaze'), ('Shifu'),
           ('Kasha'), ('Higanbana', 'Meikyo Shisui'), ('Gekko'), ('Yukikaze'),
           ('Kasha'), ('Midare Setsugekka'), ('Hakaze'), ('Jinpu'),
           ('Gekko'), ('Hakaze'), ('Shifu'), ('Kasha'),
           ('Hakaze'), ('Yukikaze'), ('Midare Setsugekka'), ('Hakaze'),
           ('Jinpu'), ('Gekko'), ('Hakaze'), ('Shifu'),
           ('Kasha'), ('Hakaze'), ('Yukikaze'), ('Midare Setsugekka')]
```


```python
df2_ext, average_potency, pps = sam.parse_rotation(actions)
display(df2_ext)
```

    average potency per GCD = 439.991960317
    average potency per second = 203.3413549
    


<div>
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
      <th>Total Potency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.00000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>150.00000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.00000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>430.00000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Kasha</td>
      <td>Meikyo Shisui</td>
      <td>400.00000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>830.00000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Jinpu</td>
      <td></td>
      <td>280.00000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>1110.00000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Gekko</td>
      <td></td>
      <td>460.00000</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>1570.00000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Yukikaze</td>
      <td></td>
      <td>391.00000</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>1961.00000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>919.08000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>2880.08000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Hakaze</td>
      <td></td>
      <td>191.47500</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>3071.55500</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Yukikaze</td>
      <td></td>
      <td>434.01000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>3505.56500</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Higanbana</td>
      <td></td>
      <td>306.36000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>3811.92500</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>4040.39297</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Shifu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>4434.80594</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Kasha</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>4982.39891</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5210.86688</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Jinpu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5605.27985</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Gekko</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>6152.87282</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>6381.34079</td>
    </tr>
    <tr>
      <th>17</th>
      <td>36.96</td>
      <td>Yukikaze</td>
      <td></td>
      <td>471.00297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>6852.34376</td>
    </tr>
    <tr>
      <th>18</th>
      <td>39.12</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>956.07297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>7808.41673</td>
    </tr>
    <tr>
      <th>19</th>
      <td>41.28</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>8036.88470</td>
    </tr>
    <tr>
      <th>20</th>
      <td>43.44</td>
      <td>Shifu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>8431.29767</td>
    </tr>
    <tr>
      <th>21</th>
      <td>45.60</td>
      <td>Kasha</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>8978.89064</td>
    </tr>
    <tr>
      <th>22</th>
      <td>47.76</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>9207.35861</td>
    </tr>
    <tr>
      <th>23</th>
      <td>49.92</td>
      <td>Jinpu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>9601.77158</td>
    </tr>
    <tr>
      <th>24</th>
      <td>52.08</td>
      <td>Gekko</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10149.36455</td>
    </tr>
    <tr>
      <th>25</th>
      <td>54.24</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10377.83252</td>
    </tr>
    <tr>
      <th>26</th>
      <td>56.40</td>
      <td>Yukikaze</td>
      <td></td>
      <td>471.00297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10848.83549</td>
    </tr>
    <tr>
      <th>27</th>
      <td>58.56</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>956.07297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>11804.90846</td>
    </tr>
    <tr>
      <th>28</th>
      <td>60.72</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>12033.37643</td>
    </tr>
    <tr>
      <th>29</th>
      <td>62.88</td>
      <td>Shifu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>12427.78940</td>
    </tr>
    <tr>
      <th>30</th>
      <td>65.04</td>
      <td>Kasha</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>12975.38237</td>
    </tr>
    <tr>
      <th>31</th>
      <td>67.20</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>13203.85034</td>
    </tr>
    <tr>
      <th>32</th>
      <td>69.36</td>
      <td>Jinpu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>13598.26331</td>
    </tr>
    <tr>
      <th>33</th>
      <td>71.52</td>
      <td>Gekko</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>14145.85628</td>
    </tr>
    <tr>
      <th>34</th>
      <td>73.68</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>14374.32425</td>
    </tr>
    <tr>
      <th>35</th>
      <td>75.84</td>
      <td>Yukikaze</td>
      <td></td>
      <td>471.00297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>14845.32722</td>
    </tr>
    <tr>
      <th>36</th>
      <td>78.00</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>956.07297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15801.40019</td>
    </tr>
    <tr>
      <th>37</th>
      <td>80.16</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>16029.86816</td>
    </tr>
    <tr>
      <th>38</th>
      <td>82.32</td>
      <td>Shifu</td>
      <td></td>
      <td>357.42000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>16387.28816</td>
    </tr>
    <tr>
      <th>39</th>
      <td>84.48</td>
      <td>Kasha</td>
      <td></td>
      <td>510.60000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>16897.88816</td>
    </tr>
    <tr>
      <th>40</th>
      <td>86.64</td>
      <td>Higanbana</td>
      <td>Meikyo Shisui</td>
      <td>306.36000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>17204.24816</td>
    </tr>
    <tr>
      <th>41</th>
      <td>88.80</td>
      <td>Gekko</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>17751.84113</td>
    </tr>
    <tr>
      <th>42</th>
      <td>90.96</td>
      <td>Yukikaze</td>
      <td></td>
      <td>471.00297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>18222.84410</td>
    </tr>
    <tr>
      <th>43</th>
      <td>93.12</td>
      <td>Kasha</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>18770.43707</td>
    </tr>
    <tr>
      <th>44</th>
      <td>95.28</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>956.07297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>19726.51004</td>
    </tr>
    <tr>
      <th>45</th>
      <td>97.44</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>19954.97801</td>
    </tr>
    <tr>
      <th>46</th>
      <td>99.60</td>
      <td>Jinpu</td>
      <td></td>
      <td>394.41297</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20349.39098</td>
    </tr>
    <tr>
      <th>47</th>
      <td>101.76</td>
      <td>Gekko</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20896.98395</td>
    </tr>
    <tr>
      <th>48</th>
      <td>103.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>21125.45192</td>
    </tr>
    <tr>
      <th>49</th>
      <td>106.08</td>
      <td>Shifu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>21519.86489</td>
    </tr>
    <tr>
      <th>50</th>
      <td>108.24</td>
      <td>Kasha</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>22067.45786</td>
    </tr>
    <tr>
      <th>51</th>
      <td>110.40</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>22295.92583</td>
    </tr>
    <tr>
      <th>52</th>
      <td>112.56</td>
      <td>Yukikaze</td>
      <td></td>
      <td>471.00297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>22766.92880</td>
    </tr>
    <tr>
      <th>53</th>
      <td>114.72</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>956.07297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>23723.00177</td>
    </tr>
    <tr>
      <th>54</th>
      <td>116.88</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>23951.46974</td>
    </tr>
    <tr>
      <th>55</th>
      <td>119.04</td>
      <td>Jinpu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>24345.88271</td>
    </tr>
    <tr>
      <th>56</th>
      <td>121.20</td>
      <td>Gekko</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>24893.47568</td>
    </tr>
    <tr>
      <th>57</th>
      <td>123.36</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>25121.94365</td>
    </tr>
    <tr>
      <th>58</th>
      <td>125.52</td>
      <td>Shifu</td>
      <td></td>
      <td>394.41297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>25516.35662</td>
    </tr>
    <tr>
      <th>59</th>
      <td>127.68</td>
      <td>Kasha</td>
      <td></td>
      <td>547.59297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>26063.94959</td>
    </tr>
    <tr>
      <th>60</th>
      <td>129.84</td>
      <td>Hakaze</td>
      <td></td>
      <td>228.46797</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>26292.41756</td>
    </tr>
    <tr>
      <th>61</th>
      <td>132.00</td>
      <td>Yukikaze</td>
      <td></td>
      <td>471.00297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>26763.42053</td>
    </tr>
    <tr>
      <th>62</th>
      <td>134.16</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>956.07297</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>27719.49350</td>
    </tr>
  </tbody>
</table>
</div>


The timing here is better. An optimal window for Meikyo Shisui presents itself right after it comes off cooldown. We do end up dropping Higanbana DoT for about 7 seconds though, although that was the case in the previous rotation. The overall potency per second or potency per GCD are similar. 


```python
compare_potencies([df4_ext, df2_ext], labels=['With Opener 5', 'With Opener 3'])
```


![png](output_42_0.png)


Ultimately, with only weaponskills to play with, one buff, and one DoT, there is a limited degree of complexity in the single target rotation at level 50. Following the described priority system for weaponskills, using Iaijutsu intelligently, and keeping the GCD moving, you will be close to optimal output.
