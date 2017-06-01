class Samurai():
    """
    SAM
    """

    def __init__(self):
        self._potency_mod = 1.0
        self._kenki_gauge = 0

        self._has_jinpu = False
        self._has_shifu = False

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

        self._enhanced_enbi = False
        self._open_eyes = False

    ## Properties
    # Potency modifier
    @property
    def potency_mod(self):
        return self._potency_mod

    @potency_mod.setter
    def potency_mod(self, value):
        if type(value) == bool:
            self._potency_mod = value

    def potency_mod_update(self):
        JINPU_MOD = 1.15
        SHIFU_MOD = 1.10

        self._potency_mod = 1.0

        if self.has_jinpu:
            self._potency_mod = 1.0*JINPU_MOD
        if self.has_shifu:
            self._potency_mod = SHIFU_MOD*self._potency_mod

    # Kenki gauge
    @property
    def kenki_gauge(self):
        return self._kenki_gauge

    @kenki_gauge.setter
    def kenki_gauge(self, value):
        self._kenki_gauge = value

    def inc_kenki_gauge(self, inc_amt):
        if type(inc_amt) == int:
            self._kenki_gauge += inc_amt

        if self._kenki_gauge < 0:
            kenki_gauge(0)
        elif self._kenki_gauge > 100:
            kenki_gauge(100)

    # Buffs
    @property
    def has_jinpu(self):
        return self._has_jinpu

    @has_jinpu.setter
    def has_jinpu(self, value):
        if type(value) == bool:
            self._has_jinpu = value

    @property
    def has_shifu(self):
        return self._has_shifu

    @has_shifu.setter
    def has_shifu(self, value):
        if type(value) == bool:
            self._has_shifu = value

    # Sen
    @property
    def has_getsu(self):
        return self._has_getsu

    @has_getsu.setter
    def has_getsu(self, value):
        if type(value) == bool:
            self._has_getsu = value

    @property
    def has_ka(self):
        return self._has_ka

    @has_ka.setter
    def has_ka(self, value):
        if type(value) == bool:
            self._has_ka = value

    @property
    def has_setsu(self):
        return self._has_setsu

    @has_setsu.setter
    def has_setsu(self, value):
        if type(value) == bool:
            self._has_setsu = value

    # Combo
    @property
    def combo_act_gekko(self):
        return self._combo_act_gekko

    @combo_act_gekko.setter
    def combo_act_gekko(self, value):
        if type(value) == bool:
            self._combo_act_gekko = value

    @property
    def combo_act_mangetsu(self):
        return self._combo_act_mangetsu

    @combo_act_mangetsu.setter
    def combo_act_magnetsu(self, value):
        if type(value) == bool:
            self._combo_act_mangetsu = value

    @property
    def combo_act_kasha(self):
        return self._combo_act_kasha

    @combo_act_kasha.setter
    def combo_act_kasha(self, value):
        if type(value) == bool:
            self._combo_act_kasha = value

    @property
    def combo_act_jinpu(self):
        return self._combo_act_jinpu

    @combo_act_jinpu.setter
    def combo_act_jinpu(self, value):
        if type(value) == bool:
            self._combo_act_jinpu = value

    @property
    def combo_act_shifu(self):
        return self._combo_act_shifu

    @combo_act_shifu.setter
    def combo_act_shifu(self, value):
        if type(value) == bool:
            self._combo_act_shifu = value

    @property
    def combo_act_oka(self):
        return self._combo_act_oka

    @combo_act_oka.setter
    def combo_act_oka(self, value):
        if type(value) == bool:
            self._combo_act_oka = value

    @property
    def combo_act_yukikaze(self):
        return self._combo_act_yukikaze

    @combo_act_yukikaze.setter
    def combo_act_yukikaze(self, value):
        if type(value) == bool:
            self._combo_act_yukikaze = value

    # Enhanced, procs, etc.
    @property
    def enhanced_enbi(self):
        return self._enhanced_enbi

    @enhanced_enbi.setter
    def enhanced_enbi(self, value):
        if type(value) == bool:
            self._enhanced_enbi = value

    @property
    def open_eyes(self):
        return self._open_eyes

    @open_eyes.setter
    def open_eyes(self, value):
        if type(value) == bool:
            self._open_eyes = value

            ## Weaponskills

    def hakaze(self):
        """ lvl 1 """

        potency = 150

        self.combo_act_yukikaze = True
        self.combo_act_shifu = True
        self.combo_act_jinpu = True

        self.inc_kenki_gauge(5)

        return self.potency_mod*potency

    def jinpu(self):
        """ lvl 4, combo Hakaze, damage up """

        if self.combo_act_jinpu:
            potency = 280
        else:
            potency = 100

        potency = self.potency_mod*potency # don't want buff before effect is applied

        self.combo_act_jinpu = False
        self.has_jinpu = True
        self.potency_mod_update()

        self.combo_act_gekko = True

        self.inc_kenki_gauge(5)

        return potency

    def gekko(self):
        """ lvl 30, combo Jinpu """

        if self.combo_act_gekko:
            potency = 400
        else:
            potency = 100

        self.combo_act_gekko = False
        self.has_getsu = True

        self.inc_kenki_gauge(10)

        return self.potency_mod*potency

    def shifu(self):
        """ lvl 18, combo Hakaze, haste """

        if self.combo_act_shifu:
            potency = 280
        else:
            potency = 100

        potency = self.potency_mod*potency # don't want updated potency before effect is applied

        self.combo_act_shifu = False
        self.has_shifu = True
        self.potency_mod_update()

        self.combo_act_kasha = True

        self.inc_kenki_gauge(5)

        return potency

    def kasha(self):
        """ lvl 40, combo Shifu """

        if self.combo_act_kasha:
            potency = 400
        else:
            potency = 100

        self.combo_act_kasha = False
        self.has_ka = True

        self.inc_kenki_gauge(10)

        return self.potency_mod*potency

    def yukikaze(self):
        """ lvl 50, combo Hakaze, slashing resist down """

        if self.combo_act_yukikaze:
            potency = 340
        else:
            potency = 100

        self.combo_act_yukikaze = False
        # add status to target?

        self.has_setsu = True

        self.inc_kenki_gauge(10)

        return self.potency_mod*potency

    def fuga(self, n_targets):
        """ lvl 26, cone AoE """

        potency = 100

        self.inc_kenki_gauge(5)

        return self.potency_mod*potency*n_targets

    def oka(self):
        """ lvl 45, combo Fuga, AoE """

        if self.combo_act_oka:
            if n_targets > 5:
                potency = 200*(1 + 0.9 + 0.8 + 0.7 + 0.6 + 0.5*(n_targets-5))
            elif n_targets > 4:
                potency = 200 * (1 + 0.9 + 0.8 + 0.7 + 0.6)
            elif n_targets > 3:
                potency = 200 * (1 + 0.9 + 0.8 + 0.7)
            elif n_targets > 2:
                potency = 200 * (1 + 0.9 + 0.8)
            elif n_targets > 1:
                potency = 200 * (1 + 0.9)
            else:
                potency = 200
        else:
            potency = 100

        self.combo_act_oka = False

        self.has_ka = True

        self.inc_kenki_gauge(10)

        return self.potency_mod*potency

    def mangetsu(self):
        """ lvl 35, combo Fuga, AoE """

        if self.combo_act_mangetsu:
            if n_targets > 5:
                potency = 200*(1 + 0.9 + 0.8 + 0.7 + 0.6 + 0.5*(n_targets-5))
            elif n_targets > 4:
                potency = 200 * (1 + 0.9 + 0.8 + 0.7 + 0.6)
            elif n_targets > 3:
                potency = 200 * (1 + 0.9 + 0.8 + 0.7)
            elif n_targets > 2:
                potency = 200 * (1 + 0.9 + 0.8)
            elif n_targets > 1:
                potency = 200 * (1 + 0.9)
            else:
                potency = 200
        else:
            potency = 100

        self.combo_act_mangetsu = False

        self.has_getsu = True

        self.inc_kenki_gauge(10)

        return self.potency_mod*potency

    def enbi(self):
        """ lvl 15, combo Hissatsu: Yaten, ranged """

        if self.enhanced_enbi:
            potency = 300
        else:
            potency = 100

        self.enhanced_enbi = False

        self.inc_kenki_gauge(10)

        return self.potency_mod*potency

    ## Iaijutsu
    def higanbana(self):
        """ 1 Sen Iaijutsu """
        if self.has_getsu or self.has_setsu or self.has_ka:
            potency = 240*self.potency_mod

            self.has_getsu = False
            self.has_setsu = False
            self.has_ka = False
        else:
            raise ValueError('No Sen opened!')

        return potency

    def higanbana_dot(self):
        """ DoT component of Higanbana """
        avg_mod = 3/2.2 # this averages the DoT potency per GCD (3 second ticks but ~2.2 GCD under Shifu)

        if self.has_jinpu:
            potency = 1.15*35*avg_mod
        else:
            potency = 35*avg_mod

        return potency

    def tenka_goken(self, n_targets):
        """ 2 Sen Iaijutsu """
        # AoE scaling

        if sum([self.has_getsu, self.has_setsu, self.has_ka]) == 2:
            if n_targets > 5:
                potency = 360*(1 + 0.9 + 0.8 + 0.7 + 0.6 + 0.5*(n_targets-5))
            elif n_targets > 4:
                potency = 360 * (1 + 0.9 + 0.8 + 0.7 + 0.6)
            elif n_targets > 3:
                potency = 360 * (1 + 0.9 + 0.8 + 0.7)
            elif n_targets > 2:
                potency = 360 * (1 + 0.9 + 0.8)
            elif n_targets > 1:
                potency = 360 * (1 + 0.9)
            else:
                potency = 360
        else:
            raise ValueError('Not enough Sen opened!')

        return self.potency_mod*potency

    def midare_setsugekka(self):
        """ 3 Sen Iaijutsu """

        if sum([self.has_getsu, self.has_setsu, self.has_ka]) == 3:
            potency = 720
        else:
            raise ValueError('Not enough Sen opened!')

        return self.potency_mod*potency

    ## Abilities
    def starry_eyes(self):
        """ lvl 66 """
        return

    def third_eye(self):
        """ lvl 6 """
        return

    def meditate(self):
        """ lvl 60, generate kenki """
        return

    def merciful_eyes(self):
        """ lvl 58, selfheal """
        return

    def meikyo_shisui(self):
        """ lvl 50, no combo prereqs """
        return

    def ageha(self):
        """ lvl 10, pseudo-execution """
        return

    def hagakure(self):
        """ lvl 68, convert Sen to Kenki """
        return

    ## Hissatsu
    def hissatsu_kaiten(self):
        """ lvl 52, weaponskill potency up """
        return

    def hissatsu_gyoten(self):
        """ lvl 54, gap closer """
        return

    def hissatsu_yaten(self):
        """ lvl 56, backstep """
        return

    def hissatsu_shinten(self):
        """ lvl 62, single target """
        return

    def hissatsu_kyuten(self):
        """ lvl 64, PBAoE """
        return

    def hissatsu_guren(self):
        """ lvl 70, line AoE """
        return