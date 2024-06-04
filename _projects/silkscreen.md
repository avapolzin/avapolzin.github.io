---
layout: page
title: "SilkScreen: Dwarf galaxy masses, distances, and metallicities from survey imaging"
description: 
img: assets/img/silkscreenlogo.png
importance: 6
category: 
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/silkscreen.png" title="silkscreen" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<!-- <div class="caption">
    This image can also have a caption. It's like magic.
</div> -->

[Miller, Pasha, Polzin, & van Dokkum 2024]()
{: style="font-size: 110%; text-align: center;"}

Dwarf galaxies represent a fascinating, but challenging regime for observational study. New low surface brightness-optimized instruments have enabled us to detect and follow-up extremely faint, low mass galaxies. Recovering distances to such galaxies remains particularly difficult as they're intrinsically faint, posing problems for TRGB estimates, blue enough for SBF relations to be poorly calibrated, and often nearby enough for peculiar velocities to preclude easy distance determination from radial velocities. At the same time, accurate distance estimation is crucial for inferring physical properties.

`SilkScreen` uses simulation-based inference to recover distances to, and properties of, resolved and semi-resolved dwarf galaxies and globular clusters from multiband imaging (as from HSC SSP and DECaLS). We train a neural network on `ArtPop`-generated stellar populations spatially distributed based on galaxy-specific, measured structural parameters; this represents our "bespoke" model. We consider the bespoke model to be an initial proof-of-concept and are moving toward an amortized, "one model to rule them all" approach, which will be especially useful in the era of large galaxy surveys (like Rubin Observatory's Legacy Survey of Space and Time) that are sensitive to a myriad of interesting, low mass objects.

`SilkScreen` is available on [GitHub](https://github.com/tbmiller-astro/silkscreen).