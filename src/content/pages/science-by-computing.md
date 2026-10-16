---
path: '/science-by-computing/'
title: 'Expertise — Science by Computing'
kind: 'page'
intro: 'Supporting scientific applications, from numerical methods to execution on supercomputers.'
editorial: true
toc:
  - id: 'team'
    title: 'Building with scientific communities'
  - id: 'health-genomics'
    title: 'Life science'
  - id: 'Astrophysics-ancre'
    title: 'Astrophysics — ARK2-MHD'
  - id: 'ancre-plasma-physics'
    title: 'Fusion plasmas — GYSELA-X++'
  - id: 'physicalchemistry-ancre'
    title: 'Physical chemistry — deMon2k and MDFT'
  - id: 'Lightmatterinterraction-ancre'
    title: 'Light–matter interaction — Smilei'
  - id: 'ancre-energy'
    title: 'Energy — AMITEX and canoP'
---

<div class="legacy-anchors">
  <span class="anchor-alias" id="s-cience-by-c-omputing"></span>
  <span class="anchor-alias" id="t-he-t-eam"></span>
</div>

<section class="editorial-section" id="team">

## Building with scientific communities

The **Science by Computing (SbC)** team helps scientific communities develop simulation codes and
analysis tools. Working alongside researchers, it adapts applications to supercomputer
architectures, particularly exascale systems, and shares this expertise across disciplines.

**Team leader:** [Charles Prouveur](__BASE__member/charles-prouveur/).

</section>

<section class="editorial-section" id="health-genomics">

<figure class="application-illustration cad-identity">
  <a href="https://www.genomecad.fr/" rel="noopener noreferrer" target="_blank"
    ><img
      alt="CAD — Collecteur Analyseur de Données"
      height="128"
      loading="lazy"
      src="__BASE__brand/cad.svg"
      width="268"
  /></a>
</figure>

## Life science

**Contacts:** [Yves Vandenbrouck](__BASE__member/yves-vandenbrouck/) and
[Jean-Michel Batto](__BASE__member/jean-michel-batto/).

Maison de la Simulation contributes to the **computing infrastructure for large-scale genomic data
analysis** being developed through the **CEA–CAD collaboration**. Planned for deployment at the
**TGCC**, it will support genomic research and data reanalysis for healthcare.

The project combines data-workflow orchestration, analysis software and HPC resources, with **secure
computing environments**, controlled data access and a preference for **open-source components**.

<div class="editorial-links">
  <a
    href="https://www.cea.fr/presse/Pages/actualites-communiques/sante-sciences-du-vivant/CEA-CAD-infrastructure-de-calcul-medecine-genomique.aspx"
    rel="noopener noreferrer"
    target="_blank"
    >CEA–CAD infrastructure project <span aria-hidden="true">↗</span></a
  ><a href="https://www.genomecad.fr/" rel="noopener noreferrer" target="_blank"
    >About CAD <span aria-hidden="true">↗</span></a
  >
</div>

</section>

<section class="editorial-section" id="Astrophysics-ancre">

<figure class="application-illustration">
  <img
    alt="ARK2-MHD logo"
    loading="lazy"
    src="__BASE__media/279323244-1153730815458744-8011380091345293918-n-1022x1024-5dc3713c86.png"
  />
</figure>

## Astrophysics — ARK2-MHD

**Contact:**
<a href="https://www.wilder.diskstation.me/pascal-tremblin/" rel="noopener noreferrer" target="_blank">Pascal
Tremblin</a>.

**ARK2-MHD** is an open-source magnetohydrodynamics code for large-scale simulation, including
turbulent flows, magnetic fields and convective dynamos in stellar atmospheres.

Its second-order **MUSCL–Hancock finite volume scheme** combines **Kokkos** for portability across
OpenMP, CUDA and HIP with **MPI** for distributed execution. I/O and in situ analysis tools support
scaling to thousands of GPUs.

The work presented covers resolutions up to **4096³** and tests on AMD MI300, NVIDIA H100 and Intel
Max 1550 GPUs.

<div class="editorial-links">
  <a href="https://gitlab.erc-atmo.eu/remi.bourgeois/ark-2-mhd"
    >ARK2-MHD source code <span aria-hidden="true">↗</span></a
  >
</div>

</section>

<section class="editorial-section" id="ancre-plasma-physics">
  <figure class="application-illustration">
    <img alt="GYSELA-X++ illustration" loading="lazy" src="__BASE__media/image1-fd04970ada.png" />
  </figure>
  <h2>Fusion plasmas — GYSELA-X++</h2>
  <span id="gysela"></span>
  <p><strong>Contact:</strong> <a href="__BASE__member/thomas-padioleau/">Thomas Padioleau</a>.</p>
  <p>
    This work develops reusable gyrokinetic operators in modern C++, based on
    <strong>Kokkos, DDC and PDI</strong>. Separating physical and computational concerns makes the
    code easier to maintain and extend.
  </p>
  <p>
    Support includes Python integration for in situ analysis, packaging from laptops to
    supercomputers, performance analysis and optimisation.
  </p>
  <div class="editorial-links">
    <a href="https://gyselax.github.io/"
      >The GYSELA-X++ project <span aria-hidden="true">↗</span></a
    >
  </div>
</section>

<section class="editorial-section" id="physicalchemistry-ancre">

## Physical chemistry — deMon2k and MDFT

**deMon2k · Contact:** [Karim Hasnaoui](__BASE__member/karim-hasnaoui/).

With the **TheoSim group at ICP Orsay**, Maison de la Simulation supports this density functional
theory (DFT) package through debugging, optimisation, parallelisation and GPU porting. The work uses
MPI, OpenMP and ScaLAPACK for scalability, and MPI, CUDA/HIP and MAGMA for multi-GPU execution. It
also includes an OpenACC implementation of the Kohn–Sham matrix.

<figure class="application-illustration">
  <img
    alt="Physical chemistry illustration"
    loading="lazy"
    src="__BASE__media/unnamed-e1f9adee8b.png"
  />
</figure>

**MDFT · Contacts:**
<a href="https://fr-moser.cecam.org/" rel="noopener noreferrer" target="_blank">Riccardo Spezia</a>
and [Jean-Marc Lude](__BASE__member/jean-marc-lude/).

MDFT uses molecular density functional theory to calculate solvation properties of complex solutes
while retaining information on solvent structure, at a lower cost than QM/MM approaches.

Physical developments address different solvents, thermodynamic properties and coupling with an
electronic structure code to optimise molecules in their solvent. Computational developments rewrite
the spherical harmonics and FFT kernel with **Kokkos FFT** for heterogeneous computing.

<figure class="application-illustration">
  <img alt="MDFT illustration" loading="lazy" src="__BASE__media/proposition-1-55832c857f.jpg" />
</figure>

<div class="editorial-links">
  <a href="http://demon-software.com/public_html/index.html"
    >deMon2k <span aria-hidden="true">↗</span></a
  ><a href="https://www.icp.universite-paris-saclay.fr/theosim/en/theosim-2/"
    >TheoSim group <span aria-hidden="true">↗</span></a
  ><a href="https://github.com/yasahi-hpc/Mini_MDFT">MDFT <span aria-hidden="true">↗</span></a>
</div>

</section>

<section class="editorial-section" id="Lightmatterinterraction-ancre">

<figure class="application-illustration">
  <img alt="Smilei illustration" loading="lazy" src="__BASE__media/images-1-0daeeeb903.png" />
</figure>

## Light–matter interaction — Smilei

**Contact:** [Charles Prouveur](__BASE__member/charles-prouveur/).

**Smilei** is an open-source, collaborative Particle-In-Cell code written in C++. It supports
studies ranging from relativistic laser–plasma interactions to astrophysics, with physical modules
and geometries evolving alongside community needs.

Engineers at Maison de la Simulation contribute to the core code, GPU porting of its modules and
their use on recent supercomputers.

<div class="editorial-links">
  <a href="https://smileipic.github.io/Smilei/"
    >The Smilei project <span aria-hidden="true">↗</span></a
  >
</div>

</section>

<section class="editorial-section" id="ancre-energy">

## Energy — AMITEX and canoP

**AMITEX\_FFTP · Contact:** [Yushan Wang](__BASE__member/yushan-wang/).

This distributed Fortran solver uses FFTs to simulate nonlinear mechanical behaviour in
heterogeneous materials represented by regular 3D images. It runs on workstations, clusters and
large HPC infrastructures.

The collaboration addresses GPU porting of constitutive laws and of the solver, particularly 3D FFTs
with pencil domain decomposition.

<figure class="application-illustration">
  <img alt="AMITEX illustration" loading="lazy" src="__BASE__media/amitex-85b92ff0ae.png" />
</figure>

**canoP · Contact:**
<a href="https://www.wilder.diskstation.me/pascal-tremblin/" rel="noopener noreferrer" target="_blank">Pascal
Tremblin</a>.

This open-source computational fluid dynamics library uses **p4est** to adapt the mesh to the
solution. Refinement and coarsening concentrate resources where gradients are steep.

Models cover single-phase and two-phase flows: **monofluid**, the five-equation **bifluid5eq** model
and the seven-equation Baer–Nunziato **bifluid7eq** model. They address different flow regimes for
energy applications.

<div class="editorial-links">
  <a href="https://amitexfftp.github.io/AMITEX/index.html"
    >AMITEX_FFTP <span aria-hidden="true">↗</span></a
  ><a href="https://canop.readthedocs.io/en/latest/"
    >canoP documentation <span aria-hidden="true">↗</span></a
  >
</div>

</section>
