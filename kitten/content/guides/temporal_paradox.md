---
title: Temporal Paradox
description: ""
date: 2026-03-12T05:40:58.861Z
preview: ""
draft: false
tags: []
categories: []
---
In *Kittens Game*, a [Temporal Paradox]( {{< relref "guides/temporal_paradox.md" >}}) is a random event tied to the late-game [Chronosphere]( {{< relref "buildings/Chronosphere.md" >}}) mega structure that serves as the primary method for generating [Void]( {{< relref "resource/void.md" >}}).

### **Mechanics and Triggering**
*   **Source:** Temporal paradoxes occur occasionally once you have built one or more [Chronospheres]( {{< relref "buildings/Chronosphere.md" >}}).
*   **Output:** During a paradox, you gain [Void]( {{< relref "resource/void.md" >}}), a unique resource required for advanced endgame technologies and structures.
*   **Visual Indicator:** The paradox is a timed event that lasts for a specific number of game days.

###  Paradox Trigger Check
On every daily tick (or skipped day during time combustion), the game evaluates whether a paradox occurs:
   {Paradox Chance per Day} =  {Chronospheres}/10,000
* Threshold: If  {Chronospheres} = 0$, chance is 0.
* With 10 Chronospheres, the daily chance is $0.1\%$ per calendar day.
* With 50 Chronospheres, the daily chance is $0.5\%$ per calendar day.

### Base Chronosphere Void Payout
When a paradox triggers, the Chronospheres generate a base quantity of Void:

   {Base Void} = 1 + ({Chronospheres} - 1)/2
   
* 1 Chronosphere: $1 + \lfloor 0 \rfloor = 1\text{ Void}$
* 5 Chronospheres: $1 + \lfloor 2 \rfloor = 3\text{ Void}$
* 10 Chronospheres: $1 + \lfloor 4.5 \rfloor = 5\text{ Void}$
* 25 Chronospheres: $1 + \lfloor 12 \rfloor = 13\text{ Void}$


See also [Order of the Void]( {{< relref "metaphysics/order_of_the_void.md" >}})

### **Benefits of Paradoxes**
*   **Happiness Boost:** Each unit of Void obtained from these events provides a **+10% happiness modifier**, which enhances your kittens' overall production efficiency.
*   **Resource Carryover:** Void is a non-crafted resource that can be preserved across resets if you have Chronospheres.

### **Associated Upgrades**
Several structures and Workshop upgrades specifically modify the efficiency and duration of a Temporal Paradox:
*   [Void Hoover:]( {{< relref "upgrade/void_hoover.md" >}}) A structure that increases the **maximum amount of Void** you can receive during a single paradox day.
*   [Chronocontrol:]( {{< relref "time/chrono_control.md" >}}) A Time-tab structure that **increases the duration** (number of days) of the paradox event.
*   [Distortion:]( {{< relref "upgrade/Distortion.md" >}}) A late-game Workshop upgrade (unlocked by Paradox Theory) that improves the effectiveness of Chronocontrol, adding **+3 days** to the Temporal Paradox per level of Chronocontrol built.
*   [Void Resonator:]( {{< relref "time/void-resonator.md" >}}) Another upgrade unlocked by Paradox Theory that further enhances Void production and interacts with the [Order of the Void]( {{< relref "metaphysics/order_of_the_void.md" >}}) metaphysics upgrade.

Strategically, players often focus on maximizing the frequency and yield of these paradoxes in Phase 4 (Endgame) to accumulate the millions of Void units required for high-tier upgrades like [Void Rifts]( {{< relref "buildings/void_rift.md" >}}), which provide permanent global storage bonuses.
