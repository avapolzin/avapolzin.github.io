---
layout: page
title: Deep Learning Identification of Galaxy Hosts of Transients using Multiresolution Images (DELIGHT)
description: 
img: assets/img/delight.png
importance: 3
category: Time-Domain Astronomy
# github: https://github.com/fforster/DELIGHT
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/delight.png" title="DELIGHT" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<!-- <div class="caption">
    This image can also have a caption. It's like magic.
</div> -->

[Förster et al. (2022)](https://ui.adsabs.harvard.edu/abs/2022AJ....164..195F/abstract)
{: style="font-size: 110%; text-align: center;"}

This project was started during the 2021 La Serena School for Data Science, and represents the first publication to come out of an LSSDS session in program history.

In conjunction with the ALeRCE team and under the supervision of Prof. Francisco Förster Burón, we trained a convolutional neural network to rapidly associate transient signals with candidate host galaxies, which is vital for gaining preliminary redshift information.

Our deep learning method (which employs the CNN to identify a transient's host from survey postage stamps) consistently does as well as, or better than, predicting hosts from normalized distances or gradient ascent measurements.

DELIGHT was featured in [El Mostrador](https://www.elmostrador.cl/cultura/2023/01/11/broker-astronomico-chileno-alerce-crea-herramienta-para-identificar-de-forma-automatica-las-galaxias-donde-se-producen-nuevas-supernovas/) and [Nova Ciencia](https://novaciencia.es/la-herramienta-para-identificar-de-forma-automatica-las-galaxias-donde-se-producen-nuevas-supernovas/).

To install DELIGHT, simply follow the instructions on [GitHub](https://github.com/fforster/DELIGHT) or `pip install astro-delight`.