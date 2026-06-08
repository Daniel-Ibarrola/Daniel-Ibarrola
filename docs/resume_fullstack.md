# Daniel Ibarrola Sánchez

+52 55 2116 5635 | daniel.ibarrola.sanchez@gmail.com | https://github.com/Daniel-Ibarrola | https://linkedin.com/in/d-ibarrola

## Professional Summary

Software Engineer with 6+ years of experience across the full stack — Python and Node.js backends, React frontends, AWS infrastructure, and CI/CD tooling. Past work includes performance improvements across both layers: API response times cut from 29s to seconds, render times reduced by up to 99%, and CI tooling at Google that eliminated hours of manual work.

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

- Built a custom ATS from the ground up using Next.js, FastAPI, PostgreSQL on RDS, and ECS, with Terraform and Bitbucket Pipelines for CI/CD.
- Fixed endpoints timing out past API Gateway's 29s limit by optimizing DynamoDB query patterns; worst-case response time dropped to a few seconds.
- Fixed a slow data table with memoization and virtualization; render time dropped from ~3s to ~30ms and INP improved by ~80%.
- Rebuilt the scheduling timeline component from scratch using virtualization; cut render time by 90%.
- Refactored Terraform into reusable modules with separate environments; reduced deployment errors by ~30%.

**Software Engineer** – Centro de Instrumentación y Registro Sísmico, A.C.  
*Aug 2019 – Nov 2023*

- Built a Python backend (asyncio, TCP sockets) that processed real-time data from thousands of seismic stations.
- Built a real-time React/TypeScript seismic data dashboard; fixed rendering performance using refs and a rolling data window, cutting render time by ~70%.
- Built an integration module for Earthworm, a legacy C application with minimal documentation; handled the full production data volume reliably.
- Replaced a manual notification process with an automated AWS pipeline (Lambda, SES, SNS, S3), sending earthquake alerts via WhatsApp, Telegram, and email.
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

- Languages: JavaScript/TypeScript, Python, Bash, SQL
- Frontend: React, Tailwind, React Query, Zustand, Jest
- Backend & Databases: Node.js, FastAPI, Flask, PostgreSQL, DynamoDB
- Cloud & Infrastructure: AWS, Terraform, Docker, Bazel, GitHub Actions, Bitbucket Pipelines
- AI tools: Claude Code, Gemini API, agentic workflow development
- Spoken Languages: English (Professional), Spanish (Native)
