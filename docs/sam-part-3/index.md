
<a id="header"></a>
# Part 3: levels 52-61

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

## lvl 52-61

Level 52 introduces the Kenki system with the Kenki Mastery I trait. The Kenki gauge takes on values between 0 and 100. This resource is used to fuel basically all of your abilities and is acquired mostly through the execution of weaponskills. The Kenki Mastery I trait grants Kenki for the following actions:


```python
kenki_table_I = [('Enpi', 5), ('Gekko (rear combo)', 5), 
                 ('Mangetsu (combo)', 5), ('Kasha (side combo)', 5), 
                 ('Oka (combo)', 5), ('Yukikaze (combo)', 5)]

kenki_table_df = pd.DataFrame(kenki_table_I, columns=['Weaponskill', 'Kenki granted'])
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
      <td>Enpi</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Gekko (rear combo)</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mangetsu (combo)</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Kasha (side combo)</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Oka (combo)</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Yukikaze (combo)</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>


Along with the trait, you acquire the first Kenki spender, Hissatsu: Kaiten. This ability, on a short 5s recast timer, increases the potency of your next weaponskill by 50% at the cost of 20 Kenki. Since it is specifically applied to the potency, it does not affect the "additional effect" aka the DoT of Higanbana. Therefore, it's basically our version of Life Surge or Barrage and we want to use it on Midare Setsugekka or Tenka Goken.

Level 54 introduces the gap-closer ability, Hissatsu: Gyoten, with a Kenki cost of 10. Level 56 gives the backstep disengage, Hissatsu: Yaten. While not part of an optimal dummy rotation, these mobility skills are useful in practice. See part 5 for in-depth discussion of the Kenki spenders.

At level 58, you learn Merciful Eyes, a self-heal linked to the Third Eye ability. At level 60, you obtain the Meditate ability. This ability, with a relatively short recast time of 60s, increases the Kenki gauge while channeled in battle for up to 15s at a rate of 10 Kenki per server tick up to a total of 50 Kenki. Note that it does nothing outside of combat.

The accrual rate of Kenki under Kenki Mastery I is quite low, about 30 Kenki every 8 GCDs (going through all three Sen combos). If we prioritize spending Kenki on Hissatsu: Kaiten for Midare Setsugekka, we'll have a net surplus of Kenki over time, assuming we don't spend Kenki on the movement utilities. This permits the use of Hissatsu: Kaiten on combo finishers (Kasha and Gekko) as excess Kenki accumulates, for a gain of 200 potency at the cost of 25 Kenki.

### Example Hissatsu: Kaiten usage


```python
sam = Samurai(kenki_mastery=1)

actions = [('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Jinpu'), ('Higanbana'), ('Gekko'), ('Hakaze'),
           ('Yukikaze'), ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka', 'Meikyo Shisui'), ('Gekko'), ('Yukikaze'), ('Kasha'),
           ('Midare Setsugekka')
           ]
```


```python
df0, average_potency, pps = sam.parse_rotation(actions)
display(df0)
```

    average potency per GCD = 452.39323529411763
    average potency per second = 208.081304113
    


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
      <td>5</td>
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
      <td>5</td>
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
      <td>5</td>
      <td>1536.000</td>
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
      <td>5</td>
      <td>2024.980</td>
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
      <td>10</td>
      <td>2226.460</td>
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
      <td>10</td>
      <td>2646.440</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Hakaze</td>
      <td></td>
      <td>220.455</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>2866.895</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Shifu</td>
      <td></td>
      <td>386.400</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>3253.295</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Kasha</td>
      <td>Hissatsu: Kaiten</td>
      <td>539.580</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>3792.875</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Midare Setsugekka</td>
      <td>Meikyo Shisui</td>
      <td>1407.600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>0</td>
      <td>5200.475</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Gekko</td>
      <td></td>
      <td>539.580</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>0</td>
      <td>5740.055</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Yukikaze</td>
      <td></td>
      <td>462.990</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5</td>
      <td>6203.045</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Kasha</td>
      <td></td>
      <td>539.580</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10</td>
      <td>6742.625</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>948.060</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>7690.685</td>
    </tr>
  </tbody>
</table>
</div>



```python
plot_potency(df0)
```


![png](output_10_0.png)


### Example Hissatsu: Kaiten usage for AoE rotations


```python
dfs_aoe = []
pps_aoe = []
labels = []

n_target_range = range(2, 8)

for n_targets in n_target_range:
    sam = Samurai(kenki_mastery=1)
    
    actions = [('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
               ('Jinpu'), ('Gekko'), ('Tenka Goken'), ('Fuga'),
               ('Oka'), ('Fuga'), ('Mangetsu', 'Hissatsu: Kaiten'), ('Tenka Goken'), 
               ('Fuga'), ('Mangetsu'), ('Fuga'), ('Oka'), 
               ('Tenka Goken')]
    
    print('number of targets = %s' % n_targets)
    df_temp, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
    dfs_aoe.append(df_temp)
    pps_aoe.append(pps)
    
    labels.append('%s targets' % n_targets)
    print('\n')

display(dfs_aoe[-1])
```

    number of targets = 2
    average potency per GCD = 420.06470588235294
    average potency per second = 193.211580087
    
    
    number of targets = 3
    average potency per GCD = 558.6058823529411
    average potency per second = 256.93452381
    
    
    number of targets = 4
    average potency per GCD = 683.2117647058824
    average potency per second = 314.247835498
    
    
    number of targets = 5
    average potency per GCD = 793.8823529411765
    average potency per second = 365.151515152
    
    
    number of targets = 6
    average potency per GCD = 890.6176470588235
    average potency per second = 409.645562771
    
    
    number of targets = 7
    average potency per GCD = 987.3529411764706
    average potency per second = 454.13961039
    
    
    


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
      <td>150.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>0</td>
      <td>150.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>0</td>
      <td>430.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Kasha</td>
      <td></td>
      <td>400.0</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>0</td>
      <td>830.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.0</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>5</td>
      <td>980.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Jinpu</td>
      <td></td>
      <td>280.0</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>5</td>
      <td>1260.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Gekko</td>
      <td></td>
      <td>460.0</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>5</td>
      <td>1720.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>2070.0</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>3790.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Fuga</td>
      <td></td>
      <td>805.0</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>4595.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Oka</td>
      <td></td>
      <td>1150.0</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>5745.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Fuga</td>
      <td></td>
      <td>805.0</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>15</td>
      <td>6550.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Mangetsu</td>
      <td>Hissatsu: Kaiten</td>
      <td>1150.0</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>15</td>
      <td>7700.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>3105.0</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>0</td>
      <td>10805.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Fuga</td>
      <td></td>
      <td>805.0</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>0</td>
      <td>11610.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Mangetsu</td>
      <td></td>
      <td>1150.0</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>0</td>
      <td>12760.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Fuga</td>
      <td></td>
      <td>805.0</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>5</td>
      <td>13565.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Oka</td>
      <td></td>
      <td>1150.0</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>5</td>
      <td>14715.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>2070.0</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>16785.0</td>
    </tr>
  </tbody>
</table>
</div>



```python
compare_n_potencies(dfs_aoe, labels)
```


![png](output_13_0.png)


<a href="#header">back to the top...</a>
