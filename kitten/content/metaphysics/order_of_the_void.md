---
title: Order of the Void
description: ""
date: 2026-10-23T09:20:31.828Z
preview: ""
draft: false
tags: []
categories: []
---
Order of the Void is an end-game Workshop upgrade that links your Religion workforce to Void generation, allowing priests to produce Void during temporal anomalies.

### Core Mechanics & Stats

* Tab: Workshop
* Cost:
  * 100,000 Science
  * 50,000 Faith
  * 50 Void
* Prerequisites: Unlocked after researching the Exophysics technology.

### How It Works

* The Trigger: Normally, Priests only produce Faith, and Void only drops passively from Chronosphere temporal paradoxes.
* The Synergistic Payout: With Order of the Void, whenever a Temporal Paradox (Day of the Void) triggers, your assigned Priests harvest extra Void directly into your stockpile.
* Scaling Factors: The amount of Void harvested per paradox scales based on:
  1. The total number of assigned Priests.
  2. Your civilization's net Faith production (boosted by Sol-tier buildings like Temples, Chapels, and Sunspires).
  3. Your accumulated Solar Revolution bonus.

### Internal Faith Weight (F_weight)
The engine first calculates the effective daily faith output per priest:
  {F_weight} = {Priests} * {Base Faith per Priest} * (1 + ({Solar Revolution Bonus %} /100))
  
### The Priest Void Yield (V_priest)
The bonus Void is evaluated using a fractional square root scaling over the accumulated faith weight, capped by diminishing returns:

   V_priest = sqrt(F_weight * {Days of the Void}/100,000) * (1 + 0.10 * {Void Resonators})
   
* __Days of the Void__: The duration of the triggered paradox (typically between 2 and 10 game days depending on Chronosphere count and temporal upgrades).
* [Void Resonators]( {{< relref "time/void-resonator.md" >}}): Each Void Resonator on the Chronoforge applies an additive +10% multiplier to temporal yield mechanics.
* __Rounding__: If V_priest < 1, the fractional value acts as an independent probabilistic check to award 1 Void; once V_priest > 1, the integer part is guaranteed and the fractional remainder rolls as a probability.

### Grand Total Payout
   Total Void per Paradox = {Base Void} + V_priest
   
### Practical Implications
1. __Why 0 Priests Yield Low Void__: Without Priests, you are receiving purely {Base Void}, which caps out at just a handful of units per event even with a dozen Chronospheres.

2. __Why Solar Revolution Matters__: Because F_weight is directly multiplied by `(1 + {Solar Rev %}/100)`, pushing Solar Revolution to +1,000% to +5,000% (via Black Obelisks) magnifies the inner value of the square root by orders of magnitude.

3. __Diminishing Returns__: The square root  prevents Void from scaling linearly into millions per click, maintaining Void as a tightly controlled gating resource even when burning thousands of Time Crystals.


### Strategic Impact in the Late Game

1. Breaks the Paradox Rate Limit: Relying solely on Chronosphere base drops yields very slow Void income. Order of the Void turns each Day of the Void into a substantial drop, dramatically reducing real-time waiting.
2. Fuels the Time Shatter Engine: When you combust Time Crystals (TCs) with Resource Retrieval (RR) active, every skipped year rolls for paradoxes. Order of the Void ensures that mass-shattering centuries in a few seconds completely floods your storage with Void.
3. Funds Expensive Chronoforge Upgrades: Provides the massive Void reserves needed to continually level:
  * Resource Retrieval (scales resource yields per shattered TC)
  * Void Resonators (projects your Solar Revolution multiplier across skipped years)
  * Void Rifts (compounds deep space storage caps using Void and Antimatter)
  * Cryochambers (preserves kittens across resets)
