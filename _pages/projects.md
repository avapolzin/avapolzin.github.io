---
layout: page
title: Research
permalink: /research/
# description: A growing collection of your cool projects.
years: [2024, 2023, 2022, 2021]
nav: true
nav_order: 2
display_categories: [Galaxy Evolution, Time-Domain Astronomy]
horizontal: false
---

My research focus is broadly galaxy evolution and cosmology. I have been a member of the Canadian Hydrogen Intensity Mapping Experiment and the Dragonfly Telephoto Array team, and I am a member of the Time Domain/Multi-Messenger Sub-Group for the High Energy X-ray Probe ([HEX-P](https://hexp.org)) proposal team.

I am interested in understanding the processes that impact star formation and the baryon cycle in low mass, low metallicity galaxies. I use both observations (of stellar populations and the gas in and around galaxies) and simulations to more holistically study the conditions under which star formation proceeds (or doesn't!) in local dwarf galaxies and galaxies at high redshift. An up-to-date list of quenched, isolated dwarf galaxy candidates and their inferred physical properties is available [here](https://avapolzin.github.io/projects/quench_list/).

See below for some research highlights (with brief summaries) and a list of publications.


<!-- pages/projects.md -->
<div class="projects">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_projects = site.projects | where: "category", category -%}
  {%- assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}

{%- else -%}
<!-- Display projects without categories -->
  {%- assign sorted_projects = site.projects | sort: "importance" -%}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div>

In a past life, my research was focused on time-domain astronomy (it's where my astrophysics research career started when I was an undergraduate at Northwestern!). It's a subfield I still love and return to sporadically.
<!-- I started my astrophysics research career in time-domain astronomy when I was an undergraduate at Northwestern. It's a subfield I love and return to sporadically. Two of the projects came out of my time at NU, while the third (at right) came about as a result of my participation in the (2021) La Serena School for Data Science. -->

<hr style="height:1px; visibility:hidden;" />

#### Software

In my spare time, I enjoy working on more computationally oriented projects that will hopefully be useful to (or fun for) the larger community. A few such projects are in the works right now, so do check back for updates.
- [`albumpl`](https://github.com/avapolzin/albumpl) -- Custom matplotlib color palettes based on album covers.
- [`angelus`](https://github.com/avapolzin/angelus) -- Crossmatch a field with existing galaxy catalogs and check virial coverage. (This idea was spun off of a function in [`uwstatus`](https://github.com/avapolzin/UWSStatusSearch), my package for checking the status of Dragonfly UW observations and cross-matching UW fields with existing galaxy catalogs.)
<!-- - [`teltrace`](https://github.com/ben-sappey/teltrace) -- Recover temperature and pressure of exoplanet atmospheres from Voigt profile fitting of telluric lines. (Made during Code/Astro 2023.) -->
- [`gaiacmds`](https://github.com/avapolzin/goodenough_gaia_cmds) -- "Good enough" star cluster color-magnitude diagrams recovered automatically from Gaia data. <!-- (designed for use in the classroom, rather than research).-->
- [`spike`](https://github.com/avapolzin/spike) -- Properly drizzled space-based point spread functions for more accurate photometry.

Some software comes out of the course of my usual (published) work, too!
- [`delight`](https://github.com/fforster/DELIGHT) -- Deep Learning Identification of Galaxy Hosts of Transients
- [`silkscreen`](https://github.com/tbmiller-astro/silkscreen) -- Infer properties of dwarf galaxies and star clusters from survey imaging using simulation-based inference.
- [`xraydlps`](https://github.com/avapolzin/X-rayLCs) -- Plot and classify X-ray transient light curves.

<hr style="height:15px; visibility:hidden;" />

## Publications

Below is a list of submitted, accepted, and published papers. My CV lists some additional *in preparation* papers, which have not yet been submitted, but for which drafts exist. These drafts may be made available upon reasonable request (as for fellowship or grant evaluation).

<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f {{ site.scholar.bibliography }} -q @*[year={{y}}]* %}
{% endfor %}

</div>
