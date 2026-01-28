+++
date = 2025-12-07T16:20:01.525062+11:00
draft = true
title = "Workers"

+++

The term "rank" in relation to kittens/workers in *Kittens Game* refers to two distinct systems: the **Skill Level** gained through job experience, which boosts a kitten's productivity in that specific job, and the **Leader Rank**, gained through promotion, which boosts the selected leader's overall production regardless of their job.

***

### 1. Kitten Skill Levels (Job Rank)

Kittens assigned to a job gather **experience** and increase their skill level in that task. This skill level provides a **multiplicative bonus** to productivity in their specific job.

The seven progressive skill levels and their associated bonuses are:

| Skill Level | Experience Needed | Bonus to Productivity |
| :--- | :--- | :--- |
| **Dabbling** | 0 | 0% |
| **Novice** | 100 | 1% |
| **Adequate** | 500 | 3% |
| **Competent** | 1200 | 4% |
| **Skilled** | 2500 | 8% |
| **Proficient** | 5000 | 13% |
| **Master** | 9000 | 18.75% |

These bonuses can be further enhanced by the Workshop upgrades [Logistics]( {{< relref "upgrade/Logistics.md" >}}) (increasing the skill bonus by 15%) and [Augmentations]( {{< relref "upgrade/Augmentations.md" >}}) (increasing the skill bonus by 100%).

### 2. Leader Rank (Promotion)

The Leader Rank is a separate ranking system unlocked by the [Civil Service]( {{< relref "techs/Civil_Service.md" >}}) science. A kitten gains a rank when promoted, which requires spending **gold and experience**. The bonus from the Leader's rank applies to that kitten's production **regardless of their job**.

| Leader Rank (n) | Experience Cost | Gold Cost | Production Bonus (to Leader) |
| :--- | :--- | :--- | :--- |
| **0** | 0 | 0 | 0% |
| **1** | 500 | 25 | 43% |
| **4** | 2680 | 100 | 257% |
| **6** | 8207 | 150 | 400% |
| **8** | 25133 | 200 | 543% |

A promoted leader can be unassigned and reassigned to whatever job needs the most assistance.

**Policy Interaction:**

*   If the [Monarchy]( {{< relref "Policy/Monarchy.md" >}}) policy is researched, the leader's **trait** is twice as powerful.
*   If the [Autocracy]( {{< relref "Policy/Autocracy.md" >}}) policy is researched, the leader's **production bonus** (based on rank) is doubled (x2).
*   If the [Republic]( {{< relref "Policy/Republic.md" >}}) policy is researched, all non-leader kittens get a bonus to their jobs equal to $1\%$ of the leader's bonus.