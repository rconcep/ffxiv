Tutorial
========

.. module:: samurai

The Samurai class is intended to represent a samurai player in combat. Features include:

* Checking for the appropriate amount of Sen opened when using Iaijutsu.
* Checking for the appropriate amount of Kenki when using Kenki spenders.
* Combo bonuses applied when appropriate.
* Buff applications adjusting outgoing potency and GCD length.

It **does not** include:

* Correctly breaking combos.

  * e.g., You use Hakaze -> Shifu -> Hakaze -> Kasha. The combo bonus for Kasha will still apply.
  * However, doing something like Hakaze -> Yukikaze -> Yukikaze will correctly not apply the combo bonus to the second Yukikaze. Obviously, this does not apply to Meikyo Shisui.
  * This behavior was not implemented because it is illogical to do in practice.

* Applying slashing resistance down to multiple targets.

  * If Yukikaze is used in multiple target scenarios, the damage increase will be applied to all targets.
  * This behavior was not implemented because it is not something you should do in practice.

* Cooldown timer tracking.
  
  * Jinpu, Shifu, Yukikaze, and Higanbana DoT timers are supported.
  * However, it is up to the user to keep track of the cooldown of abilities.

    * Meikyo Shisui, Hagakure, Hissatsu: Guren, Hissatsu: Kaiten, etc.

* Auto attacks.
  
  * This class is only intended to analyze potency per second of different weaponskill/ability rotations.

* The effect of attack power, critical hit, direct hit, determination, and damage per second calculations. Additionally, the effect of external buffs.

  * The impact of primary/secondary stats on DPS require damage formula implementation.

Usage
-----

To use this class, first you must import the class from its module and then create an instance of it:

::

  from samurai import Samurai
  
  my_first_samurai = Samurai()

There are a number of keyword arguments that may be used to modify the initial state of the Samurai instance.

::
  
  my_first_samurai = Samurai(base_gcd=2.40, kenki_mastery=0, kenki_gauge=0)

:attr:`Samurai.base_gcd` is set as 2.40s by default. :attr:`Samurai.kenki_mastery` is set to 0 by default, meaning no Kenki Mastery trait is active. Values of 1 and 2 correspond to the Mastery I and II traits, respectively. Note that these two attributes may only be set upon initialization and cannot be changed.

:attr:`Samurai.kenki_gauge` is set to 0 initially be default but may be set to a valid amount upon initialization or anytime afterwards.

After initialization, other initial conditions may be set prior to simulated combat. For example, to use Meikyo Shisui before the encounter starts:

::
  
  my_first_samurai = Samurai(kenki_mastery=2)
  my_first_samurai.meikyo_shisui()

This will trigger the effect of :meth:`Samurai.meikyo_shisui()`. To simulate the slashing resistance debuff being already applied:

::
  
  my_first_samurai.applied_yukikaze = True

The heart of this simulation tool is the :meth:`Samurai.parse_rotation()` class method. This method takes an input list of tuples describing the rotation to be simulated and tracks buffs/debuffs, Kenki, Sen, and output potency over time. It may be used to simulate against single or multiple targets. For example, to simulate the Gekko combo against a single target:

::

  my_first_samurai = Samurai(kenki_mastery=2)
  
  action_list = [('Hakaze'), ('Jinpu'), ('Gekko')]
  
  out_dataframe, out_avg_potency, out_potency_ps = my_first_samurai.parse_rotation(action_list)

The method output consists of a Pandas DataFrame object describing the simulated rotation, the average potency per GCD, and the average potency per second. The output DataFrame is compatible with the included visualization utilities in :mod:`plotting` but is also viewable just by using :func:`print()` or :func:`display()` in Jupyter notebooks.

The action list provided to the :meth:`parse_rotation()` method consists of tuples with the format:

::

  [(weaponskill_1, ability_1), ..., (weaponskill_N, ability_N)]

where the weaponskills and abilities are provided as strings. The ability is considered to be used during the GCD of the corresponding weaponskill. An ability does not have to be provided. Here is an example of simulating a scenario with multiple targets:

::

  n_targets = 5
  my_first_samurai = Samurai(kenki_mastery=2, n_targets=n_targets)
  
  action_list = [('Fuga'), ('Oka'), ('Fuga'), ('Mangetsu', 'Hissatsu: Kaiten'), ('Tenka Goken')]
  
  out_dataframe, out_avg_potency, out_potency_ps = my_first_samurai.parse_rotation(action_list)


