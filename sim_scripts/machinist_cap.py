import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from ffxiv_sim.simulator import Simulator, Target
from ffxiv_sim.machinist import Machinist 


def generate_graphs(combat_dataframe):
    fig, axes = plt.subplots(3, 1, figsize=(12, 12), sharex=True)

    combat_dataframe['DPS'].plot(drawstyle='steps-post', linewidth=2, ax=axes[0])
    combat_dataframe['damage'].plot(drawstyle='steps-post', linewidth=2, ax=axes[1])
    combat_dataframe['heat_gauge'].plot(drawstyle='steps-post', linewidth=2, ax=axes[-1], label='Heat')
    combat_dataframe['battery_gauge'].plot(drawstyle='steps-post', linewidth=2, ax=axes[-1], label='Battery')

    axes[0].set_xlabel('time [s]')
    axes[0].set_title('DPS')
    axes[0].grid(True)

    axes[1].set_xlabel('time [s]')
    axes[1].set_title('Damage')
    axes[1].grid(True)

    axes[-1].set_ylim([0, 100])
    axes[-1].set_xlabel('time [s]')
    axes[-1].set_title('resources')
    axes[-1].grid(True)
    axes[-1].legend()

    fig.suptitle('Simulation Results')

    plt.show()

def three_minute_rotation():
    sim = Simulator()

    mch = Machinist()
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    # actions_list = [
    #     'drill', 'gauss_round', 'air_anchor', 'ricochet',
    #     'heated_split_shot', 'barrel_stabilizer', 'heated_slug_shot', 'gauss_round', 'heated_clean_shot', 
    #     'wildfire', 'hypercharge',
    #     'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
    #     'heat_blast', 'ricochet', 'heat_blast',
    #     'heat_blast', 'reassemble',
    #     'drill', 'gauss_round',
    #     'heated_split_shot', 'ricochet', 'heated_slug_shot', 'ricochet', 'heated_clean_shot',
    #     'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
    #     'heated_split_shot', 'heated_slug_shot', 
    #     'drill', 'air_anchor', 'automaton_queen', 
    #     'heated_clean_shot',
    #     'heated_split_shot', 'heated_slug_shot', 'ricochet', 'hypercharge', 'heated_clean_shot',
    #     'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
    #     'heat_blast', 'ricochet', 
    #     'drill', 'ricochet',
    #     'heated_split_shot', 'barrel_stabilizer', 'heated_slug_shot', 'heated_clean_shot',
    #     'wildfire', 'hypercharge',
    #     'heat_blast', 'gauss_round', 'heat_blast', 'heat_blast', 'ricochet',
    #     'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
    #     'heated_split_shot', 'reassemble',
    #     'drill', 'air_anchor',
    #     'heated_slug_shot', 'heated_clean_shot', 'ricochet', 'hypercharge',
    #     'heat_blast', 'heat_blast', 'gauss_round', 'heat_blast', 'ricochet',
    #     'heat_blast', 'gauss_round', 'heat_blast', 'ricochet',
    #     'heated_split_shot', 'ricochet', 'drill', 'heated_slug_shot', 'heated_clean_shot', 'automaton_queen',
    #     'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
    #     'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
    # ]

    actions_list = [
        'drill', 'gauss_round', 'ricochet',
        'heated_split_shot', 'gauss_round', 'heated_slug_shot', 'barrel_stabilizer', 'heated_clean_shot',
        # opening wildfire
        'wildfire', 'hypercharge',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heat_blast', 'ricochet', 'heat_blast', 'reassemble', 'air_anchor', 'ricochet',
        'drill', 'gauss_round', 'heated_split_shot', 'ricochet', 'heated_slug_shot', 'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 'drill', 'heated_clean_shot', 'ricochet', 'hypercharge',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heated_split_shot', 'ricochet', 'heated_slug_shot', 'heated_clean_shot',
        # first automaton ready
        'automaton_queen',
        'air_anchor', 'drill',
        'heated_split_shot', 'barrel_stabilizer', 'heated_slug_shot',
        # second wildfire
        'wildfire', 'hypercharge', 'heated_clean_shot',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heat_blast', 
        'heated_split_shot', 'heated_slug_shot', 'reassemble', 'drill', 'heated_clean_shot', 'ricochet', 
        'hypercharge',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heat_blast', 'ricochet', 'heat_blast', 'gauss_round', 'heat_blast', 'ricochet',
        'heated_split_shot', 
        # 'air_anchor', 
        'heated_slug_shot', 'heated_clean_shot', 'drill',
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
        # second automaton ready
        'automaton_queen',
        'air_anchor', 'gauss_round', 'hypercharge',
        'heat_blast', 'ricochet', 
        'drill', 'barrel_stabilizer',    
        # third wildfire, extended overheat
        'heat_blast', 'wildfire', 'heat_blast', 'ricochet',
        'heat_blast', 'hypercharge', 
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round', 
        'heat_blast', 'ricochet', 'heat_blast', 'gauss_round', 'heat_blast', 'ricochet',
        'heated_split_shot', 'gauss_round', 'heated_slug_shot', 'ricochet',
        'drill',
        'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot',
        # 'air_anchor',
        'heated_clean_shot', 
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot', 'ricochet', 
        'hypercharge',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'air_anchor',
        # third automaton ready
        'automaton_queen',
        'drill', 'ricochet',
        'heated_split_shot', 'barrel_stabilizer', 'heated_slug_shot',
        # fourth wildfire
        'wildfire', 'hypercharge', 'heated_clean_shot',
        'heat_blast', 'heat_blast', 'gauss_round', 'heat_blast', 'ricochet',
        'heat_blast', 'gauss_round',
        'heated_split_shot'
    ]

    df = sim.simulate_mch(actions_list)
    df.to_csv('combat_log.csv')

    return df

def wildfire_in_overheat():
    sim = Simulator()

    mch = Machinist(base_global_cooldown=2.40)
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    actions_list = [
        'drill', 'gauss_round', 'ricochet',
        'heated_split_shot', 'barrel_stabilizer', 'heated_slug_shot', 'gauss_round',
        # opening wildfire
        'wildfire',
        'heated_clean_shot', 'reassemble', 'hypercharge',
        'air_anchor',
        'heat_blast', 'ricochet', 'heat_blast', 'gauss_round', 'heat_blast', 'ricochet',
        'heat_blast', 'gauss_round',
        'heated_split_shot', 'ricochet', 
        'drill', 'gauss_round',
        'heated_slug_shot', 'heated_clean_shot', 'ricochet',
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
        'drill', 
        # filler overheat
        'hypercharge',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
        # first automaton
        'automaton_queen',
        'air_anchor',
        'heated_split_shot', 
        'drill', 'barrel_stabilizer',
        'heated_slug_shot', 
        # second wildfire
        'wildfire', 'reassemble',
        'heated_clean_shot', 'ricochet', 'hypercharge',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heat_blast', 'ricochet', 'heat_blast', 'gauss_round', 'heat_blast',
        'heated_split_shot', 'heated_slug_shot', 
        'drill',
        'heated_clean_shot', 'ricochet',
        # filler overheat
        'hypercharge',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heat_blast', 'ricochet', 'heat_blast', 'gauss_round', 'heat_blast',
        'heated_split_shot',
        'air_anchor',
        'heated_slug_shot',
        'drill',
        'heated_clean_shot',
        'heated_split_shot', 'ricochet', 'heated_slug_shot',
        # second automaton
        'automaton_queen',
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
        'heated_split_shot',
        # extended overheat + wildfire
        'hypercharge',
        'heat_blast', 'barrel_stabilizer', 'heat_blast', 'wildfire', 
        'heat_blast', 'reassemble', 'drill', 'gauss_round', 'hypercharge', 'heat_blast', 'ricochet', 
        'heat_blast', 'ricochet', 'heat_blast', 'gauss_round', 'heat_blast', 'ricochet',
        'heat_blast', 'gauss_round',
        'heated_split_shot', 'ricochet',
        'air_anchor', 'gauss_round',
        'heated_slug_shot', 'heated_clean_shot',
        'drill',
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 'ricochet',
        'drill',
        'heated_clean_shot',
        # third automaton + filler overheat
        'automaton_queen', 'hypercharge',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heat_blast', 'ricochet', 'heat_blast', 'gauss_round', 'heat_blast', 'ricochet',
        'air_anchor', 'ricochet', 'barrel_stabilizer',
        'heated_split_shot',
        # fourth wildfire
        'wildfire', 
        'heated_slug_shot', 'reassemble', 'hypercharge', 'heated_clean_shot',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'drill',

    ]

    df = sim.simulate_mch(actions_list)
    # df.to_csv('combat_log.csv')

    return df

def compare_rotations():
    dfs = [
        ('1', three_minute_rotation()),
        ('2', wildfire_in_overheat()),
    ]

    fig, axes = plt.subplots(2, 1, figsize=(12, 10))

    for df_label, df in dfs:
        df['cumulative pps'].plot(drawstyle='steps-post', linewidth=2, ax=axes[0], label=df_label)

        # df['heat_gauge'].plot(drawstyle='steps-post', linewidth=2, ax=axes[-1], label=df_label)
        # df['battery_gauge'].plot(drawstyle='steps-post', linewidth=2, ax=axes[-1], label=df_label)

    axes[0].set_xlabel('time [s]')
    axes[0].set_title('potency per second')
    axes[0].grid(True)
    axes[0].legend()

    # axes[-1].set_ylim([0, 100])
    # axes[-1].set_xlabel('time [s]')
    # axes[-1].set_title('resources')
    # axes[-1].grid(True)
    # axes[-1].legend()

    fig.suptitle('Machinist Rotations')

    plt.show()


def monte_carlo_sim():
    fig, axes = plt.subplots(1, 1, figsize=(12, 10))

    n_trials = 50

    for ix in np.arange(n_trials):
        df = wildfire_in_overheat()

        df['DPS'].plot(drawstyle='steps-post', linewidth=2, ax=axes)

        # df['heat_gauge'].plot(drawstyle='steps-post', linewidth=2, ax=axes[-1], label=df_label)
        # df['battery_gauge'].plot(drawstyle='steps-post', linewidth=2, ax=axes[-1], label=df_label)

    axes.set_xlabel('time [s]')
    axes.set_title('DPS realizations')
    axes.grid(True)
    # axes[0].legend()

    # axes[-1].set_ylim([0, 100])
    # axes[-1].set_xlabel('time [s]')
    # axes[-1].set_title('resources')
    # axes[-1].grid(True)
    # axes[-1].legend()

    # fig.suptitle('Machinist Rotations')

    plt.show()


def main():
    # df = three_minute_rotation()
    # df = wildfire_in_overheat()
    # generate_graphs(df)

    # compare_rotations()

    monte_carlo_sim()


if __name__ == '__main__':
    main()
