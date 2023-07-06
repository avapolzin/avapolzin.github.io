---
layout: page
title: Duration-Luminosity Phase Space of X-ray Transients
description:
img: assets/img/xraydlps_crop.png
importance: 2
category: Time-Domain Astronomy
---



<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <!-- <iframe src="{{ '/assets/plotly/demo.html' | relative_url }}" frameborder='0' scrolling='no' height="500px" width="100%" style="border: 1px dashed grey;"></iframe> -->
        <iframe src="{{ '/assets/plotly/interactive_dlps.html' | relative_url }}" frameborder='0' scrolling='no' height="630px" width="100%"></iframe>
    </div>
</div>

<div class="caption">
    An interactive version of the soft X-ray DLPS. To toggle individual classes on and off, click on items in the legend. Double click on one item to show only that class (double click the legend again and all classes will be turned on). Mousing over a light curve will show the name of the event. You can also zoom and pan.
</div>

[Polzin et al. submitted](https://ui.adsabs.harvard.edu/abs/2022arXiv221101232P/abstract)
{: style="font-size: 110%; text-align: center;"}

In this paper, we give an overview of transient and variable phenomena in the 0.3 - 10 keV band, looking at gamma-ray bursts, shock breakouts, supernovae, tidal disruption events, active galactic nuclei, fast blue optical transients, cataclysmic variables (like novae and dwarf novae), magnetar flares and outbursts, fast radio bursts, cool stellar flares, X-ray binaries, and ultraluminous X-ray sources.

We use real light curves to populate the duration-luminosity phase space, and extrapolate from that areas of interest in which theorized or yet-undiscovered signals might exist. We identify L<sub>x</sub> = 10<sup>34</sup> - 10<sup>42</sup> erg s<sup>-1</sup> and t = 10<sup>-4</sup> - 0.1 days as a key discovery phase space in transient X-ray astronomy.

We also take this opportunity to look at the performance parameters of various soft X-ray imaging instruments. Both extremely sensitive and large FOV instruments are key for the future of the field, with wide field instruments enabling serendipitous discovery of transient signals and low flux limits allowing for targeted follow up.

Data used in the paper are available on [GitHub](https://github.com/avapolzin/X-rayLCs) along with a package (`xraydlps`) intended to help with plotting and, *very preliminary*, classification from X-ray light curves.

You can also play with an interactive version of the full DLPS above or some of the other phase space plots below.

{% details Subclass-highlighted DLPS %}
<!-- Somewhat more crowded, but very useful for more detailed examination! -->
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <iframe src="{{ '/assets/plotly/interactive_dlps_subclasses.html' | relative_url }}" frameborder='0' scrolling='no' height="630px" width="125%"></iframe>
    </div>
</div>
{% enddetails %}

{% details L<sub>x</sub> vs. t<sub>1/2</sub> %}
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <iframe src="{{ '/assets/plotly/interactive_dlps_lxthalf.html' | relative_url }}" frameborder='0' scrolling='no' height="630px" width="120%"></iframe>
    </div>
</div>
{% enddetails %}

{% details Subclass-highlighted L<sub>x</sub> vs. t<sub>1/2</sub> %}
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <iframe src="{{ '/assets/plotly/interactive_dlps_lxthalf_subclasses.html' | relative_url }}" frameborder='0' scrolling='no' height="630px" width="120%"></iframe>
    </div>
</div>
{% enddetails %}

{% details E<sub>iso</sub> vs. Duration %}
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <iframe src="{{ '/assets/plotly/interactive_dlps_eisodur.html' | relative_url }}" frameborder='0' scrolling='no' height="630px" width="120%"></iframe>
    </div>
</div>
{% enddetails %}


{% details Subclass-highlighted E<sub>iso</sub> vs. Duration %}
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <iframe src="{{ '/assets/plotly/interactive_dlps_eisodur_subclasses.html' | relative_url }}" frameborder='0' scrolling='no' height="630px" width="120%"></iframe>
    </div>
</div>
{% enddetails %}

{% details DFPS %}
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <iframe src="{{ '/assets/plotly/interactive_dfps.html' | relative_url }}" frameborder='0' scrolling='no' height="630px" width="120%"></iframe>
    </div>
</div>
{% enddetails %}


{% details Subclass-highlighted DFPS %}
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <iframe src="{{ '/assets/plotly/interactive_dfps_subclasses.html' | relative_url }}" frameborder='0' scrolling='no' height="630px" width="120%"></iframe>
    </div>
</div>
{% enddetails %}


