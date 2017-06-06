
# Samurai by the numbers (lvl 1-49)
## by Tzuyu Chou (Cactuar)

### Update log

```python
from samurai import *
from plotting import *

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
from IPython.display import display
%matplotlib inline
```

<hr width=75%>

## lvl 1-3

Up to level 3, you only have one weaponskill... so use it.


```python
sam = Samurai()

actions = [('Hakaze'), ('Hakaze'), ('Hakaze'), ('Hakaze'), 
           ('Hakaze'), ('Hakaze'), ('Hakaze'), ('Hakaze')]
```


```python
df0, average_potency, pps = sam.parse_rotation(actions)
display(df0)
```

    average potency per GCD = 150.0
    average potency per second = 62.5



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
      <th>Total Potency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.0</td>
      <td>150.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.4</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.0</td>
      <td>300.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.8</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.0</td>
      <td>450.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.2</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.0</td>
      <td>600.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.6</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.0</td>
      <td>750.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>12.0</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.0</td>
      <td>900.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>14.4</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.0</td>
      <td>1050.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16.8</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.0</td>
      <td>1200.0</td>
    </tr>
  </tbody>
</table>
</div>


<hr width=75%>

## lvl 4-17

At level 4, you gain the use of Jinpu, which combos from Hakaze and gives you your damage up buff. You'll definitely want to keep this buff up at all times and it should be simple enough with its 30s duration. The next weaponskill you obtain is Enbi, a ranged attack with a niche use. Level 6 grants you the defensive buff, Third Eye, and level 10 grants you the ability Ageha, an execution ability. Use it whenever available.


```python
sam = Samurai()

actions = [('Hakaze'), ('Jinpu'), ('Hakaze'), ('Jinpu'),
           ('Hakaze'), ('Jinpu'), ('Hakaze'), ('Jinpu')]
```


```python
df1, average_potency, pps = sam.parse_rotation(actions)
display(df1)
```

    average potency per GCD = 239.1875
    average potency per second = 99.6614583333



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
      <th>Total Potency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.0</td>
      <td>150.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.4</td>
      <td>Jinpu</td>
      <td></td>
      <td>280.0</td>
      <td>430.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.8</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.5</td>
      <td>602.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.2</td>
      <td>Jinpu</td>
      <td></td>
      <td>322.0</td>
      <td>924.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.6</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.5</td>
      <td>1097.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>12.0</td>
      <td>Jinpu</td>
      <td></td>
      <td>322.0</td>
      <td>1419.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>14.4</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.5</td>
      <td>1591.5</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16.8</td>
      <td>Jinpu</td>
      <td></td>
      <td>322.0</td>
      <td>1913.5</td>
    </tr>
  </tbody>
</table>
</div>


How does this compare to the previous rotation?


```python
compare_potencies([df0, df1], ['Hakaze only', 'Jinpu combo'])
```


![png](output_14_0.png)


<hr width=75%>

## lvl 18-29

Level 18 sees the introduction of your haste buff, Shifu. When executed as a combo, Shifu grants you this buff for a duration of 30s in addition to the additional combo potency. At these levels, it's fairly close as to which buff takes priority, Shifu or Jinpu. However, with the introduction of Sen, you will definitely want to prioritize Shifu so that you may open your Sen more often to execute the powerful Iaijutsu more often.


```python
sam = Samurai()

actions = [('Hakaze'), ('Shifu'), ('Hakaze'), ('Jinpu'),
           ('Hakaze'), ('Shifu'), ('Hakaze'), ('Jinpu')]
```


```python
df2, average_potency, pps = sam.parse_rotation(actions)
display(df2)
```

    average potency per GCD = 231.125
    average potency per second = 105.53652968



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
      <td>150.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.0</td>
      <td>430.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.0</td>
      <td>580.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Jinpu</td>
      <td></td>
      <td>280.0</td>
      <td>860.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.5</td>
      <td>1032.5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Shifu</td>
      <td></td>
      <td>322.0</td>
      <td>1354.5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.5</td>
      <td>1527.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Jinpu</td>
      <td></td>
      <td>322.0</td>
      <td>1849.0</td>
    </tr>
  </tbody>
</table>
</div>



```python
compare_potencies([df1, df2], ['Jinpu combo only', 'Jinpu and Shifu combos'])
```


![png](output_20_0.png)


** Note: The Shifu buff is only accounted for in potency per second calculations.

<hr width=75%>

Level 26 introduces your first AoE ability, Fuga. At this time, it does not combo to or from anything and deals 100 potency to all targets in a frontal cone.

Napkin math says that Fuga should do more potency per GCD for three or more targets. Should we put our Shifu and Jinpu buffs if they're not up before using Fuga? Depends on how long the encounter is.

### For Fuga with buffs:


```python
dfs_buff = []
pps_buff = []
labels = []

n_target_range = range(2, 8)

for n_targets in n_target_range:
    sam = Samurai()
    
    actions = [('Hakaze'), ('Shifu'), ('Hakaze'), ('Jinpu'),
               ('Fuga'), ('Fuga'), ('Fuga'), ('Fuga'),
               ('Fuga'), ('Fuga'), ('Fuga'), ('Fuga'),
               ('Fuga'), ('Fuga'), ('Fuga'), ('Fuga')]
    
    print('number of targets = %s' % n_targets)
    df_temp, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
    dfs_buff.append(df_temp)
    pps_buff.append(pps)
    
    labels.append('%s targets' % n_targets)
    
    print('\n')
```

    number of targets = 2
    average potency per GCD = 226.25
    average potency per second = 104.022988506
    
    
    number of targets = 3
    average potency per GCD = 312.5
    average potency per second = 143.67816092
    
    
    number of targets = 4
    average potency per GCD = 398.75
    average potency per second = 183.333333333
    
    
    number of targets = 5
    average potency per GCD = 485.0
    average potency per second = 222.988505747
    
    
    number of targets = 6
    average potency per GCD = 571.25
    average potency per second = 262.643678161
    
    
    number of targets = 7
    average potency per GCD = 657.5
    average potency per second = 302.298850575
    
    



```python
compare_n_potencies(dfs_buff, labels)
```


![png](output_27_0.png)


### For Fuga with no buffs:


```python
dfs_no_buff = []
pps_no_buff = []
labels = []

for n_targets in n_target_range:
    sam = Samurai()
    
    actions = [('Fuga'), ('Fuga'), ('Fuga'), ('Fuga'),
               ('Fuga'), ('Fuga'), ('Fuga'), ('Fuga'),
               ('Fuga'), ('Fuga'), ('Fuga'), ('Fuga'),
               ('Fuga'), ('Fuga'), ('Fuga'), ('Fuga')]
    
    print('number of targets = %s' % n_targets)
    df_temp, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
    dfs_no_buff.append(df_temp)
    pps_no_buff.append(pps)
    
    labels.append('%s targets' % n_targets)
    
    print('\n')
```

    number of targets = 2
    average potency per GCD = 200.0
    average potency per second = 83.3333333333
    
    
    number of targets = 3
    average potency per GCD = 300.0
    average potency per second = 125.0
    
    
    number of targets = 4
    average potency per GCD = 400.0
    average potency per second = 166.666666667
    
    
    number of targets = 5
    average potency per GCD = 500.0
    average potency per second = 208.333333333
    
    
    number of targets = 6
    average potency per GCD = 600.0
    average potency per second = 250.0
    
    
    number of targets = 7
    average potency per GCD = 700.0
    average potency per second = 291.666666667
    
    



```python
compare_n_potencies(dfs_no_buff, labels)
```


![png](output_30_0.png)


The potency over four GCDs to put up Shifu and Jinpu is about 977. If this is more than the potential potency delivered by four Fuga, we need the increased potency from the buffs to make up for this "buff tax."


```python
fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, figsize=(12,4))
fig.tight_layout(pad=2)

axes.plot(n_target_range, pps_buff, '-s', label='buffs')
axes.plot(n_target_range, pps_no_buff, ':o', label='no buffs')
axes.set_ylabel('Potency per second')
axes.set_xlabel('Number of Targets')
axes.legend(loc='upper left', framealpha=0.5)

fig.suptitle('Average Potency per second over %s GCDs' % len(actions))
```




    <matplotlib.text.Text at 0x110a28b70>




![png](output_32_1.png)


Over a 16 GCD encounter, buffing before Fuga spam wins every time. Let's see how the two rotations compare over different encounter lengths.


```python
fig, axes = plt.subplots(nrows=len(dfs_buff), ncols=1, sharex=True, figsize=(12,12))
fig.tight_layout(pad=2)

for k, _ in enumerate(dfs_buff): 
    ax = axes[k]
    
    xlocs = dfs_buff[k]['Time']
    ax.plot(xlocs, dfs_buff[k]['Total Potency'], '-s', label='buffs')
    
    xlocs = dfs_no_buff[k]['Time']
    ax.plot(xlocs, dfs_no_buff[k]['Total Potency'], ':o', label='no buffs')

    ax.set_ylabel('Cumulative Potency', fontsize=10)
    axes[-1].set_xlabel('Time')
    
    axes[-1].set_xticks(xlocs)
    ax.legend(loc='upper left', framealpha=0.5, prop={'size': 'small'})
    
    ax.set_title('on %s targets' % n_target_range[k])

fig.tight_layout(pad=3)
```


![png](output_34_0.png)


There are approximately fourteen GCDs after putting up your first buff, Shifu before you need to refresh it. For small mob counts, the crossover point where putting up buffs before using Fuga is more optimal occurs fairly early on. However, as the number of targets increases, the upfront "cost" of putting the buffs up does not pay off until much later. A sixteen GCD pull is likely to run you dry on TP, even with Invigorate. At these low levels, the pull sizes are likely to be small, so putting up buffs first is probably optimal.

Note that the potency per second of the buffed AoE rotation is greater than that of the single target rotation for pulls of three or more targets.

### Priority: Shifu > Jinpu. 
### Filler: Either combo to maintain the buffs.

### AoE: Shifu > Jinpu > Fuga for small groups. Fuga only for very large groups (>7 or so)

<hr width=75%>

## lvl 30-39

Level 30 sees the introduction of your first Sen through the Gekko combo finisher (combo from Jinpu) and with it your first Iaijutsu, Higanbana. This powerful single-target weaponskill applies a 60s DoT in addition to initial damage for a total of 940 potency over its duration.


```python
sam = Samurai()

actions = [('Hakaze'), ('Shifu'), ('Hakaze'), ('Jinpu'),
           ('Gekko'), ('Higanbana'), ('Hakaze'), ('Jinpu'),
           ('Gekko'), ('Hakaze'), ('Jinpu'), ('Gekko'),
           ('Hakaze'), ('Shifu')]
```


```python
df3, average_potency, pps = sam.parse_rotation(actions)
display(df3)
```

    average potency per GCD = 304.7225714285714
    average potency per second = 139.964435696



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
      <td>150.000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.000</td>
      <td>430.000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.000</td>
      <td>580.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Jinpu</td>
      <td></td>
      <td>280.000</td>
      <td>860.000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Gekko</td>
      <td></td>
      <td>460.000</td>
      <td>1320.000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Higanbana</td>
      <td></td>
      <td>276.000</td>
      <td>1596.000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Hakaze</td>
      <td></td>
      <td>205.827</td>
      <td>1801.827</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Jinpu</td>
      <td></td>
      <td>355.327</td>
      <td>2157.154</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Gekko</td>
      <td></td>
      <td>493.327</td>
      <td>2650.481</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Hakaze</td>
      <td></td>
      <td>205.827</td>
      <td>2856.308</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Jinpu</td>
      <td></td>
      <td>355.327</td>
      <td>3211.635</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Gekko</td>
      <td></td>
      <td>493.327</td>
      <td>3704.962</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Hakaze</td>
      <td></td>
      <td>205.827</td>
      <td>3910.789</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Shifu</td>
      <td></td>
      <td>355.327</td>
      <td>4266.116</td>
    </tr>
  </tbody>
</table>
</div>


** Note: the potency of the DoT is prorated due to the GCD being shorter than the DoT tick period. So Higanbana's initial potency is applied on action and the DoT potency is added to subsequent GCDs. 

This combo finisher is a massive increase in potency per second (~40%).


```python
plot_potency(df3)
```


![png](output_43_0.png)


At this point, the average potency of the Gekko combo is $400+280+150=830/3=~276.66$ before buffs. The average potency of the Shifu combo is $150+280=430/2=215$ before buffs. Therefore, Higanbana is more optimal than the Gekko combo after two DoT ticks. Since it takes approximately 3-4 GCDs to reapply Higanbana (Gekko combo plus cast time of Higanbana), Higanbana may be optimal to clip in single target situations. Depending on the GCD and server tick, this may be close. Additionally, in small mob groups, applying Higanbana to each target may also be optimal.


```python
sam = Samurai()

actions = [('Hakaze'), ('Shifu'), ('Hakaze'), ('Jinpu'),
           ('Gekko'), ('Higanbana'), ('Hakaze'), ('Jinpu'),
           ('Gekko'), ('Higanbana'), ('Hakaze'), ('Jinpu'),
           ('Gekko'), ('Higanbana'), ('Hakaze'), ('Shifu')]
```


```python
df3_clip, average_potency, pps = sam.parse_rotation(actions)
display(df3_clip)
```

    average potency per GCD = 305.298125
    average potency per second = 140.366954023



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
      <td>150.000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.000</td>
      <td>430.000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.000</td>
      <td>580.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Jinpu</td>
      <td></td>
      <td>280.000</td>
      <td>860.000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Gekko</td>
      <td></td>
      <td>460.000</td>
      <td>1320.000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Higanbana</td>
      <td></td>
      <td>276.000</td>
      <td>1596.000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Hakaze</td>
      <td></td>
      <td>205.827</td>
      <td>1801.827</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Jinpu</td>
      <td></td>
      <td>355.327</td>
      <td>2157.154</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Gekko</td>
      <td></td>
      <td>493.327</td>
      <td>2650.481</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Higanbana</td>
      <td></td>
      <td>309.327</td>
      <td>2959.808</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Hakaze</td>
      <td></td>
      <td>205.827</td>
      <td>3165.635</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Jinpu</td>
      <td></td>
      <td>355.327</td>
      <td>3520.962</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Gekko</td>
      <td></td>
      <td>493.327</td>
      <td>4014.289</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Higanbana</td>
      <td></td>
      <td>309.327</td>
      <td>4323.616</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Hakaze</td>
      <td></td>
      <td>205.827</td>
      <td>4529.443</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Shifu</td>
      <td></td>
      <td>355.327</td>
      <td>4884.770</td>
    </tr>
  </tbody>
</table>
</div>


In a multi-target situation, the DoT can be applied to different mobs to avoid clipping. This will increase the DoT potency accumulation following each Higanbana application, leading to a slight increase in net potency. Note the reapplication of Shifu to keep the buff up.

Now let's try applying Higanbana once and not clipping it (e.g., single target situation):


```python
sam = Samurai()

actions = [('Hakaze'), ('Shifu'), ('Hakaze'), ('Jinpu'),
           ('Gekko'), ('Higanbana'), ('Hakaze'), ('Jinpu'),
           ('Gekko'), ('Hakaze'), ('Jinpu'), ('Gekko'), 
           ('Hakaze'), ('Shifu'), ('Hakaze'), ('Jinpu')]
```


```python
df3_noclip, average_potency, pps = sam.parse_rotation(actions)
display(df3_noclip)
```

    average potency per GCD = 301.704375
    average potency per second = 138.714655172



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
      <td>150.000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.000</td>
      <td>430.000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.000</td>
      <td>580.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Jinpu</td>
      <td></td>
      <td>280.000</td>
      <td>860.000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Gekko</td>
      <td></td>
      <td>460.000</td>
      <td>1320.000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Higanbana</td>
      <td></td>
      <td>276.000</td>
      <td>1596.000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Hakaze</td>
      <td></td>
      <td>205.827</td>
      <td>1801.827</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Jinpu</td>
      <td></td>
      <td>355.327</td>
      <td>2157.154</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Gekko</td>
      <td></td>
      <td>493.327</td>
      <td>2650.481</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Hakaze</td>
      <td></td>
      <td>205.827</td>
      <td>2856.308</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Jinpu</td>
      <td></td>
      <td>355.327</td>
      <td>3211.635</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Gekko</td>
      <td></td>
      <td>493.327</td>
      <td>3704.962</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Hakaze</td>
      <td></td>
      <td>205.827</td>
      <td>3910.789</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Shifu</td>
      <td></td>
      <td>355.327</td>
      <td>4266.116</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Hakaze</td>
      <td></td>
      <td>205.827</td>
      <td>4471.943</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Jinpu</td>
      <td></td>
      <td>355.327</td>
      <td>4827.270</td>
    </tr>
  </tbody>
</table>
</div>



```python
compare_potencies([df3_clip, df3_noclip], ['Clipping', 'No clipping'])
```


![png](output_51_0.png)


It's fairly close over this time horizon. The average potency per second is vastly dependent on where the encounter ends more than anything. Regardless if you clip Higanbana or not, it is better than not using Higanbana at all. The bottom line: use your Iaijutsu!

<hr width=75%>

Level 35 introduces an AoE combo with Mangetsu (combo from Fuga). This weaponskill also opens the Getsu Sen. Due to the diminishing AoE scaling, this combo is an average of no less than 100 potency per target over two GCDs. Because Mangetsu opens the Getsu Sen, this allows you to apply Higanbana to individual targets in the group. Depending on group size and encounter duration, this may be optimal. 


```python
dfs_higanbana = []
pps_higanbana = []
labels = []

n_target_range = range(2, 8)

for n_targets in n_target_range:
    sam = Samurai()
    
    actions = [('Fuga'), ('Mangetsu'), ('Higanbana'), ('Fuga'),
               ('Mangetsu'), ('Higanbana'), ('Fuga'), ('Mangetsu'),
               ('Higanbana'), ('Fuga'), ('Mangetsu'), ('Higanbana'),
               ('Fuga'), ('Mangetsu')]
    
    print('number of targets = %s' % n_targets)
    df_temp, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
    dfs_higanbana.append(df_temp)
    pps_higanbana.append(pps)
    
    labels.append('%s targets' % n_targets)  
    print('\n')
```

    number of targets = 2
    average potency per GCD = 303.7142857142857
    average potency per second = 126.547619048
    
    
    number of targets = 3
    average potency per GCD = 408.57142857142856
    average potency per second = 170.238095238
    
    
    number of targets = 4
    average potency per GCD = 506.2857142857143
    average potency per second = 210.952380952
    
    
    number of targets = 5
    average potency per GCD = 584.8571428571429
    average potency per second = 243.69047619
    
    
    number of targets = 6
    average potency per GCD = 656.2857142857143
    average potency per second = 273.452380952
    
    
    number of targets = 7
    average potency per GCD = 727.7142857142857
    average potency per second = 303.214285714
    
    



```python
compare_n_potencies(dfs_higanbana, labels)
```


![png](output_56_0.png)



```python
dfs_no_higanbana = []
pps_no_higanbana = []
labels = []

n_target_range = range(2, 8)

for n_targets in n_target_range:
    sam = Samurai()
    
    actions = [('Fuga'), ('Mangetsu'), ('Fuga'), ('Mangetsu'),
               ('Fuga'), ('Mangetsu'), ('Fuga'), ('Mangetsu'),
               ('Fuga'), ('Mangetsu'), ('Fuga'), ('Mangetsu'),
               ('Fuga'), ('Mangetsu')]

    print('number of targets = %s' % n_targets)
    df_temp, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
    dfs_no_higanbana.append(df_temp)
    pps_no_higanbana.append(pps)
    
    labels.append('%s targets' % n_targets)  
    print('\n')
```

    number of targets = 2
    average potency per GCD = 290.0
    average potency per second = 120.833333333
    
    
    number of targets = 3
    average potency per GCD = 420.0
    average potency per second = 175.0
    
    
    number of targets = 4
    average potency per GCD = 540.0
    average potency per second = 225.0
    
    
    number of targets = 5
    average potency per GCD = 650.0
    average potency per second = 270.833333333
    
    
    number of targets = 6
    average potency per GCD = 750.0
    average potency per second = 312.5
    
    
    number of targets = 7
    average potency per GCD = 850.0
    average potency per second = 354.166666667
    
    



```python
compare_n_potencies(dfs_no_higanbana, labels)
```


![png](output_58_0.png)



```python
fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, figsize=(12,4))
fig.tight_layout(pad=2)

axes.plot(n_target_range, pps_higanbana, '-o', label='Applying Higanbana')
axes.plot(n_target_range, pps_no_higanbana, ':o', label='No Higanbana')
axes.plot(n_target_range, pps_buff, ':o', label='Buffed Fuga spam')
axes.set_ylabel('Potency per second')
axes.set_xlabel('Number of Targets')
axes.legend(loc='upper left', framealpha=0.5)

fig.suptitle('Average Potency per second over %s GCDs' % len(actions))
```




    <matplotlib.text.Text at 0x1112a1278>




![png](output_59_1.png)



```python
fig, axes = plt.subplots(nrows=len(dfs_higanbana), ncols=1, sharex=True, figsize=(12,12))
fig.tight_layout(pad=2)

for k, _ in enumerate(dfs_higanbana): 
    ax = axes[k]
    
    xlocs = dfs_higanbana[k]['Time']
    ax.plot(xlocs, dfs_higanbana[k]['Total Potency'], '-o', label='Applying Higanbana')
    
    xlocs = dfs_no_higanbana[k]['Time']
    ax.plot(xlocs, dfs_no_higanbana[k]['Total Potency'], ':o', label='No Higanbana')

    ax.set_ylabel('Cumulative Potency', fontsize=10)
    axes[-1].set_xlabel('Time')
    
    axes[-1].set_xticks(xlocs)
    ax.legend(loc='upper left', framealpha=0.5, prop={'size': 'small'})
    
    ax.set_title('on %s targets' % n_target_range[k])

fig.tight_layout(pad=3)
```


![png](output_60_0.png)


Since 3-4 is the typical pull size for leveling dungeons, it is likely optimal to not apply Higanbana to each mob at this level range. However, it is extremely close either way. One advantage for applying Higanbana, however, would be TP relief from executing the AoE weaponskills. Should we buff with Jinpu and Shifu before executing this rotation?


```python
sam = Samurai()

n_targets = 3

actions = [('Hakaze'), ('Shifu'), ('Hakaze'), ('Jinpu'),
           ('Fuga'), ('Mangetsu'), ('Fuga'), ('Mangetsu'), 
           ('Fuga'), ('Mangetsu'), ('Fuga'), ('Mangetsu'),
           ('Fuga'), ('Mangetsu'), ('Fuga'), ('Mangetsu')]
```


```python
df4_buff, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
display(df4_buff)
```

    average potency per GCD = 416.0
    average potency per second = 191.264367816



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
      <td>150.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.0</td>
      <td>430.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.0</td>
      <td>580.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Jinpu</td>
      <td></td>
      <td>280.0</td>
      <td>860.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Fuga</td>
      <td></td>
      <td>345.0</td>
      <td>1205.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Mangetsu</td>
      <td></td>
      <td>621.0</td>
      <td>1826.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Fuga</td>
      <td></td>
      <td>345.0</td>
      <td>2171.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Mangetsu</td>
      <td></td>
      <td>621.0</td>
      <td>2792.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Fuga</td>
      <td></td>
      <td>345.0</td>
      <td>3137.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Mangetsu</td>
      <td></td>
      <td>621.0</td>
      <td>3758.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Fuga</td>
      <td></td>
      <td>345.0</td>
      <td>4103.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Mangetsu</td>
      <td></td>
      <td>621.0</td>
      <td>4724.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Fuga</td>
      <td></td>
      <td>345.0</td>
      <td>5069.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Mangetsu</td>
      <td></td>
      <td>621.0</td>
      <td>5690.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Fuga</td>
      <td></td>
      <td>345.0</td>
      <td>6035.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Mangetsu</td>
      <td></td>
      <td>621.0</td>
      <td>6656.0</td>
    </tr>
  </tbody>
</table>
</div>



```python
sam = Samurai()

n_targets = 3

actions = [('Fuga'), ('Mangetsu'), ('Fuga'), ('Mangetsu'),
           ('Fuga'), ('Mangetsu'), ('Fuga'), ('Mangetsu'),
           ('Fuga'), ('Mangetsu'), ('Fuga'), ('Mangetsu'),
           ('Fuga'), ('Mangetsu'), ('Fuga'), ('Mangetsu')]
```


```python
df4_no_buff, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
display(df4_no_buff)
```

    average potency per GCD = 420.0
    average potency per second = 175.0



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
      <th>Total Potency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>Fuga</td>
      <td></td>
      <td>300.0</td>
      <td>300.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.4</td>
      <td>Mangetsu</td>
      <td></td>
      <td>540.0</td>
      <td>840.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.8</td>
      <td>Fuga</td>
      <td></td>
      <td>300.0</td>
      <td>1140.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7.2</td>
      <td>Mangetsu</td>
      <td></td>
      <td>540.0</td>
      <td>1680.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9.6</td>
      <td>Fuga</td>
      <td></td>
      <td>300.0</td>
      <td>1980.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>12.0</td>
      <td>Mangetsu</td>
      <td></td>
      <td>540.0</td>
      <td>2520.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>14.4</td>
      <td>Fuga</td>
      <td></td>
      <td>300.0</td>
      <td>2820.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16.8</td>
      <td>Mangetsu</td>
      <td></td>
      <td>540.0</td>
      <td>3360.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>19.2</td>
      <td>Fuga</td>
      <td></td>
      <td>300.0</td>
      <td>3660.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>21.6</td>
      <td>Mangetsu</td>
      <td></td>
      <td>540.0</td>
      <td>4200.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>24.0</td>
      <td>Fuga</td>
      <td></td>
      <td>300.0</td>
      <td>4500.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>26.4</td>
      <td>Mangetsu</td>
      <td></td>
      <td>540.0</td>
      <td>5040.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>28.8</td>
      <td>Fuga</td>
      <td></td>
      <td>300.0</td>
      <td>5340.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>31.2</td>
      <td>Mangetsu</td>
      <td></td>
      <td>540.0</td>
      <td>5880.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>33.6</td>
      <td>Fuga</td>
      <td></td>
      <td>300.0</td>
      <td>6180.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>36.0</td>
      <td>Mangetsu</td>
      <td></td>
      <td>540.0</td>
      <td>6720.0</td>
    </tr>
  </tbody>
</table>
</div>



```python
compare_potencies([df4_buff, df4_no_buff], ['buffs', 'no buffs'])
```


![png](output_66_0.png)


If the pull is long enough, you should buff first. Ideally, you would shift to a single target rotation as mobs die, possibly letting you refresh buffs that carry over to the next pull. 

### Priority: Shifu > Jinpu
### Filler: Gekko combo > Higanbana
### AoE: Mangetsu combo + Higanbana, depending on group size and encounter duration

<hr width=75%>

## lvl 40-49

Level 40 introduces the Kasha combo finisher (combo from Shifu). Equal in potency to the Gekko finisher, this weaponskill opens the Ka Sen. This leads to a maximum of two Sen open and also unlocks the use of the Iaijutsu Tenka Goken. This powerful, AoE weaponskill scales its potency depending on the number of targets from 180 potency up to a maximum of 360 potency for the first target hit. In AoE situations, this is likely Iaijutsu of choice due to its instantaneous damage. Unfortunately, you do not get the AoE weaponskill to open Ka until level 45. For single target, do we still want to try our shiny new Iaijutsu?


```python
sam = Samurai()

n_targets = 1

actions = [('Hakaze'), ('Shifu'), ('Kasha'), ('Higanbana'),
           ('Hakaze'), ('Jinpu'), ('Gekko'), ('Hakaze'),
           ('Shifu'), ('Kasha'), ('Tenka Goken'), ('Hakaze'),
           ('Jinpu'), ('Gekko'), ('Hakaze'), ('Shifu'),
           ('Kasha'), ('Tenka Goken')]
```


```python
df5_tenka, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
display(df5_tenka)
```

    average potency per GCD = 336.30222222222216
    average potency per second = 154.740286299



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
      <th>Total Potency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.00</td>
      <td>150.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.00</td>
      <td>430.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Kasha</td>
      <td></td>
      <td>400.00</td>
      <td>830.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Higanbana</td>
      <td></td>
      <td>240.00</td>
      <td>1070.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Hakaze</td>
      <td></td>
      <td>175.20</td>
      <td>1245.20</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Jinpu</td>
      <td></td>
      <td>308.98</td>
      <td>1554.18</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Gekko</td>
      <td></td>
      <td>488.98</td>
      <td>2043.16</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Hakaze</td>
      <td></td>
      <td>201.48</td>
      <td>2244.64</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Shifu</td>
      <td></td>
      <td>350.98</td>
      <td>2595.62</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Kasha</td>
      <td></td>
      <td>488.98</td>
      <td>3084.60</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>442.98</td>
      <td>3527.58</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>201.48</td>
      <td>3729.06</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Jinpu</td>
      <td></td>
      <td>350.98</td>
      <td>4080.04</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Gekko</td>
      <td></td>
      <td>488.98</td>
      <td>4569.02</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Hakaze</td>
      <td></td>
      <td>201.48</td>
      <td>4770.50</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Shifu</td>
      <td></td>
      <td>350.98</td>
      <td>5121.48</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Kasha</td>
      <td></td>
      <td>488.98</td>
      <td>5610.46</td>
    </tr>
    <tr>
      <th>17</th>
      <td>36.96</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>442.98</td>
      <td>6053.44</td>
    </tr>
  </tbody>
</table>
</div>



```python
sam = Samurai()

n_targets = 1

actions = [('Hakaze'), ('Shifu'), ('Kasha'), ('Higanbana'),
           ('Hakaze'), ('Jinpu'), ('Gekko'), ('Higanbana'),
           ('Hakaze'), ('Shifu'), ('Kasha'), ('Higanbana'),
           ('Hakaze'), ('Jinpu'), ('Gekko'), ('Higanbana'),
           ('Hakaze'), ('Shifu')]
```


```python
df5_no_tenka, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
display(df5_no_tenka)
```

    average potency per GCD = 313.16166666666675
    average potency per second = 144.092791411



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
      <td>150.000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.000</td>
      <td>430.000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Kasha</td>
      <td></td>
      <td>400.000</td>
      <td>830.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Higanbana</td>
      <td></td>
      <td>240.000</td>
      <td>1070.000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Hakaze</td>
      <td></td>
      <td>175.200</td>
      <td>1245.200</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Jinpu</td>
      <td></td>
      <td>308.980</td>
      <td>1554.180</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Gekko</td>
      <td></td>
      <td>488.980</td>
      <td>2043.160</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Higanbana</td>
      <td></td>
      <td>304.980</td>
      <td>2348.140</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Hakaze</td>
      <td></td>
      <td>205.827</td>
      <td>2553.967</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Shifu</td>
      <td></td>
      <td>355.327</td>
      <td>2909.294</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Kasha</td>
      <td></td>
      <td>493.327</td>
      <td>3402.621</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Higanbana</td>
      <td></td>
      <td>309.327</td>
      <td>3711.948</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Hakaze</td>
      <td></td>
      <td>205.827</td>
      <td>3917.775</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Jinpu</td>
      <td></td>
      <td>355.327</td>
      <td>4273.102</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Gekko</td>
      <td></td>
      <td>493.327</td>
      <td>4766.429</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Higanbana</td>
      <td></td>
      <td>309.327</td>
      <td>5075.756</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Hakaze</td>
      <td></td>
      <td>205.827</td>
      <td>5281.583</td>
    </tr>
    <tr>
      <th>17</th>
      <td>36.96</td>
      <td>Shifu</td>
      <td></td>
      <td>355.327</td>
      <td>5636.910</td>
    </tr>
  </tbody>
</table>
</div>



```python
compare_potencies([df5_no_tenka, df5_tenka], ['No Tenka Goken', 'With Tenka Goken'])
```


![png](output_76_0.png)


It's surprisingly close! I would favor using Tenka Goken since it's fresh though.

<hr width=75%>

With the addition of a second third-level combo finisher plus Tenka Goken, do we want to move away from the AoE weaponskill rotation in favor of a single target one for the standard three mob pull?


```python
sam = Samurai()

n_targets = 3

actions = [('Hakaze'), ('Shifu'), ('Kasha'), ('Higanbana'),
           ('Hakaze'), ('Jinpu'), ('Gekko'), ('Higanbana'),
           ('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Jinpu'), ('Gekko'), ('Tenka Goken')]
```


```python
df6_higanbana, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
display(df6_higanbana)
```

    average potency per GCD = 387.4059333333333
    average potency per second = 178.035814951



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
      <td>150.000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.000</td>
      <td>430.000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Kasha</td>
      <td></td>
      <td>400.000</td>
      <td>830.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Higanbana</td>
      <td></td>
      <td>240.000</td>
      <td>1070.000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Hakaze</td>
      <td></td>
      <td>175.200</td>
      <td>1245.200</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Jinpu</td>
      <td></td>
      <td>308.980</td>
      <td>1554.180</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Gekko</td>
      <td></td>
      <td>488.980</td>
      <td>2043.160</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Higanbana</td>
      <td></td>
      <td>304.980</td>
      <td>2348.140</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.807</td>
      <td>2582.947</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Shifu</td>
      <td></td>
      <td>384.307</td>
      <td>2967.254</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Kasha</td>
      <td></td>
      <td>522.307</td>
      <td>3489.561</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.807</td>
      <td>3724.368</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Jinpu</td>
      <td></td>
      <td>384.307</td>
      <td>4108.675</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Gekko</td>
      <td></td>
      <td>522.307</td>
      <td>4630.982</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>1180.107</td>
      <td>5811.089</td>
    </tr>
  </tbody>
</table>
</div>



```python
sam = Samurai()

n_targets = 3

actions = [('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Jinpu'), ('Gekko'), ('Tenka Goken'), ('Hakaze'),
           ('Shifu'), ('Kasha'), ('Hakaze'), ('Jinpu'),
           ('Gekko'), ('Tenka Goken'), ('Hakaze')]
```


```python
df6_tenka_only, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
display(df6_tenka_only)
```

    average potency per GCD = 402.47333333333336
    average potency per second = 184.960171569



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
      <td>150.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.0</td>
      <td>430.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Kasha</td>
      <td></td>
      <td>400.0</td>
      <td>830.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.0</td>
      <td>980.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Jinpu</td>
      <td></td>
      <td>280.0</td>
      <td>1260.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Gekko</td>
      <td></td>
      <td>460.0</td>
      <td>1720.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>1117.8</td>
      <td>2837.8</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.5</td>
      <td>3010.3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Shifu</td>
      <td></td>
      <td>322.0</td>
      <td>3332.3</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Kasha</td>
      <td></td>
      <td>460.0</td>
      <td>3792.3</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.5</td>
      <td>3964.8</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Jinpu</td>
      <td></td>
      <td>322.0</td>
      <td>4286.8</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Gekko</td>
      <td></td>
      <td>460.0</td>
      <td>4746.8</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>1117.8</td>
      <td>5864.6</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.5</td>
      <td>6037.1</td>
    </tr>
  </tbody>
</table>
</div>



```python
compare_potencies([df6_tenka_only, df6_higanbana], ['Tenka Goken only', 'Higanbana two targets first'])
```


![png](output_84_0.png)


Although close, both of these rotation potencies are inferior compared to the previous AoE rotations, even they were without Tenka Goken. However, we can open Getsu using the Mangetsu combo and open Ka using the Kasha combo. Maybe that works better?


```python
sam = Samurai()

n_targets = 3

actions = [('Hakaze'), ('Shifu'), ('Kasha'), ('Higanbana'),
           ('Hakaze'), ('Jinpu'), ('Gekko'), ('Higanbana'),
           ('Hakaze'), ('Shifu'), ('Kasha'), ('Fuga'), 
           ('Mangetsu'), ('Tenka Goken'), ('Fuga'), ('Mangetsu'),
           ('Hakaze'), ('Shifu'), ('Kasha'), ('Tenka Goken')]
```


```python
df6_aoe_higanbana2, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
display(df6_aoe_higanbana2)
```

    average potency per GCD = 458.62119999999993
    average potency per second = 211.151565378



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
      <td>150.000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.000</td>
      <td>430.000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Kasha</td>
      <td></td>
      <td>400.000</td>
      <td>830.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Higanbana</td>
      <td></td>
      <td>240.000</td>
      <td>1070.000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Hakaze</td>
      <td></td>
      <td>175.200</td>
      <td>1245.200</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Jinpu</td>
      <td></td>
      <td>308.980</td>
      <td>1554.180</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Gekko</td>
      <td></td>
      <td>488.980</td>
      <td>2043.160</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Higanbana</td>
      <td></td>
      <td>304.980</td>
      <td>2348.140</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.807</td>
      <td>2582.947</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Shifu</td>
      <td></td>
      <td>384.307</td>
      <td>2967.254</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Kasha</td>
      <td></td>
      <td>522.307</td>
      <td>3489.561</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Fuga</td>
      <td></td>
      <td>407.307</td>
      <td>3896.868</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Mangetsu</td>
      <td></td>
      <td>683.307</td>
      <td>4580.175</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>1180.107</td>
      <td>5760.282</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Fuga</td>
      <td></td>
      <td>407.307</td>
      <td>6167.589</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Mangetsu</td>
      <td></td>
      <td>683.307</td>
      <td>6850.896</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Hakaze</td>
      <td></td>
      <td>234.807</td>
      <td>7085.703</td>
    </tr>
    <tr>
      <th>17</th>
      <td>36.96</td>
      <td>Shifu</td>
      <td></td>
      <td>384.307</td>
      <td>7470.010</td>
    </tr>
    <tr>
      <th>18</th>
      <td>39.12</td>
      <td>Kasha</td>
      <td></td>
      <td>522.307</td>
      <td>7992.317</td>
    </tr>
    <tr>
      <th>19</th>
      <td>41.28</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>1180.107</td>
      <td>9172.424</td>
    </tr>
  </tbody>
</table>
</div>



```python
sam = Samurai()

n_targets = 3

actions = [('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Jinpu'), ('Gekko'), ('Tenka Goken'), ('Hakaze'), 
           ('Shifu'), ('Kasha'), ('Fuga'), ('Mangetsu'), 
           ('Tenka Goken'), ('Hakaze'), ('Shifu'), ('Kasha'), 
           ('Fuga'), ('Mangetsu'), ('Tenka Goken'), ('Hakaze')]
```


```python
df6_aoe_tenka_only, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
display(df6_aoe_tenka_only)
```

    average potency per GCD = 454.34499999999997
    average potency per second = 209.182780847



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
      <td>150.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.0</td>
      <td>430.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Kasha</td>
      <td></td>
      <td>400.0</td>
      <td>830.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Hakaze</td>
      <td></td>
      <td>150.0</td>
      <td>980.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Jinpu</td>
      <td></td>
      <td>280.0</td>
      <td>1260.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Gekko</td>
      <td></td>
      <td>460.0</td>
      <td>1720.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>1117.8</td>
      <td>2837.8</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.5</td>
      <td>3010.3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Shifu</td>
      <td></td>
      <td>322.0</td>
      <td>3332.3</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Kasha</td>
      <td></td>
      <td>460.0</td>
      <td>3792.3</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Fuga</td>
      <td></td>
      <td>345.0</td>
      <td>4137.3</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Mangetsu</td>
      <td></td>
      <td>621.0</td>
      <td>4758.3</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>1117.8</td>
      <td>5876.1</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.5</td>
      <td>6048.6</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Shifu</td>
      <td></td>
      <td>322.0</td>
      <td>6370.6</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Kasha</td>
      <td></td>
      <td>460.0</td>
      <td>6830.6</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Fuga</td>
      <td></td>
      <td>345.0</td>
      <td>7175.6</td>
    </tr>
    <tr>
      <th>17</th>
      <td>36.96</td>
      <td>Mangetsu</td>
      <td></td>
      <td>621.0</td>
      <td>7796.6</td>
    </tr>
    <tr>
      <th>18</th>
      <td>39.12</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>1117.8</td>
      <td>8914.4</td>
    </tr>
    <tr>
      <th>19</th>
      <td>41.28</td>
      <td>Hakaze</td>
      <td></td>
      <td>172.5</td>
      <td>9086.9</td>
    </tr>
  </tbody>
</table>
</div>



```python
compare_potencies([df6_aoe_tenka_only, df6_aoe_higanbana2], ['Tenka Goken only', 'Higanbana two targets first'])
```


![png](output_90_0.png)


They're virtually equal, but applying Higanbana twice takes more time to pay off. Using Tenka Goken only is probably better in most cases. Although the inclusion of the AoE weaponskills will scale better with larger pulls, TP sustainability is a concern. As the number of targets dwindles down to 3, it may be better to favor rotations with single target weaponskills.

<hr width=75%>

Thankfully, level 45 introduces the Oka AoE combo (combo from Fuga). This finisher is equal in potency to the Mangetsu finisher, but similarly to Kasha for single target, opens the Ka Sen instead. This opens the AoE rotation of alternating combos to open Ka and Getsu in order to use Tenka Goken. While this is definitely TP unfriendly, it should scale very well with mob size.


```python
dfs_aoe2 = []
pps_aoe2 = []
labels = []

n_target_range = range(2, 8)

for n_targets in n_target_range:
    sam = Samurai()
    
    actions = [('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
               ('Jinpu'), ('Gekko'), ('Tenka Goken'), ('Fuga'),
               ('Oka'), ('Fuga'), ('Mangetsu'), ('Tenka Goken'), 
               ('Fuga'), ('Mangetsu'), ('Fuga'), ('Oka'), 
               ('Tenka Goken')]
    
    print('number of targets = %s' % n_targets)
    df_temp, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
    dfs_aoe2.append(df_temp)
    pps_aoe2.append(pps)
    
    labels.append('%s targets' % n_targets)
    print('\n')
```

    number of targets = 2
    average potency per GCD = 396.92941176470583
    average potency per second = 182.57034632
    
    
    number of targets = 3
    average potency per GCD = 525.7294117647059
    average potency per second = 241.812770563
    
    
    number of targets = 4
    average potency per GCD = 641.8117647058824
    average potency per second = 295.205627706
    
    
    number of targets = 5
    average potency per GCD = 745.1764705882352
    average potency per second = 342.748917749
    
    
    number of targets = 6
    average potency per GCD = 835.8235294117648
    average potency per second = 384.442640693
    
    
    number of targets = 7
    average potency per GCD = 926.4705882352941
    average potency per second = 426.136363636
    
    



```python
compare_n_potencies(dfs_aoe2, labels)
```


![png](output_95_0.png)



```python
fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, figsize=(12,4))
fig.tight_layout(pad=2)

axes.plot(n_target_range, pps_aoe2, '-o', label='Mangetsu, Oka, and Tenka Goken')
axes.plot(n_target_range, pps_higanbana, '-^', label='Mangetsu and Higanbana only')
axes.plot(n_target_range, pps_no_higanbana, ':^', label='Mangetsu only')
axes.set_ylabel('Potency per second')
axes.set_xlabel('Number of Targets')
axes.legend(loc='upper left', framealpha=0.5)

fig.suptitle('Average Potency per second')
```




    <matplotlib.text.Text at 0x11084fe48>




![png](output_96_1.png)


At 3 targets, the potency of a full duration Higanbana is comparable to Tenka Goken, so applying Higanbana to some targets has merit (especially due to its 1 Sen cost). However, the AoE-centric rotation scales exceptionally well as pull size passes 3. The ability to open up Getsu and Ka with only four GCDs allowing for more frequent Tenka Goken casts facilitates that.

For a pull size of three:


```python
sam = Samurai()

n_targets = 3
    
actions = [('Hakaze'), ('Shifu'), ('Kasha'), ('Higanbana'),
           ('Hakaze'), ('Jinpu'), ('Gekko'), ('Higanbana'),
           ('Fuga'), ('Oka'), ('Fuga'), ('Mangetsu'), 
           ('Tenka Goken'), ('Fuga'), ('Mangetsu'), ('Fuga'), 
           ('Oka'), ('Tenka Goken')]
```


```python
df7_3, average_potency, pps = sam.parse_rotation(actions, n_targets=n_targets)
display(df7_3)
```

    average potency per GCD = 503.93388888888876
    average potency per second = 231.871421268



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
      <td>150.000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.000</td>
      <td>430.000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Kasha</td>
      <td></td>
      <td>400.000</td>
      <td>830.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Higanbana</td>
      <td></td>
      <td>240.000</td>
      <td>1070.000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Hakaze</td>
      <td></td>
      <td>175.200</td>
      <td>1245.200</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Jinpu</td>
      <td></td>
      <td>308.980</td>
      <td>1554.180</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Gekko</td>
      <td></td>
      <td>488.980</td>
      <td>2043.160</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Higanbana</td>
      <td></td>
      <td>304.980</td>
      <td>2348.140</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Fuga</td>
      <td></td>
      <td>407.307</td>
      <td>2755.447</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Oka</td>
      <td></td>
      <td>683.307</td>
      <td>3438.754</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Fuga</td>
      <td></td>
      <td>407.307</td>
      <td>3846.061</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Mangetsu</td>
      <td></td>
      <td>683.307</td>
      <td>4529.368</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>1180.107</td>
      <td>5709.475</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Fuga</td>
      <td></td>
      <td>407.307</td>
      <td>6116.782</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Mangetsu</td>
      <td></td>
      <td>683.307</td>
      <td>6800.089</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Fuga</td>
      <td></td>
      <td>407.307</td>
      <td>7207.396</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Oka</td>
      <td></td>
      <td>683.307</td>
      <td>7890.703</td>
    </tr>
    <tr>
      <th>17</th>
      <td>36.96</td>
      <td>Tenka Goken</td>
      <td></td>
      <td>1180.107</td>
      <td>9070.810</td>
    </tr>
  </tbody>
</table>
</div>



```python
compare_potencies([df7_3, dfs_aoe2[1]], labels=['Higanbana two first', 'Tenka Goken only'])
```


![png](output_101_0.png)


Once again, Higanbana takes some time to pay off. For pulls reaching the 60 second mark, it may be optimal, especially if we consider that targets start to die, reducing the advantage of Tenka Goken only.

### Priority: Shifu > Jinpu and Higanbana > Tenka Goken

### Filler: Alternate Kasha and Gekko combos to maintain buffs and enable Tenka Goken

### AoE: Buff first Shifu > Jinpu. Mangetsu combo, Oka combo if available, otherwise Kasha combo. For packs of 3, apply Higanbana to 1-2 sturdy targets before building for Tenka Goken if pulls approach 60 seconds in duration. For larger packs, use Tenka Goken only. Shift to single target weaponskills if TP is scarce but prioritize Iaijutsu as described.

Up to this point, Samurai has no abilities or offensive cooldowns that are used in its regular rotation, save for Ageha. The main themes are always keeping buffs up and making use of Iaijutsu as regularly as you can. Samurai has strong AoE although it is expensive to use. From level 50 going forward, Samurai picks up all of its abilities and at level 52, the Kenki gauge and Hissatsu abilities start to be introduced. Once you master the weaponskill rotation that is completed at level 50, you will need to start learning to manage Kenki and use the Kenki spenders efficiently to become a good samurai.


```python

```
