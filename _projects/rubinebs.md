---
layout: page
# title: The Eclipsing Binary Yield of the Vera Rubin Observatory
title: Simulating Eclipsing Binary Yields of the Rubin Observatory in the Galactic Field and Star Clusters
description: 
img: assets/img/geller21_fig.png
importance: 1
category: Time-Domain Astronomy
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/geller21_figemph.png" title="EB properties -- Rubin Obs." class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Histograms showing the ratio of recoverable-to-observable, observable-to-all, and recoverable-to-all eclipsing binaries in our simulation as a function of their properties. Solid lines show the <i>baseline</i> simulation and dotted lines show the <i>colossus</i> simulation; <i>baseline</i> refers to the standard planned observing cadence for the Rubin Observatory Legacy Survey of Space and Time. Recoverable EBs are ones for which we return an accurate period given observations over the ten-year run of the survey.
</div>

[Geller, Polzin et al. (2021)](https://ui.adsabs.harvard.edu/abs/2021ApJ...919...83G/abstract)
{: style="font-size: 110%; text-align: center;"}

<!-- This work examined looked at how many eclipsing binaries (EBs) we should anticipate observing (and correctly characterizing) during the Rubin Observatory's Legacy Survey of Space and Time. We explore two observing cadences -- the first, *baseline2018a* (*baseline*) is LSST's default cadence (roughly even sky coverage every \~3 days) and the second, *colossus_2664* (*colossus*), is a proposed cadence that better samples the plane of the Galaxy.

We generate stellar populations with `TRILEGAL`(Girardi et al. 2012; for the Galactic field) and `COSMIC`(Breivik et al. 2020; for the star clusters), and randomly select stars from these populations to create binaries. Taking those binary stars, we derive reasonable properties, sampling from period, eccentricity, and mass ratio distributions consistent with observations.

After screening for basic observability -- i.e., the modeled binaries have to eclipse, have periods <10 years, and be bright enough that they are observable with the Rubin Observatory but not so bright that they saturate the sensitive detector, we generate mock light curves (`ellc`; Maxted 2016) for the detached binaries that meet our observability criteria, using the two Rubin Observatory cadences (*baseline* and *colossus*) modeled with `OpSim` (Delgado et al. 2014). Light curves (and so EBs) for which we return the period via Lomb-Scargle periodograms (`gatspy`; VanderPlas & Ivezić 2015) are considered recoverable. 

Looking at the number of observable and recoverable EBs for the two cadences, more EBs are observable with *colossus*, but of those that are observable, a higher fraction are recoverable with the *baseline* cadence. With *baseline*, we expect \~3 million detached EBs to be observed and correctly characterized over the course of the Legacy Survey of Space and Time; the *colossus* cadence could potentially increase the observed sample by a factor of \~2 and increase the recoverable sample by up to 1.7x. Adding in non-detached eclipsing binaries results in an additional increase of up to a factor of \~3. -->

This work examined looked at how many eclipsing binaries (EBs) we should anticipate observing (and correctly characterizing) during the Rubin Observatory's Legacy Survey of Space and Time. We explore two observing cadences -- the first, *baseline2018a* (*baseline*) is LSST's default cadence (roughly even sky coverage every \~3 days) and the second, *colossus_2664* (*colossus*), is a proposed cadence that better samples the plane of the Galaxy.

We generate a realistic stellar population for each of the Galaxy, Galactic globular clusters, and Galactic open clusters, randomly selecting stars from these populations to create binaries and sampling their properties from realistic distributions consistent with observations. This constitutes our *all* binary population.

We designate eclipsing binaries which meet several observability criteria (including being oriented so that they eclipse, having periods < 10 years, band eing luminous enough to be detected with the Rubin Observatory but not so bright that they saturate the sensitive detector) as *observable* with Rubin Observatory. This population is further broken down into *recoverable* EBs, for which we return an accurate period from multi-band observations during the ten years of our simulated survey. 

Looking at the number of observable and recoverable EBs for the two cadences, more EBs are observable with *colossus*, but of those that are observable, a higher fraction are recoverable with the *baseline* cadence. With *baseline*, we expect \~3 million detached EBs to be observed and correctly characterized over the course of the Legacy Survey of Space and Time; the *colossus* cadence could potentially increase the observed sample by a factor of \~2 and increase the recoverable sample by up to 1.7x. Adding in non-detached eclipsing binaries results in an additional increase of up to a factor of \~3.

