+++
date = 2025-12-07T08:15:29.436671+11:00
draft = true
title = "Steamworks"

+++

The [Steamworks]( {{< relref "steamworks.md" >}}) is an essential industrial building in *Kittens Game* that introduces early automation, supplements energy production, and is crucial for overcoming the manuscript bottleneck in the mid-game.

### Unlocks, Cost, and Base Effects

The Steamworks building is unlocked by researching the [Machinery]( {{< relref "techs/machinery.md" >}}) technology, which costs 15,000 Science.

*   **Cost:** The base cost to construct a Steamworks is **65 Steel, 20 Gear, and 1 Blueprint**.
*   **Price Ratio:** The building has a high price ratio of 1.25.
*   **Base Effects:**
    *   [Energy:]( {{< relref "energy.md" >}}) Provides **+1 Energy**.
    *   [Coal:]( {{< relref "resource/coal.md" >}}) Reduces Coal consumption by **80%**.
    *   **Production Boost:** Provides a **Magneto Boost of +15%**.
*   **Drawback:** Like other industrial buildings (Mines, Smelters, etc.), the Steamworks produces **Pollution**.

### Strategic Purpose: Automation and Manuscript Production

The primary strategic role of the Steamworks is to introduce automation and overcome resource bottlenecks:

1.  **Manuscript Automation:** Steamworks consume Coal to create a variety of handy items. Critically, once the [Printing Press]( {{< relref "printing_press.md" >}}) upgrade is researched, Steamworks automatically print [Manuscripts]( {{< relref "craft/Manuscript.md" >}}) at a base rate of 0.0025 manuscripts/sec. Manuscript production can be further boosted by the [Offset Press]( {{< relref "offset_press.md" >}}) and [Photolithography]( {{< relref "photolithography.md" >}}) upgrades, which each multiply production by a factor of 4. This automation is necessary for overcoming the steep requirements of the later [Theology]( {{< relref "science/theology.md" >}}) and [Astronomy]( {{< relref "astronomy.md" >}}) sciences.
 
2.  **Resource Conversion:** The [Workshop Automation]( {{< relref "workshop_automation.md" >}}) upgrade allows Steamworks to automatically convert a percentage of wood into beams and minerals into slabs once per year when those resources are nearly capped (at 98% of capacity). The [Advanced Automation]( {{< relref "advanced_automation.md" >}}) upgrade makes this process activate twice per year, and [Pneumatic Press]( {{< relref "pneumatic_press.md" >}}) adds the conversion of iron to plates.
3.  **Industrial Foundation:** Steamworks are listed among the supplemental production-boosting buildings (alongside Magnetos, Reactors, Calciners, and Quarrys) that cost blueprints and help create base resources.

### Upgrades and Efficiency

Several upgrades directly affect the Steamworks' efficiency and resource consumption:

*   **Coal Efficiency:** The [High Pressure Engine]( {{< relref "high_pressure_engine.md" >}}) and **Fuel Injector** upgrades each reduce the Coal consumption of Steamworks by 20%.
*   **Magneto Synergy:** The Magneto Boost is further improved by the **Griffin Relations: Machinists** policy, which increases the Steamworks' Magneto boost bonus by +0.5%.

### Contextual Notes

*   **Prerequisite Grinding:** The Steamworks presents a hurdle because it requires [Blueprints]( {{< relref "resource/Blueprint.md" >}}) and [Gears]( {{< relref "craft/Gear.md" >}}) (which require Steel). In the IW 40K run, the Sharks and Griffins trading loop is cited as a key method for collecting the necessary steel, gears, and blueprints for Steamworks.
*   **Coal Management:** Since Steamworks consume coal, players are advised to **turn off Steamworks** when grinding coal for other priorities, such as building Oil Wells.
*   **Challenges:**
    *   The Steamworks is listed as a necessary building to complete the **Energy Challenge**.
    *   In the **Pacifism Challenge**, the cost of the Steamworks increases by 1.5, rounded down to the nearest integer, and the blueprint cost linearly increases by 5.

### 4. Magneto (Boosted Production)

The Magneto building receives a direct, inherent boost from the Steamworks.

*   **Magneto Boost:** Each Steamworks provides a **+15% Magneto Boost**. This increases the Magneto's effect of providing a **+2% Global Production** bonus.
*   **Policy Enhancement:** This Magneto boost provided by the Steamworks can be further improved by the **Griffin Relations: Machinists** policy, which increases the Steamwork's Magneto boost bonus by **+0.5%**.

### 5. Manuscripts (Automated Production)

The Steamworks facility can be upgraded to automate the production of the advanced resource [Manuscripts]( {{< relref "resource/manuscript.md" >}}).

*   [Printing Press:]( {{< relref "upgrade/Printing_Press.md" >}}) The [Printing Press]( {{< relref "upgrade/Printing_Press.md" >}}) upgrade allows Steamworks to produce **Manuscript per Tick +0.0005** (or 0.0025 manuscripts/sec). This requires the Steamworks building (unlocked by Machinery).
*   **Further Upgrades:** This automated production rate can be substantially increased by subsequent Workshop upgrades:
    *   [Offset Press]( {{< relref "upgrade/Offset_Press.md" >}}) increases manuscript production by a factor of **4** (to 0.01 manuscripts/sec).
    *   [Photolithography]( {{< relref "upgrade/Photolithography.md" >}}) also increases manuscript production by a factor of **4** (to 0.04 manuscripts/sec).

### 3. Crafted Resources (Automation)

The core functionality of the Workshop benefits from Steamworks through automated material conversion:

*   [Workshop Automation:]( {{< relref "upgrade/Workshop_Automation.md" >}}) Steamworks unlock the [Workshop Automation]( {{< relref "upgrade/Workshop_Automation.md" >}}) upgrade, which causes the Steamworks to convert resources into craftable materials when those resources reach their cap.
    *   Once per year, Steamworks convert **wood (to beams)** and **minerals (to slabs)** at $98\%$ of the resource's cap.
    *   The [Advanced Automation]( {{< relref "upgrade/Advanced_Automation.md" >}}) upgrade allows this conversion to activate **twice per year**.
*   [Pneumatic Press:]( {{< relref "upgrade/Pneumatic_Press.md" >}}) This upgrade further expands the automation to include **iron being converted to plates**.

### Strategic Considerations

It is noted that Steamworks consume coal. In the mid-game, experts advise against keeping Steamworks active unless you plan to be idle for long periods, as running them can severely restrict your [coal production]( {{< relref "resource/coal_production.md" >}}).