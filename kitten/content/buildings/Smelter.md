+++
date = 2025-12-07T08:15:29.431671+11:00
draft = true
title = "Smelter"

+++

The [Smelter]( {{< relref "smelter.md" >}}) is a foundational industrial building in *Kittens Game*, crucial for transitioning from basic resource gathering into metal production and industrial expansion. It is primarily used to refine raw minerals and wood into Iron and, eventually, other critical resources.

### 1. Unlocking and Base Function

*   **Prerequisite:** The Smelter building is unlocked once you research the [Metal Working]( {{< relref "metal_working.md" >}}) technology. Metal Working costs 900 Science.
*   **Cost:** The base cost to build one Smelter is **200 Minerals**, with a price ratio of 1.15.
*   **Base Conversion:** The Smelter converts Wood and Minerals into **Iron**.
    *   It consumes **0.05 Wood per Tick** and **0.1 Minerals per Tick**.
    *   It produces **0.02 Iron per Tick**.

### 2. Strategic Importance

Smelters are vital in the early-to-mid game because they provide the necessary resources to construct key infrastructure and unlock economic options:

*   **Iron for Construction:** Iron produced by Smelters is necessary for building:
    *   [Lumber Mills]( {{< relref "buildings/Lumber_Mill.md" >}}), which significantly boost Wood output.
    *   **Observatories**, required for Starchart generation.
*   **Gold Production for Trade:** You must begin creating [Gold]( {{< relref "resource/Gold.md" >}}) before you can trade with other civilizations. Smelters enable Gold production once the [Gold Ore]( {{< relref "gold_ore.md" >}}) upgrade is researched in the Workshop.
*   **Conversion Production:** Smelters are categorized as buildings that contribute to "Conversion production". Policies like [Autocracy]( {{< relref "autocracy.md" >}}) can boost the output of conversion production based on leader ranks and uncapped housing buildings.

### 3. Key Upgrades (Expanding Output)

Through Workshop upgrades, the Smelter's function can be greatly enhanced to produce resources beyond just Iron:

| Upgrade Name | Resource Unlocked | Effect/Purpose | Technology Prerequisite |
| :--- | :--- | :--- | :--- |
| [Gold Ore]( {{< relref "gold_ore.md" >}}) | Gold | Allows Smelters to produce **0.001 Gold/tick**. (In Iron Will mode, Hunting also produces gold after this is researched.) | Currency |
| [Coal Furnace]( {{< relref "coal_furnace.md" >}}) | Coal | Smelters produce **0.005 Coal/tick** while operating. | Steel |
| [Electrolytic Smelting]( {{< relref "electrolytic_smelting.md" >}}) | Increased Iron & Coal | Makes Smelters "twice as effective," producing **+95% more Iron and Coal**. | Metallurgy |
| [Nuclear Smelters]( {{< relref "nuclear_smelters.md" >}}) | Titanium | Allows Smelters to produce a small amount of [Titanium]( {{< relref "resource/titanium.md" >}}) (**0.0015 per tick**). | Nuclear Fission |

### 4. Context and Drawbacks

Smelters are considered "Industry" buildings, and they are a source of **Pollution**. Along with other industrial buildings like Mines, Steamworks, Calciners, and Oil Wells, they contribute to the high level of CO2 in the atmosphere that negatively affects kitten happiness and resource production.

In the **Iron Will** challenge, where kittens are unavailable, players on a long run are advised that Smelters operate at a loss until they reach a "smelt-positive point" where they have enough Magnetos and Steamworks (and potentially Solar Revolution bonus) to make Gold production positive. For early runs generally, Smelters are initially recommended as a way to convert Minerals into Iron.