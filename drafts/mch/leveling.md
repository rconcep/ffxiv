# Machinist

## Introduction

Machinist has undergone a complete rework in Shadowbringers. In Stormblood, Machinist was a job centered around its periodic Wildfire windows. During these windows approximately every minute, the Machinist damage output significantly peaked due to the layering of several factors:

* Cooldown alignment (every 60s along with Wildfire)
* The Overheated damage bonus
* Party buff windows designed around 60s periods
* The Wildfire detonation itself

These massive peaks in damage output were accompanied with corresponding lows in damage output. The filler rotation outside of these Wildfire windows consisted of "1-2-3" (Split Shot/Slug Shot/Clean Shot) pseudo-combos with randomness due to the ammunition system (albeit somewhat deterministic with relatively short cooldowns on (Quick) Reload). Nevertheless, many critics of the job design disliked that "boring" and "RNG-dependent" part of the rotation. (Mathematical analysis reveals that the damage variance of the pseudo-combo system was actually quite small but, understandably, it's the player perception that counts.)

Additionally, the turret system was an arguably underwhelming pet system. There were some interactions or considerations such as placement of the turret or some abilities such as Hypercharge and Overload. In general, the turret was "set and forget it" that happened to compose around 20-30% of your combined damage output. It was something that you forgot to resummon after you blew it up with Overload.

Other weaknesses of the job included:

* Strong dependence on party composition to reach damage potential. Despite a reduction of efficacy, Dragoon's Disembowel debuff of the afflicted target having 5% increased damage taken from piercing damage (i.e., all of Machinist's damage) was still critical to Machinist. By comparison, Bard, the competitor for the physical ranged DPS role, was not as adversely affected by the absence of a piercing debuff due to having a healthy contribution from damage over time to its damage composition. Furthermore, since Machinist's damage output was concentrated into 10s Wildfire windows every minute, it was critically affected by "proper" party cooldown alignment such as Ninja's Trick Attack. 
* The Wildfire mechanic requires the debuff applied to actually detonate on the target to reap any benefit. This is in contrast with, for example, Bard's Raging Strikes buff which just increases damage dealt during its duration. Any Machinist who experienced a target dying or becoming untargetable or invulnerable before the Wildfire can detonate can attest to how vital it is to plan Wildfire windows such that these incidents do not occur. You were at the mercy of fight design.

In Shadowbringers, the complete overhaul of the job in addition to the raised level cap resulted in a comparatively refreshing new take on Machinist. Gone is the identity of a gunslinger with a turret pet. The new identity is more of a Machinist inspired by Edgar from Final Fantasy VI: a gunslinger with a collection of various tools to turn the tide of battle.

The tempo and cadence of the Machinist rotation has smoothened out compared to its previous incarnation. The damage output profile is less peaks and valleys and more hilly. The rotation is less 10s of intensity and 50s of cooldown (no pun intended) and more active and frenetic yet flexible.

### Ammunition and combos

The ammunition system is completely gone. The (Heated) Split/Slug/Clean Shot weaponskills now form a real 1-2-3 combo with each Heated version being acquired through traits.

### Resource (gauge) system

Since Stormblood, Square-Enix has focused on gauge systems in addition to traditional, shared TP/MP resources. In Shadowbringers, Machinist retains its heat gauge from before. Instead of Overheated status being achieved by filling the heat gauge, it is achieved through the new Hypercharge ability at the cost of heat gauge. Additionally, the Overheated status has been adjusted as we will discuss later. The heat gauge does not need to be filled to be usable which provides some flexibility in using it.

Like many other jobs, Machinist gained another gauge called the battery gauge. This resource is more passively raised than the heat gauge. This resource is used to summon the automaton which is a temporary pet. The battery gauge does not need to be filled to be usable, but several aspects of your automaton are improved by having more "juice" in the tank when it is deployed.

### Automaton/Pet

The turrets are no longer persistent pets like Summoner's egis. Instead, Machinist's automatons are temporary summons like Summoner's Demi-Bahamut that last a short duration before leaving the battlefield. The bishop autoturret is gone and the rook autoturret is available at level 40. The rook autoturret gets promoted at level 80 to the automaton queen, a much more powerful version. 

Regardless of the model, the two automatons function identically. They are now exclusively single target. Upon spending battery gauge to summon them, they are deployed to the field and "auto-attack" your active target. The duration of their deployment scales with the amount of battery gauge at the time of summoning. Upon execution of the "Overdrive" ability, the automaton will perform its "Overload" ability whose potency also scales with the amount of battery gauge at summoning time. Additionally, the automaton will automatically perform its Overload ability before desummoning if it is not manually executed; it will even stay after its time has expired in order to perform it. Because of this feature, the automaton is basically "summon and forget" unless you need to prematurely execute its Overload for whatever reason.

### Wildfire

Wildfire and Barrel Stabilizer now have 120s recast times. Wildfire works significantly differently now. Before, it recorded damage dealt by you during its duration and dealt a portion of it again with its detonation. Now, Wildfire deals damage with a potency that is a function of the number of your weaponskills landed on the target during its duration. This means that abilities landed have no effect on Wildfire's potency. As a result, there's less incentive to play "mad piano" during Wildfire windows to maximize damage. Between that change and the increased recast time, Wildfire is now a much less significant proportion of Machinist's damage composition (less than 5%).

### Overheat

The Overheated status, granted by spending heat gauge with the new version of the Hypercharge ability, now grants a flat +20 potency to single target weaponskills during its duration (8s) instead of an increased damage dealt bonus. Additionally, two weaponskills are only available while your weapon is Overheated: Heat Blast (formerly Cooldown) and Auto-Crossbow. These two weaponskills have the special property of having a fixed recast time of 1.5s. If you use these weaponskills while Overheated, it is reminiscent of having Rapid Fire on for the entirety of the window. (Rapid Fire is otherwise gone.) Heat Blast has an additional special property which shall be discussed later.

### New tools/weaponskills

Hot Shot survived the action culling but has lost its increased damage dealt buff. Instead, it is a high potency (300)weaponskill that increases your battery gauge by 20. The only other way to increment battery gauge is through the combo bonus of (Heated) Clean Shot which increases it by 10. Hot Shot is upgraded via a trait at level 76 into Air Anchor which brings its potency to a whopping 700. Both Air Anchor and Hot Shot have a recast time of 40s that *does* scale with skill speed.

Drill is a new weaponskill introduced at level 58. It deals damage with a hefty potency of 700 to a single target with a relatively short recast time of 20s that scales with skill speed. Bio Blaster is the AoE analog of Drill, sharing recast time with Drill and acquired at level 72. These weaponskills serve nicely to create variety in the rotation.

### AoE

Previously, the AoE capabilities of Machinist were proficient yet somewhat stale. The bishop autoturret, Spread Shot, and Flamethrower were the extent of Machinist's AoE toolkit.

In Shadowbringers, the AoE toolkit has been significantly expanded. While Spread Shot remains and the bishop autoturret is gone, Machinist acquires several actions to make mowing down packs more interesting. While Overheated, you can use Auto-Crossbow to barrage foes in a cone before you. You can use Bio Blaster to hit and apply damage over time to mobs in front of you. Additionally, Flamethrower remains as potent as ever for area damage and is no longer used to generate heat. In tandem, the use of all these tools truly creates the feeling of throwing the kitchen sink at packs of mobs.

### General gameplay

With the reduction of Wildfire's importance, frequent Overheat windows, and new weaponskills with short recast times, the rotation can feel frenetic. You'll open by dumping your cooldowns and setting up a Wildfire. As your Drill and Air Anchor weaponskills come off cooldown, you'll mix them into your filler heated shots. With enough heat gauge built up as you go through your rotation, you'll enter a Overheat window in which you rapidly fire off Heat Blasts and generate Gauss Round and Ricochet charges to weave in. Eventually, your battery gauge hits 100 and you can summon your automaton queen to pummel your target. Before you know it, two minutes have almost passed and it's about time to set up another Wildfire.

## Leveling 

We'll go through the leveling process to outline action acquisition. This helps in understanding in how the job is constructed and could be a useful reference if you're looking to maximize performance below the level cap.

### Level 1-15
Actions acquired:
* Split Shot
* Slug Shot
* Hot Shot
* Reassemble
* Gauss Round

Role actions acquired: 
* Leg Graze
* Second Wind
* Foot Graze

Split Shot and Slug Shot form the 1-2 of your basic combo. Hot Shot should be used on cooldown because it is your highest potency action and it will generate battery gauge later on. 

Reassemble guarantees a direct critical hit on the next weaponskill. At this level, Hot Shot is your highest potency weaponskill so use it for Hot Shot. An interesting thing to note about Reassemble is that when using it on a weaponskill that hits multiple targets, all targets will be hit with a direct critical hit. 

Gauss Round is one of the new charged actions. A new charge is generated after a certain cooldown period up to a maximum number of charges. This permits you to hoard charges for opportunistic use. Otherwise, get used to weaving Gauss Round between weaponskills to avoid capping charges.

### Level 15-29
Actions acquired:
* Spread Shot
* Clean Shot

Role actions acquired: 
* Peloton
* Head Graze

Spread Shot is the basic component of your AoE toolkit. Dealing damage with a potency of 180 to all targets, it is more efficient than the Shot combo at 2 or more targets. The acquisition of Clean Shot completes your basic 1-2-3 combo. Clean Shot's combo bonus deals damage with a potency of 320, making it the most suitable candidate for Reassemble. With the interesting interaction between Reassemble and AoE weaponskills, Reassemble can be used for Spread Shot while killing trash packs.

Head Graze is one of the new "interrupt" actions. It essentially plays the role that silence did previously but with more guidance in the user interface on what can be interrupted. Since this role action is part of the physical ranged DPS's utility, it should be noted that Machinist has this action.

### Level 30-39
Actions acquired:
* Hypercharge
* Heat Blast

Role actions acquired:
* Arm's Length

At level 30, you acquire Hypercharge. This ability is used to spend heat gauge and become Overheated for 8s. The Overheated status increases the potency of your single target weaponskills by a flat 20 potency. You can expect to generate 50 heat gauge approximately every 30-40s while going through your rotation.

 At level 35, you acquire Heat Blast. This weaponskill is only usable while Overheated. It deals 200 potency (plus the 20 potency from the Overheated effect) but has the special property of having a fixed recast time of 1.5s. This puts its potency per second at approximately 146.67 potency per second:

``
220/1.5 = 146.67 potency per second
``

compared to the Heated Shot combo:

``
(220+320+420)/3/2.5 = 120 potency per second
``

Theoretically, since the Heated Shot combo's recast times scale with skill speed, its potency per second exceeds that of Heat Blast at a GCD of around 2.18s. 

The other major effect of Heat Blast is that it reduces the recast time of Gauss Round (and Ricochet later) by 15s. Those abilities deal damage with a potency of 150. We can consider two Heat Blast uses to grant one charge each of Gauss Round and Ricochet, further increasing Heat Blast's utility. Furthermore, since the Overheated bonus is a flat +20 potency to weaponskills, there is no additional bonus to using higher potency weaponskills there; instead, you are incentivized to use more weaponskills while Overheated. Therefore, it's difficult to justify using any other weaponskill than Heat Blast (in single target situations) while Overheated.

The Arm's Length role action is a new addition to the physical ranged DPS role kit. Rejoice that Machinist can now have knockback and draw-in prevention.

#### Additional notes on Overheat and Hypercharge
The Overheat status lasts for 8s. Theoretically, you can fit in six Heat Blasts during its duration:

`0, 1.5, 3.0, 4.5, 6.0, 7.5`

However, due to animation delay and latency, you can't expect to fire off a weaponskill at the instant you use Hypercharge. If you try to get a sixth in and you're late, you run the risk of action cancelation or hitting a keybind for something you can't use. It's more realistic to expect to fit five Heat Blasts in. 

Since Overheat is exactly activated by using Hypercharge, you will want to weave Hypercharge in late between weaponskills to maximize the usable Overheat duration. You can double weave, say, Gauss Round and Hypercharge to help you space the timing. At higher skill speeds and/or with higher latency this may not be a good option due to clipping. In any case, since we only anticipate getting five Heat Blasts in the window, the timing requirement is somewhat more relaxed.

Regarding weaving abilities between Heat Blasts, it should be doable to weave in one. After all, weaving between Cooldown uses under Rapid Fire was a staple during Wildfire windows in the old days. In my experience thus far, however, it feels like I'm clipping when weaving abilities like Gauss Round and Ricochet between Heat Blasts. This is somewhat surprising as I'm playing with approximately 45ms ping. It's entirely possible that animations and delays have changed. Given the Heat Blast property of reducing Gauss Round and Ricochet recast times, I inferred that the intent is to generate those charges and spend them while you use Heat Blast. 

### Level 40-50
Actions acquired:
* Rook Autoturret
* Wildfire
* Ricochet

Level 40 grants you your first automaton, the rook autoturret. This familiar companion can be summoned when you have at least 50 battery gauge. If you have more than 50 battery gauge when you summon it, its duration on the battlefield will increase up to a maximum of 15s when at full battery gauge. The rook autoturret will shoot your active target with 80 potency Volley Fire attacks. At this level, you also gain the Rook Overdrive ability which orders the rook autoturret to execute Rook Overload. As in Stormblood, Rook Overload is a finisher nuke that desummons the rook autoturret after execution. It has a base potency of 400 that also increases with the amount of battery gauge spent to deploy it. Additionally, if you do not manually order Rook Overload, the rook autoturret will automatically use it before it leaves the battlefield (provided there is a target to use it on). It will even stay past its prescribed duration to execute it if, for example, it is on global cooldown from its previous action. One final thing to note regarding the rook autoturret: Rook Overdrive and Rook Autoturret (the summon) share a recast timer. Given that the recast timer of Rook Autoturret is 6s, this means that you cannot summon the rook autoturret and immediately use Rook Overdrive.

Battery gauge can only be incremented from Hot Shot or the Clean Shot combo bonus. Optimal use of Overheat windows means not incrementing battery gauge as a result. Therefore, you can expect to generate 100 battery gauge every 80-90 seconds.

Wildfire is acquired at level 45. Previously, it was the foundation of Machinist's rotation. In Shadowbringers, it can be more thought of as a bonus to an Overheat window. Wildfire deals damage with a potency of 150 per weaponskill landed on the target during its duration. This gets upgraded to 200 per weaponskill with a level 78 trait. Consequently, you will want to land as many weaponskills as you can while Wildfire is applied and there is no better way to facilitate that than the Overheated status.

The target number of weaponskills is six. A Wildfire rotation may look something like:

```
00.00 Hypercharge
00.50 Wildfire
01.00 Heat Blast
02.50 Heat Blast
04.00 Heat Blast
05.50 Heat Blast
07.00 Heat Blast
08.00 (Overheated status expires)
08.50 <Another Weaponskill>
10.50 (Wildfire detonates)
```

An alternative may look like:
```
00.00 Hypercharge
00.50 Heat Blast
01.50 Wildfire
02.00 Heat Blast
03.50 Heat Blast
05.00 Heat Blast
06.50 Heat Blast
08.00 (Overheated status expires)
08.00 <Another Weaponskill>
10.50 <Another Weaponskill>
11.50 (Wildfire detonates)
```

In either case, you get six weaponskills inside Wildfire comfortably, resulting in a 1,200 potency Wildfire. Yes, that is nominally the highest damage action in Machinist's toolkit. However, its long recast time of 120s limits its importance. A Drill or Air Anchor with Reassemble every 60s (or with a direct critical hit in general) will deal more damage. Furthermore, based on my admittedly limited sample size, it doesn't appear that Wildfire can direct hit or critical hit. Additional testing is required to see if it is affected by increased damage dealt buffs or the target's increased damage taken debuffs. If not, that has consequences for rotation design (in terms of action alignment).

At these levels, you don't have much control over your heat gauge to overheat on demand. You will have to wait quite a few levels until you do.

At level 50, you get Ricochet, the other charged action. It is an AoE analog of Gauss Round that is perfectly usable in single target situations. Use it like Gauss Round.

#### At level 50 cap
You've got your basic 1-2-3 combo. Keep your Hot Shot on cooldown so you can build battery gauge. Summon your rook autoturret at maximum battery gauge unless you want to get it out before the encounter ends. Try to build heat so you can Overheat for Wildfire. Overheat for Heat Blasts otherwise. Try to spend Gauss Round and Ricochet charges so you can keep building them unless absolutely necessary. Use Reassemble on Clean Shot.

For AoE, unfortunately, all you have is Spread Shot. Remember you can use Reassemble on Spread Shot and that it applies to all targets.

### Level 51-65
* Auto Crossbow
* Heated Split Shot
* Heated Slug Shot 
* Heated Clean Shot
* Drill
* Tactician

At level 52, you acquire Auto Crossbow. This is the AoE analog to Heat Blast: it is only usable while Overheated and has the same (shared) recast time as Heat Blast (1.5s). However, it does **not** decrease the recast time of Gauss Round and Ricochet. With the same potency per target of 180 as Spread Shot with a much shorter recast time, it is by far your best option for AoE provided you are Overheated. Fortunately, Spread Shot does generate some heat gauge per use so you can build towards an Overheat window.

Tactician is a utility ability that has analogs among the physical ranged DPS jobs. It grants decreased damage taken to party members in range for a duration. As it is an integral part of the job role along with Head Graze, it's important to remember that you have it.

At levels 54 and 60, you acquire the Heated upgrades of Split Shot and Slug Shot. At level 64, you get the trait for Heated Clean Shot. Interestingly, this means at synced level 60 content, your Heated combo is incomplete. The acquisition of these upgrades are straight upgrades to your basic combo but don't functionally change how you should play.

Level 58 grants Drill. This weaponskill deals damage with a massive potency of 700 and has a base recast time of 20s that scales with skill speed. First of all, this is your best choice by far for Reassemble. It is your biggest or tied for the biggest contributor to your total damage output (rivals Heat Blast). With high potency and a relatively short recast time, you will want to try to use it on cooldown to maximize the number of uses. With the addition of another non-combo weaponskill, it is time to discuss...

#### Combos
The very notion of combos is a string of weaponskills that grant benefits from using them in sequence. Dragoon is notorious for having long combos that are unforgiving if you break them. As a reward, the later components of the combo deal damage with high potencies. For Machinist, despite the removal of the ammunition system and the transformation of the "Shot" weaponskills into a 1-2-3 combo, the "Shot" combo feels as flexible as ever. Of course, this is due in part to a system-wide change to the combo system. Previously, if you used a combo action and didn't follow through with the next action in sequence, you would "lose" your combo bonus and have to start the combo over. You could lose it by using an improper weaponskill or just by not acting for about 9-10 seconds. With regards to Machinist, you can pause a "Shot" combo, perform other actions or do nothing otherwise, and pick it up again. 

For example, you can start a combo with Heated Split Shot, Heated Slug Shot, and do any of the following:

* Hot Shot/Air Anchor
* Drill/Bio Blaster
* Heat Blast
* An entire Overheat window with five Heat Blasts and Wildfire
* Abilities like Rook Autoturret or Reassemble
* Nothing for ~10-12 seconds

(Not sure about Auto Crossbow and Flamethrower)

And still keep your combo and finish it with Heated Clean Shot. What you cannot do, however:

* Spread Shot
* Out of order combo action (e.g., Heated Split Shot)

This provides *extreme* flexibility in your rotation. This helps you keep your Hot Shot and Drill on cooldown. This helps you keep your Overheats and Wildfires on schedule. Of course, you will lose your combo eventually if you do not continue it.

#### At level 60 cap
In addition to what you've done thus far, keep Drill and Hot Shot on cooldown. Definitely use Reassemble for Drill. Remember your role actions and utility like Tactician. You have Heated Split and Slug Shots but not Clean Shot but it doesn't change your priorities.

AoE capabilities are much better at level 60. You can spend your Overheat windows on Auto Crossbow spam. Remember you can use Reassemble on it for the damage boost. Otherwise, it's back to Spread Shot spam.

### Level 66-70
* Barrel Stabilizer
* Flamethrower

Obtained at level 66, Barrel Stabilizer adds some much needed heat gauge management ability. With a recast time of 120s, it grants you 50 heat gauge, which is exactly the cost of Hypercharge. Effectively, it's a way to Overheat on demand. Given that it also shares a recast time with Wildfire, we can use it to prep an Overheat for a Wildfire window. This also means we can Overheat at will at all other times since we can guarantee enough heat gauge for Wildfire with this ability.

Flamethrower, obtained at level 70, is relieved of its duty of forcing Overheat from the Stormblood days. In fact, it ironically doesn't generate any heat gauge in Shadowbringers. Now, Flamethrower plays the role of one of Machinist's best AoE options... which it actually was before. It's effectively a channeled ability that ticks for 100 potency on each target in its conal AoE every second. Comparing Machinist's other AoE options:

```
Auto Crossbow: 180 potency per 1.5 seconds = 120 pps, per target
Flamethrower: 100 potency per 1 second = 100 pps, per target
Spread Shot: 180 potency per ~2.5 seconds = 72 pps, per target
```

We can assert the following AoE action priority:

1. Overheat to spam Auto Crossbow. Use Barrel Stabilizer to do so if desired.
2. Channel Flamethrower.
3. Use Spread Shot and generate heat gauge.

(Use Ricochet liberally, of course.)

In terms of when to use AoE actions versus single target, three targets or more is a safe bet to use AoE actions.

#### At level 70 cap
After obtaining Barrel Stabilizer, Machinist basically has all of the tools that structure its general gameplay. A sample opener on a single target will look like:

```
Drill (Gauss Round, Ricochet)
Hot Shot (Gauss Round, Ricochet)
Heated Split Shot
Heated Slug Shot
Heated Clean Shot (Barrel Stabilizer, Hypercharge) 
**Overheated**
Heat Blast (Wildfire)
Heat Blast (Gauss Round)
Heat Blast (Ricochet)
Heat Blast (Gauss Round)
Heat Blast (Reassemble)
**End Overheat**
Drill (Ricochet)
Heated Split Shot
**Wildfire detonates)
...
```

The general priority system looks like:

1. Keep Overheat+Wildfire window aligned every two minutes. The sample opener above is designed to pack as much damage into typical raid buff windows.
1. Keep Drill and Hot Shot on cooldown. Use the flexibility of the combo system to your advantage. Delay Overheat windows as necessary to facilitate this.
1. Overheat at will. Avoid capping heat gauge, but it's not horrible to do so since we generate heat gauge so readily.
1. Charge battery gauge to 100 before summoning your turret/automaton. Avoid capping battery gauge. Be aware of forced downtime that would waste your summon. Remember you can force the automaton to use its finisher and be dismissed using the Overload command. 
1. Use Reassemble on Drill. Remember that it has half the recast time of Wildfire now (so don't sit on it for Wildfire).
1. Spend Gauss Round and Ricochet charges to avoid capping them unless it makes sense to save them.
1. Shot combo

### Level 71-80
* Bioblaster
* Charge Action Mastery (trait, lvl 74)
* Air Anchor
* Enhanced Wildfire (trait, lvl 78)
* Automaton Queen

Level 72 grants Bioblaster which is the AoE alternative to Drill (they share recast times). The total potency of it is 360 per target, assuming that the DoT ticks for its full duration. With the same assumption, we can value Bioblaster at 144 pps:

```
60 + 60*5 = 360 potency per 2.5 seconds = 144 pps, per target
```

This puts it at the highest priority for multi target situations. (At 4 DoT ticks only, it equals Auto Crossbow.)

Level 74 grants Charge Action Mastery, allowing the accumulation of an additional charge each of Gauss Round and Ricochet.

At level 76, Hot Shot is upgraded to Air Anchor. Functionally, it is the same as Hot Shot but deals an impressive 700 potency (equal to Drill). This increases its priority and also lets it be an alternative candidate for Reassemble.

Level 78 upgrades Wildfire via a trait. Wildfire's potency per weaponskill landed increases from 150 to 200. This is a small but nice boost.

Finally, at level 80, the rook autoturret is promoted to the automaton queen. This is a massive upgrade but functionally, your general gameplay is unchanged. Some notes on the automaton queen:

* It attacks in melee range.
* Its maximum duration is 20s (up from 15s).
* Its Overload ability, Pile Bunker, deals damage with a baseline potency of 800 (up from 400).
* Its "auto-attack", Arm Punch, deals damage with a potency of 150 (up from 80).
* It uses a gap closer, Roller Dash, upon summoning and when otherwise needed. It will use it even when summoned right next to a target. It is DPS-neutral to use Roller Dash since it is twice the potency and recast time as Arm Punch.
* It walks *really* fast so it is capable of tracking moving targets.