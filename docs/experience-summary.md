# Experience Summary

This document contains my experience summary divided by company and then by project.

## Grid Dynamics (Consulting Engagement at Google)

### JAX and XLA CI

I was a main contributor of the CI of JAX and XLA libraries. The CI of the libraries was very complex as it involved 
building and testing the libraries on different hardware (CPU, GPU, and TPU) as well as different 
operating systems, python versions, etc. The CI was using GitHub Actions, bash and python scripts.
The libraries used bazel for building and running tests.

My main contributions were:

- I implemented new workflows that verified the Bazel build graph, making it much faster to catch breaking changes
in the build graph (in a matter of seconds, in contrast the whole build could take hours).
- I addressed security vulnerabilities in the GitHub Actions workflows and implemented new workflows that use static
code analysis tools to prevent any more security vulnerabilities being added in the future.
- Fixing bugs in the CI system and responding to incidents when something was broken.

### Culprit Finder

Implemented a Python tool to automate regression bisection in GitHub Actions workflows, improving the speed of finding
bugs across JAX, XLA, and TensorFlow. Previously, engineers had to manually trigger and monitor workflow runs one by
one until they identified the responsible commit — a tedious process requiring constant attention over several hours.
The tool fully automated this bisection, eliminating the manual effort entirely. Total elapsed time still depended on
individual workflow durations (some took about an hour per run), but engineers no longer needed to babysit the process.

### CI Assistant Tool

Implemented a tool that helped engineers diagnose issues in CI workflows. This tool was integrated with Google's Gemini SDK.
According to some users, it helped reduce the time to diagnose and find bugs in CI workflows by a few hours.

## Intercon Security Systems

### Security Officer Scheduling Application

This project consisted of an application used to manage the schedules for security officers of the company.
It consisted of a Typescript/React frontend and a microservices architecture using lambda and Dynamo DB.

These were the main challenges:
- Legacy codebase with technical debt. Refactored both backend and frontend by splitting code by
concerns, separating data, business and presentation layers. Removed duplicate code.
Made the code more readable and easier to maintain by sticking to SOLID principles,
which sped up the development of new features and bug fixing.
- Codebase had no unit tests at all. Added unit tests for the core functionality.
- Improved the performance of the backend by reworking access patterns in DynamoDB. Some endpoints were taking
longer than the API gateway limit of 29 seconds because they performed full table scans. For example, one of the main
access patterns was shifts by contract and day. This was improved significantly by adding a GSI to the shifts table
that had contractId#date as partition key and created-date as sort key. The time was reduced to a couple of seconds
in the worst case.
- One of the main screens of the app was a Gantt chart taking too long to render when a contract
had a lot of data. This component relied on a deprecated React open source library
not designed for this use case. I built a new Gantt chart component from scratch using
virtualization, which made it much faster to render. The render time improved by 90%.
- Another part of the application had an officer sidebar with negative performance. This was caused because
the component was using useEffect hooks for event handlers, causing cascade re-renders. The other issue was
that the array of officers suffered many transformations in this component and it wasn't cached. The issues
were fixed by refactoring event handling and memoizing the officer array.
- After the refactoring, the metrics improved like this:

INP: roughly 84% improvement
LCP: roughly 69% improvement

### ATS

This project consisted of a custom ATS that facilitated the company's process of hiring new security officers. The app
had the following architecture:

Next.js (TypeScript) frontend deployed on ECS, and a FastAPI backend also in ECS. The database was a PostgreSQL instance
in RDS and we used Terraform and Bitbucket pipelines for CI/CD.

These are some of the main challenges I faced in this project:

- One of the screens consisted of a spreadsheet-like table having performance issues. I improved this significantly first
by using memoization and then applying virtualization. This improved rendering time from approximately 3s to 30ms (~99%)
and INP by about 80%.
- The CD process of the pipeline was having issues because it ran a bash script to run terraform and set all necessary
variables based on the environment (staging or prod). I refactored the terraform code into modules and created
different environments to avoid having to do this. This reduced deployment errors by about 30%. This also helped improve
code readability and maintainability as it was all written in a single large file; I split the code by functionality
(vpc, ecs, etc.).
- Found security vulnerabilities in the cloud infrastructure as some resources were publicly exposed, and moved them
to a private subnet. Also improved security by using WAF.

## Centro de Instrumentación y Registro Sísmico

### Seismic data acquisition system

This was a system that collected data from thousands of seismic stations that sent data every second. The data was processed
and sent to different locations for further analysis, visualization, etc. The backend was using Python with asyncio, TCP
sockets, numpy, pytest. There was also a dashboard that showed the data using React, TypeScript and react-chartjs.

The main challenges were:
- Interfacing with legacy applications. Part of the data was sent to a legacy application called Earthworm. The documentation
was scarce and not friendly. Building a module that interfaced with Earthworm required a lot of research and diving
into its legacy C codebase. The resulting module reliably handled the full production data volume.
- The frontend plotted the data in real time every second and it was becoming slow. It was fixed by storing incoming data in refs,
updating the chart instance directly, disabling animations, and limiting visible points to a rolling window. This improved
rendering time by about 70%.

### Automated Notification System

Implemented an automatic notification system to inform authorities when there was an earthquake, via different channels like
WhatsApp, Telegram and email. It ran in AWS Lambda, using SES for email, SNS to handle SES bounces and complaints,
and S3 to store media. It was deployed using Terraform and GitHub Actions. This was an improvement over the old system that
was using a Gmail account to send emails and notifications were sent manually to Telegram and WhatsApp.

## Hospital Infantil de México Federico Gómez

### Drug Discovery Library

I owned a Python drug discovery library. One of the main challenges was the implementation of algorithms that screened
large molecular databases. To implement this, I researched scientific papers and implemented the algorithms in Python.
For example, the ZINC250k subset (~250k molecules) was screened in seconds, and larger subsets like Clean Leads
(~4.5M molecules) were screened in minutes. As a new project, there was no prior baseline to compare against.
