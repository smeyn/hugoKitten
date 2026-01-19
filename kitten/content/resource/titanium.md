+++
date = 2025-12-06T06:37:34.320989+11:00
draft = true
title = "Titanium"

+++

[Titanium]( {{< relref "resource/titanium.md" >}}) is a vital common resource in *Kittens Game*, marking the entry into the mid-to-late game "Titanium era," where complex construction and space exploration become possible.

It is particularly difficult to acquire in large volumes early on, necessitating a pivot to advanced trade and refined production methods.

### 1. Acquisition and Trade

Titanium is initially acquired primarily through trade, though advanced structures provide domestic production later.

#### Trading with Zebras
The most important early source is through trading with [Zebras]( {{< relref "trade/zebras.md" >}}), who are initially a Hostile civilisation (-30% attitude).

*   **Trade Mechanism:** Zebras sell Titanium in exchange for **Slab** (a craftable resource made from Minerals).
*   **Scaling:** The amount of titanium sold by Zebras is **not** affected by typical trading bonuses like those from Tradeposts. Instead, the amount of titanium they give is calculated as **(0.03 * Trade Ships) + 1.5**.
*   **Prerequisite:** To unlock Zebras for trade, you must first build at least one [Trade Ship]( {{< relref "craft/Trade_Ship.md" >}}).
*   **Policy Boost:** The policy **Zebra Relations: Appeasement** improves relations with Zebras (as 15 extra Tradeposts) and grants a **+15 tradeposts worth of trade ratio titanium sold** (multiplicative).
*   **Strategic Focus:** The strategic goal in the mid-game is to build **Observatories** to generate **Starcharts**, which allow you to craft more Trade Ships, thereby accelerating the rate of titanium flow.

#### Domestic Production (Conversion)
Titanium can be produced domestically through industrial structures that convert other resources:

*   [Calciners:]( {{< relref "buildings/Calciner.md" >}}) Titanium is refined from **oil and minerals** by Calciners. A single Calciner produces **+0.0005 Titanium per Tick**. This production can be significantly boosted by upgrades like [Oxidation]( {{< relref "upgrade/Oxidation.md" >}}) (+285%) and [Fluidized Reactors]( {{< relref "upgrade/Fluidized_Reactors.md" >}}) (+300%).
*   [Smelters:]( {{< relref "buildings/Smelter.md" >}}) After researching [Nuclear Fission]( {{< relref "techs/Nuclear_Fission.md" >}}), the **Nuclear Smelter** upgrade allows Smelters to produce Titanium at a rate of **0.0015 per tick**.
*   **Policy Boost:** The [Communism]( {{< relref "policies/Communism.md" >}}) policy provides a straight **+25% production boost** to iron, coal, and [titanium]( {{< relref "resource/titanium.md" >}}).

### 2. Strategic Uses and Cost

Titanium is a heavily demanded resource for high-level buildings, workshop upgrades, and space travel.

#### Key Building Costs
Titanium is required for constructing advanced infrastructure and housing:

| Building | Titanium Cost | Prerequisite/Context |
| :--- | :--- | :--- |
| [Reactor]( {{< relref "buildings/Reactor.md" >}}) | 3500 | Required for Nuclear Fission |
| [Factory]( {{< relref "buildings/Factory.md" >}}) | 2000 | Unlocked by Mechanization |
| [Hydro Plant]( {{< relref "buildings/Hydro_Plant.md" >}}) | 2500 | Upgrade from Aqueduct; transition should wait until Titanium production is good |
| [Accelerator]( {{< relref "buildings/Accelerator.md" >}}) | 7500 | Unlocked by Particle Physics |
| [Mansion]( {{< relref "buildings/Mansion.md" >}}) | 25 | High-tier housing |
| **Cryostation** | 7500 (in cost of Cryostation) | Advanced storage facility |

#### Upgrades and Progression
Titanium is needed to progress through the housing and crafting technology tree:

*   **Housing Upgrades:** The core progression upgrade [Concrete Huts]( {{< relref "upgrade/Concrete_Huts.md" >}}) requires **3000 Titanium**, and the later [Unobtainium Huts]( {{< relref "upgrade/Unobtainium_Huts.md" >}}) requires **15,000 Titanium**.
*   **Workshop Upgrades:** Titanium is needed for efficiency upgrades such as [Titanium Saw]( {{< relref "upgrade/Titanium_Saw.md" >}}) and [Titanium Axe]( {{< relref "upgrade/Titanium_Axe.md" >}}), and advanced industrial upgrades like [Factory Logistics]( {{< relref "upgrade/Factory_Logistics.md" >}}).
*   **Space Missions:** Titanium is a required resource for several space missions, including the [Moon Mission]( {{< relref "space/Moon_Mission.md" >}}) (5000 Titanium) and [Dune Mission]( {{< relref "space/Dune_Mission.md" >}}) (7000 Titanium).
*   **Uranium Acquisition:** Dragons **buy Titanium** (250 units) and sell [Uranium]( {{< relref "resource/uranium.md" >}}).

### 3. Storage and Capacity

Titanium has a default initial storage capacity of **2** units. This limit must be increased via storage buildings:

*   [Harbours]( {{< relref "buildings/Harbour.md" >}}) increase storage by **+50** Titanium.
*   **Moon Bases** increase storage by **+1250** Titanium.
*   **Cryostations** increase storage by **+7500** Titanium.
*   [Accelerators]( {{< relref "buildings/Accelerator.md" >}}) with the [Energy Rifts]( {{< relref "upgrade/Energy_Rifts.md" >}}) upgrade provide a substantial storage boost, including **+750** Titanium.
*   **Sunforges** also improve storage capacity for base metals, including titanium, by **+1%** each.

In the mid-game, Titanium storage may become capped quickly due to high rates of trade, requiring players to continuously build more storage structures and trade with Dragons to convert excess Titanium into Uranium.