+++
date = 2025-11-29T20:44:33.332594+11:00
draft = false
title = "Steel Armour"

+++
[Steel Armour]( {{< relref "upgrade/Steel_Armour.md" >}}) is a mid-game Workshop upgrade that enhances the effectiveness of the hunting system. It is researched in the Workshop tab and is unlocked once you have discovered the [Steel]( {{< relref "craft/Steel.md" >}}) science technology.

### **Costs and Prerequisites**
*   **Science Cost:** 10,000.
*   **Resource Cost:** 50 Steel.
*   **Prerequisite:** Researching the [Steel]( {{< relref "craft/Steel.md" >}}) technology is mandatory before this upgrade appears.

### **Effects on Hunting**
The primary function of Steel Armour is to increase the **hunting bonus** for your kittens (or Zebras in Iron Will mode).
*   **Hunting Bonus:** It provides a flat **+0.5 bonus** to hunting effectiveness.
*   **Additive Stacking:** This bonus is additive with other hunting upgrades. For example, if you have already researched Bolas (+1.0) and Hunting Armour (+2.0), adding Steel Armour brings your total hunting bonus to **3.5**.
*   **Yield Increase:** This upgrade increases the basic fur and ivory hunting amounts by approximately **40–50%**.
*   **Expected Results:** With Bolas, Hunting Armour, and Steel Armour active, the expected yield per hunt is approximately **153.25 fur** and **47.94 ivory**.

### **Technical Mechanics**
Because Steel Armour provides a non-integral bonus (+0.5), it causes the probability distribution for hunting resources to become **non-uniform**. When calculating the amount of furs or gold acquired, the game generates a random integer range; a non-integral hunting bonus allows for the possibility of generating the next highest integer in the range, though with half the probability of the other integers.

### **Strategic Utility**
Steel Armour is essential for scaling your **cultural engine** in the mid-game. Higher fur yields allow for more rapid crafting of [Parchment]( {{< relref "craft/Parchment.md" >}}), which is the foundational material for [Manuscripts]( {{< relref "resource/manuscript.md" >}}) and [Compendiums]( {{< relref "resource/Compendium.md" >}}). Additionally, increased ivory yields are critical for trading with the [Nagas]( {{< relref "Civilisations/Nagas.md" >}}) to resolve mineral bottlenecks.