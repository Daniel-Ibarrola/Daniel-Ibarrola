# Daniel Ibarrola Sánchez

+52 55 2116 5635 | daniel.ibarrola.sanchez@gmail.com | https://github.com/Daniel-Ibarrola | https://linkedin.com/in/d-ibarrola

## Professional Summary

Software Engineer with 6+ years of experience building and improving systems across the full stack and cloud infrastructure. Has worked on Python and TypeScript backends, React frontends, AWS infrastructure, CI/CD pipelines, and developer tooling. Background includes CI/CD infrastructure for Google's JAX and XLA libraries at Grid Dynamics, full-stack development and performance work at Inter-Con Security Systems, real-time seismic data systems at a research center, and drug discovery software at a hospital research unit.

Known for making systems faster, safer, and easier to maintain.

***

## Work Experience

**Senior Software Engineer** – Grid Dynamics (client: Google)  
*Sep 2025 – Present*

- Contributed to the CI and build infrastructure for Google's JAX and XLA libraries, which support machine learning at scale on CPU, GPU, and TPU hardware.
- Built new GitHub Actions workflows that verified the Bazel build graph and caught breaking build changes in seconds, compared to waiting for full builds that took hours.
- Addressed security vulnerabilities in CI pipelines and added static analysis workflows to prevent new ones from being introduced.
- Built a Python CLI tool (Culprit Finder) that automated regression bisection across GitHub Actions workflows for JAX, XLA, and TensorFlow. Before this, engineers had to manually trigger and monitor workflow runs one by one to find the responsible commit — a process requiring constant attention over several hours. The tool eliminated the manual effort entirely.
- Built a CI diagnostic tool backed by Google's Gemini SDK that helped engineers diagnose and find bugs in CI workflows, reducing investigation time by several hours according to users.
- Helped build and maintain a GCP platform for GPU and TPU CI runners handling thousands of jobs per day.
- Responded to CI incidents and fixed bugs across GitHub Actions workflows and Bazel build configurations.

**Full Stack Developer** – Inter-Con Security Systems  
*Nov 2023 – Aug 2025*

- Refactored a legacy TypeScript/React and Node.js codebase: split code by concern (data, business, presentation layers), removed duplicate logic, and applied SOLID principles — sped up feature development and reduced regressions.
- Added unit tests for core functionality to a codebase that had none.
- Reworked DynamoDB access patterns that were causing endpoints to exceed API Gateway's 29-second limit due to full table scans. Added a GSI on the shifts table with contractId#date as partition key and created-date as sort key; worst-case response time dropped to a few seconds.
- Rebuilt the Gantt chart component from scratch after the existing one (based on a deprecated library not designed for this use case) became too slow. The new component used virtualization and cut render time by 90%.
- Fixed performance issues in an officer sidebar caused by useEffect-based event handlers triggering cascade re-renders and an uncached officer array. Moved to direct event handlers and added memoization.
- After the above refactoring, Core Web Vitals improved: INP by ~84%, LCP by ~69%.

- Fixed a slow spreadsheet-like table using memoization and virtualization; cut render time from ~3s to ~30ms (~99% improvement) and INP by ~80%.
- Refactored Terraform configuration from a single large file into reusable modules with separate staging and production environments; reduced deployment errors by ~30% and made the infrastructure code easier to read and maintain.
- Found and fixed security vulnerabilities in AWS infrastructure: moved publicly exposed resources to a private subnet and added WAF protection.
- Mentored developers and helped raise testing and code review standards across the team.

**Software Engineer** – Centro de Instrumentación y Registro Sísmico, A.C.  
*Aug 2019 – Nov 2023*

- Built and maintained a Python backend using asyncio and TCP sockets that collected and processed data from thousands of seismic stations, each sending updates every second.
- Built an integration module for Earthworm, a legacy seismic processing application with limited documentation; required reading through its C codebase to understand the wire protocol. The module reliably handled the full production data volume.
- Built a real-time React/TypeScript dashboard that visualized incoming seismic data. Fixed rendering performance by storing incoming data in refs, updating the chart instance directly, disabling animations, and capping visible points to a rolling window — cut render time by ~70%.

- Built an automated alerting system that notified authorities when an earthquake was detected, via WhatsApp, Telegram, and email.
- Replaced a manual process (personal Gmail account for emails, hand-sent Telegram and WhatsApp messages) with a fully automated AWS pipeline using Lambda, SES, SNS, and S3.
- Deployed and managed the system using Terraform and GitHub Actions.

**Research Assistant (Software Development)** – Hospital Infantil de México Federico Gómez  
*Apr 2021 – Apr 2023*

- Built and maintained an open-source Python library for drug discovery research.
- Researched and translated molecular screening algorithms from scientific papers into Python. The ZINC250k subset (~250k molecules) was screened in seconds; larger subsets like Clean Leads (~4.5M molecules) ran in minutes.
- Added tests and refactored core parts of the library to improve reliability and maintainability.

***

## Education & Certifications

- B.Sc. in Biochemical Engineering – Universidad Autónoma Metropolitana, 2017–2021, First Class Honors
- AWS Certified Solutions Architect – Associate, Amazon Web Services, Issued April 2025

***

## Skills

- Languages: JavaScript/TypeScript, Python, Rust, Go, Bash, SQL
- Frontend: React, Tailwind, React Query, Zustand, Jest
- Cloud & Infrastructure: AWS, Terraform, Docker, Bazel, GitHub Actions, Bitbucket Pipelines
- AI: Claude Code, Gemini, Agentic Coding, Prompt Engineering
- Backend & Databases: Express.js, FastAPI, Flask, PostgreSQL, DynamoDB
- Spoken Languages: English (Professional), Spanish (Native)
