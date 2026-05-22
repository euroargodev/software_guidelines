# Software development guidelines for Argo

This repository is dedicated to organize all the relevant content with regard to software development guidelines for the Argo community.

🎫 Guidelines are documented with [issues on this repository](https://github.com/euroargodev/software_guidelines/issues). 

You can check a simplified view of all guidelines in here:  
😉 https://euroargodev.github.io/software_guidelines

You can build your own tool based on the guidelines using this machine-to-machine readible file:
⚙️[Guidelines as a json file](https://raw.githubusercontent.com/euroargodev/software_guidelines/refs/heads/main/docs/guidelines_last.json)

If you participate in an Argo project and would like to evaluate your codebase, you can use the online evaluator at:  
🚀 https://euroargodev.github.io/Software-Evaluator

We manage guidelines with the following Github project:  
📋 https://github.com/orgs/euroargodev/projects/20

## Why software development guidelines ?
In the realm of oceanographic research infrastructures, the Argo program stands as a cornerstone, providing invaluable examples of data management good practices. As part of the Euro-Argo ERIC, the development of collaborative and open-source software is crucial for leveraging Argo data effectively. However, researchers and data engineers, who may not have a background in software development, face unique challenges in creating software that are both robust and compliant with FAIR principles (Findable, Accessible, Interoperable, and Reusable). This is where tailored guidelines become essential. 

## Guideline labels

Each guideline is labeled according to several categories. Here is the definition of such labels.

### Programming Skill Level
This category is not based on pure programming skills, it also blends with skill in open-source and collaborative development good practices. Here are the possible levels:
- Novice: Familiar with programming and open-source/collaborative development concepts but lacks practical experience.
- Beginner: Writes basic code, applies foundational practices, and may need guidance for open-source/collaborative workflows.
- Intermediate: Develops functional software, actively implements guidelines, and debugs independently.
- Advanced: Fully integrates best practices into workflows, mentors others, and contributes to collaborative projects.
- Expert: Drives best practices across teams, sets standards for open-source/collaborative development, and contributes to community tools or frameworks.

### Software Development Model (SDM)

- Open Source: Open-Source Guidelines focus on licensing, documentation, testing, distribution, and compliance with standards (e.g., Argo formats, FAIR principles).
- Collaborative: Collaborative Guidelines emphasize teamwork, version control, communication, and project management (e.g., Git workflows, meetings, issue tracking).

### Project Aspects

- Project Location: About where to store and manage the project content
- Project Content: About the repository content and organisation
- Project Management: About how the project and its codebase are managed, possibly collectively
- Codebase: About the codebase design and organisation
- Documentation and Outreach: About the project and codebase documentation and outreach (communication and dissemination)
- Argo compliance: About making use of all Argo tools

### FAIR4RS

FAIR for Research Software are the FAIR principles applied to a software. These are general guidelines that can be applied to any software, not only those related to Argo. 

- _Software is_ Findable: Software, and its associated metadata, is easy for both humans and machines to find
- _Software is_ Accessible: Software, and its metadata, is retrievable via standardised protocols
- _Software is_ Interoperable: Software interoperates with other software by exchanging data and/or metadata, through interaction via application programming interfaces (APIs), described through standards
- _Software is_ Reusable: Software is both usable (can be executed) and reusable (can be understood, modified, built upon, or incorporated into other software)

### Argo data FAIR tools

When developing an Argo software, we believe it is of primary importance to use and preserve all the tools and properties of the Argo dataset that make it FAIR data. The Argo dataset and GDAC services make Argo data FAIR in many ways. Here is a cherry-picked list of the tools to be used and preserved wherever relevant by any Argo RI Software:

- _Data used by the software is_ Findable: Input data are uniquely identifiable, i.e. based on Argo DOI and GDAC snapshot DOIs (persistent identifiers), Argo Netcdf and Vocabulary/Conventions (rich metadata), GDAC index files (index of data repositories)
- _Data used by the software is_ Accessible: Input data are fetched from public http, ftp, s3 GDAC servers, Vocabulary web-API (standardised, open and free protocols)
- _Data used by the software is_ Interoperable: Output data follow Argo conventions and vocabulary 
- _Data used by the software is_ Reusable: Output data preserve CC BY 4.0 License





***
This repository is developed within the framework of the Euro-Argo ONE project. This project has received funding from the European Union’s Horizon 2020 research and innovation programme under project no 101188133. Call HORIZON-INFRA-2024-DEV-03: Developing, consolidating and optimising the European research infrastructures landscape, maintaining global leadership.

<p align="center">
<a href="https://www.euro-argo.eu/EU-Projects/Euro-Argo-ONE-2025-2027">
<img src="https://github.com/user-attachments/assets/03865f96-010d-4712-a233-eb92e47be4ba" height="75"/>
</a>
</p>
