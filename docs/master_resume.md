# Daniel Ibarrola Sánchez

+52 55 2116 5635 | daniel.ibarrola.sanchez@gmail.com | https://github.com/Daniel-Ibarrola | https://linkedin.com/in/d-ibarrola

## Professional Summary

Senior software engineer with a track record of inheriting slow or fragile systems and making them fast and maintainable — API latency, frontend render times, CI pipelines, Terraform infrastructure. Currently building CI tooling for Google's JAX and XLA. Six years of full-stack production experience across Python, TypeScript, React, and AWS.

***

## Work Experience

**Senior Software Engineer** – Grid Dynamics (client: Google)  
*Sep 2025 – Present*

- Worked on CI and build infrastructure for Google's JAX and XLA libraries across CPU, GPU, and TPU hardware.
- Wrote GitHub Actions workflows that caught Bazel build graph breakages in seconds instead of waiting hours for a full build.
- Fixed security vulnerabilities in CI pipelines and added static analysis to prevent new ones.
- Wrote a Python CLI tool that automated regression bisection for JAX, XLA, and TensorFlow CI, eliminating hours of manual workflow monitoring.

**Full Stack Developer** – Inter-Con Security Systems  
*Nov 2023 – Aug 2025*

- Refactored a legacy TypeScript/React and Node.js codebase by separating concerns and removing duplicate logic; reduced regressions and sped up feature development.
- Increased testing coverage by 20%.
- Fixed endpoints timing out past API Gateway's 29s limit by optimizing DynamoDB query patterns; worst-case response time dropped to a few seconds.
- Rebuilt the scheduling timeline component from scratch using virtualization; cut render time by 90%.
- Fixed excessive re-renders in a sidebar by replacing useEffect-attached handlers with direct JSX handlers and memoizing the list data.
- Combined with the timeline virtualization work above, improved Core Web Vitals: INP ~84% better, LCP ~69% better.
- Built a custom ATS from the ground up using Next.js, FastAPI, PostgreSQL on RDS, and ECS, with Terraform and Bitbucket Pipelines for CI/CD.
- Fixed a slow data table with memoization and virtualization; render time dropped from ~3s to ~30ms and INP improved by ~80%.
- Refactored Terraform into reusable modules with separate environments; reduced deployment errors by ~30%.
- Moved publicly exposed AWS resources to a private subnet and added WAF protection.

**Software Engineer** – Centro de Instrumentación y Registro Sísmico, A.C.  
*Aug 2019 – Nov 2023*

- Wrote a Python backend (asyncio, TCP sockets) that processed real-time data from thousands of seismic stations.
- Implemented an integration module for Earthworm, a legacy C application with minimal documentation; handled the full production data volume reliably.
- Built a real-time React/TypeScript seismic data dashboard; fixed rendering performance using refs and a rolling data window, cutting render time by ~70%.
- Implemented an automated alerting system for earthquake detection, notifying authorities via WhatsApp, Telegram, and email.
- Replaced a manual notification process with an automated AWS pipeline (Lambda, SES, SNS, S3).
- Deployed and managed the system using Terraform and GitHub Actions.

***

## Education & Certifications

- B.Sc. in Biochemical Engineering – Universidad Autónoma Metropolitana, 2017–2021, First Class Honors
- AWS Certified Solutions Architect – Associate, Amazon Web Services, Issued April 2025

***

## Skills

- Languages: JavaScript/TypeScript, Python, Bash, SQL
- Frontend: React, Tailwind, React Query, Zustand, Jest
- Cloud & Infrastructure: AWS, Terraform, Docker, Bazel, GitHub Actions, Bitbucket Pipelines
- Backend & Databases: Express.js, FastAPI, Flask, PostgreSQL, DynamoDB
- Spoken Languages: English (Professional), Spanish (Native)
