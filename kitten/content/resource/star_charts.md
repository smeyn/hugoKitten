+++
date = 2025-12-06T06:37:34.308989+11:00
draft = true
title = "Star Charts"

+++

The **Starchart** is a critical mid-to-late-game special resource necessary for advancing space exploration, unlocking advanced trade methods, and progressing the technological tree.

Here is a detailed breakdown of its acquisition, production, and importance:

### 1. Acquisition and Production

Starcharts are unlocked after researching [Astronomy]( {{< relref "techs/Astronomy.md" >}}). They are initially acquired through rare events, with later production managed through dedicated buildings and kitten jobs.

| Method | Mechanism/Source | Details |
| :--- | :--- | :--- |
| **Astronomical Events** | Observing rare events after building a [Library]( {{< relref "buildings/Library.md" >}}). | The base chance for an event is **0.25% every day**. Each [Observatory]( {{< relref "buildings/Observatory.md" >}}) built increases this chance by an additive **0.2%** per day. The event must be manually clicked, or it may automatically succeed with a **1% chance per Observatory**. |
| **Automation** | [SETI]( {{< relref "upgrade/SETI.md" >}}) Workshop Upgrade (unlocked by Electronics). | This upgrade causes all astronomical events to succeed automatically and silently, instantly granting associated science and starcharts. |
| **Buildings** | **Observatories**, [Satellites]( {{< relref "techs/Satellites.md" >}}), **Research Vessels**, and **Space Beacons**. | Research Vessels produce **0.05 starcharts/sec**, and Space Beacons produce **0.125 starcharts/sec**. Satellites produce **0.005 starcharts/sec**. |
| **Kitten Jobs** | [Scholar]( {{< relref "job/Scholar.md" >}}) profession. | The [Astrophysicists]( {{< relref "upgrade/Astrophysicists.md" >}}) Workshop upgrade allows Scholar kittens to produce **+0.0005 starcharts/sec**. |
| **Trade** | [Leviathans]( {{< relref "trade/Leviathans.md" >}}). | Leviathans trade **250 Starchart** (with a 50% chance) in exchange for 5000 Unobtainium. |
| **Cycles** | **Numerology** and [Numeromancy]( {{< relref "metaphysics/numeromancy.md" >}}) Metaphysics. | Certain cycles (Kairo, Cath, Piscine) boost the production of starcharts from space structures. The [Kairo Cycle]( {{< relref "Cycles/Kairo_Cycle.md" >}}) provides a large boost, increasing starchart income by 5x and increasing space beacon starchart production by +400%. |

### 2. Strategic Role and Progression Bottleneck

Starcharts are often considered a **major roadblock** in the progression towards the space phase of the game.

**Key Uses:**

*   [Trade Ships:]( {{< relref "craft/Trade_Ship.md" >}}) Starcharts are required for crafting [Trade Ships]( {{< relref "craft/Trade_Ship.md" >}}), which are crucial for finding and trading with the [Zebras]( {{< relref "trade/zebras.md" >}}) to acquire [Titanium]( {{< relref "resource/titanium.md" >}}). Crafting a Trade Ship costs 25 Starchart (this cost can be reduced by the [Satellite Navigation]( {{< relref "upgrade/Satellite_Navigation.md" >}}) upgrade).
*   **Space Missions:** They are required for all missions in the Space tab, which is unlocked by [Rocketry]( {{< relref "techs/Rocketry.md" >}}). The costs escalate significantly: the initial [Orbital Launch]( {{< relref "space/Orbital_Launch.md" >}}) costs 250 Starchart, and the subsequent [Moon Mission]( {{< relref "space/Moon_Mission.md" >}}) costs 500 Starchart. Later missions require thousands, such as the [Kairo Mission]( {{< relref "space/Kairo_Mission.md" >}}) (5000 Starchart) and **Rorschach Mission** (15,000 Starchart).
*   **Advanced Structures:** They are necessary for high-tier structures like the **Space Beacon** (25,000 Starchart) and the [Orbital Array]( {{< relref "space/orbital_array.md" >}}) (2000 Starchart).
*   **Workshop Upgrades:** The [Geodesy]( {{< relref "upgrade/Geodesy.md" >}}) Workshop upgrade, which enables Geologists to find gold, requires **500 Starchart**.

**Mitigation Strategy:**

*   To overcome the starchart bottleneck and obtain the necessary titanium, it is crucial to focus on **Observatories** immediately after unlocking Astronomy.
*   Metaphysics upgrades like [Chronomancy]( {{< relref "metaphysics/Chronomancy.md" >}}) and **Astromancy** are recommended because starchart production tends to lag, and these upgrades help increase the chance of astronomical events, accelerating the building of a large trade fleet.
*   In the late game, the **most efficient method** for starchart production is through **Research Vessels**, although acquiring the first vessel is costly (requiring 2000 total Starcharts for mission and building).

### 3. Challenge Mode Interactions

The production and necessity of Starcharts change dramatically when certain challenges are active:

*   **Black Sky Challenge:** This challenge specifically disables astronomical events. Furthermore, **Research Vessels no longer produce starcharts** in this challenge. However, the initial cost of the [Orbital Launch]( {{< relref "space/Orbital_Launch.md" >}}) mission is altered, and the **starchart requirement is removed**.
*   **Iron Will Mode:** In this challenging mode, astronomical events observed after building Libraries are the **only initial source of Science**. If the Iron Will mode is combined with the Black Sky Challenge, astrological events are fully disabled, removing one of the main sources of science.

Starcharts are one of the resources that may conditionally carry over on a reset if you have [Chronospheres]( {{< relref "buildings/Chronosphere.md" >}}). Specifically, starcharts are included in the list of non-crafted resources preserved by Chronospheres. For a quick paragon farming run, players may stock up to **390k starcharts** to carry over **5,850 starcharts** (assuming one Chronosphere).