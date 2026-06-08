# Daniel Ibarrola Sánchez

+52 55 2116 5635 | daniel.ibarrola.sanchez@gmail.com | https://github.com/Daniel-Ibarrola | https://linkedin.com/in/d-ibarrola

## Professional Summary

Software Engineer with 6+ years of experience building and improving frontend applications with React and TypeScript. Has worked on performance-critical UIs across scheduling, hiring, and data visualization products. Background includes significant render and interaction performance improvements at Inter-Con Security Systems, a real-time seismic data dashboard, and CI tooling at Google.

Known for making UIs faster, more maintainable, and easier to work with.

***

## Work Experience

**Senior Software Engineer** – Grid Dynamics (client: Google)  
*Sep 2025 – Present*

- Contributed to the CI infrastructure for Google's JAX and XLA libraries across CPU, GPU, and TPU hardware.
- Built a CI diagnostic tool backed by Google's Gemini SDK that helped engineers diagnose and find bugs in CI workflows, reducing investigation time by several hours according to users.
- Addressed security vulnerabilities in CI pipelines and added static analysis workflows to prevent new ones from being introduced.

**Full Stack Developer** – Inter-Con Security Systems  
*Nov 2023 – Aug 2025*

- Rebuilt the Gantt chart component from scratch after the existing one (based on a deprecated library not designed for this use case) became too slow. The new component used virtualization and cut render time by 90%.
- Fixed performance issues in an officer sidebar caused by useEffect-based event handlers triggering cascade re-renders and an uncached officer array. Moved to direct event handlers and added memoization.
- After the above refactoring, Core Web Vitals improved: INP by ~84%, LCP by ~69%.
- Fixed a slow spreadsheet-like table using memoization and virtualization; cut render time from ~3s to ~30ms (~99% improvement) and INP by ~80%.
- Refactored a legacy TypeScript/React codebase: split code by concern (data, business, presentation layers), removed duplicate logic, and applied SOLID principles — sped up feature development and reduced regressions.
- Added unit tests for core functionality to a codebase that had none.
- Mentored developers and helped raise testing and code review standards across the team.

**Software Engineer** – Centro de Instrumentación y Registro Sísmico, A.C.  
*Aug 2019 – Nov 2023*

- Built a real-time React/TypeScript dashboard that visualized incoming seismic data every second. Fixed rendering performance by storing incoming data in refs, updating the chart instance directly, disabling animations, and capping visible points to a rolling window — cut render time by ~70%.
- Built and maintained a Python backend using asyncio and TCP sockets that collected and processed data from thousands of seismic stations.
- Built an automated alerting system on AWS (Lambda, SES, SNS, S3) that notified authorities when an earthquake was detected, via WhatsApp, Telegram, and email.

**Research Assistant (Software Development)** – Hospital Infantil de México Federico Gómez  
*Apr 2021 – Apr 2023*

- Built and maintained an open-source Python library for drug discovery research.
- Researched and translated molecular screening algorithms from scientific papers into Python.
- Added tests and refactored core parts of the library to improve reliability and maintainability.

***

## Education & Certifications

- B.Sc. in Biochemical Engineering – Universidad Autónoma Metropolitana, 2017–2021, First Class Honors
- AWS Certified Solutions Architect – Associate, Amazon Web Services, Issued April 2025

***

## Skills

- Frontend: React, TypeScript, Tailwind, React Query, Zustand, Jest
- Languages: JavaScript/TypeScript, Python, Bash, SQL
- Cloud & Infrastructure: AWS, Terraform, Docker, GitHub Actions, Bitbucket Pipelines
- AI: Claude Code, Gemini, Agentic Coding, Prompt Engineering
- Backend & Databases: Node.js, FastAPI, PostgreSQL, DynamoDB
- Spoken Languages: English (Professional), Spanish (Native)
