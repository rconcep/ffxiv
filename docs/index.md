# Samurai by the numbers
## by Tzuyu Chou (Cactuar)
An analytical investigation into playing Samurai in FFXIV optimally in any scenario. This analysis is based on the Python class for Samurai that I've written, located in this repository plus some visualization tools also living in the repository. The format of these pages is of exported Jupyter notebooks that include the code used for analysis. Interested users may clone the code and try out some testing themselves (refer to the [documentation](https://rconcep.github.io/ffxiv-docs/html/).)

The parts are broken up into logical partitions where the gameplay changes significantly. Part 1 covers pre-level 50. Part 2 covers up to the level 50 cap but before Kenki is introduced. Part 3 covers gameplay with Kenki Mastery I. Part 4 covers gameplay with Kenki Mastery II up to the level 70 cap. 

Part 5 explores advanced, miscellaneous topics for refined optimization points. Part 8 adds tips for specific trial and raid encounters.

[Official job guide: tool tips and more](http://na.finalfantasyxiv.com/jobguide/samurai/)

[Part 1: levels 1-49](sam-part-1/)

[Part 2: levels 50-51](sam-part-2/)

[Part 3: levels 52-61](sam-part-3/)

[Part 4: levels 62-70](sam-part-4/)

[Part 5: advanced topics](sam-part-5/)

Part 6: openers

Part 7: two-minute drills (optimizing over finite horizons)

[Encounter-specific tips](sam-es-tips/)

View the code documentation [here](https://rconcep.github.io/ffxiv-docs/html/).

### Revision history
- 07/20/2017: Added more discussion on Hagakure in part 5. Added a section in part 5 regarding Higanbana. Added encounter-specific tips.
- 07/08/2017: Added support for double+ weaving abilities. Fixed Hissatsu: Kaiten to affect the Higanbana DoT. Content in parts 3-5 changed accordingly. This slightly changes the DoT potency calculations at each GCD.
- 07/02/2017: Edited parts 1-4 to reflect 4.0 changes.
- 07/01/2017: First edition of part 5, advanced/miscellaneous topics.
- 06/30/2017: First revision since 4.0. Changed Enbi to Enpi. Changed Starry Eyes to Hissatsu: Seigan. Updated behavior for Meikyo Shisui (charge does not get consumed by Iaijutsu).
- 06/07/2017: Added up to part 3.
- 06/07/2017: Added Sphinx documentation for the Python code.
- 06/06/2017: GitHub page now open! Parts 1 and 2 are more or less done and may be updated as DataFrame output or additional data visualization is added. Actual details for 4.0 will need to be implemented.

### About the author
I started playing FFXIV during the 2.3 patch series as a WHM main. I started raiding in the middle of the Second Coil of Bahamut as a SMN main and continued on through the Final Coil of Bahamut. I started Heavensward and Alexander: Gordias as SMN but switched to MNK/DRG for A3S/A4S, respectively. I started as a DRG main for Alexander: Midas but ended up playing SCH for A6S and NIN for A8S. For Alexander: The Creator, I mained BRD but dabbled in some other roles such as NIN and DRK. I main DPS jobs but play other roles occasionally. I play pretty casually in general.

My character on FF Logs is [here](https://www.fflogs.com/rankings/character/2395789/15/).
