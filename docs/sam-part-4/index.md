
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

These last nine levels are truly the formative levels for Samurai. They add the fundamental traits and actions that give the job its complexity. Up to this point, most decision making was obvious and any alternate decision paths often led to virtually indistinguishable results under ideal conditions. The Kenki mechanic was relatively low pressure decision-making as it accumulated slowly and the choices for its spenders were rather limited. We'll see how this changes rapidly over the final leveling stretch.

## lvl 62-67

Level 62 is indeed a gamechanger. The trait Kenki Mastery II adds a Kenki bonus to almost every weaponskill (barring Iaijutsu), significantly increasing our Kenki accrual rate to 10 for combo finishers plus 5 for non finishers, or a net 55 Kenki per 8 GCD rotation (going through all Sen combos). This will net a substantial surplus if we reserve Kenki solely for Hissatsu: Kaiten -> Midare Setsugekka. Level 62 also grants the ability Hissatsu: Shinten, dealing 300 potency off the GCD at a cost of 25 Kenki on a 1s recast. This is significantly more value than spending on Hissatsu: Kaiten on Kasha/Gekko and only ~16.6% less value than spending Hissatsu: Kaiten on Midare Setsugekka (300 potency vs. 360 potency gain per 25 Kenki vs. 20 Kenki, respectively). In terms of potency per Kenki, it's 12 vs. 18 in favor of Hissatsu: Kaiten on Midare Setsugeka. Needless to say, if we're not saving for Hissatsu: Kaiten on Midare Setsugekka or for utility, we spend Kenki on Hissatsu: Shinten.

Level 66 grants the Starry Eyes ability... depending on its potency and Kenki cost, it may not be worth using at all when Hissatsu: Shinten is an option. On the other hand, if it does become worth it, it might encourage you to take damage so that you can use Third Eye and Starry Eyes...

With the increased Kenki generation, let's revisit our single target situations with the expectation of capping Kenki very early on.

### Example Hissatsu usage with Opener 1


```python
sam = Samurai(kenki_mastery=True)

actions = [('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Jinpu'), ('Higanbana'), ('Gekko'), ('Hakaze'),
           ('Yukikaze'), ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka', 'Meikyo Shisui'), ('Gekko'), ('Yukikaze'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'), ('Hakaze'), ('Jinpu'), ('Gekko'),
           ('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Yukikaze', 'Hissatsu: Kaiten'), ('Midare Setsugekka'), ('Hakaze'),
           ('Jinpu'), ('Gekko'), ('Hakaze'), ('Shifu'),
           ('Higanbana'), ('Kasha'), ('Hakaze'), ('Yukikaze'),
           ('Hakaze'), ('Jinpu'), ('Gekko', 'Hissatsu: Kaiten'), ('Midare Setsugekka'),
           ('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Jinpu'), ('Gekko'), ('Hakaze'), ('Yukikaze', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'), ('Hakaze'), ('Shifu'), ('Kasha'),
           ('Hakaze'), ('Jinpu'), ('Gekko'), ('Hakaze'),
           ('Yukikaze', 'Hissatsu: Kaiten'), ('Midare Setsugekka', 'Meikyo Shisui'), ('Kasha'), ('Gekko'),
           ('Yukikaze', 'Hissatsu: Kaiten'), ('Midare Setsugekka'), ('Hakaze'), ('Shifu'), 
           ('Kasha'), ('Higanbana')]
```


```python
df0, average_potency, pps = sam.parse_rotation(actions)
display(df0)
```

    average potency per GCD = 487.523430769
    average potency per second = 225.320129408
    


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
      <td></td>
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
      <td>276.000</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>30</td>
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
      <td>30</td>
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
      <td>40</td>
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
      <td>45</td>
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
      <td>55</td>
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
      <td>60</td>
      <td>3275.030</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Kasha</td>
      <td>Hissatsu: Kaiten</td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>3818.957</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Midare Setsugekka</td>
      <td>Meikyo Shisui</td>
      <td>1411.947</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>55</td>
      <td>5230.904</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Gekko</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>55</td>
      <td>5774.831</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Yukikaze</td>
      <td></td>
      <td>467.337</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>6242.168</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Kasha</td>
      <td>Hissatsu: Kaiten</td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>6786.095</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1411.947</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>8198.042</td>
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
      <td>65</td>
      <td>8422.844</td>
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
      <td>70</td>
      <td>8813.591</td>
    </tr>
    <tr>
      <th>19</th>
      <td>41.28</td>
      <td>Gekko</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>9357.518</td>
    </tr>
    <tr>
      <th>20</th>
      <td>43.44</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>85</td>
      <td>9582.320</td>
    </tr>
    <tr>
      <th>21</th>
      <td>45.60</td>
      <td>Shifu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>90</td>
      <td>9973.067</td>
    </tr>
    <tr>
      <th>22</th>
      <td>47.76</td>
      <td>Kasha</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>95</td>
      <td>10516.994</td>
    </tr>
    <tr>
      <th>23</th>
      <td>49.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>10741.796</td>
    </tr>
    <tr>
      <th>24</th>
      <td>52.08</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Kaiten</td>
      <td>467.337</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>11209.133</td>
    </tr>
    <tr>
      <th>25</th>
      <td>54.24</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1411.947</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>12621.080</td>
    </tr>
    <tr>
      <th>26</th>
      <td>56.40</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>12845.882</td>
    </tr>
    <tr>
      <th>27</th>
      <td>58.56</td>
      <td>Jinpu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>85</td>
      <td>13236.629</td>
    </tr>
    <tr>
      <th>28</th>
      <td>60.72</td>
      <td>Gekko</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>90</td>
      <td>13780.556</td>
    </tr>
    <tr>
      <th>29</th>
      <td>62.88</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>14005.358</td>
    </tr>
    <tr>
      <th>30</th>
      <td>65.04</td>
      <td>Shifu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>14396.105</td>
    </tr>
    <tr>
      <th>31</th>
      <td>67.20</td>
      <td>Higanbana</td>
      <td></td>
      <td>339.687</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>14735.792</td>
    </tr>
    <tr>
      <th>32</th>
      <td>69.36</td>
      <td>Kasha</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>15279.719</td>
    </tr>
    <tr>
      <th>33</th>
      <td>71.52</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>15504.521</td>
    </tr>
    <tr>
      <th>34</th>
      <td>73.68</td>
      <td>Yukikaze</td>
      <td></td>
      <td>467.337</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>15971.858</td>
    </tr>
    <tr>
      <th>35</th>
      <td>75.84</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>16196.660</td>
    </tr>
    <tr>
      <th>36</th>
      <td>78.00</td>
      <td>Jinpu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>16587.407</td>
    </tr>
    <tr>
      <th>37</th>
      <td>80.16</td>
      <td>Gekko</td>
      <td>Hissatsu: Kaiten</td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>17131.334</td>
    </tr>
    <tr>
      <th>38</th>
      <td>82.32</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1411.947</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>18543.281</td>
    </tr>
    <tr>
      <th>39</th>
      <td>84.48</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>18768.083</td>
    </tr>
    <tr>
      <th>40</th>
      <td>86.64</td>
      <td>Shifu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>85</td>
      <td>19158.830</td>
    </tr>
    <tr>
      <th>41</th>
      <td>88.80</td>
      <td>Kasha</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>90</td>
      <td>19702.757</td>
    </tr>
    <tr>
      <th>42</th>
      <td>90.96</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>19927.559</td>
    </tr>
    <tr>
      <th>43</th>
      <td>93.12</td>
      <td>Jinpu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>20318.306</td>
    </tr>
    <tr>
      <th>44</th>
      <td>95.28</td>
      <td>Gekko</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>20862.233</td>
    </tr>
    <tr>
      <th>45</th>
      <td>97.44</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>21087.035</td>
    </tr>
    <tr>
      <th>46</th>
      <td>99.60</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Kaiten</td>
      <td>467.337</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>21554.372</td>
    </tr>
    <tr>
      <th>47</th>
      <td>101.76</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1411.947</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>22966.319</td>
    </tr>
    <tr>
      <th>48</th>
      <td>103.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>23191.121</td>
    </tr>
    <tr>
      <th>49</th>
      <td>106.08</td>
      <td>Shifu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>85</td>
      <td>23581.868</td>
    </tr>
    <tr>
      <th>50</th>
      <td>108.24</td>
      <td>Kasha</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>90</td>
      <td>24125.795</td>
    </tr>
    <tr>
      <th>51</th>
      <td>110.40</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>24350.597</td>
    </tr>
    <tr>
      <th>52</th>
      <td>112.56</td>
      <td>Jinpu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>24741.344</td>
    </tr>
    <tr>
      <th>53</th>
      <td>114.72</td>
      <td>Gekko</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>25285.271</td>
    </tr>
    <tr>
      <th>54</th>
      <td>116.88</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>25510.073</td>
    </tr>
    <tr>
      <th>55</th>
      <td>119.04</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Kaiten</td>
      <td>467.337</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>25977.410</td>
    </tr>
    <tr>
      <th>56</th>
      <td>121.20</td>
      <td>Midare Setsugekka</td>
      <td>Meikyo Shisui</td>
      <td>1411.947</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>27389.357</td>
    </tr>
    <tr>
      <th>57</th>
      <td>123.36</td>
      <td>Kasha</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>27933.284</td>
    </tr>
    <tr>
      <th>58</th>
      <td>125.52</td>
      <td>Gekko</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>90</td>
      <td>28477.211</td>
    </tr>
    <tr>
      <th>59</th>
      <td>127.68</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Kaiten</td>
      <td>467.337</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>100</td>
      <td>28944.548</td>
    </tr>
    <tr>
      <th>60</th>
      <td>129.84</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1378.620</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>80</td>
      <td>30323.168</td>
    </tr>
    <tr>
      <th>61</th>
      <td>132.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>191.475</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>80</td>
      <td>30514.643</td>
    </tr>
    <tr>
      <th>62</th>
      <td>134.16</td>
      <td>Shifu</td>
      <td></td>
      <td>357.420</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>85</td>
      <td>30872.063</td>
    </tr>
    <tr>
      <th>63</th>
      <td>136.32</td>
      <td>Kasha</td>
      <td></td>
      <td>510.600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>90</td>
      <td>31382.663</td>
    </tr>
    <tr>
      <th>64</th>
      <td>138.48</td>
      <td>Higanbana</td>
      <td></td>
      <td>306.360</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>100</td>
      <td>31689.023</td>
    </tr>
  </tbody>
</table>
</div>


As you can see, we capped Kenki less than a minute into the encounter. Let's add in Hissatsu: Shinten to dump some Kenki.


```python
sam = Samurai(kenki_mastery=True)

actions = [('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Jinpu'), ('Higanbana'), ('Gekko'), ('Hakaze'),
           ('Yukikaze'), ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka', 'Meikyo Shisui'), ('Gekko'), ('Yukikaze'), ('Kasha', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'), ('Hakaze'), ('Jinpu'), ('Gekko', 'Hissatsu: Shinten'),
           ('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Yukikaze', 'Hissatsu: Kaiten'), ('Midare Setsugekka'), ('Hakaze'),
           ('Jinpu'), ('Gekko', 'Hissatsu: Shinten'), ('Hakaze'), ('Shifu'),
           ('Higanbana'), ('Kasha', 'Hissatsu: Shinten'), ('Hakaze'), ('Yukikaze'),
           ('Hakaze'), ('Jinpu', 'Hissatsu: Shinten'), ('Gekko', 'Hissatsu: Kaiten'), ('Midare Setsugekka'),
           ('Hakaze'), ('Shifu'), ('Kasha'), ('Hakaze'),
           ('Jinpu', 'Hissatsu: Shinten'), ('Gekko'), ('Hakaze'), ('Yukikaze', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'), ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Shinten'),
           ('Hakaze'), ('Jinpu'), ('Gekko', 'Hissatsu: Shinten'), ('Hakaze'),
           ('Yukikaze', 'Hissatsu: Kaiten'), ('Midare Setsugekka', 'Meikyo Shisui'), ('Kasha'), ('Gekko', 'Hissatsu: Shinten'),
           ('Yukikaze', 'Hissatsu: Kaiten'), ('Midare Setsugekka'), ('Hakaze', 'Hissatsu: Shinten'), ('Shifu'), 
           ('Kasha', 'Hissatsu: Shinten'), ('Higanbana')]
```


```python
df1, average_potency, pps = sam.parse_rotation(actions)
display(df1)
```

    average potency per GCD = 546.438815385
    average potency per second = 252.549224972
    


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
      <td></td>
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
      <td>276.000</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>30</td>
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
      <td>30</td>
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
      <td>40</td>
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
      <td>45</td>
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
      <td>55</td>
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
      <td>60</td>
      <td>3275.030</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Kasha</td>
      <td>Hissatsu: Kaiten</td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>3818.957</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Midare Setsugekka</td>
      <td>Meikyo Shisui</td>
      <td>1411.947</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>55</td>
      <td>5230.904</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Gekko</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>55</td>
      <td>5774.831</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Yukikaze</td>
      <td></td>
      <td>467.337</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>6242.168</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Kasha</td>
      <td>Hissatsu: Kaiten</td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>6786.095</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1411.947</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>8198.042</td>
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
      <td>65</td>
      <td>8422.844</td>
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
      <td>70</td>
      <td>8813.591</td>
    </tr>
    <tr>
      <th>19</th>
      <td>41.28</td>
      <td>Gekko</td>
      <td>Hissatsu: Shinten</td>
      <td>926.877</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>9740.468</td>
    </tr>
    <tr>
      <th>20</th>
      <td>43.44</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>60</td>
      <td>9965.270</td>
    </tr>
    <tr>
      <th>21</th>
      <td>45.60</td>
      <td>Shifu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>10356.017</td>
    </tr>
    <tr>
      <th>22</th>
      <td>47.76</td>
      <td>Kasha</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>70</td>
      <td>10899.944</td>
    </tr>
    <tr>
      <th>23</th>
      <td>49.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>11124.746</td>
    </tr>
    <tr>
      <th>24</th>
      <td>52.08</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Kaiten</td>
      <td>467.337</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>85</td>
      <td>11592.083</td>
    </tr>
    <tr>
      <th>25</th>
      <td>54.24</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1411.947</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>13004.030</td>
    </tr>
    <tr>
      <th>26</th>
      <td>56.40</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>13228.832</td>
    </tr>
    <tr>
      <th>27</th>
      <td>58.56</td>
      <td>Jinpu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>13619.579</td>
    </tr>
    <tr>
      <th>28</th>
      <td>60.72</td>
      <td>Gekko</td>
      <td>Hissatsu: Shinten</td>
      <td>926.877</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>85</td>
      <td>14546.456</td>
    </tr>
    <tr>
      <th>29</th>
      <td>62.88</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>70</td>
      <td>14771.258</td>
    </tr>
    <tr>
      <th>30</th>
      <td>65.04</td>
      <td>Shifu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>15162.005</td>
    </tr>
    <tr>
      <th>31</th>
      <td>67.20</td>
      <td>Higanbana</td>
      <td></td>
      <td>339.687</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>15501.692</td>
    </tr>
    <tr>
      <th>32</th>
      <td>69.36</td>
      <td>Kasha</td>
      <td>Hissatsu: Shinten</td>
      <td>926.877</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>16428.569</td>
    </tr>
    <tr>
      <th>33</th>
      <td>71.52</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>16653.371</td>
    </tr>
    <tr>
      <th>34</th>
      <td>73.68</td>
      <td>Yukikaze</td>
      <td></td>
      <td>467.337</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>70</td>
      <td>17120.708</td>
    </tr>
    <tr>
      <th>35</th>
      <td>75.84</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>17345.510</td>
    </tr>
    <tr>
      <th>36</th>
      <td>78.00</td>
      <td>Jinpu</td>
      <td>Hissatsu: Shinten</td>
      <td>773.697</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>85</td>
      <td>18119.207</td>
    </tr>
    <tr>
      <th>37</th>
      <td>80.16</td>
      <td>Gekko</td>
      <td>Hissatsu: Kaiten</td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>18663.134</td>
    </tr>
    <tr>
      <th>38</th>
      <td>82.32</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1411.947</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>55</td>
      <td>20075.081</td>
    </tr>
    <tr>
      <th>39</th>
      <td>84.48</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>55</td>
      <td>20299.883</td>
    </tr>
    <tr>
      <th>40</th>
      <td>86.64</td>
      <td>Shifu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>60</td>
      <td>20690.630</td>
    </tr>
    <tr>
      <th>41</th>
      <td>88.80</td>
      <td>Kasha</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>21234.557</td>
    </tr>
    <tr>
      <th>42</th>
      <td>90.96</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>21459.359</td>
    </tr>
    <tr>
      <th>43</th>
      <td>93.12</td>
      <td>Jinpu</td>
      <td>Hissatsu: Shinten</td>
      <td>773.697</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>22233.056</td>
    </tr>
    <tr>
      <th>44</th>
      <td>95.28</td>
      <td>Gekko</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>60</td>
      <td>22776.983</td>
    </tr>
    <tr>
      <th>45</th>
      <td>97.44</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>70</td>
      <td>23001.785</td>
    </tr>
    <tr>
      <th>46</th>
      <td>99.60</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Kaiten</td>
      <td>467.337</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>23469.122</td>
    </tr>
    <tr>
      <th>47</th>
      <td>101.76</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1411.947</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>24881.069</td>
    </tr>
    <tr>
      <th>48</th>
      <td>103.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>25105.871</td>
    </tr>
    <tr>
      <th>49</th>
      <td>106.08</td>
      <td>Shifu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>70</td>
      <td>25496.618</td>
    </tr>
    <tr>
      <th>50</th>
      <td>108.24</td>
      <td>Kasha</td>
      <td>Hissatsu: Shinten</td>
      <td>926.877</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>26423.495</td>
    </tr>
    <tr>
      <th>51</th>
      <td>110.40</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>60</td>
      <td>26648.297</td>
    </tr>
    <tr>
      <th>52</th>
      <td>112.56</td>
      <td>Jinpu</td>
      <td></td>
      <td>390.747</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>27039.044</td>
    </tr>
    <tr>
      <th>53</th>
      <td>114.72</td>
      <td>Gekko</td>
      <td>Hissatsu: Shinten</td>
      <td>926.877</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>70</td>
      <td>27965.921</td>
    </tr>
    <tr>
      <th>54</th>
      <td>116.88</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.802</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>55</td>
      <td>28190.723</td>
    </tr>
    <tr>
      <th>55</th>
      <td>119.04</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Kaiten</td>
      <td>467.337</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>60</td>
      <td>28658.060</td>
    </tr>
    <tr>
      <th>56</th>
      <td>121.20</td>
      <td>Midare Setsugekka</td>
      <td>Meikyo Shisui</td>
      <td>1411.947</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>50</td>
      <td>30070.007</td>
    </tr>
    <tr>
      <th>57</th>
      <td>123.36</td>
      <td>Kasha</td>
      <td></td>
      <td>543.927</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>50</td>
      <td>30613.934</td>
    </tr>
    <tr>
      <th>58</th>
      <td>125.52</td>
      <td>Gekko</td>
      <td>Hissatsu: Shinten</td>
      <td>926.877</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>60</td>
      <td>31540.811</td>
    </tr>
    <tr>
      <th>59</th>
      <td>127.68</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Kaiten</td>
      <td>467.337</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>45</td>
      <td>32008.148</td>
    </tr>
    <tr>
      <th>60</th>
      <td>129.84</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1378.620</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>35</td>
      <td>33386.768</td>
    </tr>
    <tr>
      <th>61</th>
      <td>132.00</td>
      <td>Hakaze</td>
      <td>Hissatsu: Shinten</td>
      <td>574.425</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>35</td>
      <td>33961.193</td>
    </tr>
    <tr>
      <th>62</th>
      <td>134.16</td>
      <td>Shifu</td>
      <td></td>
      <td>357.420</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>15</td>
      <td>34318.613</td>
    </tr>
    <tr>
      <th>63</th>
      <td>136.32</td>
      <td>Kasha</td>
      <td>Hissatsu: Shinten</td>
      <td>893.550</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>20</td>
      <td>35212.163</td>
    </tr>
    <tr>
      <th>64</th>
      <td>138.48</td>
      <td>Higanbana</td>
      <td></td>
      <td>306.360</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>5</td>
      <td>35518.523</td>
    </tr>
  </tbody>
</table>
</div>


Here I made the conscious effort to try to spend all the Kenki generated by the end. I haphazardly inserted Hissatsu: Shinten throughout whenever I was exceeding about 75 Kenki or so. In a vacuum, we have this flexibility of spending Kenki whenever especially with the 1s recast time on Hissatsu: Shinten. We could even use it every GCD for increased burst provided we have enough Kenki. 

Although a fairer comparison would have been to spend all the Kenki on Hissatsu: Kaiten for the first example, we observe a roughly 10% increase in potency per second from level 61 to level 62 just by acquiring Kenki Mastery II and Hissatsu: Shinten.


```python
compare_potencies([df0, df1], ['lvl 52-61 rotation', 'lvl 62-67 rotation'])
```


![png](output_14_0.png)


The first 50 seconds or so are identical because I made the decision to not use Hissatsu: Shinten until I nearly capped on Kenki. Again, depending on encounter and party specifics, you may place your Shinten better; this freedom is facilitated by the flexibility of the Kenki gauge system.

### Example Hissatsu usage with AoE rotations

Hissatsu: Kyuten is learned at level 64 and is the AoE analog of Hissatsu: Shinten, matching it in potency at two targets. However, its value needs to be compared to spending Hissatsu: Kaiten on Tenka Goken. Hissatsu: Kyuten does 150 potency to all targets without AoE downscaling at the cost of 25 Kenki whereas Hissatsu: Kaiten increases the potency of the next weaponskill, in our case Tenka Goken, by 50% at the cost of 20 Kenki. Additionally, Tenka Goken experiences decreased potency per target as target numbers goes up. Let's see each compares as a function of number of targets.


```python
dfs_aoe_kaiten_only = []
pps_aoe_kaiten_only = []
labels = []

n_target_range = range(2, 8)

for n_targets in n_target_range:
    sam = Samurai(kenki_mastery=True, kenki_gauge=50)
    
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
      <td>Hissatsu: Kaiten</td>
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
      <td>Hissatsu: Kaiten</td>
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
      <td>Hissatsu: Kaiten</td>
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


![png](output_19_0.png)



```python
dfs_aoe_kyuten_only = []
pps_aoe_kyuten_only = []
labels = []

n_target_range = range(2, 8)

for n_targets in n_target_range:
    sam = Samurai(kenki_mastery=True, kenki_gauge=50)
    
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
      <td>Hissatsu: Kyuten</td>
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
      <td>Hissatsu: Kyuten</td>
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
      <td>Hissatsu: Kyuten</td>
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
      <td>Hissatsu: Kyuten</td>
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
      <td>Hissatsu: Kyuten</td>
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


![png](output_21_0.png)


Now it would be downright wasteful to use Kenki on Hissatsu: Kaiten with Tenka Goken exclusively as we have a net surplus of Kenki so let's fill in the gaps with Hissatsu: Kyuten.


```python
dfs_aoe_both = []
pps_aoe_both = []
labels = []

n_target_range = range(2, 8)

for n_targets in n_target_range:
    sam = Samurai(kenki_mastery=True, kenki_gauge=50)
    
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
      <td>Hissatsu: Kyuten</td>
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
      <td>Hissatsu: Kaiten</td>
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
      <td>Hissatsu: Kyuten</td>
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
      <td>Hissatsu: Kaiten</td>
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
      <td>Hissatsu: Kyuten</td>
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
      <td>Hissatsu: Kaiten</td>
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


![png](output_24_0.png)



```python
potency_one_tenka = []
labels = []

n_target_range = range(2, 8)

for n_targets in n_target_range:
    sam = Samurai(kenki_mastery=True, kenki_gauge=50)
    sam.has_getsu = True
    sam.has_ka = True
    sam.has_hissatsu_kaiten = True
    
    df, _, _ = sam.parse_rotation([('Tenka Goken')], n_targets=n_targets)
    
    potency_one_tenka.append(df['Potency']/20)
```

    average potency per GCD = 1026.0
    average potency per second = 427.5
    average potency per GCD = 1458.0
    average potency per second = 607.5
    average potency per GCD = 1836.0
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




    <matplotlib.text.Text at 0xe111198>




![png](output_26_1.png)


Expending Kenki on Hissatsu: Kaiten for Tenka Goken is the best bang for your buck, no question. When you only have enough Kenki for Hissatsu: Kaiten or Hissatsu: Kyuten, choose Hissatsu: Kaiten, hands down.

However, as we saw in the two previous examples, using Kenki exclusively on Hissatsu: Kyuten is extremely competitive with using Kenki on both. Additionally, it is superior to using Hissatsu: Kaiten exclusively. We can credit this to the minimal prerequisites for using Hissatsu: Kyuten; even though it costs more Kenki, you do not have to build Sen to use it, unlike Tenka Goken (with Hissatsu: Kaiten).

## Level 68-70

Level 68 is a pivotal shift in how Samurai plays. It grants you Hagakure, an ability on a short 40s that converts open Sen to Kenki at a 1 to 20 rate. Initially, this came as a headscratcher to many folks: why would I want to sacrifice muh Iaijutsu? Samurai post-50 has grown to be driven by Kenki more than Sen. The addition of powerful Kenki spenders like Hissatsu: Shinten and the level 70 capstone Hissatsu: Guren add significant potency to the Samurai rotation off the GCD. Iaijutsu, while powerful in their own right, "cost" a GCD and delay Kenki generation from the other weaponskills.

Consider Midare Setsugekka. At the cost of three Sen, it deals 720 potency unbuffed. If instead of using those three Sen on Iaijutsu, what if we used Hagakure to generate $3*20=60$ Kenki?

We could spend it on...
- Hissatsu: Guren, for 800+ potency for 50 Kenki.
- Hissatsu: Shinten (x2.4), for 720 potency for 60 Kenki.
- Hissatsu: Kyuten (x2.4), for burst AoE opportunities with even better payoff than Hissatsu: Shinten.

For the three Sen to Kenki conversion rate, we at least get our potency back if we spend on Hissatsu: Shinten exclusively. However, this payoff comes with the bonus of not requiring the GCD and cast time of Midare Setsugekka and letting us continue our weaponskill rotation sooner. A small gain is still a gain.

Hagakure obviously opens up a ton of opportunities. With its 40s recast time and Meikyo Shisui's 80s recast time, maybe there's some synergy there. Let's briefly explore some use cases of Hagakure. We'll delve into opener analysis and other advanced topics in the next section.

### Example Hagakure usage


```python
sam = Samurai(kenki_mastery=True)

n_targets = 1

actions = [('Hakaze'), ('Shifu'), ('Kasha', 'Meikyo Shisui'), ('Jinpu'),
           ('Yukikaze', 'Hissatsu: Shinten'), ('Gekko', 'Hagakure'), ('Hakaze', 'Hissatsu: Guren'), ('Shifu', 'Hissatsu: Shinten'),
           ('Kasha', 'Hissatsu: Shinten'), ('Higanbana'), ('Hakaze'), ('Jinpu'),
           ('Gekko'), ('Hakaze'), ('Yukikaze'), ('Hakaze'),
           ('Shifu'), ('Kasha', 'Hissatsu: Kaiten'), ('Midare Setsugekka'), ('Hakaze', 'Hissatsu: Shinten'),
           ('Jinpu'), ('Gekko'), ('Hakaze', 'Hissatsu: Shinten'), ('Yukikaze'),
           ('Hakaze', 'Hissatsu: Shinten'), ('Shifu'), ('Kasha', 'Hagakure'), ('Hakaze', 'Hissatsu: Shinten'),
           ('Jinpu', 'Hissatsu: Shinten'), ('Gekko', 'Hissatsu: Shinten'), ('Hakaze'), ('Yukikaze'),
           ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Kaiten'), ('Midare Setsugekka'),
           ('Hakaze'), ('Jinpu', 'Hissatsu: Shinten'), ('Gekko', 'Hissatsu: Shinten'), ('Higanbana', 'Meikyo Shisui'),
           ('Kasha'), ('Gekko'), ('Yukikaze', 'Hissatsu: Kaiten'), ('Hakaze'),
           ('Shifu', 'Hagakure'), ('Kasha', 'Hissatsu: Shinten'), ('Hakaze'), ('Yukikaze', 'Hissatsu: Shinten'),
           ('Hakaze'), ('Jinpu'), ('Gekko', 'Hissatsu: Kaiten'), ('Midare Setsugekka'),
           ('Hakaze'), ('Shifu'), ('Kasha', 'Hissatsu: Shinten'), ('Hakaze'),
           ('Yukikaze'), ('Hakaze'), ('Jinpu'), ('Gekko', 'Hissatsu: Kaiten'),
           ('Midare Setsugekka'), ('Hakaze'), ('Shifu', 'Hissatsu: Guren'), ('Kasha', 'Hissatsu: Shinten'),
           ('Hakaze')]
```


```python
df2, average_potency, pps = sam.parse_rotation(actions)
display(df2)
```

    average potency per GCD = 559.000976923
    average potency per second = 258.355115899
    


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
      <td>150.0000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>0</td>
      <td>150.0000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.40</td>
      <td>Shifu</td>
      <td></td>
      <td>280.0000</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>0</td>
      <td>5</td>
      <td>430.0000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.56</td>
      <td>Kasha</td>
      <td>Meikyo Shisui</td>
      <td>400.0000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>10</td>
      <td>830.0000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.72</td>
      <td>Jinpu</td>
      <td></td>
      <td>280.0000</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>20</td>
      <td>1110.0000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8.88</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Shinten</td>
      <td>773.9500</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>0</td>
      <td>25</td>
      <td>1883.9500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11.04</td>
      <td>Gekko</td>
      <td>Hagakure</td>
      <td>510.6000</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>10</td>
      <td>2394.5500</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13.20</td>
      <td>Hakaze</td>
      <td>Hissatsu: Guren</td>
      <td>1212.6750</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>80</td>
      <td>3607.2250</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.36</td>
      <td>Shifu</td>
      <td>Hissatsu: Shinten</td>
      <td>740.3700</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>35</td>
      <td>4347.5950</td>
    </tr>
    <tr>
      <th>8</th>
      <td>17.52</td>
      <td>Kasha</td>
      <td>Hissatsu: Shinten</td>
      <td>893.5500</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>15</td>
      <td>5241.1450</td>
    </tr>
    <tr>
      <th>9</th>
      <td>19.68</td>
      <td>Higanbana</td>
      <td></td>
      <td>306.3600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>0</td>
      <td>5547.5050</td>
    </tr>
    <tr>
      <th>10</th>
      <td>21.84</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.8020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>0</td>
      <td>5772.3070</td>
    </tr>
    <tr>
      <th>11</th>
      <td>24.00</td>
      <td>Jinpu</td>
      <td></td>
      <td>390.7470</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5</td>
      <td>6163.0540</td>
    </tr>
    <tr>
      <th>12</th>
      <td>26.16</td>
      <td>Gekko</td>
      <td></td>
      <td>543.9270</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10</td>
      <td>6706.9810</td>
    </tr>
    <tr>
      <th>13</th>
      <td>28.32</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.8020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>6931.7830</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30.48</td>
      <td>Yukikaze</td>
      <td></td>
      <td>467.3370</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>25</td>
      <td>7399.1200</td>
    </tr>
    <tr>
      <th>15</th>
      <td>32.64</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.8020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>7623.9220</td>
    </tr>
    <tr>
      <th>16</th>
      <td>34.80</td>
      <td>Shifu</td>
      <td></td>
      <td>390.7470</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>40</td>
      <td>8014.6690</td>
    </tr>
    <tr>
      <th>17</th>
      <td>36.96</td>
      <td>Kasha</td>
      <td>Hissatsu: Kaiten</td>
      <td>543.9270</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>45</td>
      <td>8558.5960</td>
    </tr>
    <tr>
      <th>18</th>
      <td>39.12</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1411.9470</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>9970.5430</td>
    </tr>
    <tr>
      <th>19</th>
      <td>41.28</td>
      <td>Hakaze</td>
      <td>Hissatsu: Shinten</td>
      <td>607.7520</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>10578.2950</td>
    </tr>
    <tr>
      <th>20</th>
      <td>43.44</td>
      <td>Jinpu</td>
      <td></td>
      <td>390.7470</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>10969.0420</td>
    </tr>
    <tr>
      <th>21</th>
      <td>45.60</td>
      <td>Gekko</td>
      <td></td>
      <td>543.9270</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>11512.9690</td>
    </tr>
    <tr>
      <th>22</th>
      <td>47.76</td>
      <td>Hakaze</td>
      <td>Hissatsu: Shinten</td>
      <td>607.7520</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>30</td>
      <td>12120.7210</td>
    </tr>
    <tr>
      <th>23</th>
      <td>49.92</td>
      <td>Yukikaze</td>
      <td></td>
      <td>467.3370</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>10</td>
      <td>12588.0580</td>
    </tr>
    <tr>
      <th>24</th>
      <td>52.08</td>
      <td>Hakaze</td>
      <td>Hissatsu: Shinten</td>
      <td>607.7520</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>13195.8100</td>
    </tr>
    <tr>
      <th>25</th>
      <td>54.24</td>
      <td>Shifu</td>
      <td></td>
      <td>390.7470</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>0</td>
      <td>13586.5570</td>
    </tr>
    <tr>
      <th>26</th>
      <td>56.40</td>
      <td>Kasha</td>
      <td>Hagakure</td>
      <td>543.9270</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5</td>
      <td>14130.4840</td>
    </tr>
    <tr>
      <th>27</th>
      <td>58.56</td>
      <td>Hakaze</td>
      <td>Hissatsu: Shinten</td>
      <td>607.7520</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>14738.2360</td>
    </tr>
    <tr>
      <th>28</th>
      <td>60.72</td>
      <td>Jinpu</td>
      <td>Hissatsu: Shinten</td>
      <td>773.6970</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>55</td>
      <td>15511.9330</td>
    </tr>
    <tr>
      <th>29</th>
      <td>62.88</td>
      <td>Gekko</td>
      <td>Hissatsu: Shinten</td>
      <td>926.8770</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>16438.8100</td>
    </tr>
    <tr>
      <th>30</th>
      <td>65.04</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.8020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>16663.6120</td>
    </tr>
    <tr>
      <th>31</th>
      <td>67.20</td>
      <td>Yukikaze</td>
      <td></td>
      <td>467.3370</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>25</td>
      <td>17130.9490</td>
    </tr>
    <tr>
      <th>32</th>
      <td>69.36</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.8020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>17355.7510</td>
    </tr>
    <tr>
      <th>33</th>
      <td>71.52</td>
      <td>Shifu</td>
      <td></td>
      <td>390.7470</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>40</td>
      <td>17746.4980</td>
    </tr>
    <tr>
      <th>34</th>
      <td>73.68</td>
      <td>Kasha</td>
      <td>Hissatsu: Kaiten</td>
      <td>543.9270</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>45</td>
      <td>18290.4250</td>
    </tr>
    <tr>
      <th>35</th>
      <td>75.84</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1411.9470</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>19702.3720</td>
    </tr>
    <tr>
      <th>36</th>
      <td>78.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.8020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>35</td>
      <td>19927.1740</td>
    </tr>
    <tr>
      <th>37</th>
      <td>80.16</td>
      <td>Jinpu</td>
      <td>Hissatsu: Shinten</td>
      <td>773.6970</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>40</td>
      <td>20700.8710</td>
    </tr>
    <tr>
      <th>38</th>
      <td>82.32</td>
      <td>Gekko</td>
      <td>Hissatsu: Shinten</td>
      <td>893.5500</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>20</td>
      <td>21594.4210</td>
    </tr>
    <tr>
      <th>39</th>
      <td>84.48</td>
      <td>Higanbana</td>
      <td>Meikyo Shisui</td>
      <td>306.3600</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>0</td>
      <td>5</td>
      <td>21900.7810</td>
    </tr>
    <tr>
      <th>40</th>
      <td>86.64</td>
      <td>Kasha</td>
      <td></td>
      <td>543.9270</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>5</td>
      <td>22444.7080</td>
    </tr>
    <tr>
      <th>41</th>
      <td>88.80</td>
      <td>Gekko</td>
      <td></td>
      <td>543.9270</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>22988.6350</td>
    </tr>
    <tr>
      <th>42</th>
      <td>90.96</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Kaiten</td>
      <td>467.3370</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>25</td>
      <td>23455.9720</td>
    </tr>
    <tr>
      <th>43</th>
      <td>93.12</td>
      <td>Hakaze</td>
      <td></td>
      <td>320.5395</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>23776.5115</td>
    </tr>
    <tr>
      <th>44</th>
      <td>95.28</td>
      <td>Shifu</td>
      <td>Hagakure</td>
      <td>390.7470</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>20</td>
      <td>24167.2585</td>
    </tr>
    <tr>
      <th>45</th>
      <td>97.44</td>
      <td>Kasha</td>
      <td>Hissatsu: Shinten</td>
      <td>926.8770</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>85</td>
      <td>25094.1355</td>
    </tr>
    <tr>
      <th>46</th>
      <td>99.60</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.8020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>70</td>
      <td>25318.9375</td>
    </tr>
    <tr>
      <th>47</th>
      <td>101.76</td>
      <td>Yukikaze</td>
      <td>Hissatsu: Shinten</td>
      <td>850.2870</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>26169.2245</td>
    </tr>
    <tr>
      <th>48</th>
      <td>103.92</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.8020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>60</td>
      <td>26394.0265</td>
    </tr>
    <tr>
      <th>49</th>
      <td>106.08</td>
      <td>Jinpu</td>
      <td></td>
      <td>390.7470</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>26784.7735</td>
    </tr>
    <tr>
      <th>50</th>
      <td>108.24</td>
      <td>Gekko</td>
      <td>Hissatsu: Kaiten</td>
      <td>543.9270</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>70</td>
      <td>27328.7005</td>
    </tr>
    <tr>
      <th>51</th>
      <td>110.40</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1411.9470</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>60</td>
      <td>28740.6475</td>
    </tr>
    <tr>
      <th>52</th>
      <td>112.56</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.8020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>60</td>
      <td>28965.4495</td>
    </tr>
    <tr>
      <th>53</th>
      <td>114.72</td>
      <td>Shifu</td>
      <td></td>
      <td>390.7470</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>65</td>
      <td>29356.1965</td>
    </tr>
    <tr>
      <th>54</th>
      <td>116.88</td>
      <td>Kasha</td>
      <td>Hissatsu: Shinten</td>
      <td>926.8770</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>70</td>
      <td>30283.0735</td>
    </tr>
    <tr>
      <th>55</th>
      <td>119.04</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.8020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>55</td>
      <td>30507.8755</td>
    </tr>
    <tr>
      <th>56</th>
      <td>121.20</td>
      <td>Yukikaze</td>
      <td></td>
      <td>467.3370</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>60</td>
      <td>30975.2125</td>
    </tr>
    <tr>
      <th>57</th>
      <td>123.36</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.8020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>70</td>
      <td>31200.0145</td>
    </tr>
    <tr>
      <th>58</th>
      <td>125.52</td>
      <td>Jinpu</td>
      <td></td>
      <td>390.7470</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>31590.7615</td>
    </tr>
    <tr>
      <th>59</th>
      <td>127.68</td>
      <td>Gekko</td>
      <td>Hissatsu: Kaiten</td>
      <td>543.9270</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>80</td>
      <td>32134.6885</td>
    </tr>
    <tr>
      <th>60</th>
      <td>129.84</td>
      <td>Midare Setsugekka</td>
      <td></td>
      <td>1411.9470</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>70</td>
      <td>33546.6355</td>
    </tr>
    <tr>
      <th>61</th>
      <td>132.00</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.8020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>70</td>
      <td>33771.4375</td>
    </tr>
    <tr>
      <th>62</th>
      <td>134.16</td>
      <td>Shifu</td>
      <td>Hissatsu: Guren</td>
      <td>1411.9470</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>75</td>
      <td>35183.3845</td>
    </tr>
    <tr>
      <th>63</th>
      <td>136.32</td>
      <td>Kasha</td>
      <td>Hissatsu: Shinten</td>
      <td>926.8770</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>30</td>
      <td>36110.2615</td>
    </tr>
    <tr>
      <th>64</th>
      <td>138.48</td>
      <td>Hakaze</td>
      <td></td>
      <td>224.8020</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>1</td>
      <td>15</td>
      <td>36335.0635</td>
    </tr>
  </tbody>
</table>
</div>



```python
plot_potency(df2, truncate_actions=True)
```


![png](output_33_0.png)



```python
compare_n_potencies([df0, df1, df2], ['lvl 52-61 rotation', 'lvl 62-67 rotation', 'lvl 70 rotation'])
```


![png](output_34_0.png)


Here I used the first Meikyo Shisui to get buffs up and three Sen open ASAP. The first set of three Sen went to Hagakure; this was an attempt to synchronize Meikyo Shisui and Hagakure to rapidly generate 60 Kenki. Unfortunately, while the recast timers seem like logical matches, the Sen generation does not fall in line.

It takes eight GCDs to open three Sen from scratch. Depending on your base GCD, this is in the neighborhood of 16-19 seconds while Shifu is active. This gives us the opportunity to alternate spending three Sen on Midare Setsugekka and spending three Sen on Hagakure while keeping Hagakure on cooldown. Reapplying Higanbana will increase the period of this cycle. We have some flexibility in holding onto three Sen by using the fact that Iaijutsu doesn't break combo. Nevertheless, unless we reapply Higanbana every Hagakure cycle (significantly clipping it), it will be difficult to convert three Sen via Hagakure as soon as Hagakure comes off cooldown.

<a href="#header">back to the top...</a>
