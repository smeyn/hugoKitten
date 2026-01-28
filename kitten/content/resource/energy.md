+++
date = 2025-12-07T22:48:49.301716+11:00
draft = true
title = "Energy"

+++

Power generation, referred to in the game as [Energy]( {{< relref "energy.md" >}}), is produced by specific advanced buildings and structures, typically unlocked starting in the mid-game, and becomes increasingly important as pollution and energy consumption penalties become factors [1-3].

Here is a breakdown of the buildings that produce Energy:

### Buildings Producing Energy

| Building/Upgrade | Technology Prerequisite | Energy Produced (Base) | Notes | Source |
| :--- | :--- | :--- | :--- | :--- |
| [Steamworks]( {{< relref "steamworks.md" >}}) | Machinery | +1 Wt | This building consumes coal, and the [High Pressure Engine]( {{< relref "high_pressure_engine.md" >}}) and **Fuel Injector** upgrades reduce its coal consumption [4-7]. | [4] |
| [Magneto]( {{< relref "magneto.md" >}}) | Electricity | +5 Wt | This building consumes oil at a rate of $0.05$ per tick [4, 8]. | [4] |
| [Solar Farm]( {{< relref "solar_farm.md" >}}) (Upgrade of Pasture) | Ecology | +2 Wt | Solar Farms are safer to upgrade to than Hydro Plants. They produce **+1.5 Wt in Winter** and **+2.67 Wt in Summer** [9-11]. | [9] |
| [Hydro Plant]( {{< relref "hydro_plant.md" >}}) (Upgrade of Aqueduct) | Robotics | +5 Wt | Upgrading Aqueducts to Hydro Plants should be approached cautiously as it can lead to starvation if catnip production is insufficient [9, 11, 12]. | [9] |
| [Reactor]( {{< relref "reactor.md" >}}) | Nuclear Fission | +10 Wt | Reactors consume uranium at a rate of $0.001$ per tick [4, 13]. | [4] |
| **Satellite** | Satellites | +1 Wt | Satellites initially consume 1 Wt, but with the [Solar Satellites]( {{< relref "solar_satellites.md" >}}) upgrade (unlocked by Orbital Engineering), they produce **+1 Wt** instead of consuming it [7]. | [7, 9, 14] |
| [Sunlifter]( {{< relref "space/sunlifter.md" >}}) | N/A (Space Structure) | N/A (Antimatter) | Sunlifters produce Antimatter when the year changes, provided energy is positive [15]. | [15] |
| **Advanced Energy Challenge Buildings** | N/A | N/A | The [Energy]( {{< relref "energy.md" >}}) challenge requires unlocking and building at least one of every energy production building and space structure, which includes **Steamworks, Magneto, Solar Farms, Hydro Plant, Reactor, Satellite, Sunlifter, Tectonic, and HR Harvester** [3]. | [3] |

### Energy Boosts and Management

Energy production and consumption can be managed through various upgrades and cycles:

*   **Reactor Upgrades:** The [Cold Fusion]( {{< relref "cold_fusion.md" >}}) upgrade increases Reactor energy output by **2.5 Wt** (+25%) [16]. The [Thorium Reactors]( {{< relref "thorium_reactors.md" >}}) upgrade also increases Reactor energy output by $0.25$ Wt (+25%) [16].
*   **Solar Farm Upgrades:** [Photovoltaic Cells]( {{< relref "photovoltaic_cells.md" >}}) increase Solar Farm energy production by **+50%** [7]. [Thin Film Cells]( {{< relref "thin_film_cells.md" >}}) and [Quantum Dot Cells]( {{< relref "quantum_dot_cells.md" >}}) provide further percentage increases, especially in specific seasons [7].
*   [Oil Wells:]( {{< relref "buildings/Oil_Well.md" >}}) The [Pumpjack]( {{< relref "pumpjack.md" >}}) upgrade for Oil Wells increases oil output by 45% and causes Oil Wells to consume **1 Wt** of energy [16].
*   **Cycles:** The [Helios]( {{< relref "helios.md" >}}) cycle increases [Sunlifter]( {{< relref "space/sunlifter.md" >}}) energy output by **+50%** [17]. Conversely, the [T-minus]( {{< relref "t_minus.md" >}}) cycle decreases [Sunlifter]( {{< relref "space/sunlifter.md" >}}) energy output by **-50%** [17].
*   **Policy/:** The [Dark Nova]( {{< relref "dark_nova.md" >}}) cryptotheology upgrade provides a **+2% global energy production** bonus [18].

Maintaining positive energy is vital, as a negative energy balance will result in production penalties [3, 19]. Pollution is partially mitigated by using environmentally friendly energy sources [2].