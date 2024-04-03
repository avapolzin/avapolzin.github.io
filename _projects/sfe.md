---
layout: page
title: Uniformity of Star Formation Efficiency # with Local Properties
description: 
img: assets/img/sfe.png
importance: 4
category: Galaxy Evolution
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/sfe_full.png" title="star formation efficiency" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<!-- <div class="caption">
    This image can also have a caption. It's like magic.
</div> -->

Polzin et al. in prep<!-- [Polzin et al. in prep]() -->
{: style="font-size: 110%; text-align: center;"}

The star formation efficiency (SFE) is a key means of describing star formation activity in galaxies; here we adopt the more theory-driven value of star formation efficiency per free fall time, which is \~equivalent to the fraction of gas converted into stars over the lifetime of dense star-forming regions. There have been a number of observational studies that have found that the SFE is at the percent-level in giant molecular clouds and galaxies regardless of the local conditions (gas phase metallicity, surface density, ionizing radation field strength).

<!-- Using a realistic isolated disk simulation shown to reproduce the star forming properties of local dwarf galaxies (Semenov et al. 2021) and a suite of disks with the same physics run at different fixed metallicities (described in greater detail Polzin et al. submitted), --> 
Using a suite of realistic simulations, we look at the uniformity of star formation efficiency as a function of local galaxy properties. The star formation efficiency is defined as an exponental function of the virial parameter, taking into account density as well as both turbulent and thermal motions of the gas. We find that, with no fine-tuning, our simulations produce percent-level SFEs in star-forming gas across metallicity, radiation field strength, and the density of gas and stars, which is indicative of the physical prescriptions that govern simulated star formation/feedback processes being good descriptions of how the universe works. 

Since the uniformity of SFE is attributable to self-regulation of star formation (i.e., when the SFE increases past a certain stable point, the energy and momentum injection from stellar feedback returns the efficiency to \~0.01), we explore a toy case where we ignore the role of turbulence in computing the virial parameter. In the "turbulence-free" case, star formation efficiency is a strong function of gas metallicity (likely due to the varying strength of different cooling processes and the now-increased dependence on thermal properties of the gas) and is dependent on the surface density of gas and stars. Turbulence plays a key role in regulating star formation; not accounting for turbulence is tantamount to turning off self-regulation, which is why SFE is no longer independent of local galaxy properties.

