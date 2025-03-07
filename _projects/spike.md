---
layout: page
title: "spike: All-in-one tool to generate and resample space-based PSFs"
description: 
img: assets/img/spike.png
importance: 7
category: Galaxy Evolution
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/spike.png" title="silkscreen" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<!-- <div class="caption">
    This image can also have a caption. It's like magic.
</div> -->

[Polzin (2025)](https://ui.adsabs.harvard.edu/abs/2025arXiv250302288P/abstract)
{: style="font-size: 110%; text-align: center;"}

Point spread functions (PSFs) describe the distribution of light for a pure point source in an astronomical image due to the instrument optics. For deconvolution, as for point source photometry and for source removal, it is key to have an accurate PSF for a particular image. Space-based telescopes can then pose a challenge as their PSFs are informed by their complex construction and the myriad of pointings and rotations used to capture deep images. These telescopes also capture the highest resolution images of astronomical sources, resolving stars around even relatively distant galaxies. Proper co-addition of PSFs at a specific source position for space-based imaging is then both critical and challenging. This code, `spike`, can generate model and empirical PSFs for an arbitrary location on a single chip and then runs them through the same processing pipeline used to derive deep, co-added images, providing correctly co-added and resampled PSFs for images from the Hubble Space Telescope, the James Webb Space Telescope, and the Nancy Grace Roman Space Telescope.

`spike` is available on [GitHub](https://github.com/avapolzin/spike).