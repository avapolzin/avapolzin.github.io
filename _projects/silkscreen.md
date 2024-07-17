---
layout: page
title: "Silkscreen: Dwarf galaxy properties and distances from survey imaging"
description: 
img: assets/img/silkscreenlogo.png
importance: 6
category: Galaxy Evolution
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/new_silkscreen.png" title="silkscreen" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<!-- <div class="caption">
    This image can also have a caption. It's like magic.
</div> -->

[Miller, Pasha, Polzin, & van Dokkum (2024)](https://ui.adsabs.harvard.edu/abs/2024arXiv240704091M/abstract)
{: style="font-size: 110%; text-align: center;"}

Dwarf galaxies represent a fascinating, but challenging regime for observational study. New low surface brightness-optimized instruments have enabled us to detect and follow-up extremely faint, low mass galaxies. Recovering distances to such galaxies remains particularly difficult as they're intrinsically faint, posing problems for TRGB estimates; blue enough for SBF relations to be poorly calibrated; and often nearby enough for peculiar velocities to preclude easy distance determination from radial velocities. At the same time, accurate distance estimation is crucial for inferring physical properties.

`Silkscreen` uses simulation-based inference to recover distances to, and properties of, resolved and semi-resolved dwarf galaxies and globular clusters from multiband imaging (as from HSC SSP and DECaLS). We train a neural network on `ArtPop`-generated stellar populations spatially distributed based on galaxy-specific, measured structural parameters; this represents our "bespoke" model. We consider the bespoke model to be an initial proof-of-concept and are moving toward an amortized, "one model to rule them all" approach, which will be especially useful in the era of large galaxy surveys (like Rubin Observatory's Legacy Survey of Space and Time) that are sensitive to a myriad of interesting, low mass objects.

*We note that, though we focus on applications of `Silkscreen` to dwarf galaxies in this paper, the code can, in principle, be used on galaxies of all masses. This will be explored further in a future work.*

`Silkscreen` is available on [GitHub](https://github.com/tbmiller-astro/silkscreen).