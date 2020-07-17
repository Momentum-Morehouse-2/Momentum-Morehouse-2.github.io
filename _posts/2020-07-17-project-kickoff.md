---
layout: post
title: Ready Set Code
tags: phase-4 agile final-project
---


## Before you start writing code

Today should be used for finalizing planning and doing research on data, technology, and tools you might need.

Check to see if you have these pieces in place before you start writing code:

- Every team member is clear on your MVP and you know what you are building.
- You have added user stories and tasks for MVP to your Trello board.
  - Your tasks should reflect the decisions you have made about how you will implement things
  - Make sure you are clear on what responsibilities belong to the front end or back end.
- You have created a team organization on GitHub and added every team member.
- You have created your project repo or repos on GitHub.
- You are clear on the git and GitHub workflow for your team.

### Checklist for the back-end

- Models! What models will you need?
  - What fields belong on those models? Use the Django Model Field Reference.
  - What relationships exist between your models? (one-to-many, many-to-many?)
    - Consider using [the CRC model](http://agilemodeling.com/artifacts/crcModel.htm) to help guide your discussions.
    - You should create an ER diagram for your models to map relationships.
- What URLs will the front end need?
- What data will the front end request?
  - Are you returning HTML? -> What templates does the front end need, and who will make those?
  - Are you returning JSON? -? How will you structure your data?

### Checklist for the front-end

- Can you map out a user flow through your app?
- Wireframes for each interface the user will see
  - With backend, can you say what URL corresponds to each page or interface the user sees?
  - If using React Router, what urls do you need?
- What data will you need on each page or interface? Where is it coming from?
  - What requests will you need to make from the front end?
- Are you making forms? Discuss data with the backend.
- What assets will you need?
- General strategy for css so that you can budget time for it
  - Starting to think about UI and design
