---
layout: page
title: Modeling Molecular Hydrogen in Low Metallicity Galaxies
description: 
img: assets/img/fh2_crop.png
importance: 3
category: Galaxy Evolution
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/fh2.png" title="DELIGHT" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<!-- <div class="caption">
    This image can also have a caption. It's like magic.
</div> -->

[Polzin et al. submitted](https://ui.adsabs.harvard.edu/abs/2023arXiv231010712P/abstract)
{: style="font-size: 110%; text-align: center;"}

In this work, we present analytic prescriptions that can be used to accurate model molecular hydrogen in the interstellar medium based on gas density, metallicity, and ionizing radiation field. Previous models have been calibrated for higher metallicity galaxies; we have calibrated our expressions for f<sub>H<sub>2</sub>></sub> down to 0.01 Z<sub>sun</sub>, which corresponds to metallicities consistent with local dwarf galaxies and galaxies at high redshift where the global gas metallicity is lower.

We share two expressions -- one for use in 3D simulation grid cells and the other for use with projected 2D maps smoothed on various scales. This allows for H<sub>2</sub> modeling in both high-resolution galaxy simulations and semi-analytic models of galaxy formation and evolution. We accurately recover the molecular hydrogen mass across the entire range we've tested (0.01 - 1 Z<sub>sun</sub> and scales of 10 pc - 1 kpc) to a factor of < 1.5 and perform significantly better than any existing models in the literature.

We also demonstrate that the structure of the interstellar medium is heavily dependent on the gas metallicity (with a smoother density distribution at lower Z) and that the molecular gas fraction drops at < 0.1 Z<sub>sun</sub>, consistent with  H<sub></sub> formation timescales that are longer than the average lifetime of giant molecular clouds.

Though our prescriptions accurately describe the behavior of H<sub>2</sub>, we note that these expressions should not be used to directly model star formation. We find that, while the depletion time of molecular hydrogen varies by a factor of >200 across two decades in metallicity, the star formation rate onky varies by a factor of 10. In this regime f<sub>H<sub>2</sub>></sub> and star formation are not tightly/linearly coupled, and it is likely that the proportion of star formation occuring in atomic (rather than molecular) gas increases at low metallicity.



