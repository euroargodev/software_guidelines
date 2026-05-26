#  Argo Research Infrastructure Software Integration Level (SIL)

A maturity scale to assess the development stage and integration level of Argo-related software, from early concepts to foundational tools.

Here is the list of SILs:
- 🏆 SIL-1: Basic Concept Exploration 
- 🛠️ SIL-2: Functional Prototype 
- 🧪 SIL-3: Minimal Viable Research Software 
- 🔄 SIL-4: Structured Open-Source Project 
- ✅ SIL-5: Verified Research Software 
- 👥 SIL-6: Community-Driven Tool 
- 🏗️ SIL-7: Robust Open-Source Software
- 🌍 SIL-8: Field-Tested Open-Source Software
- 🏛️ SIL-9: Foundational Software

Each SIL is assigned a list of guidelines categorised as: "1-Required", "2-Recommended" and "3-Best effort".

Guidelines marked as "3-Best effort" always stay on this requirement level.
However, a guideline marked as "2-Recommended" for a given SIL is considered as "1-Required" for any upper SIL. Therefore, the higher the SIL, the higher the number of required guidelines to follow.

SIL are envisioned as a 2-ways improvement feature: 
- it help the RI staff to develop softwares,
- it provides softwares a RI _certification_.
In other words, the SIL framework not only guides developers in progressively improving their software to meet higher standards, but also serves as a formal recognition system, certifying that a software meets the Argo Research Infrastructure's expectations for quality, interoperability, and community integration at a given level.

## SIL description

### 🏆 **SIL-1: Basic Concept Exploration**
![](https://img.shields.io/badge/content-🏆%201--Basic%20Concept%20Exploration-066889?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)

- **Description**: Initial research ideas or concepts often explored as a simple script or notebook.
- **Focus**: Early exploratory stage.
- **Example Requirements**:
  - Basic statement explaining the problem or scientific objective.
  - Proof of concept demonstrated for a specific scientific question or calculation.
  - Limited scope: code tailored to specific data or a single-use case.
  - Minimal documentation (e.g., inline comments or short descriptions).

### 🛠️ **SIL-2: Functional Prototype**
![](https://img.shields.io/badge/content-🛠️%202--Functional%20Prototype-00788f?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)

- **Description**: Standalone code that expands the initial concept into a functional tool with a clear purpose.
- **Focus**: Moving toward broader applicability.
- **Example Requirements**:
  - Code hosted on a repository under version control.
  - Code modularized into functions or classes.
  - Basic usage instructions (e.g., a `README` file).
  - Version control for code and possibly required data.
  - Basic error handling and input validation.
  - Licensing information included in a LICENSE file (we recommend EUPL).

### 🧪 **SIL-3: Minimal Viable Research Software**
![](https://img.shields.io/badge/content-🧪%203--Minimal%20Viable%20Research%20Software-00888d?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)

- **Description**: The software is usable by collaborators in a limited context, with basic documentation and installation instructions.
- **Focus**: Limited sharing and reproducibility.
- **Example Requirements**:
  - Clear separation of code, configuration parameters, data inputs, and outputs.
  - Complete `README` explaining installation and usage.
  - Simple example datasets included for user testing.
  - Tested on at least one computing environment.
  - Ability to process different datasets (e.g.: other WMOs, sensors or missions) with minor modifications.
  - Initial presentation to an Argo-related group.


### 🔄 **SIL-4: Structured Open-Source Project**
![](https://img.shields.io/badge/content-🔄%204--Structured%20Open%20Source%20Project-009784?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)

- **Description**: Transition to a structured open-source project with initial community input and adherence to Argo standards and open-source best practices.
- **Focus**: Adoption of open-source principles.
- **Example Requirements**:
  - Code bugs and issues can be reported with an online tracker.
  - Modular codebase with reusable components fully integrated into the software design.
  - External dependencies are identified (e.g., numerical libraries, plotting packages).
  - Automated unit tests for critical functions.
  - Full documentation: usage examples, API references, and installation instructions.
  - Installation via package managers (e.g., `pip`, `conda`, `Pkg.jl`, `CRAN`).
  - I/O compatibility with Argo data formats (e.g., NetCDF, CF conventions, CSV).


### ✅ **SIL-5: Verified Research Software**
![](https://img.shields.io/badge/content-✅%205--Verified%20Research%20Software-17a575?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)

- **Description**: The software is stable, well-documented, and ready for broader use in the Argo community.
- **Focus**: Broader use and validation within the community.
- **Example Requirements**:
  - Comprehensive testing suite (unit tests, integration tests).
  - Continuous integration (CI) for automated testing.
  - Broader compatibility (e.g., works on multiple operating systems).
  - Growing documentation: tutorials, FAQs, and troubleshooting guides.
  - Community involvement: feedback mechanisms like GitHub discussions and Argo meeting presentations.
  - Call for feedback from the ADMT.


### 👥 **SIL-6: Community-Driven Tool**
![](https://img.shields.io/badge/content-👥%206--Community%20Driven%20Tool-53b063?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)

- **Description**: The software is actively used by the Argo community, with contributions from external developers.
- **Focus**: Initial community engagement.
- **Example Requirements**:
  - Active contributors and maintainers outside the initial team.
  - Regular software updates, bug fixes, and a changelog.
  - Governance model (e.g., code of conduct, contributing guidelines).
  - Increasing user base, evidenced by citations or mentions in papers or by ADMT.
  - Interoperability with other tools, frameworks, or data formats.


### 🏗️ **SIL-7: Robust Open-Source Software**
![](https://img.shields.io/badge/content-🏗️%207--Robust%20Open%20Source%20Software-82b951?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)

- **Description**: Mature open-source software with a solid architecture and established role in the community.
- **Focus**: Stability and maturity.
- **Example Requirements**:
  - Proven robustness through user feedback and stress testing.
  - Backward compatibility maintained across versions and deprecation policy.
  - Extensive user documentation, including detailed API references.
  - High-quality assurance (e.g., coverage metrics for testing).
  - Support channels available (e.g., mailing lists or forums).

### 🌍 **SIL-8: Field-Tested Open-Source Software**
![](https://img.shields.io/badge/content-🌍%208--Field%20Tested%20Open%20Source%20Software-b2bf44?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)

- **Description**: Software proven to perform reliably in extensive use cases or collaborative research initiatives.
- **Focus**: Proven performance in real-world use.
- **Example Requirements**:
  - Advanced features for scalability and performance.
  - Real-world testing for diverse datasets, sensors, and platforms.
  - Support for long-term reproducibility: archived versions with DOI.
  - Peer-reviewed publication describing the software.
  - Active support channels.

### 🏛️ **SIL-9: Foundational Software**
![](https://img.shields.io/badge/content-🏛️%209--Fundational%20Software-e4c144?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)

- **Description**: The software is a critical component of the Argo research infrastructure.
- **Focus**: Widespread adoption and sustainability.
- **Example Requirements**:
  - Adoption and integration into operational Argo workflows (real-time, delayed mode or research procedures).
  - Extensive and active community support.
  - Long-term sustainability plan (e.g., funding, governance).
  - Actively cited in peer-reviewed research or Argo international report or governance bodies.
  - Integration with major data portals or modeling frameworks.

    
## Badges

![SIL-1](https://img.shields.io/badge/content-🏆%201--Basic%20Concept%20Exploration-066889?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```markdown
![SIL-1](https://img.shields.io/badge/content-🏆%201--Basic%20Concept%20Exploration-066889?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```

![SIL-2](https://img.shields.io/badge/content-🛠️%202--Functional%20Prototype-00788f?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```markdown
![SIL-2](https://img.shields.io/badge/content-🛠️%202--Functional%20Prototype-00788f?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level
```

![SIL-3](https://img.shields.io/badge/content-🧪%203--Minimal%20Viable%20Research%20Software-00888d?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```markdown
![SIL-3](https://img.shields.io/badge/content-🧪%203--Minimal%20Viable%20Research%20Software-00888d?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```

![SIL-4](https://img.shields.io/badge/content-🔄%204--Structured%20Open%20Source%20Project-009784?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```markdown
![SIL-4](https://img.shields.io/badge/content-🔄%204--Structured%20Open%20Source%20Project-009784?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```

![SIL-5](https://img.shields.io/badge/content-✅%205--Verified%20Research%20Software-17a575?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```markdown
![SIL-5](https://img.shields.io/badge/content-✅%205--Verified%20Research%20Software-17a575?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```

![SIL-6](https://img.shields.io/badge/content-👥%206--Community%20Driven%20Tool-53b063?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```markdown
![SIL-6](https://img.shields.io/badge/content-👥%206--Community%20Driven%20Tool-53b063?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```

![SIL-7](https://img.shields.io/badge/content-🏗️%207--Robust%20Open%20Source%20Software-82b951?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```markdown
![SIL-7](https://img.shields.io/badge/content-🏗️%207--Robust%20Open%20Source%20Software-82b951?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```

![SIL-8](https://img.shields.io/badge/content-🌍%208--Field%20Tested%20Open%20Source%20Software-b2bf44?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```markdown
![SIL-8](https://img.shields.io/badge/content-🌍%208--Field%20Tested%20Open%20Source%20Software-b2bf44?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```

![SIL-9](https://img.shields.io/badge/content-🏛️%209--Fundational%20Software-e4c144?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```markdown
![SIL-9](https://img.shields.io/badge/content-🏛️%209--Fundational%20Software-e4c144?logo=opensourceinitiative&logoColor=green&label=Argo%20R.I.%20Software%20Integration%20Level)
```

