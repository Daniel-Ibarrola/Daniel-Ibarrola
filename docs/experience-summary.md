# Experience Summary

This document contains my experience summary divided by company and then by project.

## Grid Dynamics - Project at Google

### JAX and XLA CI

I was a main contributor of the CI of JAX and XLA libraries. The CI of the libraries was very complex as it involved 
building and testing the libraries on different hardware (CPU, GPU, and TPU) as well as different 
operating systems, python versions, etc. The CI was using GitHub Actions, bash and python scripts.
The libraries used bazel for building and running tests.

My main contributions were:

- I implemented new workflows that that verified the Bazel build graph, making it much faster to catch breaking changes
in the build graph.
- I addressed security vulnerabilities in the GitHub Actions workflows and implemented new workflows that use static
code analysis tools to prevent any more security vulnerabilites being added in the future.
- Fixing bugs in the CI system and responding to incidents went something was broken.

### Culprit Finder

Implemented a python tool to catch regressions in GitHub Actions workflows. These improved the speed of finding bugs 
across JAX, XLA, and Tensorflow. Before this, engineers needed to manually bisect a workflow until they found the commit
responsible for the issue; this was a long and tedious task, that could take hours. The tool made possible to automate
this and reduce the process by a few hours (it could still take long to find the culprit commits as some workflows took
about an hour to run).

### CI Assistant Tool

## Intercon Security Systems

### Security Officer Scheduling Application

This project consisted of an application used to manage the schedules for security officers of the company.
It consisted of a Typescript/React frontend and a microservices architecture using lambda and Dynamo DB.

These were the main challenges:
- Legacy codebase with technical debt. Refactored both backend and frontend by splitting code by splitting code by 
concerns, separate data, business and presentation layer. Removed duplicate code. 
Made the code more readable and easier to maintain by sticking to SOLID principles, 
which speeded up the development of new features and bug fixing.
- Codebase had no unit tests at all. Added unit tests for the core functionality.
- Improved the performance of the backend by reworking access patterns in dynamo db. Some endpoints were taking
longer than the API gateway limit of 29 seconds because they performed full table scans. For example, one of the main
access patterns was shifts of contract by day. This was improved significantly by adding a GSI to the shifts table
that had contractId#date as partition key and created-date as sort key. The time was reduced to a couple of seconds
in the worst case.
- One of the main screens of the app was a gantt chart taking too long to render when a contract
had a lot of data. This component relied on a deprecated react open source library 
not designed for this use case. I built a new gantt chart component from scratch. This component used
 virtualization, which made it much faster to render.
- Another part of the application had an officer sidebar also having negative performance. This was caused because
the component was using useEffect hooks for event handlers, causing cascade re-renders. The other issue was used 
because the array of officers suffered many transformations in this component and it wasn't cached. The issues
were fixed by refactoring the code to move events to event handlers and memoizing the officer array.

### ATS

This project consisted of a custom ATS that facilitated the company the process of hiring new security officers. The app
had the following architecture:

Next.js (typescript) frontend deployed on ECS, and a Fast API backend as well in ECS. The database was PostgreSQL instance
in RDS and we used Terraform and Bitbucket pipelines for CI/CD. 

These are some of the main challenges I faced in this project:

**TODO**: investigate the exact metrics and steps to debug a slow react application.
- One of the screens consisted of a spreadsheet-like table having performance issues. I improved this significanlty first
by using memoization and then applying virtualization.
- The CD process of the pipeline was having issues because it ran a bash script to run terraform and set all necessary
variables based on the environment (staging or prod). I refactored the terraform code into modules and created
different environments to avoid having to do this. This reduced deployment errors by about 30%. This also helped improve
the code readability and maintainability as it was all written in a huge file, and I splitted the code by functionalities
like vpc, ecs, etc.
- Found security vulnerabilities in the cloud infrastructure as some resources were publicly exposed, and were moved
to a private subnet. Also improved security by using WAF

## Centro de Instrumentación y Registro Sísmico

### Seismic data acquisition system

This was a system that collected data from thousands of seismic stations that sent data every second. The data was processed
and sent to different locations for further analysis, visualization, etc. The backend was using python with asyncio, TCP
sockets, numpy, pytest. There was also a dashboard that showed the data using react and typescript and react-chartjs.

The main challenges were:
- Interfacing with legacy applications. Part of the data was sent to a legacy application called Earthworm. The documentation
was scarce and not friendly. Building a module that interfaced with Earthworm required a lot of research and diving
into its legacy C codebase.
- The frontend plotted the data in real time every second and it was becoming slow. It was fixed by storing incoming data in refs,
updating the chart instance directly, disabling animations, and limiting visible points to a rolling window.

  
### Automated Notification System

Implemented an automatic notification system to inform authorities when there was an earthquake, via different channels like
whats app, telegram and email. It ran in AWS lambda, using SES for email, SNS to integrate SES bonces, complaints, etc.
S3 to store media. It was deployed using terraform, github actions. This was an improvement over the old system that
was using a Gmail account to send emails and notifications were sent manually to telegram and whats app.

## Hospital Infantil de México Federico Gómez

### Drug Discovery Library

I owned a python drug discovery library. One of the main challenges was the implementation of algorithms that
screened databases of moleclues in seconds.