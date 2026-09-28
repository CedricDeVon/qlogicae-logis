</br>

<div style="width: 100%; display: flex; justify-content: center;">
    <image alt="the ${{ main-company-base-name }} logo" src="${{ main-company-base-logo-filesystem-path }}" width="256px">
</div>

</br>


<div style="text-align: center;">
  <h1>${{ qlogicae-logis-display-brand-name }}</h1>
  <p style="font-style: italic;">${{ qlogicae-logis-base-description }}</p>
<div style="margin: 32px 64px;">

![Project - Version](https://img.shields.io/badge/Version-${{ qlogicae-logis-current-version-label }}-blue)
[![Python - Versions](https://img.shields.io/badge/Python-3.12|%933.13|%933.14-blue?logo=python&logoColor=gold)](https://www.python.org/)
![License - MIT](https://img.shields.io/badge/License-MIT-red)

![GitHub - Stars](https://img.shields.io/github/stars/CedricDeVon/qlogicae-logis)
[![GitHub - Actions](https://github.com/CedricDeVon/qlogicae-logis/actions/workflows/quality-assurance.yml/badge.svg)](https://img.shields.io/github/actions/workflow/status/CedricDeVon/qlogicae-logis/codeql.yml)

  </div>
</div>

</br>



<h2>📚 Table of Contents</h2>
<ul>
  <li><a href="#about">About</a></li>
  <ul>
    <li><a href="#about-description">Description</a></li>
    <li><a href="#about-supported-platforms">Supported Platforms</a></li>
    <li><a href="#about-core-features">Core Features</a></li>
    <li><a href="./documentation/index.md">Extended Documentation</a></li>
  </ul>
  <li><a href="#usage">Usage</a>
    <ul>
      <li><a href="#usage-pre-requisites">Pre-Requisites</a></li>
      <li><a href="#usage-installation">Installation</a></li>
    </ul>
  </li>
  <li><a href="#legalities">Legalities</a>
    <ul>
      <li><a href="#legalities-license">License</a></li>
    </ul>
  </li>  
</ul>

</br>



<h2 id="about">
  📖 About
</h2>
<h3 id="about-description">
  🧾 Description
</h3>
<p>
  "Hour-long build times is never a good sign, looking at you, mobile dev ecosystem ...".
</p>
<p>
  <strong>QLogicae Logis</strong> is an opinionated, multi-platform, multi-project, software development tool, as a CLI, written in Python3.
</p>
<ul>
  <li>
    <p>
      <strong>Opinionated</strong> - To contribute in developing software projects, regardless of programming language and integrated software development tools of choice.
    </p>
  </li>
  <li>
    <p>
      <strong>Multi-platform</strong> - Maximizing usability, to develop software projects, across multiple operating systems.
    </p>
  </li>
  <li>
    <p>
      <strong>Software Automation</strong> - Implemented via user-defined CI/CD-like workflows via YAML files - feeling right at home when using GitHub Actions. Other major built-in operations include: workflow macros programming, and applying filesystem templates across projects.
    </p>
  </li> 
  <li>
    <p>
      <strong>Python3</strong> - Selected as one of the codebase programming language of choice, with the aim to ease development time, learning curve, ease of collaboration, and multi-platform usage stability.
    </p>
  </li>
</ul>

<p>
  <strong>ADVICE</strong>: To get things straight, this tool is designed to be best suited for orchestrating large, or multiple projects with a shared deliverable. Developers can still utilize its features for relatively small, single-repository projects. Having said that, please do review your own project requirements.
</p>



<h3 id="about-core-features">
  ⚙️ Core Features
</h3>
<p>
  More can be potentially added, eventually. What this project offers now to its users (and contributors) are as follows:
</p>
<ul>
  <li>
    <p>Implementing CI/CD-Like Workflows via YAML Files</p>    
  </li>
  <li>
    <p>Applying Filesystem Templates</p>    
  </li>
  <li>
    <p>Workflow Macros Static and Dynamic Value Programming</p>    
  </li>
  <li>
    <p>3rd-Party Plugin API for Custom Commands, And Macros Values</p>    
  </li>
  <li>
    <p>And potentially more to come!</p>    
  </li>
</ul>

</br>

<p>
  To know more, check out the <a href="./documentation/index.md">extended documentation</a>.
</p>

</br>



<h2 id="usage">
  📋 Usage
</h2>

<h3 id="usage-prerequisites">
  📋 Prerequisites
</h3>

<p>
  For maximum convenience, please make sure that your computer meets these minimum system requirement(s) or have installed the following software:
</p>

<ul>
  <li>
    <p>
      <strong>Python Version</strong> >= 3.12
    </p>
  </li>
  <li>
    <p>
      <strong>Disk Memory Storage</strong> < 1 MB
    </p>
  </li>
  <li>
    <p>
      <strong>Supported Platform(s)</strong>    
      <ul>
        <li>
          <p>Windows 11</p>
        </li>
        <li>
          <p>macOS</p>
        </li>
        <li>
          <p>Linux Ubuntu</p>
        </li>
      </ul>
    </p>
  </li>
</ul>

<h3 id="usage-installation">
  📋 Installation
</h3>

<p>
  This application can be run as a global pip package or within python virtual environments.
</p>
<p>
  1. First, simply copy and paste the <code>pip install qlogicae-logis</code> comand on your command-line of choice. If you intend to use a python virtual environment, do activate your environment first, then run the installation command.
</p>
<p>
  2. After download completion, run <code>qlogicae-logis about version</code>. A verified, successful installation will be confirmed if either no error messages are displayed or the application version has been displayed.
</p>

</br>



<h2 id="legalities">
  🏛️ Legalities
</h2>

<h3 id="legalities-license">
  📋 License
</h3>

<p>
  The project is currently under the <a href="./LICENSE">MIT License</a>.
</p>

</br>
