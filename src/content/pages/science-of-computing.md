---
path: '/science-of-computing/'
title: 'Research — Science of Computing'
kind: 'page'
intro:
  'Developing methods, libraries and software environments that help scientific applications make
  effective use of large-scale computing.'
editorial: true
toc:
  - id: 'team'
    title: 'The science behind large-scale computing'
  - id: 'programming-models'
    title: 'Programming for heterogeneous architectures'
  - id: 'runtime-for-data-handling'
    title: 'Keeping data analysis close to the simulation'
  - id: 'hpda-and-visualization'
    title: 'Analyse, compare and visualise'
  - id: 'packaging-deployment-and-ci'
    title: 'Making scientific software usable'
  - id: 'ancre-AI'
    title: 'Connecting mathematics and architectures'
  - id: 'software'
    title: 'Software for the community'
---

<div class="legacy-anchors">
  <span class="anchor-alias" id="s-cience-of-c-omputing"></span>
  <span class="anchor-alias" id="themes"></span>
  <span class="anchor-alias" id="projects-collaborations"></span>
  <span class="anchor-alias" id="related-software"></span>
  <span class="anchor-alias" id="projects-collaborations-2"></span>
  <span class="anchor-alias" id="related-software-2"></span>
  <span class="anchor-alias" id="related-software-3"></span>
  <span class="anchor-alias" id="projects-collaborations-3"></span>
</div>

<section class="editorial-section" id="team">

## The science behind large-scale computing

The **Science of Computing (SoC)** team develops methods and tools that help scientific applications
benefit from high-performance computing. Computer science, artificial intelligence and applied
mathematics come together in five complementary research areas.

**Team leader:**
<a href="https://work.julien-bigot.fr" rel="noopener noreferrer" target="_blank">Julien Bigot</a>.

<p class="scientific-networks">
  Our research is connected with the national scientific computing community through
  <a
    href="https://groupe-calcul.cnrs.fr/pages/presentation_gdr.html"
    rel="noopener noreferrer"
    target="_blank"
    >RT Calcul (formerly GDR Calcul)</a
  >
  and <a href="https://gdr-c4p.cnrs.fr/" rel="noopener noreferrer" target="_blank">GDR C4P</a>. The
  team is also connected with the <strong>CEA “Calcul intensif” network</strong>. These links
  support exchanges on numerical methods, parallel computing, software and computing architectures.
</p>

<div class="editorial-links">
  <a href="__BASE__science-by-computing/"
    >Explore the applications supported by SbC <span aria-hidden="true">↗</span></a
  ><a href="#software">Browse our software <span aria-hidden="true">↗</span></a>
</div>

</section>

<section class="editorial-section" id="programming-models">

<figure class="chapter-icon">
  <img
    alt="Programming models"
    loading="lazy"
    src="__BASE__media/programming-model-icon-993ee465f6.png"
  />
</figure>

## Programming for heterogeneous architectures

**Contact:**
<a href="https://orcid.org/0000-0003-1269-1825" rel="noopener noreferrer" target="_blank">Mathieu
Lobet</a>.

We investigate performance portability, particularly with **Kokkos** and **SYCL**, and emerging GPU,
FPGA and Arm architectures. Our goal is to make it easier to develop scientific applications that
perform well across supercomputers, while exploring energy efficiency and quantum computing.

The team contributes to **Kokkos** and **DDC**, a library used by
[GYSELA-X++](__BASE__science-by-computing/#gysela) for tokamak plasma simulation. We also study FPGA
implementations of molecular dynamics and hydrodynamics kernels, using tools such as Maxeler and
oneAPI.

These activities are connected with [NumPEx / Exa-Soft](https://numpex.fr/), including Task 1.1 on
C++ code transformations and optimisation, the [CExA](https://cexa-project.org/) project on GPU
computing tools, and the application work package of the [HQI](https://www.hqi.fr/) initiative.

</section>

<section class="editorial-section" id="runtime-for-data-handling">

<figure class="chapter-icon">
  <img alt="Data handling" loading="lazy" src="__BASE__media/parallel-io-icon-f2b86ac54c.png" />
</figure>

## Keeping data analysis close to the simulation

**Contact:** [Yushan Wang](__BASE__member/yushan-wang/).

Large simulations require new approaches to I/O and analysis. With **PDI** and its plugins, we
develop data handling that is decoupled from simulation code. **Deisa** connects MPI applications
with distributed Dask processing to analyse results during computation.

The team supports the integration of these tools, in situ analytics and event detection, in
collaboration with the AI and visualisation group. It has contributed to data handling in the
astrophysics applications **ARK-MHD** and **NOVA++**.

Maison de la Simulation contributes to the leadership of **Exa-DoST**, the NumPEx project on
exascale data software and tools, and its Work Package 3.

</section>

<section class="editorial-section" id="hpda-and-visualization">

<figure class="chapter-icon">
  <img
    alt="Data analytics and visualisation"
    loading="lazy"
    src="__BASE__media/data-icon-49980464f0.png"
  />
</figure>

## Analyse, compare and visualise

**Contact:** [Martial Mancip](__BASE__member/martial-mancip/).

We build tools to make sense of simulation results, either during execution or after data has been
stored. Computer vision and supervised learning help detect events and structures and produce
indicators of a simulation’s evolution.

[TiledViz & VRWall](__BASE__tiledviz-2/) supports the exploration of simulation ensembles. VisIt,
ParaView and VMD complement our analysis and visualisation workflows. These approaches also address
complex data from medicine and biology.

</section>

<section class="editorial-section" id="packaging-deployment-and-ci">

<figure class="chapter-icon">
  <img
    alt="Software deployment"
    loading="lazy"
    src="__BASE__media/massive-parallelism-icon-62b2bef949.png"
  />
</figure>

## Making scientific software usable

**Contact:** <a href="https://work.julien-bigot.fr" rel="noopener noreferrer" target="_blank">Julien
Bigot</a>.

A library’s usefulness depends on more than its algorithms. Installation, packaging, continuous
integration and deployment are essential to adoption. Our experience combines the perspectives of
users, library developers and supercomputer administrators.

Collaboration with **IDRIS** covers the software environments of **Jean Zay** and regional resources
such as the Moulon computing centre. Supporting applications also builds practical experience with
containers, including Singularity on Adastra.

Established as a dedicated activity in 2023, this work draws on [Spack](https://spack.io/) and
[Guix-HPC](https://hpc.guix.info/). It is part of NumPEx, including **Exa-DI Work Package 3** on
packaging, deployment and continuous integration.

</section>

<section class="editorial-section" id="ancre-AI">

<figure class="chapter-icon">
  <img
    alt="Mathematics and computing architectures"
    height="230"
    loading="lazy"
    src="__BASE__media/mathematics-architectures-icon.svg"
    width="230"
  />
</figure>

## Connecting mathematics and architectures

**Contact:**
<a href="https://skokh.pages.math.cnrs.fr/homepage/" rel="noopener noreferrer" target="_blank">Samuel
Kokh</a>.

The team develops mathematical analysis and numerical methods suited to supercomputers and large
datasets, connecting theoretical foundations with the requirements of large-scale execution.

Research covers large linear systems, numerical methods for partial differential equations —
including finite volume methods — and algorithms for machine learning and artificial intelligence.

</section>

<section class="editorial-section" id="software">

## Software for the community

<div class="editorial-software-grid">

<article class="editorial-software" id="ddc">
  <figure class="software-logo">
    <img alt="Logo: DDC" loading="lazy" src="__BASE__media/logo-8ac2999c15.png" />
  </figure>
  <p class="eyebrow">Discrete domain computation</p>
  <h3>DDC</h3>
  <p>
    A header-only C++ library for multidimensional meshes. It provides containers based on C++23
    <code>mdspan</code>, geometric iterators and type-safe indexing. Mesh semantics support both
    generic and specialised algorithms.
  </p>
  <a href="https://ddc.mdls.fr/">Explore the project ↗</a>
</article>

<article class="editorial-software" id="deisa">
  <figure class="software-logo">
    <img alt="Logo: Deisa" loading="lazy" src="__BASE__media/deisa-6bf450eb35.png" />
  </figure>
  <p class="eyebrow">In situ analytics</p>
  <h3>Deisa</h3>
  <p>
    Deisa connects MPI simulations with distributed Dask processing. Analysing data during
    computation reduces transfers and intermediate storage.
  </p>
  <a href="https://github.com/deisa-project/deisa-dask">Explore the project ↗</a>
</article>

<article class="editorial-software" id="kokkos">
  <figure class="software-logo">
    <img alt="Logo: Kokkos" loading="lazy" src="__BASE__media/kokkos-621x1024-304fb1a36a.png" />
  </figure>
  <p class="eyebrow">Performance portability</p>
  <h3>Kokkos</h3>
  <p>
    The Kokkos ecosystem supports C++ applications across different hardware architectures using a
    shared code base. It is a Linux Foundation project and part of the High Performance Software
    Foundation.
  </p>
  <a href="https://kokkos.org/">Explore the project ↗</a>
</article>

<article class="editorial-software" id="pdi">
  <figure class="software-logo">
    <img alt="Logo: PDI" loading="lazy" src="__BASE__media/pdi-icon-5d8a2f1085.png" />
  </figure>
  <p class="eyebrow">Data interface</p>
  <h3>PDI</h3>
  <p>
    PDI decouples applications from data handling libraries. Code annotations and an external
    specification organise parameter reading, initialisation, post-processing, output,
    visualisation, fault tolerance, logging, coupling and simulation ensembles.
  </p>
  <a href="https://pdi.dev/">Explore the project ↗</a>
</article>

<article class="editorial-software" id="tiledviz">
  <figure class="software-logo">
    <img alt="Logo: TiledViz" loading="lazy" src="__BASE__media/logo-tiledviz-69ab7d6594.png" />
  </figure>
  <p class="eyebrow">Collaborative visualisation</p>
  <h3>TiledViz &amp; VRWall</h3>
  <p>
    A web application for organising and exploring sets of results. Metadata supports sorting and
    comparison on a workstation or an image wall.
  </p>
  <a href="__BASE__tiledviz-2/">Explore the project ↗</a>
</article>

<article class="editorial-software" id="yml">
  <figure class="software-logo">
    <img alt="Logo: YML" loading="lazy" src="__BASE__media/yml-icon-42f58d989d.png" />
  </figure>
  <p class="eyebrow">Computing workflows</p>
  <h3>YML</h3>
  <p>
    YML describes parallel applications using the YvetteML workflow language, independently of the
    underlying environment: grids, peer-to-peer systems or metacomputing.
  </p>
  <a href="http://yml.prism.uvsq.fr/">Explore the project ↗</a>
</article>

</div>

</section>
