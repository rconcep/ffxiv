import pandas as pd
import string

# potency modifiers for each buff
JINPU_MOD = 1.15
SHIFU_MOD = 1.0
YUKIKAZE_MOD = 1.11
KAITEN_MOD = 1.5


class Samurai():
    """
    Far across the rolling waves, towards the rising sun, there lies the island nation of Hingashi.
    
    In the distant past, the realm's great lords vied for supremacy over its sea-girt confines in a long and bloody conflict. And taking to battle in their lieges' names were noble swordsmen whose art was forged in the crucible of war: the samurai.
    
    Eventually, the nation was unified under one banner, and these warriors came to wield their katana not upon fields as part of an army, but upon streets as protectors of the peace.
    
    But as a neglected blade grows dull with rust, so too do men forget their purpose. Amidst waning memories of the old ways, a determined few hold fast to their convictions, hands by katana grips, awaiting the moment for steel to sing.
    """

    def __init__(self, base_gcd=2.40, kenki_mastery=False, kenki_gauge=0):
        """
        Constructor for an instance of the Samurai class.
        """
        self._base_gcd = base_gcd
        self._current_gcd = self._base_gcd

        self._kenki_mastery = kenki_mastery

        self._potency_mod = 1.0
        self._kenki_gauge = kenki_gauge

        self._has_jinpu = False
        self._has_shifu = False

        self._applied_yukikaze = False
        self._applied_higanbana = 0

        self._has_meikyo_shisui = False

        self._has_hissatsu_kaiten = False

        self._has_getsu = False
        self._has_ka = False
        self._has_setsu = False

        self._combo_act_gekko = False
        self._combo_act_mangetsu = False
        self._combo_act_kasha = False
        self._combo_act_shifu = False
        self._combo_act_jinpu = False
        self._combo_act_oka = False
        self._combo_act_yukikaze = False

        self._enhanced_enpi = False
        self._open_eyes = False

    def parse_rotation(self, rotation, n_targets=1):
        """
        Creates a dataframe describing the given rotation.

        :param rotation: A list of tuples describing each GCD with strings.
         Each tuple takes the format (weaponskill, ability). If no ability is used, a 1-tuple may be supplied:
         ('weaponskill).

        :param n_targets: Number of targets available in the encounter. Defaults to 1.

        :return: df: A Pandas DataFrame object describing the rotation

        :return: average_potency: The average potency per GCD of the rotation

        :return: pps: The average potency per second of the rotation
        """

        parsed_gcds = []
        snapshot_dot_modifier = 0
        n_applied_higanbana = 0
        meikyo_shisui_counter = 3

        higanbana_timer = 0
        shifu_timer = 0
        jinpu_timer = 0
        yukikaze_timer = 0

        current_time = 0
        
        # string translator for text parsing
        translator = str.maketrans(' ', '_', string.punctuation)

        for k in range(len(rotation)):
            gcd = rotation[k]

            if type(gcd) != tuple:
                weaponskill = gcd
                ability = []
            else:
                weaponskill = gcd[0]
                ability = gcd[1]

            # convert input text to lowercase, replace punctuation, and replace spaces with underscores
            parsed_ws = weaponskill.lower().translate(translator)

            # record buff status at beginning of GCD
            buff_status = (self.has_jinpu, self.has_shifu, self.applied_yukikaze,
                           self.applied_higanbana, self.kenki_gauge)

            # compute potency of weaponskill
            if self.has_hissatsu_kaiten:
                # Hissatsu: Kaiten buff is active; apply increased potency
                ws_potency = KAITEN_MOD*getattr(self, parsed_ws)(n_targets)
                self.has_hissatsu_kaiten = False
            else:
                ws_potency = getattr(self, parsed_ws)(n_targets)

            if not ability:
                # use empty string to fill the ability value
                parsed_gcds.append((current_time, weaponskill, '', ws_potency
                                    + snapshot_dot_modifier*self.higanbana_dot())
                                   + buff_status)
            else:
                # convert input text to lowercase, replace punctuation, and replace spaces with underscores
                parsed_ability = ability.lower().translate(translator)

                parsed_gcds.append((current_time, weaponskill, ability, ws_potency
                                    + getattr(self, parsed_ability)(n_targets)
                                    + snapshot_dot_modifier*self.higanbana_dot())
                                   + buff_status)

                if parsed_ability == 'meikyo_shisui':
                    # allocate three weaponskills for Meikyo Shisui buff
                    meikyo_shisui_counter = 3

            # update Higanbana DoT potency
            if parsed_ws == 'higanbana':
                # add a target afflicted by Higanbana DoT
                n_applied_higanbana += 1

                if n_targets >= n_applied_higanbana:
                    # in this case, there are more total targets than those afflicted with Higanbana DoT
                    # snapshot buffs at time of DoT application and add to current DoT tick multiplier
                    snapshot_dot_modifier += JINPU_MOD if self.has_jinpu else 1.0

                    # update the number of targets afflicted by Higanbana DoT
                    self.applied_higanbana = n_applied_higanbana
                else:
                    # in this case, all targets have been afflicted with Higanbana DoT
                    # overwrite the DoT modifier due to clipping
                    snapshot_dot_modifier = JINPU_MOD if self.has_jinpu else 1.0

                    # max out the number of afflicted targets
                    self.applied_higanbana = n_targets

            # update counters
            if parsed_ws not in set(['higanbana', 'tenka goken', 'midare setsugekka']):
                # Iaijutsu does not consume a Meikyo Shisui charge
                meikyo_shisui_counter -= 1  # expended one Meikyo Shisui charge

            if meikyo_shisui_counter <= 0:
                # deactivate Meikyo Shisui if all charges expended
                self.has_meikyo_shisui = False

            if parsed_ws == 'higanbana':
                # start Higanbana DoT timer
                # accounts for cast time
                higanbana_timer = 60 + 1.8/2.5*self.current_gcd

            if parsed_ws == 'shifu':
                # start Shifu buff timer
                shifu_timer = 30

            if parsed_ws == 'jinpu':
                # start Jinpu buff timer
                jinpu_timer = 30

            if parsed_ws == 'yukikaze':
                # start slashing resistance down timer
                yukikaze_timer = 30

            # update time and timers
            if self.has_shifu:
                # Shifu haste buff reduces recast time/GCD
                self.current_gcd = 0.90*self.base_gcd

            current_time += self.current_gcd
            higanbana_timer -= self.current_gcd
            shifu_timer -= self.current_gcd
            jinpu_timer -= self.current_gcd
            yukikaze_timer -= self.current_gcd

            if higanbana_timer <= 0:
                # DoT has fallen off
                n_applied_higanbana = 0
                self.applied_higanbana = 0
                snapshot_dot_modifier = 0
            if shifu_timer <= 0:
                # Shifu has fallen off
                self.has_shifu = False
            if jinpu_timer <= 0:
                # Jinpu has fallen off
                self.has_jinpu = False
            if yukikaze_timer <= 0:
                # Slashing resistance down has fallen off
                self.applied_yukikaze = False

        # form output DataFrame and metrics
        df = pd.DataFrame(parsed_gcds,
                          columns=['Time', 'Weaponskill', 'Ability', 'Potency',
                                   'Jinpu', 'Shifu', 'Yukikaze', 'Higanbana',
                                   'Kenki'])
        df['Total Potency'] = df['Potency'].cumsum(axis=0)

        average_potency = df['Potency'].mean()
        potency_ps = df['Total Potency'].max()/current_time

        print('average potency per GCD = %s' % average_potency)
        print('average potency per second = %s' % potency_ps)

        return df, average_potency, potency_ps

    @property
    def base_gcd(self):
        """The base GCD length in seconds."""
        return self._base_gcd

    @base_gcd.setter
    def base_gcd(self, value):
        raise NotImplementedError('The base GCD may only be set in the constructor!')

    @property
    def current_gcd(self):
        """The current GCD length in seconds."""
        return self._current_gcd

    @current_gcd.setter
    def current_gcd(self, value):
        if type(value) == float:
            self._current_gcd = value

    @property
    def kenki_mastery(self):
        """Kenki Mastery II trait is active if True; False if Kenki Mastery I only."""
        return self._kenki_mastery

    @kenki_mastery.setter
    def kenki_mastery(self, value):
        raise NotImplementedError('Kenki Mastery may only be set in the constructor!')

    @property
    def potency_mod(self):
        """Potency modifier based on Jinpu buff and slashing resistance down debuff."""
        return self._potency_mod

    @potency_mod.setter
    def potency_mod(self, value):
        if type(value) == bool:
            self._potency_mod = value

    def potency_mod_update(self):
        """Method to update the potency modifier when weaponskills are used."""
        self._potency_mod = 1.0

        if self.has_jinpu:
            self._potency_mod = 1.0*JINPU_MOD
        if self.applied_yukikaze:
            self._potency_mod = YUKIKAZE_MOD*self._potency_mod

    @property
    def kenki_gauge(self):
        """The current Kenki gauge reading."""
        return self._kenki_gauge

    @kenki_gauge.setter
    def kenki_gauge(self, value):
        self._kenki_gauge = value

    def inc_kenki_gauge(self, inc_amt):
        """Changes the Kenki gauge amount by inc_amt."""
        if type(inc_amt) == int:
            self.kenki_gauge += inc_amt

            if self.kenki_gauge < 0:
                self.kenki_gauge = 0
            elif self.kenki_gauge > 100:
                self.kenki_gauge = 100
        else:
            raise TypeError('Must provide int to change Kenki gauge by!')

    @property
    def has_jinpu(self):
        """If the Jinpu buff is active."""
        return self._has_jinpu

    @has_jinpu.setter
    def has_jinpu(self, value):
        if type(value) == bool:
            self._has_jinpu = value

    @property
    def has_shifu(self):
        """If the Shifu buff is active."""
        return self._has_shifu

    @has_shifu.setter
    def has_shifu(self, value):
        if type(value) == bool:
            self._has_shifu = value

    @property
    def applied_yukikaze(self):
        """If the slashing resistance down debuff from Yukikaze is applied."""
        return self._applied_yukikaze

    @applied_yukikaze.setter
    def applied_yukikaze(self, value):
        if type(value) == bool:
            self._applied_yukikaze = value

    @property
    def applied_higanbana(self):
        """Number of targets afflicted with the Higanbana DoT."""
        return self._applied_higanbana

    @applied_higanbana.setter
    def applied_higanbana(self, n_applied):
        if type(n_applied) == int:
            self._applied_higanbana = n_applied

    @property
    def has_meikyo_shisui(self):
        """If the Meikyo Shisui buff is active."""
        return self._has_meikyo_shisui

    @has_meikyo_shisui.setter
    def has_meikyo_shisui(self, value):
        if type(value) == bool:
            self._has_meikyo_shisui = value

    def meikyo_shisui_active(self):
        """The Meikyo Shisui buff allows combo bonuses without executing combos for up to three weaponskills."""
        if self.has_meikyo_shisui:
            self.combo_act_gekko = True
            self.combo_act_mangetsu = True
            self.combo_act_kasha = True
            self.combo_act_shifu = True
            self.combo_act_jinpu = True
            self.combo_act_oka = True
            self.combo_act_yukikaze = True
        else:
            self.combo_act_gekko = False
            self.combo_act_mangetsu = False
            self.combo_act_kasha = False
            self.combo_act_shifu = False
            self.combo_act_jinpu = False
            self.combo_act_oka = False
            self.combo_act_yukikaze = False

    @property
    def has_hissatsu_kaiten(self):
        """If the Hissatsu: Kaiten buff is active."""
        return self._has_hissatsu_kaiten

    @has_hissatsu_kaiten.setter
    def has_hissatsu_kaiten(self, value):
        if type(value) == bool:
            self._has_hissatsu_kaiten = value

    @property
    def has_getsu(self):
        """If the Getsu Sen is opened."""
        return self._has_getsu

    @has_getsu.setter
    def has_getsu(self, value):
        if type(value) == bool:
            self._has_getsu = value

    @property
    def has_ka(self):
        """If the Ka Sen is opened."""
        return self._has_ka

    @has_ka.setter
    def has_ka(self, value):
        if type(value) == bool:
            self._has_ka = value

    @property
    def has_setsu(self):
        """If the Setsu Sen is opened."""
        return self._has_setsu

    @has_setsu.setter
    def has_setsu(self, value):
        if type(value) == bool:
            self._has_setsu = value

    @property
    def combo_act_gekko(self):
        """If the Gekko combo bonus is applicable."""
        return self._combo_act_gekko

    @combo_act_gekko.setter
    def combo_act_gekko(self, value):
        if type(value) == bool:
            self._combo_act_gekko = value

    @property
    def combo_act_mangetsu(self):
        """If the Mangetsu combo bonus is applicable."""
        return self._combo_act_mangetsu

    @combo_act_mangetsu.setter
    def combo_act_mangetsu(self, value):
        if type(value) == bool:
            self._combo_act_mangetsu = value

    @property
    def combo_act_kasha(self):
        """If the Kasha combo bonus is applicable."""
        return self._combo_act_kasha

    @combo_act_kasha.setter
    def combo_act_kasha(self, value):
        if type(value) == bool:
            self._combo_act_kasha = value

    @property
    def combo_act_jinpu(self):
        """If the Jinpu combo bonus is available."""
        return self._combo_act_jinpu

    @combo_act_jinpu.setter
    def combo_act_jinpu(self, value):
        if type(value) == bool:
            self._combo_act_jinpu = value

    @property
    def combo_act_shifu(self):
        """If the Shifu combo bonus is available."""
        return self._combo_act_shifu

    @combo_act_shifu.setter
    def combo_act_shifu(self, value):
        if type(value) == bool:
            self._combo_act_shifu = value

    @property
    def combo_act_oka(self):
        """If the Oka combo bonus is available."""
        return self._combo_act_oka

    @combo_act_oka.setter
    def combo_act_oka(self, value):
        if type(value) == bool:
            self._combo_act_oka = value

    @property
    def combo_act_yukikaze(self):
        """If the Yukikaze combo bonus is available."""
        return self._combo_act_yukikaze

    @combo_act_yukikaze.setter
    def combo_act_yukikaze(self, value):
        if type(value) == bool:
            self._combo_act_yukikaze = value

    @property
    def enhanced_enpi(self):
        """If the Enhanced Enpi status is active."""
        return self._enhanced_enbi

    @enhanced_enpi.setter
    def enhanced_enpi(self, value):
        if type(value) == bool:
            self._enhanced_enbi = value

    @property
    def open_eyes(self):
        """If the Open Eyes status from Third Eye is active."""
        return self._open_eyes

    @open_eyes.setter
    def open_eyes(self, value):
        if type(value) == bool:
            self._open_eyes = value

    def hakaze(self, n_targets=1):
        """
        lvl 1

        Delivers an attack with a potency of 150.

        **Additional Effect**: Increases Kenki Gauge by 5
        """
        potency = 150

        self.combo_act_yukikaze = True
        self.combo_act_shifu = True
        self.combo_act_jinpu = True

        if self.kenki_mastery:
            self.inc_kenki_gauge(5)

        return self.potency_mod*potency

    def jinpu(self, n_targets=1):
        """
        lvl 4

        Delivers an attack with a potency of 100.

        **Combo Action**: Hakaze

        **Combo Potency**: 280

        **Combo Bonus**: Increases damage dealt by 15%

        **Duration**: 30s

        **Combo Bonus**: Increases Kenki Gauge by 5
        """
        if self.combo_act_jinpu:
            potency = 280
            self.has_jinpu = True
            self.combo_act_gekko = True
            if self.kenki_mastery:
                self.inc_kenki_gauge(5)
        else:
            potency = 100

        potency = self.potency_mod*potency  # don't want buff before effect is applied

        self.combo_act_jinpu = False
        self.potency_mod_update()

        return potency

    def gekko(self, n_targets=1):
        """
        lvl 30

        Delivers an attack with a potency of 100.

        **Combo Action**: Jinpu

        **Combo Potency**: 400

        **Rear Combo Bonus**: Increases Kenki Gauge by 10

        **Combo Bonus**: Grants Getsu
        """
        if self.combo_act_gekko:
            potency = 400
            self.has_getsu = True
            self.inc_kenki_gauge(10)
        else:
            potency = 100

        self.combo_act_gekko = False

        return self.potency_mod*potency

    def shifu(self, n_targets=1):
        """
        lvl 18

        Delivers an attack with a potency of 100.

        **Combo Action**: Hakaze

        **Combo Potency**: 280

        **Combo Bonus**: Reduces weaponskill cast time and recast time, spell cast time and recast time,
        and auto-attack delay by 10%

        **Duration**: 30s

        **Combo Bonus**: Increases Kenki Gauge by 5
        """
        if self.combo_act_shifu:
            potency = 280
            self.has_shifu = True
            self.combo_act_kasha = True
            if self.kenki_mastery:
                self.inc_kenki_gauge(5)
        else:
            potency = 100

        potency = self.potency_mod*potency # don't want updated potency before effect is applied

        self.combo_act_shifu = False
        self.potency_mod_update()

        return potency

    def kasha(self, n_targets=1):
        """
        lvl 40

        Delivers an attack with a potency of 100.

        **Combo Action**: Shifu

        **Combo Potency**: 400

        **Side Combo Bonus**: Increases Kenki Gauge by 10

        **Combo Bonus**: Grants Ka
        """
        if self.combo_act_kasha:
            potency = 400
            self.has_ka = True
            self.inc_kenki_gauge(10)
        else:
            potency = 100

        self.combo_act_kasha = False

        return self.potency_mod*potency

    def yukikaze(self, n_targets=1):
        """
        lvl 50

        Delivers an attack with a potency of 100.

        **Combo Action**: Hakaze

        **Combo Potency**: 340

        **Combo Bonus**: Reduces target's slashing resistance by 10%

        **Duration**: 30s

        **Combo Bonus**: Increases Kenki Gauge by 10

        **Combo Bonus**: Grants Setsu
        """
        if self.combo_act_yukikaze:
            potency = 340
            self.applied_yukikaze = True
            self.has_setsu = True
            self.inc_kenki_gauge(10)
        else:
            potency = 100

        potency = self.potency_mod*potency # don't want updated potency before effect is applied

        self.combo_act_yukikaze = False
        # add status to target?

        self.potency_mod_update()

        return potency

    def fuga(self, n_targets):
        """
        lvl 26

        Delivers an attack with a potency of 100 to all enemies in a cone before you.

        **Additional Effect**: Increases Kenki Gauge by 5
        """
        potency = 100

        self.combo_act_mangetsu = True
        self.combo_act_oka = True

        if self.kenki_mastery:
            self.inc_kenki_gauge(5)

        return self.potency_mod*potency*n_targets

    def oka(self, n_targets):
        """
        lvl 45

        Delivers an attack with a potency of 100 to all nearby enemies.

        **Combo Action**: Fuga

        **Combo Potency**: 200 for the first enemy, 10% less for the second, 20% less for the third,
        30% less for the fourth, 40% less for the fifth, and 50% less for all remaining enemies

        **Combo Bonus**: Increases Kenki Gauge by 10

        **Combo Bonus**: Grants Ka
        """
        base_potency = 200

        if self.combo_act_oka:
            if n_targets > 5:
                potency = base_potency*(1 + 0.9 + 0.8 + 0.7 + 0.6 + 0.5*(n_targets-5))
            elif n_targets > 4:
                potency = base_potency * (1 + 0.9 + 0.8 + 0.7 + 0.6)
            elif n_targets > 3:
                potency = base_potency * (1 + 0.9 + 0.8 + 0.7)
            elif n_targets > 2:
                potency = base_potency * (1 + 0.9 + 0.8)
            elif n_targets > 1:
                potency = base_potency * (1 + 0.9)
            else:
                potency = base_potency

            self.has_ka = True
            self.inc_kenki_gauge(10)
        else:
            potency = 100

        self.combo_act_oka = False

        return self.potency_mod*potency

    def mangetsu(self, n_targets):
        """
        lvl 35

        Delivers an attack with a potency of 100 to all nearby enemies.

        **Combo Action**: Fuga

        **Combo Potency**: 200 for the first enemy, 10% less for the second, 20% less for the third,
        30% less for the fourth, 40% less for the fifth, and 50% less for all remaining enemies

        **Combo Bonus**: Increases Kenki Gauge by 10

        **Combo Bonus**: Grants Getsu
        """
        base_potency = 200

        if self.combo_act_mangetsu:
            if n_targets > 5:
                potency = base_potency*(1 + 0.9 + 0.8 + 0.7 + 0.6 + 0.5*(n_targets-5))
            elif n_targets > 4:
                potency = base_potency * (1 + 0.9 + 0.8 + 0.7 + 0.6)
            elif n_targets > 3:
                potency = base_potency * (1 + 0.9 + 0.8 + 0.7)
            elif n_targets > 2:
                potency = base_potency * (1 + 0.9 + 0.8)
            elif n_targets > 1:
                potency = base_potency * (1 + 0.9)
            else:
                potency = base_potency

            self.has_getsu = True
            self.inc_kenki_gauge(10)
        else:
            potency = 100

        self.combo_act_mangetsu = False

        return self.potency_mod*potency

    def enpi(self, n_targets=1):
        """
        lvl 15

        Delivers a ranged attack with a potency of 100.

        **Yaten Bonus Potency**: 300

        **Additional Effect**: Increases Kenki Gauge by 10
        """
        if self.enhanced_enbi:
            potency = 300
        else:
            potency = 100

        self.enhanced_enbi = False

        if self.kenki_mastery:
            self.inc_kenki_gauge(10)

        return self.potency_mod*potency

    def higanbana(self, n_targets=1):
        """
        Delivers an attack with a potency of 240.

        **Additional Effect**: Damage over time

        **Potency**: 35

        **Duration**: 60s
        """
        if self.has_getsu or self.has_setsu or self.has_ka:
            potency = 240*self.potency_mod

            self.has_getsu = False
            self.has_setsu = False
            self.has_ka = False
        else:
            raise ValueError('No Sen opened!')

        return potency

    def higanbana_dot(self, n_targets=1):
        """
        DoT component of Higanbana.
        """
        avg_mod = self.current_gcd/3.0  # this averages the DoT potency per GCD (3 second ticks)

        if self.has_jinpu:
            potency = JINPU_MOD*35*avg_mod
        else:
            potency = 35*avg_mod

        return potency

    def tenka_goken(self, n_targets):
        """
        Delivers an attack to all nearby enemies with a potency of 360 for the first enemy, 10% less for the second,
        20% less for the third, 30% less for the fourth, 40% less for the fifth, and 50% less for all remaining enemies.
        """
        base_potency = 360

        if sum([self.has_getsu, self.has_setsu, self.has_ka]) == 2:
            if n_targets > 5:
                potency = base_potency*(1 + 0.9 + 0.8 + 0.7 + 0.6 + 0.5*(n_targets-5))
            elif n_targets > 4:
                potency = base_potency * (1 + 0.9 + 0.8 + 0.7 + 0.6)
            elif n_targets > 3:
                potency = base_potency * (1 + 0.9 + 0.8 + 0.7)
            elif n_targets > 2:
                potency = base_potency * (1 + 0.9 + 0.8)
            elif n_targets > 1:
                potency = base_potency * (1 + 0.9)
            else:
                potency = base_potency
        else:
            raise ValueError('Not enough Sen opened!')

        return self.potency_mod*potency

    def midare_setsugekka(self, n_targets=1):
        """
        Delivers an attack with a potency of 720.
        """
        if sum([self.has_getsu, self.has_setsu, self.has_ka]) == 3:
            potency = 720
        else:
            raise ValueError('Not enough Sen opened!')

        return self.potency_mod*potency

    def hissatsu_seigan(self, n_targets=1):
        """
        lvl 66

        Delivers an attack with a potency of 200.

        **Kenki Gauge Cost**: 15

        Can only be executed while under the effect of Open Eyes.

        Shares a recast timer with Merciful Eyes.
        """
        potency = 200
        kenki_cost = 25

        if self.kenki_gauge >= kenki_cost:
            if self.open_eyes:
                return potency*self.potency_mod
            else:
                raise ValueError('Open Eyes status not active!')
        else:
            raise ValueError('Not enough Kenki available!')

    def third_eye(self):
        """
        lvl 6

        **Recast**: 15s

        Grants the Open Eyes status, reducing the amount of damage taken by the next attack by 20%.

        **Duration**: 3s
        """
        self.open_eyes = True
        return 0

    def meditate(self):
        """
        lvl 60

        **Recast**: 60s

        Gradually increases your Kenki Gauge.

        **Duration**: 15s

        Kenki Gauge not affected when used outside battle.

        Cancels auto-attack upon execution.
        """
        return 0

    def merciful_eyes(self):
        """
        lvl 58

        **Recast**: 1s

        Instantly restores own HP.

        **Cure Potency**: 500

        Cure potency varies with current attack power.

        Can only be executed while under the effect of Open Eyes.

        Shares a recast timer with Starry Eyes.
        """
        return 0

    def meikyo_shisui(self, n_targets=1):
        """
        lvl 50

        **Recast**: 80s

        Execute up to 3 combos without meeting combo prerequisites.

        **Duration**: 10s
        """
        self.has_meikyo_shisui = True
        self.meikyo_shisui_active()
        return 0

    def ageha(self, n_targets=1):
        """
        lvl 10

        **Recast**: 60s

        Delivers an attack with a potency of 250.

        **Additional Effect**: Increases Kenki Gauge by 10

        If target's HP is 20% or less and killing blow is dealt, Kenki Gauge will increase by 20.

        *Only available if target's HP is 20% or less*
        """
        potency = 250
        self.inc_kenki_gauge(10)

        return potency*self.potency_mod

    def hagakure(self, n_targets=1):
        """
        lvl 68

        **Recast**: 40s

        Converts Setsu, Getsu, and Ka into Kenki. Each Sen converted increases your Kenki Gauge by 20. Can only be
        executed if under the effect of at least one of the three statuses.
        """
        sen_total = sum([self.has_setsu + self.has_getsu + self.has_ka])

        if sen_total > 0:
            self.inc_kenki_gauge(sen_total*20)
            self.has_setsu = False
            self.has_getsu = False
            self.has_ka = False
        else:
            raise ValueError('No Sen open to convert!')

        return 0

    def hissatsu_kaiten(self, n_targets=1):
        """
        lvl 52

        **Recast**: 5s

        Increases potency of next weaponskill by 50%.

        **Duration**: 10s

        **Kenki Gauge Cost**: 20
        """
        kenki_cost = 20

        if self.kenki_gauge >= kenki_cost:
            self.has_hissatsu_kaiten = True
            self.inc_kenki_gauge(-kenki_cost)
            return 0
        else:
            raise ValueError('Not enough Kenki available!')

    def hissatsu_gyoten(self, n_targets=1):
        """
        lvl 54

        **Recast**: 10s

        Rushes target and delivers an attack with a potency of 100.

        **Kenki Gauge Cost**: 10

        Cannot be executed while bound.
        """
        potency = 100
        kenki_cost = 10

        if self.kenki_gauge >= kenki_cost:
            self.inc_kenki_gauge(-kenki_cost)
            return potency*self.potency_mod
        else:
            raise ValueError('Not enough Kenki available!')

    def hissatsu_yaten(self, n_targets=1):
        """
        lvl 56

        **Recast**: 10s

        Delivers an attack with a potency of 100.

        **Additional Effect**: 10-yalm backstep

        **Additional Effect**: Grants Enhanced Enbi

        **Kenki Gauge Cost**: 10

        Cannot be executed while bound.
        """
        potency = 100
        kenki_cost = 10

        if self.kenki_gauge >= kenki_cost:
            self.inc_kenki_gauge(-kenki_cost)
            self.enhanced_enbi = True
            return potency * self.potency_mod
        else:
            raise ValueError('Not enough Kenki available!')

    def hissatsu_shinten(self, n_targets=1):
        """
        lvl 62

        **Recast**: 1s

        Delivers an attack with a potency of 300.

        **Kenki Gauge Cost**: 25
        """
        potency = 300
        kenki_cost = 25

        if self.kenki_gauge >= kenki_cost:
            self.inc_kenki_gauge(-kenki_cost)
            return potency * self.potency_mod
        else:
            raise ValueError('Not enough Kenki available!')

    def hissatsu_kyuten(self, n_targets):
        """
        lvl 64

        **Recast**: 1s

        Delivers an attack with a potency of 150 to all nearby enemies.

        **Kenki Gauge Cost**: 25
        """
        potency = n_targets*150
        kenki_cost = 25

        if self.kenki_gauge >= kenki_cost:
            self.inc_kenki_gauge(-kenki_cost)
            return potency * self.potency_mod
        else:
            raise ValueError('Not enough Kenki available!')


    def hissatsu_guren(self, n_targets):
        """
        lvl 70

        **Recast**: 120s

        Delivers an attack to all enemies in a straight line before you with a potency of 800 for the first enemy,
        25% less for the second, and 50% less for all remaining enemies.

        **Kenki Gauge Cost**: 50
        """
        base_potency = 800
        kenki_cost = 50

        if self.kenki_gauge >= kenki_cost:
            self.inc_kenki_gauge(-kenki_cost)

            if n_targets > 2:
                potency = base_potency*(1+0.75+0.50*(n_targets-2))
            elif n_targets > 1:
                potency = base_potency*(1+0.75)
            else:
                potency = base_potency

            return potency * self.potency_mod
        else:
            raise ValueError('Not enough Kenki available!')

