import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from ffxiv_sim.simulator import Simulator, Target
from ffxiv_sim.machinist import Machinist 


def level_15_mch():
    sim = Simulator()

    mch = Machinist()
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    actions_list = [
        'hot_shot', 'gauss_round',
        'split_shot', 'reassemble',
        'slug_shot', 'gauss_round',
        'split_shot', 'slug_shot',
        'split_shot', 'slug_shot',
        'split_shot', 'slug_shot',
        'split_shot', 'slug_shot',
        'split_shot', 'slug_shot',
        'split_shot', 'slug_shot', 
        'split_shot', 'gauss_round', 'slug_shot', 
        'hot_shot',
    ]

    df_combat_15 = sim.simulate_mch(actions_list)

    return df_combat_15


def level_26_mch():
    sim = Simulator()

    mch = Machinist()
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    actions_list = [
        'hot_shot', 'gauss_round',
        'split_shot', 'gauss_round', 'slug_shot', 'reassemble', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot', 
        'split_shot', 'slug_shot', 'clean_shot', 'gauss_round',
        'split_shot', 'slug_shot', 'clean_shot',
        'hot_shot',
    ]

    df_combat_26 = sim.simulate_mch(actions_list)

    return df_combat_26


def level_35_mch():
    sim = Simulator()

    mch = Machinist()
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    actions_list = [
        'hot_shot', 'gauss_round',
        'split_shot', 'gauss_round', 'slug_shot', 'reassemble', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot', 'hypercharge', 
        'heat_blast', 'gauss_round', 'heat_blast', 'heat_blast', 'gauss_round', 'heat_blast',
        'split_shot', 'slug_shot', 'clean_shot',
        'hot_shot',
    ]

    df_combat_35 = sim.simulate_mch(actions_list)

    return df_combat_35


def level_40_mch():
    sim = Simulator()

    mch = Machinist()
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    actions_list = [
        'hot_shot', 'gauss_round',
        'split_shot', 'gauss_round', 'slug_shot', 'reassemble', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot', 'hypercharge', 
        'heat_blast', 'heat_blast', 'gauss_round', 'heat_blast', 'heat_blast', 'gauss_round',
        'split_shot', 'slug_shot', 'clean_shot',
        'hot_shot',
        'split_shot', 'slug_shot', 'clean_shot', 'rook_autoturret',
        'split_shot', 'slug_shot', 'clean_shot',
    ]

    df_combat_40 = sim.simulate_mch(actions_list)

    return df_combat_40


def level_45_mch():
    # Add Wildfire
    # Clean Shot = 320 potency
    # W/S in Wildfire add 150 potency (with trait). Unknown before lvl 78 trait.
    # Heat Blast has a shorter recast time and can add additional Wildfire "stacks"
    # Wildfire duration = 10s
    # All Heat Blasts in W/F => 6 W/S, limited by Hypercharge duration
    # All normal shots in W/F => 4 W/S
    # With sufficient SKS, you can fit in 7 W/S with:
    # (normal shot) + wildfire / (normal shot) + hypercharge / heat blast x6
    # You'll need a late weave on the wildfire (double weave can help with timing)
    # There is a risk of missing the 7th W/S but you shouldn't miss the 6 Heat Blasts. 
    # This is a missed opportunity of 150 potency.
    # Remember that only the number of W/S in WF duration matters but you also get 20% increased damage during overheat
    # A more comfortable rotation would be 6 W/S in WF with a high potency W/S in overheat
    # Since Heat Blast reduces c/d of Ricochet and Gauss Round, it is probably better to maximize Heat Blast uses
    # Remember there's a max of 2 charges until the trait (lvl 74)
    sim = Simulator()

    mch = Machinist()
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    actions_list = [
        'hot_shot', 'gauss_round',
        'split_shot', 'gauss_round', 'slug_shot', 'reassemble', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot',
        'split_shot', 'slug_shot', 'wildfire', 'clean_shot', 'hypercharge', 
        'heat_blast', 'gauss_round', 'heat_blast', 'heat_blast', 'gauss_round', 'heat_blast', 'heat_blast', 'gauss_round',
        'split_shot', 'slug_shot', 'clean_shot',
        'hot_shot',
        'split_shot', 'slug_shot', 'clean_shot', 'rook_autoturret',
        'split_shot', 'slug_shot', 'clean_shot',
    ]

    df_combat_45 = sim.simulate_mch(actions_list)

    return df_combat_45


def level_50_mch():
    # Add Ricochet
    # This adds additional ability that also gets CDR from Heat Blast
    # This is a big boost
    sim = Simulator()

    mch = Machinist()
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    actions_list = [
        'hot_shot', 'gauss_round',
        'split_shot', 'ricochet', 'slug_shot', 'reassemble', 'clean_shot', 'gauss_round',
        'split_shot', 'ricochet', 'slug_shot', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot',
        'split_shot', 'slug_shot', 'wildfire', 'clean_shot', 'hypercharge', 
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round', 
        'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'split_shot', 'slug_shot', 'clean_shot',
        'hot_shot',
        'split_shot', 'slug_shot', 'clean_shot', 'rook_autoturret',
        'split_shot', 'slug_shot', 'clean_shot',
    ]

    df_combat_50 = sim.simulate_mch(actions_list)

    return df_combat_50


def level_54_mch():
    # Add Heated Split Shot
    # This is a direct increase of 60 potency to your Split Shots
    sim = Simulator()

    mch = Machinist()
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    actions_list = [
        'hot_shot', 'gauss_round',
        'heated_split_shot', 'ricochet', 'slug_shot', 'reassemble', 'clean_shot', 'gauss_round',
        'heated_split_shot', 'ricochet', 'slug_shot', 'clean_shot',
        'heated_split_shot', 'slug_shot', 'clean_shot',
        'heated_split_shot', 'slug_shot', 'wildfire', 'clean_shot', 'hypercharge', 
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round', 
        'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heated_split_shot', 'slug_shot', 'clean_shot',
        'hot_shot',
        'heated_split_shot', 'slug_shot', 'clean_shot', 'rook_autoturret',
        'heated_split_shot', 'slug_shot', 'clean_shot',
    ]

    df_combat_54 = sim.simulate_mch(actions_list)

    return df_combat_54


def level_54_mch_heat_generation():
    # You generate 50 Heat approximately every 28-30s.
    # You can use Hypercharge/Overheat outside of Wildfire.
    # Hypercharge can also be used to extend an Overheat window. This is not really beneficial for Wildfire windows.
    # It could be useful to extend Overheat windows during long buff windows.
    # It's likely better to use it pretty regularly to reduce GR/Ricochet cooldowns.
    sim = Simulator()

    mch = Machinist()
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    actions_list = [
        'hot_shot', 'gauss_round',
        'heated_split_shot', 'ricochet', 'slug_shot', 'reassemble', 'clean_shot', 'gauss_round',
        'heated_split_shot', 'ricochet', 'slug_shot', 'clean_shot',
        'heated_split_shot', 'slug_shot', 'clean_shot',
        'heated_split_shot', 'slug_shot', 'wildfire', 'clean_shot', 'hypercharge', 
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round', 
        'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heated_split_shot', 'slug_shot', 'clean_shot',
        'hot_shot',
        'heated_split_shot', 'slug_shot', 'clean_shot', 'rook_autoturret',
        'heated_split_shot', 'slug_shot', 'ricochet', 'clean_shot', 'hypercharge',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round', 
        'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
    ]

    df_combat_54 = sim.simulate_mch(actions_list)

    return df_combat_54


def level_58_mch():
    # Add Drill
    # Drill = 400 potency and battery gauge incrementation on ~20s cooldown
    # High potency W/S and faster autoturret deployment
    # Candidate for Reassemble (highest potency W/S atm)
    sim = Simulator()

    mch = Machinist()
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    actions_list = [
        'hot_shot', 'gauss_round', 'reassemble', 'drill',
        'heated_split_shot', 'ricochet', 'slug_shot', 'clean_shot', 'gauss_round',
        'heated_split_shot', 'ricochet', 'slug_shot', 'clean_shot',
        'heated_split_shot', 'slug_shot', 'clean_shot',
        'drill',
        'heated_split_shot', 'slug_shot', 'wildfire', 'clean_shot', 'hypercharge', 
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round', 
        'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heated_split_shot', 'slug_shot', 'clean_shot',
        'drill', 'rook_autoturret',
        'hot_shot',
        'heated_split_shot', 'slug_shot', 'clean_shot',
    ]

    df_combat_58 = sim.simulate_mch(actions_list)

    return df_combat_58


def level_64_mch():
    # Add Heated Slug Shot and Heated Clean Shot
    # These are straight upgrades of Slug Shot and Clean Shot of 60 and 80 potency, respectively
    # Huuuuge    
    sim = Simulator()

    mch = Machinist()
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    actions_list = [
        'hot_shot', 'gauss_round', 'reassemble', 'drill',
        'heated_split_shot', 'ricochet', 'heated_slug_shot', 'heated_clean_shot', 'gauss_round',
        'heated_split_shot', 'ricochet', 'heated_slug_shot', 'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
        'drill',
        'heated_split_shot', 'heated_slug_shot', 'wildfire', 'heated_clean_shot', 'hypercharge', 
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round', 
        'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
        'drill', 'rook_autoturret',
        'hot_shot',
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
    ]

    df_combat_64 = sim.simulate_mch(actions_list)

    return df_combat_64


def level_66_mch():
    # Add Barrel Stabilizer
    # This lets you add 50 Heat on demand every minute
    # Previously, our Heat generation was about 50 per 25s or so
    # We can use this to align our Wildfire phases
    sim = Simulator()

    mch = Machinist()
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    actions_list = [
        'drill', 'gauss_round', 'hot_shot', 'ricochet',
        'heated_split_shot', 'barrel_stabilizer', 'heated_slug_shot', 'heated_clean_shot', 
        'wildfire', 'hypercharge',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heat_blast', 'ricochet', 'heat_blast', 'ricochet',
        'heat_blast', 'reassemble',
        'drill', 'gauss_round',
        'heated_split_shot', 'ricochet', 'heated_slug_shot', 'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 
        'drill', 'hot_shot', 'rook_autoturret', 
        'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 'ricochet', 'hypercharge', 'heated_clean_shot',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heat_blast',
        'drill', 'ricochet',
    ]

    df_combat_66 = sim.simulate_mch(actions_list)

    return df_combat_66


def level_76_mch():
    # Add Air Anchor
    # This is a direct upgrade of Hot Shot from 200 to 400 potency
    # Since this equals Drill and Heated Clean Shot in potency, it is a candidate for Reassemble
    # level 74 additionally granted an extra charge each for GR and Ricochet
    sim = Simulator()

    mch = Machinist()
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    actions_list = [
        'drill', 'gauss_round', 'air_anchor', 'ricochet',
        'heated_split_shot', 'barrel_stabilizer', 'heated_slug_shot', 'gauss_round', 'heated_clean_shot', 
        'wildfire', 'hypercharge',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heat_blast', 'ricochet', 'heat_blast',
        'heat_blast', 'reassemble',
        'drill', 'gauss_round',
        'heated_split_shot', 'ricochet', 'heated_slug_shot', 'ricochet', 'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 
        'drill', 'air_anchor', 'rook_autoturret', 
        'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 'ricochet', 'hypercharge', 'heated_clean_shot',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heat_blast', 'ricochet',
        'drill', 'ricochet',
    ]

    df_combat_76 = sim.simulate_mch(actions_list)

    return df_combat_76


def level_80_mch():
    # Add Automaton Queen
    # This is a significant upgrade to your autoturret
    # I doubt that its W/S counts towards the Wildfire counter
    sim = Simulator()

    mch = Machinist()
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    actions_list = [
        'drill', 'gauss_round', 'air_anchor', 'ricochet',
        'heated_split_shot', 'barrel_stabilizer', 'heated_slug_shot', 'gauss_round', 'heated_clean_shot', 
        'wildfire', 'hypercharge',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heat_blast', 'ricochet', 'heat_blast',
        'heat_blast', 'reassemble',
        'drill', 'gauss_round',
        'heated_split_shot', 'ricochet', 'heated_slug_shot', 'ricochet', 'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 
        'drill', 'air_anchor', 'automaton_queen', 
        'heated_clean_shot',
        'heated_split_shot', 'heated_slug_shot', 'ricochet', 'hypercharge', 'heated_clean_shot',
        'heat_blast', 'gauss_round', 'heat_blast', 'ricochet', 'heat_blast', 'gauss_round',
        'heat_blast', 'ricochet',
        'drill', 'ricochet',
    ]

    df_combat_80 = sim.simulate_mch(actions_list)

    return df_combat_80


def compare_leveling_rotations():
    dfs = [
        # ('lvl 15', level_15_mch()),
        # ('lvl 26', level_26_mch()),
        # ('lvl 35', level_35_mch()),
        # ('lvl 40', level_40_mch()),
        # ('lvl 45', level_45_mch()),
        ('lvl 50', level_50_mch()),
        ('lvl 54', level_54_mch()),
        ('lvl 58', level_58_mch()),
        ('lvl 64', level_64_mch()),
        ('lvl 66', level_66_mch()),
        ('lvl 76', level_76_mch()),
        ('lvl 80', level_80_mch()),
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

    fig.suptitle('Machinist Leveling Rotations')

    plt.show()


def test_rook_autoturret():
    sim = Simulator()

    mch = Machinist()
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    actions_list = [
        'hot_shot', 'gauss_round',
        'split_shot', 'gauss_round', 'slug_shot', 'reassemble', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot', 'hypercharge', 
        'heat_blast', 'heat_blast', 'gauss_round', 'heat_blast', 'heat_blast', 'gauss_round',
        'split_shot', 'slug_shot', 'clean_shot',
        'hot_shot',
        'split_shot', 'slug_shot', 'clean_shot', 'rook_autoturret',
        'split_shot', 'slug_shot', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot',
        'split_shot', 'slug_shot', 'clean_shot',
    ]

    df = sim.simulate_mch(actions_list)
    df.to_csv('combat_log.csv')


if __name__ == '__main__':
    compare_leveling_rotations()
    # test_rook_autoturret()
