# Daniel Ibarrola Sánchez

+52 55 2116 5635 | daniel.ibarrola.sanchez@gmail.com | https://github.com/Daniel-Ibarrola | https://linkedin.com/in/d-ibarrola

## Professional Summary

Software Engineer with 6+ years of experience building backend systems and cloud infrastructure in Python, Node.js, and AWS. Past work includes fixing DynamoDB access patterns that cut API response times from 29s to a few seconds, building a CI bisection tool at Google that eliminated hours of manual regression hunting, and a real-time data pipeline serving thousands of seismic stations.

***

## Work Experience

**Senior Software Engineer** – Grid Dynamics (client: Google)  
*Sep 2025 – Present*

- Worked on CI and build infrastructure for Google's JAX and XLA libraries across CPU, GPU, and TPU hardware.
- Built GitHub Actions workflows that caught Bazel build graph breakages in seconds instead of waiting hours for a full build.
- Fixed security vulnerabilities in CI pipelines and added static analysis to prevent new ones.
- Built a Python CLI tool (Culprit Finder) that automated regression bisection for JAX, XLA, and TensorFlow CI, eliminating hours of manual workflow monitoring.
- Built a Gemini-backed CI diagnostic tool that reduced bug investigation time by 2–3 hours based on user feedback.

**Full Stack Developer** – Inter-Con Security Systems  
*Nov 2023 – Aug 2025*

- Fixed endpoints timing out past API Gateway's 29s limit by optimizing DynamoDB query patterns; worst-case response time dropped to a few seconds.
- Built a custom ATS from the ground up using Next.js, FastAPI, PostgreSQL on RDS, and ECS, with Terraform and Bitbucket Pipelines for CI/CD.
- Refactored Terraform into reusable modules with separate environments; reduced deployment errors by ~30%.
- Moved publicly exposed AWS resources to a private subnet and added WAF protection.
- Refactored a legacy Node.js and TypeScript/React codebase by separating concerns and removing duplicate logic; reduced regressions and sped up feature development.
- Added unit tests for core functionality to a codebase that had none.
- Mentored developers and helped raise testing and code review standards across the team.

**Software Engineer** – Centro de Instrumentación y Registro Sísmico, A.C.  
*Aug 2019 – Nov 2023*

- Built a Python backend (asyncio, TCP sockets) that processed real-time data from thousands of seismic stations.
- Built an integration module for Earthworm, a legacy C application with minimal documentation; handled the full production data volume reliably.
- Built an automated alerting system for earthquake detection, notifying authorities via WhatsApp, Telegram, and email.
- Replaced a manual notification process with an automated AWS pipeline (Lambda, SES, SNS, S3).
- Deployed and managed the system using Terraform and GitHub Actions.

**Research Assistant (Software Development)** – Hospital Infantil de México Federico Gómez  
*Apr 2021 – Apr 2023*

- Built and maintained an open-source Python library for drug discovery research.
- Coded molecular screening algorithms from scientific papers; screened ~250k molecules in seconds and ~4.5M in minutes.
- Added tests and refactored core parts of the library to improve reliability and maintainability.

***

## Education & Certifications

- B.Sc. in Biochemical Engineering – Universidad Autónoma Metropolitana, 2017–2021, First Class Honors
- AWS Certified Solutions Architect – Associate, Amazon Web Services, Issued April 2025

***

## Skills

- Backend & Databases: Node.js, FastAPI, Flask, PostgreSQL, DynamoDB, asyncio
- Cloud & Infrastructure: AWS, Terraform, Docker, Bazel, GitHub Actions, Bitbucket Pipelines
- Languages: JavaScript/TypeScript, Python, Bash, SQL
- AI tools: Claude Code, Gemini API, agentic workflow development
- Spoken Languages: English (Professional), Spanish (Native)
