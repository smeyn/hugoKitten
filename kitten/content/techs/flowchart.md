+++
date = 2025-12-24T09:54:31.502035+11:00
draft = true
title = "Flowchart"

+++

```mermaid
---
config:
  flowchart:
    defaultRenderer: "elk"
---
flowchart TD
  
  
    calendar["`[Calendar]( {{< relref "techs/Calendar.md" >}}) 30 science`"]
    agriculture["`[Agriculture]( {{< relref "techs/Agriculture.md" >}}) 100 science`"]
    mining["`[Mining]( {{< relref "techs/Mining.md" >}}) 500 Science`"]
    metal_working["`[Metal Working]( {{< relref "techs/Metal_Working.md" >}})  900 Science`"]
    archery["`[Archery]( {{< relref "techs/Archery.md" >}}) 300 science`"]
    animal["`[Animal Husbandry]( {{< relref "techs/Animal_Husbandry.md" >}}) 500 science`"]
    math["`[Mathematics]( {{< relref "techs/Mathematics.md" >}})<br> 1000 science`"]
    civil["`[Civil Service]( {{< relref "techs/Civil_Service.md" >}})<br> 1500 science`"]
    currency["`[Currency]( {{< relref "techs/Currency.md" >}})<br> 2200 science`"]
    construction["`[Construction]( {{< relref "techs/Construction.md" >}})<br> 1300 science`"]
    engineering["`[Engineering]( {{< relref "techs/Engineering.md" >}})<br> 1500 science`"]
    writing["`[Writing]( {{< relref "techs/Writing.md" >}})<br>1500 science`"]
    steel["`[Steel]( {{< relref "craft/Steel.md" >}})<br> 1500 science`"]
    machinery["`[Machinery]( {{< relref "science/machinery.md" >}}) <br>00 science`"]
  
    Philosophy["`[Philosophy]( {{< relref "science/Philosophy.md" >}})<br> 00 science`"]
    Theology["`[Theology]( {{< relref "science/theology.md" >}})<br> 00 science`"]
    CryptoTheology["`[CryptoTheology]( {{< relref "techs/Cryptotheology.md" >}})<br> 00 science`"]
    Astronomy["`[Astronomy]( {{< relref "techs/Astronomy.md" >}})<br> 00 science`"]
    Navigation["`[Navigation]( {{< relref "techs/Navigation.md" >}})<br> 00 science`"]
    Geology["`[Geology]( {{< relref "techs/Geology.md" >}})<br> 00 science`"]
    Biology["`[Biology]( {{< relref "techs/Biology.md" >}})<br> 00 science`"]
    BioChemistry["`[BioChemistry]( {{< relref "techs/Biochemistry.md" >}})<br> 00 science`"]
    Genetics["`[Genetics]( {{< relref "techs/Genetics.md" >}})<br> 00 science`"]
    Architecture["`[Architecture]( {{< relref "techs/Architecture.md" >}})<br> 00 science`"]
    Acoustics["`[Acoustics]( {{< relref "techs/Acoustics.md" >}})<br> 00 science`"]

    Drama["`[Drama and Poetry]( {{< relref "techs/Drama_and_Poetry.md" >}})<br> 00 science`"]
    Physics["`[Physics]( {{< relref "techs/Physics.md" >}})<br> 00 science`"]
    Electricity["`[Electricity]( {{< relref "techs/Electricity.md" >}})<br> 00 science`"]
    Industrialization["`[Industrialization]( {{< relref "techs/Industrialization.md" >}})<br> 00 science`"]
    Metallurgy["`[Metallurgy]( {{< relref "techs/Metallurgy.md" >}})<br> 00 science`"]
    Combustion["`[Combustion]( {{< relref "techs/Combustion.md" >}})<br> 00 science`"]
    Ecology["`[Ecology]( {{< relref "techs/Ecology.md" >}})<br> 00 science`"]
    Mechanization["`[Mechanization]( {{< relref "techs/Mechanization.md" >}})<br> 00 science`"]

    calendar --> agriculture
    agriculture --> mining --> metal_working
   
    agriculture-->archery
     archery-->animal
    animal-->math
    animal-->construction--> engineering-->writing
    animal-->civil-->currency
    writing-->steel
    writing-->machinery
    writing-->Philosophy
    Philosophy-->Theology-->CryptoTheology
    Theology-->Astronomy-->Navigation
    Navigation-->Physics-->Electricity-->Industrialization-->Mechanization
    Navigation-->Geology-->Biology-->BioChemistry-->Genetics
    Navigation-->Architecture-->Acoustics-->Drama
    Industrialization-->Metallurgy
    Industrialization-->Combustion-->Ecology
    Industrialization-->Mechanization-->Electronics
    Electronics-->Robotics-->AI-->Quantum_crypto-->BlackChain
    Electronics-->Rocketry-->OilProcessing
    Rocketry-->Satellites-->Orbital_Engineering-->Thorium
    Orbital_Engineering-->ExoGeology-->Advanced_exoGeology
    Electronics-->Nuclear_Fission-->NanoTechnology-->SuperConductors-->Antimatter-->TerraFormation-->Hyrdoponics
    Nuclear_Fission-->Particle_physics-->Chronophysics-->TachyonTheory-->VoidSpace-->ParadoxTheory
    Particle_physics-->DimensionalPhysics

```
 {{< img src="techs.png" alt="A detailed flowchart of the process" >}}