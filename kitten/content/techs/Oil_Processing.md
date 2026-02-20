+++
date = 2025-11-29T20:44:33.320594+11:00
draft = false
title = "Oil Processing"

+++
[Oil processing]( {{< relref "techs/Oil_Processing.md" >}}) in *Kittens Game* is a multi-stage industrial system that involves extracting raw oil, refining it for greater efficiency, and eventually converting it into high-tier fuels like [Kerosene]( {{< relref "resource/kerosene.md" >}}). 

### **Primary Production and Automation**
Oil is initially produced by [Oil Wells]( {{< relref "buildings/Oil_Well.md" >}}) (unlocked via Chemistry), which provide a base of +0.02 oil per tick. As you progress, you can unlock two primary methods for scaling this output:
*   **Mechanical Extraction:** The [Pumpjack]( {{< relref "upgrade/Pumpjack.md" >}}) workshop upgrade improves Oil Well effectiveness by **45%** and introduces automation (costing 1 Watt per well), while the [Oil Refinery]( {{< relref "upgrade/Oil_Refinery.md" >}}) upgrade provides a separate **+35%** boost.
*   **Biological Refinement:** After researching [Biochemistry]( {{< relref "techs/Biochemistry.md" >}}), the [Biofuel Processing]( {{< relref "upgrade/Biofuel_Processing.md" >}}) upgrade allows [Bio Labs]( {{< relref "buildings/Bio_Lab.md" >}}) to automatically convert 5 catnip/sec into 0.10 oil/sec at the cost of 1 Watt of energy. This biological output can be further increased by **60%** with the [GM Catnip]( {{< relref "upgrade/GM_Catnip.md" >}}) genetics upgrade.

### **Refinement Multipliers**
Once you have established a steady flow of raw oil, you can use specialized technologies and structures to improve its refinement:
*   [Oil Distillation:]( {{< relref "upgrade/Oil_Distillation.md" >}}) Researching [Rocketry]( {{< relref "techs/Rocketry.md" >}}) unlocks this upgrade, which provides a massive **75% boost** to the output of your Oil Wells.
*   [Factory Processing:]( {{< relref "upgrade/Factory_Processing.md" >}}) This workshop upgrade (unlocked by the [Oil Processing]( {{< relref "techs/Oil_Processing.md" >}}) technology) causes every [Factory]( {{< relref "buildings/Factory.md" >}}) to increase your oil refinement effectiveness by **5%**. This bonus is particularly powerful because it stacks multiplicatively with regular craft bonuses.
*   [Space Manufacturing:]( {{< relref "upgrade/Space_Manufacturing.md" >}}) Factories also apply a "Space Production Bonus" to structures like **Hydraulic Fracturers** (on Dune), which produce 2.5 oil/sec.

### **Processed Output: Kerosene**
The ultimate goal of oil processing is the creation of [Kerosene]( {{< relref "resource/kerosene.md" >}}), a specialized fuel required for nearly all space-faring missions and structures. 
*   **Crafting:** Kerosene is crafted from oil once the [Oil Processing]( {{< relref "techs/Oil_Processing.md" >}}) technology is researched. 
*   **Efficiency:** The [Factory Processing]( {{< relref "upgrade/Factory_Processing.md" >}}) workshop upgrade also provides a **+5% bonus** specifically to Kerosene crafting. 
*   **Automation:** In the late game, [Engineers]( {{< relref "job/Engineer.md" >}}) can be assigned to automatically craft Kerosene, ensuring your oil production does not stall when it hits the storage cap.

### **Strategic Consumption and Storage**
Managing processed oil is a delicate balance, as it is a major input for other systems:
*   **Industrial Use:** [Calciners]( {{< relref "buildings/Calciner.md" >}}) consume oil (-0.024/tick) to produce Iron and Titanium. 
*   **Energy Production:** [Magnetos]( {{< relref "buildings/Magneto.md" >}}) consume oil (-0.05/tick) to provide a global production boost.
*   **Storage Barriers:** Oil has a default storage cap of 1,500. This limit is expanded by [Oil Wells]( {{< relref "buildings/Oil_Well.md" >}}) (+1500), [Tankers]( {{< relref "craft/Tanker.md" >}}) (+500), and large-scale structures like **Moon Bases** (+3500) and **Cryostations** (+7500). High oil storage is mandatory for the [Moon Mission]( {{< relref "space/Moon_Mission.md" >}}) (45K Oil) and building [Lunar Outposts]( {{< relref "planet/lunar_outpost.md" >}}) (55K Oil).

 