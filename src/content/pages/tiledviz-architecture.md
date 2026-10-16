---
path: '/tiledviz/'
title: 'TiledViz: use cases & architecture'
kind: 'page'
intro:
  'Brain imaging, climate science and collaboration: turning an image wall into a scientific
  analysis tool.'
editorial: true
toc:
  - id: 'scientific-and-technological-objectives-of-this-platform'
    title: 'Comparing ensembles, not just individual images'
  - id: 'braintwister-on-the-mandelbrot-image-wall'
    title: 'Brain imaging: understanding cortical diversity'
  - id: 'murs-images'
    title: 'From Wilder to Mandelbrot'
  - id: 'tiledviz'
    title: 'An architecture for moving results'
  - id: 'climat-neuro'
    title: 'Demonstrators in climate science and health'
---

<div class="legacy-anchors">
  <span class="anchor-alias" id="tiledviz-web-tool-for-tiled-visualisation"></span>
</div>

<section class="editorial-section" id="scientific-and-technological-objectives-of-this-platform">

## Comparing ensembles, not just individual images

Simulation produces sets of results that cannot be understood through a sequence of isolated figures
alone. In climate science, astrophysics and brain imaging, analysis often requires comparing tens or
hundreds of cases simultaneously.

**TiledViz & VRWall** retrieves results from a post-processing server and uses metadata to organise
them. It supports sorting and grouping images, annotating thumbnails, selective zooming, moving rows
and columns, and saving a layout for reuse.

<figure class="editorial-image">
  <img
    alt="Tiled visualisation on the Mandelbrot image wall"
    loading="lazy"
    src="__BASE__media/mandelbrot-tiledviz-03-1024x679-547a054f87.jpg"
  />
</figure>

</section>

<section class="editorial-section" id="braintwister-on-the-mandelbrot-image-wall">

## Brain imaging: understanding cortical diversity

Patterns in cortical folds differ between individuals and emerge during development. Comparing them
helps researchers study normal variability and anomalies associated with developmental conditions.
NeuroSpin’s work includes building a dictionary of patterns from tens of thousands of brains.

This requires training datasets prepared and corrected by experts. Viewing many brains side by side,
grouping similar conformations and synchronising their rotation supports this work and the
validation of classification methods.

The **BrainVISA** platform, developed by NeuroSpin’s UNATI laboratory, provides cortical fold
analysis tools. Its **Anatomist** visualisation software represents MRI data, brain meshes and
sulci. Identifications can be corrected manually, while C++ and Python libraries support dedicated
applications.

The **BrainTwister** prototype was developed with LRI at DIGITEO Moulon and Inria’s ExSitu team
within DIGISCOPE. It demonstrated the value of image walls for NeuroSpin’s research and, in the
longer term, the national CATI platform’s work on large cohorts.

</section>

<section class="editorial-section" id="murs-images">

## From Wilder to Mandelbrot

BrainTwister used **WildOS**, a node-webkit platform developed at LRI by Michel Beaudouin-Lafon’s
team. Multiple Anatomist instances displayed pairs of hemispheres on the Wilder wall, with
approximately **100 million pixels** across **6 metres**.

Infrared interaction supported group selection and synchronised rotations, but moving elements
between instances limited sorting. Freely comparing and rearranging brains is central to the
scientists’ work.

At Maison de la Simulation, **Mandelbrot** provides **33 million pixels** across **4.3 metres**,
with around twenty square metres of collaborative working space. The described setup uses a control
workstation and tablets and differs from Wilder’s infrared and touch interaction systems.

<figure class="editorial-image">
  <img
    alt="Exploring results on the Mandelbrot image wall"
    loading="lazy"
    src="__BASE__media/mandelbrot-tiledviz-01-1024x682-51161d4d6a.jpg"
  />
</figure>

</section>

<section class="editorial-section" id="tiledviz">

## An architecture for moving results

After WildOS and BrainTwister were installed at Saclay, TiledViz was designed as a generic
application independent of WildOS, removing sorting constraints and supporting different families of
simulations and experiments.

Visualisation applications run in **Docker containers**, exporting their output through **VNC** over
secure tunnels. Sharing the host kernel and devices limits 3D rendering overhead. Containers also
control communication ports and allow databases to be mounted read-only.

The described implementations include VNC communication on the cluster’s internal network and remote
access through SSH tunnels. Early demonstrators ran up to a hundred containers on a shared-memory
server, before distributing rendering across dedicated graphics nodes.

A client–server mechanism manages streams and launches remote containers as displayed elements move.
Client startup is automated to maintain interaction across the full image wall.

</section>

<section class="editorial-section" id="climat-neuro">

## Demonstrators in climate science and health

An initial prototype was built with **LSCE** and **CliMAF** work involving IPSL and Météo-France. It
supported interactive sorting of climate output images using metadata, in a browser and during
sessions in front of Mandelbrot.

Integrating Anatomist then enabled comparison of brain series from NeuroSpin databases. Both use
cases share an objective: organise data visually so several specialists can examine it and discuss
it together.

<figure class="editorial-image">
  <img alt="TiledViz interface" loading="lazy" src="__BASE__media/tiledviz-487e217704.png" />
</figure>

<div class="editorial-links">
  <a href="__BASE__tiledviz-2/">TiledViz and VRWall <span aria-hidden="true">↗</span></a
  ><a href="__BASE__contact/">Contact the visualisation team <span aria-hidden="true">↗</span></a>
</div>

</section>
