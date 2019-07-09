import logging

class Automaton():
    """An automaton deployed by the Machinist after spending 50 Battery gauge."""
    def __init__(
        self, initial_duration, attack_delay, 
        critical_hit_chance=0.10, critical_hit_multiplier=1.40, 
        direct_hit_chance=0.10
        ):
        # TODO: Remove default arguments for CHC, CHM, DHC when implementing those stats on the Machinist.
        self._initial_duration = initial_duration
        self._attack_delay = attack_delay
        self._critical_hit_chance = critical_hit_chance
        self._critical_hit_multiplier = critical_hit_multiplier
        self._direct_hit_chance = direct_hit_chance

        self._remaining_duration = initial_duration

    @property
    def initial_duration(self):
        """The duration of deployment in seconds. Scales the damage of Rook Overload and Pile Bunker."""
        return self._initial_duration
    
    @initial_duration.setter
    def initial_duration(self, value):
        raise ValueError('Cannot change the value of initial duration deployment.')
    
    @property
    def attack_delay(self):
        """The amount of time until the next Volley Fire in seconds."""
        return self._attack_delay
    
    @attack_delay.setter
    def attack_delay(self, value):
        self._attack_delay = value
    
    @property
    def critical_hit_chance(self):
        """The chance to deal a critical hit. Inherited from the owner at the time of deployment."""
        return self._critical_hit_chance
    
    @critical_hit_chance.setter
    def critical_hit_chance(self, value):
        raise ValueError('Cannot change the value of critical hit chance.')
    
    @property
    def critical_hit_multiplier(self):
        """The multiplier on potency from critical hits. Inherited from the owner at the time of deployment."""
        return self._critical_hit_multiplier
    
    @critical_hit_multiplier.setter
    def critical_hit_multiplier(self, value):
        raise ValueError('Cannot change the value of critical hit multiplier.')
    
    @property
    def direct_hit_chance(self):
        """The chance to deal a direct hit. Inherited from the owner at the time of deployment."""
        return self._direct_hit_chance
    
    @direct_hit_chance.setter
    def direct_hit_chance(self, value):
        raise ValueError('Cannot change the value of direct hit chance.')
    
    @property
    def remaining_duration(self):
        """The remaining duration on the current deployment."""
        return self._remaining_duration
    
    @remaining_duration.setter
    def remaining_duration(self, value):
        self._remaining_duration = max(0, value)

        if self._remaining_duration == 0:
            logging.info('Automaton has left the battlefield.')


class RookAutoturret(Automaton):
    """A type of automaton deployed by the Machinist who acquires the ability to do so at level 40."""
    @property
    def remaining_duration(self):
        """The remaining duration on the current deployment."""
        return self._remaining_duration
    
    @remaining_duration.setter
    def remaining_duration(self, value):
        self._remaining_duration = max(0, value)

        if self._remaining_duration == 0:
            logging.info('The Rook Autoturret withdraws from the battlefield.')


class AutomatonQueen(Automaton):
    """A type of automaton deployed by the Machinist who acquires the ability to do so at level 80."""
    @property
    def remaining_duration(self):
        """The remaining duration on the current deployment."""
        return self._remaining_duration
    
    @remaining_duration.setter
    def remaining_duration(self, value):
        self._remaining_duration = max(0, value)

        if self._remaining_duration == 0:
            logging.info('The Automaton Queen withdraws from the battlefield.')


class Machinist():
    """"""
    def __init__(self, 
        base_global_cooldown=2.45, weave_delay=1.00,
        critical_hit_chance=0.10, critical_hit_multiplier=1.40, 
        direct_hit_chance=0.10,
        auto_attack_potency=95.92, auto_attack_delay=2.64,        
        ):
        self._increased_damage_dealt = 0
        self._critical_hit_chance = critical_hit_chance
        self._critical_hit_multiplier = critical_hit_multiplier
        self._direct_hit_chance = direct_hit_chance
        self._auto_attack_potency = auto_attack_potency
        self._auto_attack_delay = auto_attack_delay
        self._auto_attack_recast_timer = 0

        self._base_global_cooldown = base_global_cooldown
        self._on_global_cooldown = False
        self._global_cooldown_timer = 0
        self._global_cooldown = self._base_global_cooldown

        self._automaton = None

        self._weave_delay = weave_delay

        self._total_time_elapsed = 0
        self._time_stamp = 0

        self._heat_gauge = 0
        self._battery_gauge = 0
        self._overheat_duration = 0
        self._wildfire_duration = 0

        self._overheated = False
        self._reassembled = False
        self._wildfire_applied = False

        self._wildfire_weaponskill_counter = 0

        self._gauss_round_charges = 3
        self._ricochet_charges = 3

        self._gauss_round_charge_timer = 30
        self._ricochet_charge_timer = 30

        self._hot_shot_cooldown = 0
        self._reassemble_cooldown = 0
        self._hypercharge_cooldown = 0
        self._wildfire_cooldown = 0
        self._drill_cooldown = 0
        self._barrel_stabilizer_cooldown = 0
        # flamethrower, automaton_queen/rook_autoturret

        self._slug_shot_combo_ready = False
        self._clean_shot_combo_ready = False

        self.weaponskills = [
            'split_shot', 'slug_shot', 'clean_shot',
            'heated_split_shot', 'heated_slug_shot', 'heated_clean_shot',
            'spread_shot',
            'hot_shot', 'air_anchor',
            'heat_blast', 'auto_crossbow',
            'drill', 'bio_blaster',
            'flamethrower',            
            ]

        self._main_target = None
    
    @property
    def increased_damage_dealt(self):
        """The total amount of increased damage dealt modifiers."""
        return self._increased_damage_dealt
    
    @increased_damage_dealt.setter
    def increased_damage_dealt(self, value):
        self._increased_damage_dealt = value
    
    @property
    def critical_hit_chance(self):
        """The chance to deal a critical hit."""
        return self._critical_hit_chance
    
    @critical_hit_chance.setter
    def critical_hit_chance(self, value):
        self._critical_hit_chance = value
    
    @property
    def critical_hit_multiplier(self):
        """The multiplier on potency from critical hits."""
        return self._critical_hit_multiplier
    
    @critical_hit_multiplier.setter
    def critical_hit_multiplier(self, value):
        self._critical_hit_multiplier = value
    
    @property
    def direct_hit_chance(self):
        """The chance to deal a direct hit."""
        return self._direct_hit_chance
    
    @direct_hit_chance.setter
    def direct_hit_chance(self, value):
        self._direct_hit_chance = value
    
    @property
    def auto_attack_potency(self):
        """The potency of an auto-attack, an intrinsic property of equipped weapon."""
        return self._auto_attack_potency
    
    @auto_attack_potency.setter
    def auto_attack_potency(self, value):
        self._auto_attack_potency = value
    
    @property
    def auto_attack_delay(self):
        """The delay of an auto-attack in seconds, an intrinsic property of equipped weapon."""
        return self._auto_attack_delay
    
    @auto_attack_delay.setter
    def auto_attack_delay(self, value):
        self._auto_attack_delay = value
    
    @property
    def auto_attack_recast_timer(self):
        """The amount of time until the next auto-attack in seconds."""
        return self._auto_attack_recast_timer
    
    @auto_attack_recast_timer.setter
    def auto_attack_recast_timer(self, value):
        self._auto_attack_recast_timer = max(0, value)
    
    @property
    def base_global_cooldown(self):
        """The base global cooldown length in seconds."""
        return self._base_global_cooldown
    
    @base_global_cooldown.setter
    def base_global_cooldown(self, value):
        self._base_global_cooldown = value
    
    @property
    def on_global_cooldown(self):
        """Returns True if currently on global cooldown."""
        return self._on_global_cooldown
    
    @on_global_cooldown.setter
    def on_global_cooldown(self, value):
        self._on_global_cooldown = value

        if value:
            self.global_cooldown_timer = self.global_cooldown
    
    @property
    def global_cooldown_timer(self):
        """The remaining duration on the current global cooldown in seconds."""
        return self._global_cooldown_timer
    
    @global_cooldown_timer.setter
    def global_cooldown_timer(self, value):
        if value < 0:
            self._global_cooldown_timer = self.global_cooldown
            self.on_global_cooldown = False
        else:
            self._global_cooldown_timer = value
    
    @property
    def global_cooldown(self):
        """The current global cooldown length in seconds."""
        return self._global_cooldown
    
    @global_cooldown.setter
    def global_cooldown(self, value):
        self._global_cooldown = value
    
    @property
    def automaton(self):
        """The instance of the summoned Rook Autoturret or Automaton Queen."""
        return self._automaton
    
    @automaton.setter
    def automaton(self, value):
        self._automaton = value
    
    @property
    def weave_delay(self):
        """The delay between weaving abilities in seconds."""
        return self._weave_delay
    
    @weave_delay.setter
    def weave_delay(self, value):
        self._weave_delay = value
    
    @property
    def total_time_elapsed(self):
        """The total time elapsed since combat start."""
        return self._total_time_elapsed
    
    @total_time_elapsed.setter
    def total_time_elapsed(self, value):
        self._total_time_elapsed = value
    
    @property
    def time_stamp(self):
        """The total time elapsed since combat start."""
        return '{0:2f}'.format(self.total_time_elapsed)
    
    @time_stamp.setter
    def time_stamp(self, value):
        pass
    
    @property
    def heat_gauge(self):
        """The current value of the heat gauge. Minimum value is 0 and maximum value is 100."""
        return self._heat_gauge
    
    @heat_gauge.setter
    def heat_gauge(self, value):
        if value < 0:
            raise ValueError("Heat gauge cannot be set below zero.")
        elif value > 100:
            self._heat_gauge = value
            logging.warning('{0}: Heat gauge has been overcapped.'.format(self.time_stamp))
        else:
            self._heat_gauge = value
    
    @property
    def battery_gauge(self):
        """The current value of the battery gauge. Minimum value is 0 and maximum value is 100."""
        return self._battery_gauge
    
    @battery_gauge.setter
    def battery_gauge(self, value):
        if value < 0:
            raise ValueError("Battery gauge cannot be set below zero.")
        elif value > 100:
            self._battery_gauge = 100
            logging.warning('{0}: Battery gauge has been overcapped.'.format(self.time_stamp))
        else:
            self._battery_gauge = value
    
    @property
    def overheat_duration(self):
        """The current remaining duration of the Overheated status."""
        return self._overheat_duration
    
    @overheat_duration.setter
    def overheat_duration(self, value):
        if value < 0:
            self.overheated = False
            self._overheat_duration = 0
        else:
            self._overheat_duration = value

    @property
    def wildfire_duration(self):
        """The current remaining duration of the active Wildfire application."""
        return self._wildfire_duration
    
    @wildfire_duration.setter
    def wildfire_duration(self, value):
        if value <= 0:
            self.wildfire_applied = False
            logging.info('{0}: Wildfire has detonated.'.format(self.total_time_elapsed))
            self._wildfire_duration = 0
            self.wildfire_weaponskill_counter = 0
        else:
            self._wildfire_duration = value
    
    @property
    def overheated(self):
        """Returns True if currently overheated."""
        return self._overheated
    
    @overheated.setter
    def overheated(self, value):
        if type(value) == bool:
            self._overheated = value
        else:
            return TypeError("overheated must be of type bool.")
    
    @property
    def reassembled(self):
        """Returns True if currently Reassemble is active."""
        return self._reassembled
    
    @reassembled.setter
    def reassembled(self, value):
        if type(value) == bool:
            self._reassembled = value
        else:
            return TypeError("reassembled must be of type bool.")
    
    @property
    def wildfire_applied(self):
        """Returns True if currently Wildfire is active on a target."""
        return self._wildfire_applied
    
    @wildfire_applied.setter
    def wildfire_applied(self, value):
        if type(value) == bool:
            self._wildfire_applied = value
        else:
            return TypeError("wildfire_applied must be of type bool.")
    
    @property
    def wildfire_weaponskill_counter(self):
        """The number of weaponskills landed during the current active Wildfire."""
        return self._wildfire_weaponskill_counter
    
    @wildfire_weaponskill_counter.setter
    def wildfire_weaponskill_counter(self, value):
        if value < 0:
            raise ValueError("The number of weaponskills landed during Wildfire cannot be set below zero.")
        else:
            self._wildfire_weaponskill_counter = value
    
    @property
    def gauss_round_charges(self):
        """The amount of available Gauss Round charges available."""
        return self._gauss_round_charges
    
    @gauss_round_charges.setter
    def gauss_round_charges(self, value):
        if value < 0:
            raise ValueError("Gauss Round charges cannot be set below zero.")
        elif value > 3:
            raise ValueError("Gauss Round charges cannot be greater than 3.")
        else:
            self._gauss_round_charges = value
            self.gauss_round_charge_timer = 30
    
    @property
    def ricochet_charges(self):
        """The amount of available Ricochet charges available."""
        return self._ricochet_charges
    
    @ricochet_charges.setter
    def ricochet_charges(self, value):
        if value < 0:
            raise ValueError("Ricochet charges cannot be set below zero.")
        elif value > 3:
            raise ValueError("Ricochet charges cannot be greater than 3.")
        else:
            self._ricochet_charges = value
    
    @property
    def gauss_round_charge_timer(self):
        """The amount of remaining time until the next Gauss Round charge accrual."""
        return self._gauss_round_charge_timer
    
    @gauss_round_charge_timer.setter
    def gauss_round_charge_timer(self, value):
        if value < 0:
            self.gauss_round_charges += 1
            self._gauss_round_charge_timer = 30
        elif self.gauss_round_charges == 3:
            self._gauss_round_charge_timer = 30
        else:
            self._gauss_round_charge_timer = value
    
    @property
    def ricochet_charge_timer(self):
        """The amount of remaining time until the next Ricochet charge accrual."""
        return self._ricochet_charge_timer
    
    @ricochet_charge_timer.setter
    def ricochet_charge_timer(self, value):
        if value < 0:
            self.ricochet_charges += 1
            self._ricochet_charge_timer = 30
        elif self.ricochet_charges == 3:
            self._ricochet_charge_timer = 30
        else:
            self._ricochet_charge_timer = value
    
    @property
    def hot_shot_cooldown(self):
        """The remaining cooldown on Hot Shot/Air Anchor in seconds."""
        return self._hot_shot_cooldown
    
    @hot_shot_cooldown.setter
    def hot_shot_cooldown(self, value):
        self._hot_shot_cooldown = max(0, value)
    
    @property
    def reassemble_cooldown(self):
        """The remaining cooldown on Reassemble in seconds."""
        return self._reassemble_cooldown
    
    @reassemble_cooldown.setter
    def reassemble_cooldown(self, value):
        self._reassemble_cooldown = max(0, value)
    
    @property
    def hypercharge_cooldown(self):
        """The remaining cooldown on Hypercharge in seconds."""
        return self._hypercharge_cooldown
    
    @hypercharge_cooldown.setter
    def hypercharge_cooldown(self, value):
        self._hypercharge_cooldown = max(0, value)
    
    @property
    def wildfire_cooldown(self):
        """The remaining cooldown on Wildfire in seconds."""
        return self._wildfire_cooldown
    
    @wildfire_cooldown.setter
    def wildfire_cooldown(self, value):
        self._wildfire_cooldown = max(0, value)
    
    @property
    def drill_cooldown(self):
        """The remaining cooldown on Drill in seconds."""
        return self._drill_cooldown
    
    @drill_cooldown.setter
    def drill_cooldown(self, value):
        self._drill_cooldown = max(0, value)
    
    @property
    def barrel_stabilizer_cooldown(self):
        """The remaining cooldown on Barrel Stabilizer in seconds."""
        return self._barrel_stabilizer_cooldown
    
    @barrel_stabilizer_cooldown.setter
    def barrel_stabilizer_cooldown(self, value):
        self._barrel_stabilizer_cooldown = max(0, value)
    
    @property
    def slug_shot_combo_ready(self):
        """Returns True if (Heated) Slug Shot combo action is ready."""
        return self._slug_shot_combo_ready
    
    @slug_shot_combo_ready.setter
    def slug_shot_combo_ready(self, value):
        if type(value) == bool:
            self._slug_shot_combo_ready = value
        else:
            return TypeError("slug_shot_combo_ready must be of type bool.")
    
    @property
    def clean_shot_combo_ready(self):
        """Returns True if (Heated) Clean Shot combo action is ready."""
        return self._clean_shot_combo_ready
    
    @clean_shot_combo_ready.setter
    def clean_shot_combo_ready(self, value):
        if type(value) == bool:
            self._clean_shot_combo_ready = value
        else:
            return TypeError("slug_shot_combo_ready must be of type bool.")
    
    @property
    def main_target(self):
        """The main target of the character."""
        return self._main_target
    
    @main_target.setter
    def main_target(self, value):
        self._main_target = value
    
    def reset_to_normal_global_cooldown(self):
        self.global_cooldown = self.base_global_cooldown
    
    def update_time(self, time_increment):
        callback = {}
        interrupting_events = []
        interrupting_events.append(('attack', self.auto_attack_recast_timer))

        if self.automaton is not None:
            interrupting_events.append(('automaton.remaining_duration', self.automaton.remaining_duration))
            interrupting_events.append(('automaton.attack_delay', self.automaton.attack_delay))
        
        if self.wildfire_applied:
            interrupting_events.append(('wildfire_duration', self.wildfire_duration))

        if len(interrupting_events) > 0 and any([x[-1] < time_increment for x in interrupting_events]):
            # Check if any interrupting event actually occurs during the current time increment.
            interrupting_events = sorted(interrupting_events, key=lambda event: event[-1])
            next_interrupting_event = interrupting_events[0]

            if next_interrupting_event[-1] < time_increment:
                if next_interrupting_event[0] == 'attack':
                    time_increment = self.auto_attack_recast_timer
                    self.total_time_elapsed += time_increment

                    callback['attack'] = self.attack()
                    callback['re-update time'] = time_increment
                elif next_interrupting_event[0] == 'automaton.attack_delay':
                    time_increment = self.automaton.attack_delay
                    self.total_time_elapsed += time_increment

                    if isinstance(self.automaton, RookAutoturret):
                        callback['rook_volley_fire'] = self.volley_fire()
                        callback['re-update time'] = time_increment
                    elif isinstance(self.automaton, AutomatonQueen):
                        # TODO: Implement Arm Punch and Roller Dash

                        # Automaton Queen opens with Roller Dash to close distance and then prioritizes Arm Punch
                        if self.automaton.initial_duration - self.automaton.remaining_duration > 5:
                            # Arm Punch
                            callback['queen_arm_punch'] = self.arm_punch()
                            callback['re-update time'] = time_increment
                        else:
                            # Roller Dash
                            callback['queen_roller_dash'] = self.roller_dash()
                            callback['re-update time'] = time_increment
                elif next_interrupting_event[0] == 'automaton.remaining_duration':
                    time_increment = self.automaton.remaining_duration
                    self.total_time_elapsed += time_increment

                    if isinstance(self.automaton, RookAutoturret):
                        callback['rook_overdrive'] = self.rook_overdrive()
                        callback['re-update time'] = time_increment
                    elif isinstance(self.automaton, AutomatonQueen):
                        callback['queen_overdrive'] = self.queen_overdrive()
                        callback['re-update time'] = time_increment
                elif next_interrupting_event[0] == 'wildfire_duration':
                    time_increment = self.wildfire_duration
                    self.total_time_elapsed += time_increment

                    callback['wildfire'] = self.wildfire_weaponskill_counter
                    callback['re-update time'] = time_increment

                    self.wildfire_duration = 0
        else:
            interrupting_events = []

        # Decrease timers
        self.gauss_round_charge_timer -= time_increment
        self.ricochet_charge_timer -= time_increment
        self.hot_shot_cooldown -= time_increment
        self.reassemble_cooldown -= time_increment
        self.hypercharge_cooldown -= time_increment
        self.wildfire_cooldown -= time_increment
        self.drill_cooldown -= time_increment
        self.barrel_stabilizer_cooldown -= time_increment

        if len(interrupting_events) > 0 and next_interrupting_event[0] == 'attack':
            # Do not decrement auto-attack recast timer if an auto-attack was just delivered.
            pass
        else:
            self.auto_attack_recast_timer -= time_increment

        if self.wildfire_applied:
            self.wildfire_duration -= time_increment
        
        if self.overheated:
            self.overheat_duration -= time_increment
        
        if self.automaton:
            if self.automaton.remaining_duration > 0:
                self.automaton.remaining_duration -= time_increment

            if len(interrupting_events) > 0 and next_interrupting_event[0] == 'automaton.attack_delay':
                # Do not decrement automaton attack timer if the automaton just acted.
                pass       
            else:
                self.automaton.attack_delay -= time_increment       

        # Advance global cooldown
        self.global_cooldown_timer -= time_increment

        return callback
    
    def attack(self, target=None):
        """
        An auto-attack. Delivers an attack with a potency and delay based on equipped weapon.
        """
        potency = self.auto_attack_potency
        self.auto_attack_recast_timer = self.auto_attack_delay

        return potency

    def split_shot(self, target=None):
        """
        lvl 1

        Delivers an attack with a potency of 160.

        **Additional Effect**: Increases Heat Gauge by 5
        """
        potency = 160

        self.slug_shot_combo_ready = True
        self.clean_shot_combo_ready = False
        self.heat_gauge += 5

        if self.wildfire_applied:
            self.wildfire_weaponskill_counter += 1

        logging.info('{0}: You use Split Shot.'.format(self.time_stamp))

        self.reset_to_normal_global_cooldown()
        self.on_global_cooldown = True

        if self.overheated:
            potency += 20

        return potency
    
    def slug_shot(self, target=None):
        """
        lvl 2

        Delivers an attack with a potency of 100.

        **Combo Action**: Split Shot or Heated Split Shot

        **Combo Potency**: 240

        **Combo Bonus**: Increases Heat Gauge by 5
        """
        potency = 100

        if self.slug_shot_combo_ready:
            potency = 240
            self.clean_shot_combo_ready = True
            self.slug_shot_combo_ready = False
        
        self.heat_gauge += 5

        if self.wildfire_applied:
            self.wildfire_weaponskill_counter += 1

        logging.info('{0}: You use Slug Shot.'.format(self.time_stamp))

        self.reset_to_normal_global_cooldown()
        self.on_global_cooldown = True

        if self.overheated:
            potency += 20

        return potency
    
    def hot_shot(self, target=None):
        """
        lvl 4

        Delivers an attack with a potency of 300.

        Base recast time: 40s

        **Additional Effect**: Increases Battery Gauge by 20

        This weaponskill does not share a recast timer with any other actions.
        """
        if self.hot_shot_cooldown > 0:
            logging.error('{0}: Hot Shot is still on cooldown.'.format(self.time_stamp))
            raise ValueError('Hot Shot is still on cooldown.')
        else:
            potency = 300

            self.battery_gauge += 20

            if self.wildfire_applied:
                self.wildfire_weaponskill_counter += 1

            logging.info('{0}: You use Hot Shot.'.format(self.time_stamp))
        
            self.hot_shot_cooldown = self.base_global_cooldown/2.5*40
            self.reset_to_normal_global_cooldown()
            self.on_global_cooldown = True

            if self.overheated:
                potency += 20

        return potency
    
    def reassemble(self):
        """
        lvl 10

        Next weaponskill will result in a critical direct hit.

        **Duration**: 5s

        Recast time: 60s
        """
        if self.reassemble_cooldown > 0:
            logging.error('{0}: Reassemble is still on cooldown.'.format(self.time_stamp))
            raise ValueError('Reassemble is still on cooldown.')
        else:
            self.reassembled = True

            self.reassemble_cooldown = 60

            logging.info('{0}: You gain the effect of Reassembled.'.format(self.time_stamp))

        return 0
    
    def gauss_round(self, target=None):
        """
        lvl 15

        Delivers an attack with a potency of 150.

        Charge Time: 30s

        **Maximum Charges**: 3
        """
        if self.gauss_round_charges < 1:
            logging.error('{0}: No Gauss Round charges available to use.'.format(self.time_stamp))
            raise ValueError('No Gauss Round charges available to use.')
        else:
            potency = 150
            self.gauss_round_charges -= 1

            logging.info('{0}: You use Gauss Round.'.format(self.time_stamp))
        
        return potency
    
    def spread_shot(self, target=None):
        """
        lvl 18

        Delivers an attack with a potency of 180 to all enemies in a cone before you.

        **Additional Effect**: Increases Heat Gauge by 5
        """
        potency = 180
        
        self.heat_gauge += 5

        if self.wildfire_applied:
            self.wildfire_weaponskill_counter += 1

        logging.info('{0}: You use Spread Shot.'.format(self.time_stamp))

        self.reset_to_normal_global_cooldown()
        self.on_global_cooldown = True

        return potency
    
    def clean_shot(self, target=None):
        """
        lvl 26

        Delivers an attack with a potency of 100.

        **Combo Action**: Slug Shot or Heated Slug Shot
        
        **Combo Potency**: 320

        **Combo Bonus**: Increases Heat Gauge by 5

        **Combo Bonus**: Increases Battery Gauge by 10
        """
        potency = 100

        if self.clean_shot_combo_ready:
            potency = 320
            self.heat_gauge += 5
            self.battery_gauge += 10

            self.clean_shot_combo_ready = False
            self.slug_shot_combo_ready = False
        
        if self.wildfire_applied:
            self.wildfire_weaponskill_counter += 1

        logging.info('{0}: You use Clean Shot.'.format(self.time_stamp))

        self.reset_to_normal_global_cooldown()
        self.on_global_cooldown = True

        if self.overheated:
            potency += 20
        
        return potency
    
    def hypercharge(self):
        """
        lvl 30

        Releases the energy building in your firearm, causing it to become Overheated, increasing the potency of single-target weaponskills by 20.

        **Duration**: 8s

        Extends effect duration if firearm is already overheated.

        **Heat Gauge Cost**: 50

        Recast time: 10s
        """
        if self.hypercharge_cooldown > 0:
            logging.error('{0}: Hypercharge is still on cooldown.'.format(self.time_stamp))
            raise ValueError('Hypercharge is still on cooldown.')
        elif self.heat_gauge >= 50:
            self.overheated = True
            self.overheat_duration += 8
            self.heat_gauge -= 50

            self.hypercharge_cooldown = 10

            logging.info('{0}: You use Hypercharge.'.format(self.time_stamp))
            logging.info('{0}: Your weapon has become overheated.'.format(self.time_stamp))
        elif self.heat_gauge < 50:
            logging.error('{0}: Hypercharge costs 50 Heat Gauge to use.'.format(self.time_stamp))
            raise ValueError('Hypercharge costs 50 Heat Gauge to use.')
        
        return 0
    
    def heat_blast(self, target=None):
        """
        lvl 35

        Delivers an attack with a potency of 200.

        **Additional Effect**: Reduces the recast time of both Gauss Round and Ricochet by 15s

        Can only be executed when firearm is Overheated.

        Recast timer cannot be affected by status effects or gear attributes.
        """
        if not self.overheated:
            logging.error('{0}: Heat Blast may only be used when firearm is Overheated.'.format(self.time_stamp))
            raise ValueError('Heat Blast may only be used when firearm is Overheated.')
        else:
            potency = 200

            self.global_cooldown = 1.5
            self.on_global_cooldown = True

            self.gauss_round_charge_timer -= 15
            self.ricochet_charge_timer -= 15

            if self.wildfire_applied:
                self.wildfire_weaponskill_counter += 1
        
        logging.info('{0}: You use Heat Blast.'.format(self.time_stamp))
        
        if self.overheated:
            potency += 20
        
        return potency
    
    def rook_autoturret(self, target=None):
        """
        lvl 40

        Deploys a single-target battle turret which attacks using Volley Fire, dealing damage with a potency of 80.

        **Battery Gauge Cost**: 50

        Duration increases as Battery Gauge exceeds required cost at time of deployment, up to a maximum of 15 seconds.

        Consumes Battery Gauge upon execution.

        Shuts down when time expires or upon execution of Rook Overdrive.

        Shares a recast timer with Rook Overdrive.

        Recast time: 6s
        """
        if self.battery_gauge >= 50:
            self.automaton = RookAutoturret(
                initial_duration=10+(self.battery_gauge-50)/10,
                attack_delay=1,  # TODO: This delay of one second is to model deployment delay.
                )
            self.battery_gauge = 0

            logging.info('{0}: You use Rook Autoturret.'.format(self.time_stamp))
        elif self.battery_gauge < 50:
            logging.error('{0}: Rook Autoturret requires a minimum of 50 Battery Gauge to use.'.format(self.time_stamp))
            raise ValueError('Rook Autoturret requires a minimum of 50 Battery Gauge to use.')
        
        return 0
    
    def volley_fire(self, target=None):
        """
        lvl 40

        Rook Autoturret's auto-attack.
        """
        if not self.automaton:
            logging.error('{0}: Rook Autoturret is not currently deployed.')
            raise ValueError('Rook Autoturret is not currently deployed.')
        else:
            potency = 80

            # TODO: What is the rook's auto-attack delay?
            self.automaton.attack_delay = 3

            logging.info('{0}: Rook Autoturret uses Volley Fire.'.format(self.time_stamp))

        return potency

    
    def rook_overdrive(self, target=None):
        """
        lvl 40

        Orders the rook autoturret to use Rook Overload.

        Delivers an attack with a potency of 400.

        Potency increases as remaining Battery Gauge exceeds required cost at time of deployment.

        The rook autoturret shuts down after execution. If this action is not used manually while the rook autoturret is active, it will be triggered automatically immediately before shutting down.

        Recast time: 15s
        """
        if not self.automaton or not isinstance(self.automaton, RookAutoturret):
            logging.error('{0}: Rook Autoturret is not currently deployed.')
            raise ValueError('Rook Autoturret is not currently deployed.')
        else:
            # TODO: Potency scales with initial deployment duration (self.automaton.initial_duration)
            potency = 400

            logging.info('{0}: Rook Autoturret gains the effect of Egi Assault III.'.format(self.time_stamp))
            logging.info('{0}: Rook Autoturret uses Rook Overload.'.format(self.time_stamp))

            self.automaton.remaining_duration = 0
            # self.automaton = None

        return potency
    
    def wildfire(self, target=None):
        """
        lvl 45

        Covers target's body in a slow-burning pitch. Action is changed to Detonator for the duration of the effect.

        Deals damage when time expires or upon executing Detonator.

        Potency is increased by 200 for each of your own weaponskills landed prior to the end of the effect.

        **Duration**: 10s

        Recast time: 120s
        """
        if self.wildfire_cooldown > 0:
            logging.error('{0}: Wildfire is still on cooldown.'.format(self.time_stamp))
            raise ValueError('Wildfire is still on cooldown.')
        else:
            self.wildfire_applied = True
            self.wildfire_weaponskill_counter = 0
            self.wildfire_cooldown = 120
            self.wildfire_duration = 10

            logging.info('{0}: You use Wildfire.'.format(self.time_stamp))

        return 0
    
    def ricochet(self, target=None):
        """
        lvl 50

        Deals damage to all nearby enemies with a potency of 150 for the first enemy, and 50% less for all remaining enemies.

        **Maximum Charges**: 3
        """
        if self.ricochet_charges < 1:
            logging.error('{0}: No Ricochet charges available to use.'.format(self.time_stamp))
            raise ValueError('No Ricochet charges available to use.')
        else:
            potency = 150
            self.ricochet_charges -= 1

            # TODO: AoE

            logging.info('{0}: You use Ricochet.'.format(self.time_stamp))
        
        return potency
    
    def auto_crossbow(self, target=None):
        """
        lvl 52

        Delivers an attack with a potency of 180 to all enemies in a cone before you.

        Can only be executed when firearm is Overheated.

        Recast timer cannot be affected by status effects or gear attributes.
        """
        if not self.overheated:
            return ValueError("Auto Crossbow may only be used when firearm is Overheated.")
        else:
            potency = 180

            #TODO: AoE

            self.global_cooldown = 1.5
            self.on_global_cooldown = True

            if self.wildfire_applied:
                self.wildfire_weaponskill_counter += 1

            logging.info('{0}: You use Auto Crossbow.'.format(self.time_stamp))
        
        return potency
    
    def heated_split_shot(self, target=None):
        """
        lvl 54

        Delivers an attack with a potency of 200.

        **Additional Effect**: Increases Heat Gauge by 5

        Upgraded from Split Shot
        """
        potency = 200

        self.slug_shot_combo_ready = True
        self.clean_shot_combo_ready = False
        self.heat_gauge += 5

        if self.wildfire_applied:
            self.wildfire_weaponskill_counter += 1

        logging.info('{0}: You use Heated Split Shot.'.format(self.time_stamp))

        self.reset_to_normal_global_cooldown()
        self.on_global_cooldown = True

        if self.overheated:
            potency += 20

        return potency

    def drill(self, target=None):
        """
        lvl 58

        Delivers an attack with a potency of 700.

        # **Additional Effect**: Increases Battery Gauge by 10

        Shares a recast timer with Bioblaster.

        Base recast time: 20s
        """
        if self.drill_cooldown > 0:
            logging.error('{0}: Drill is still on cooldown.'.format(self.time_stamp))
            raise ValueError('Drill is still on cooldown.')
        else:
            potency = 700
            # self.battery_gauge += 10

            self.drill_cooldown = self.base_global_cooldown/2.5*20

            if self.wildfire_applied:
                self.wildfire_weaponskill_counter += 1

            logging.info('{0}: You use Drill.'.format(self.time_stamp))

            self.reset_to_normal_global_cooldown()
            self.on_global_cooldown = True

            if self.overheated:
                potency += 20

        return potency
    
    def heated_slug_shot(self, target=None):
        """
        lvl 60

        Delivers an attack with a potency of 100.

        **Combo Action**: Heated Split Shot

        **Combo Potency**: 300

        **Combo Bonus**: Increases Heat Gauge by 5

        Upgraded from Slug Shot
        """
        potency = 100

        if self.slug_shot_combo_ready:
            potency = 300
            self.clean_shot_combo_ready = True
            self.slug_shot_combo_ready = False
        
        self.heat_gauge += 5

        if self.wildfire_applied:
            self.wildfire_weaponskill_counter += 1

        logging.info('{0}: You use Heated Slug Shot.'.format(self.time_stamp))

        self.reset_to_normal_global_cooldown()
        self.on_global_cooldown = True

        if self.overheated:
            potency += 20

        return potency
    
    def heated_clean_shot(self, target=None):
        """
        lvl 64

        Delivers an attack with a potency of 100.

        **Combo Action**: Heated Slug Shot
        
        **Combo Potency**: 400

        **Combo Bonus**: Increases Heat Gauge by 5

        **Combo Bonus**: Increases Battery Gauge by 10

        Upgraded from Clean Shot
        """
        potency = 100

        if self.clean_shot_combo_ready:
            potency = 400
            self.heat_gauge += 5
            self.battery_gauge += 10

            self.slug_shot_combo_ready = False
            self.clean_shot_combo_ready = False
        
        if self.wildfire_applied:
            self.wildfire_weaponskill_counter += 1

        logging.info('{0}: You use Heated Clean Shot.'.format(self.time_stamp))

        self.reset_to_normal_global_cooldown()
        self.on_global_cooldown = True

        if self.overheated:
            potency += 20
        
        return potency
    
    def barrel_stabilizer(self):
        """
        lvl 66

        Increases Heat Gauge by 50.

        Can only be executed while in combat.

        Recast time: 120s
        """
        if self.barrel_stabilizer_cooldown > 0:
            logging.error('{0}: Barrel Stabilizer is still on cooldown.'.format(self.time_stamp))
            raise ValueError('Barrel Stabilizer is still on cooldown.')
        else:
            self.heat_gauge += 50

            self.barrel_stabilizer_cooldown = 120

            logging.info('{0}: You use Barrel Stabilizer.'.format(self.time_stamp))

        return 0
    
    def flamethrower(self, target=None):
        """
        lvl 70

        Delivers damage over time to all enemies in a cone before you.

        **Potency**: 100

        **Duration**: 10s

        Effect ends upon using another action or moving (including facing a different direction).

        Cancels auto-attack upon execution.

        Triggers the cooldown of weaponskills upon execution. Cannot be executed during the cooldown of weaponskills.

        Base recast time: 60s
        """
        #TODO:
        pass
    
    def bio_blaster(self, target=None):
        """
        lvl 72

        Delivers an attack with a potency of 50 to all enemies in a cone before you.

        **Additional Effect**: Damage over time
        
        **Potency**: 60

        **Duration**: 15s

        **Additional Effect**: Increases Battery Gauge by 10

        Shares a recast timer with Drill.
        """
        #TODO:

        self.reset_to_normal_global_cooldown()
    
    def air_anchor(self, target=None):
        """
        lvl 76

        Delivers an attack with a potency of 700.

        **Additional Effect**: Increases Battery Gauge by 20

        This action does not share a recast timer with any other actions.

        Base recast time: 40s

        Upgraded from Hot Shot
        """
        if self.hot_shot_cooldown > 0:
            logging.error('{0}: Air Anchor is still on cooldown.'.format(self.time_stamp))
            raise ValueError('Air Anchor is still on cooldown.')
        else:
            potency = 700

            self.battery_gauge += 20

            if self.wildfire_applied:
                self.wildfire_weaponskill_counter += 1

            logging.info('{0}: You use Air Anchor.'.format(self.time_stamp))
        
            self.hot_shot_cooldown = self.base_global_cooldown/2.5*40
            # TODO: Cooldown changes with skill speed / base GCD.
            self.reset_to_normal_global_cooldown()
            self.on_global_cooldown = True

            if self.overheated:
                potency += 20

        return potency
    
    def automaton_queen(self, target=None):
        """
        lvl 80

        Deploys an Automaton Queen to fight at your side.

        **Battery Gauge Cost**: 50

        Duration increases as Battery Gauge exceeds minimum cost time at time of deployment, up to a maximum of 20 seconds.

        Consumes Battery Gauge upon execution.

        Shuts down when time expires or upon execution of Queen Overdrive.

        Shares a recast timer with Queen Overdrive.

        Recast time: 6s
        """
        if self.battery_gauge >= 50:
            # TODO: Determine Battery Gauge to duration function
            self.automaton = AutomatonQueen(
                initial_duration=10+(self.battery_gauge-50)/5,
                attack_delay=5,  # TODO: This delay is to model deployment delay.
                )
            self.battery_gauge = 0

            logging.info('{0}: You use Automaton Queen.'.format(self.time_stamp))
        elif self.battery_gauge < 50:
            logging.error('{0}: Automaton Queen requires a minimum of 50 Battery Gauge to use.'.format(self.time_stamp))
            raise ValueError('Automaton Queen requires a minimum of 50 Battery Gauge to use.')
        
        return 0
    
    def arm_punch(self, target=None):
        """
        Delivers an attack with a potency of 150.

        Recast time: 1.5s
        """
        if not self.automaton:
            logging.error('{0}: Automaton Queen is not currently deployed.')
            raise ValueError('Automaton Queen is not currently deployed.')
        else:
            potency = 150

            self.automaton.attack_delay = 1.5

            logging.info('{0}: Automaton Queen uses Arm Punch.'.format(self.time_stamp))

        return potency
    
    def roller_dash(self, target=None):
        """
        Rushes target and delivers an attack with a potency of 300.

        Base recast time: 3s
        """
        if not self.automaton:
            logging.error('{0}: Automaton Queen is not currently deployed.')
            raise ValueError('Automaton Queen is not currently deployed.')
        else:
            potency = 300

            self.automaton.attack_delay = self.base_global_cooldown/2.5*3

            logging.info('{0}: Automaton Queen uses Roller Dash.'.format(self.time_stamp))

        return potency
    
    def queen_overdrive(self, target=None):
        """
        Orders the Automaton Queen to use Pile Bunker.

        Shares a recast timer with Automaton Queen.

        Delivers an attack with a potency of 800.

        Potency increases as Batter Gauge exceeds required cost at time of deployment.

        The Automaton Queen shuts down after execution. If this action is not used manually while Automaton Queen is active, it will be triggered automatically immediately before shutting down.

        Recast time: 15s
        """
        if not self.automaton or not isinstance(self.automaton, AutomatonQueen):
            logging.error('{0}: Automaton Queen is not currently deployed.')
            raise ValueError('Automaton Queen is not currently deployed.')
        else:
            # TODO: Potency scales with initial deployment duration (self.automaton.initial_duration)
            potency = 800

            logging.info('{0}: Automaton Queen gains the effect of Egi Assault III.'.format(self.time_stamp))
            logging.info('{0}: Automaton Queen uses Pile Bunker.'.format(self.time_stamp))

            self.automaton.remaining_duration = 0
            # self.automaton = None

        return potency
