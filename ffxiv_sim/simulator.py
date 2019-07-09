import logging
import sys

import numpy as np
from numpy.random import random, random_sample
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from ffxiv_sim.machinist import Machinist

class Target():
    pass

class Simulator():
    """"""
    def __init__(self, logging_stream=False):
        self._combatants = []
        self._targets = []
        self._time = 0

        with open('combat.log', 'w'):
            pass
        
        log = logging.getLogger('')
        log.setLevel(logging.INFO)

        formatter = logging.Formatter('[%(levelname)s] %(message)s')

        fh = logging.FileHandler('combat.log')
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        log.addHandler(fh)

        if logging_stream:
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            ch.setFormatter(formatter)
            log.addHandler(ch)
    
    @property
    def combatants(self):
        """The list of active combatants."""
        return self._combatants
    
    @combatants.setter
    def combatants(self, value):
        raise NotImplementedError("Cannot assign the list of combatants directly.")
    
    @property
    def targets(self):
        """The list of active targets."""
        return self._targets
    
    @targets.setter
    def targets(self, value):
        raise NotImplementedError("Cannot assign the list of targets directly.")
    
    @property
    def time(self):
        """The current simulation time."""
        return self._time
    
    @time.setter
    def time(self, value):
        self._time = value

    def add_combatant(self, combatant):
        """Adds combatant to the list of combatants."""
        self.combatants.append(combatant)
    
    def add_target(self, target):
        """Adds target to the list of targets."""
        self.targets.append(target)
    
    def record_combatant(self, participant):
        """Records time series data for specified combat participant."""
        return_dict = {}

        if isinstance(participant, Machinist):
            fields = [
                'heat_gauge',
                # 'overheated',
                'battery_gauge',
                'gauss_round_charges',
                # 'gauss_round_charge_timer',
                'ricochet_charges',
                # 'ricochet_charge_timer',
                # 'hot_shot_cooldown',
                # 'global_cooldown',
                # 'global_cooldown_timer',
                # 'on_global_cooldown',
                # 'wildfire_cooldown',
            ]

            for field_name in fields:
                field_value = getattr(participant, field_name)

                return_dict[field_name] = field_value
        
        return return_dict
    
    def do_damage_roll(self, action, potency, combatant, target=None):
        """Rolls for damage based on potency, combatant stats, and target stats."""
        if potency > 0:
            direct_hit_chance = combatant.direct_hit_chance
            critical_hit_chance = combatant.critical_hit_chance
            critical_hit_multiplier = combatant.critical_hit_multiplier

            # Sample for variance: +/- 10% uniformly distributed
            damage = potency*(0.2*random_sample() + 0.9)

            if action == 'wildfire':
                direct_hit_chance = 0
                critical_hit_chance = 0
                critical_hit_multiplier = 1

            # Check for guaranteed DH+Crit
            if isinstance(combatant, Machinist):
                if action in combatant.weaponskills and combatant.reassembled:
                    direct_hit_chance = 1.0
                    critical_hit_chance = 1.0
                    combatant.reassembled = False

            # Roll for direct hit
            direct_hit_roll = random()

            if direct_hit_roll < direct_hit_chance:
                # Rolled a direct hit
                is_direct_hit = True
                damage = damage*1.25
            else:
                is_direct_hit = False

            # Roll for crit
            critical_hit_roll = random()

            if critical_hit_roll < critical_hit_chance:
                # Rolled a critical hit
                is_critical_hit = True
                damage = damage*critical_hit_multiplier
            else:
                is_critical_hit = False
            
            # Apply effective potency to attack power for final damage calculation
            # TODO:
            damage = 34.27056229*damage
            
            # Log
            # TODO:
            if is_critical_hit and is_direct_hit:
                pass
            elif is_direct_hit:
                pass
            elif is_critical_hit:
                pass
            else:
                pass
        else:
            damage = 0

        return damage
    
    def simulate_mch(self, actions_list):
        for combatant in self.combatants:
            if isinstance(combatant, Machinist):
                mch = combatant
        
        if not mch:
            raise TypeError('No Machinists in active combatants found.')

        combat_record = []

        for ix, action in enumerate(actions_list, start=0):
            pot = getattr(mch, action)()

            try:
                next_action = actions_list[ix+1]
            except IndexError:
                time_increment = mch.weave_delay
            else:
                if next_action in mch.weaponskills:
                    # Finish the remainder of the current GCD timer.
                    time_increment = mch.global_cooldown_timer
                else:
                    time_increment = mch.weave_delay

            mch_record = self.record_combatant(mch)
            mch_record['time'] = float('{0:2f}'.format(self.time))
            mch_record['ability'] = action
            mch_record['potency'] = pot
            mch_record['damage'] = self.do_damage_roll(action, pot, mch)
            combat_record.append(mch_record)
            
            # Update time.
            callback = mch.update_time(time_increment)

            while len(callback) > 0:
                if callback.get('attack', False):
                    # Add auto-attack.
                    self.time += callback['re-update time']

                    mch_record = self.record_combatant(mch)
                    mch_record['time'] = float('{0:2f}'.format(self.time))
                    mch_record['ability'] = 'attack'
                    mch_record['potency'] = callback['attack']
                    mch_record['damage'] = self.do_damage_roll('attack', callback['attack'], mch)
                    combat_record.append(mch_record)
                elif callback.get('rook_volley_fire', False):
                    # Add Rook Volley Fire.
                    self.time += callback['re-update time']

                    mch_record = self.record_combatant(mch)
                    mch_record['time'] = float('{0:2f}'.format(self.time))
                    mch_record['ability'] = 'volley_fire'
                    mch_record['potency'] = callback['rook_volley_fire']
                    mch_record['damage'] = self.do_damage_roll('volley_fire', callback['rook_volley_fire'], mch.automaton)
                    combat_record.append(mch_record)
                elif callback.get('queen_arm_punch', False):
                    # Add Queen Arm Punch.
                    self.time += callback['re-update time']

                    mch_record = self.record_combatant(mch)
                    mch_record['time'] = float('{0:2f}'.format(self.time))
                    mch_record['ability'] = 'arm_punch'
                    mch_record['potency'] = callback['queen_arm_punch']
                    mch_record['damage'] = self.do_damage_roll('arm_punch', callback['queen_arm_punch'], mch.automaton)
                    combat_record.append(mch_record)
                elif callback.get('queen_roller_dash', False):
                    # Add Queen Roller Dash.
                    self.time += callback['re-update time']

                    mch_record = self.record_combatant(mch)
                    mch_record['time'] = float('{0:2f}'.format(self.time))
                    mch_record['ability'] = 'roller_dash'
                    mch_record['potency'] = callback['queen_roller_dash']
                    mch_record['damage'] = self.do_damage_roll('roller_dash', callback['queen_roller_dash'], mch.automaton)
                    combat_record.append(mch_record)
                elif callback.get('wildfire', False):
                    # Add Wildfire detonation.
                    self.time += callback['re-update time']

                    mch_record = self.record_combatant(mch)
                    mch_record['time'] = float('{0:2f}'.format(self.time))
                    mch_record['ability'] = 'wildfire'
                    mch_record['potency'] = 200*callback['wildfire']
                    mch_record['damage'] = self.do_damage_roll('wildfire', 200*callback['wildfire'], mch)
                    combat_record.append(mch_record)
                elif callback.get('rook_overdrive', False):
                    # Add Rook Overdrive.
                    self.time += callback['re-update time']

                    mch_record = self.record_combatant(mch)
                    mch_record['time'] = float('{0:2f}'.format(self.time))
                    mch_record['ability'] = 'rook_overload'
                    mch_record['potency'] = callback['rook_overdrive']
                    mch_record['damage'] = self.do_damage_roll('rook_overload', callback['rook_overdrive'], mch.automaton)
                    combat_record.append(mch_record)

                    mch.automaton = None
                elif callback.get('queen_overdrive', False):
                    # Add Queen Overdrive.
                    self.time += callback['re-update time']

                    mch_record = self.record_combatant(mch)
                    mch_record['time'] = float('{0:2f}'.format(self.time))
                    mch_record['ability'] = 'pile_bunker'
                    mch_record['potency'] = callback['queen_overdrive']
                    mch_record['damage'] = self.do_damage_roll('pile_bunker', callback['queen_overdrive'], mch.automaton)
                    combat_record.append(mch_record)

                    mch.automaton = None
                
                # Re-update time with new time increment after interrupting event.
                mch.total_time_elapsed = self.time
                time_increment -= callback['re-update time']
                callback = mch.update_time(time_increment)

            self.time += time_increment
            mch.total_time_elapsed = self.time

        df_combat = pd.DataFrame(combat_record)

        df_combat['Cumulative Damage'] = df_combat['damage'].cumsum()
        df_combat['DPS'] = df_combat['Cumulative Damage']/df_combat['time']
        df_combat['PPS'] = df_combat['potency'].cumsum()/df_combat['time']
        df_combat.replace([np.inf, -np.inf], 0)

        df_combat.set_index('time', inplace=True)

        # print(df_combat)

        # fig, ax = plt.subplots(figsize=(12, 5))
        # df_combat['cumulative pps'].plot(drawstyle='steps-pre', linewidth=2, ax=ax)

        # ax.set_xlabel('time [s]')
        # ax.set_title('potency per second')
        # ax.grid(True)
        # plt.show()

        return df_combat


def main():
    # pass 
    sim = Simulator()

    mch = Machinist()
    target = Target()

    sim.add_combatant(mch)
    sim.add_target(target)

    actions_list = [
        'drill',
        'air_anchor', 'barrel_stabilizer',
        'heated_split_shot', 'gauss_round',
        'heated_slug_shot', 'wildfire',
        'heated_clean_shot', 'hypercharge',
        'heat_blast', 'ricochet',
        'heat_blast', 'gauss_round',
        'heat_blast', 'ricochet',
        'heat_blast', 
        'heated_split_shot', 'gauss_round',
        'heated_slug_shot', 'ricochet',
        'heated_clean_shot', 'reassemble',
        'drill',
        'heated_split_shot', 'gauss_round',
        'heated_slug_shot', 'ricochet',
        'heated_clean_shot', 'ricochet',
        'heated_split_shot',
        'heated_slug_shot',
        'heated_clean_shot',
        'air_anchor',
    ]

    df = sim.simulate_mch(actions_list)

    fig, ax = subplots(1, 2, figsize=(16, 10))

    df['cumulative pps'].plot(drawstyle='steps-post', linewidth=2, ax=axes[0])
    df['heat_gauge'].plot(drawstyle='steps-post', linewidth=2, ax=axes[-1], label='Heat')
    df['battery_gauge'].plot(drawstyle='steps-post', linewidth=2, ax=axes[-1], label='Battery')

    axes[0].set_xlabel('time [s]')
    axes[0].set_title('potency per second')
    axes[0].grid(True)
    axes[0].legend()

    axes[-1].set_ylim([0, 100])
    axes[-1].set_xlabel('time [s]')
    axes[-1].set_title('resources')
    axes[-1].grid(True)
    axes[-1].legend()

    fig.suptitle('Simulation Results')

    plt.show()

if __name__ == '__main__':
    main()