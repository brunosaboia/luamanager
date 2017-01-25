# LUA Manager
A system to help manage Academic Centers from [Universidade Federal do Ceará](https://ufc.br)

## TL;DR
This project has the goal to provide student-run academic centers an easy way to manage their work.

## Description
The project is written in [python](https://python.org), and it aimed specifically to aid UFC students who are responsible to run their respective course's academic centers in their operation.

The aim is to have the following modules:

- **Voting platform**: Allow students to vote on important matters;
- **"Carteirinha de Estudante" (Student Card) assistant**: Help the center to organize all the process relative to obtain a student's card;
- **Teacher's avaliation**: Enable students to give their opinion about a specific teacher;
- **Exams database**: Collects previous exams to aid students to prepare for exams;
- **Course Tree**: Shows a tree-like visualization of the course, which aid students to plan their disciplines in order to graduate faster;

## Setup
In order to use the system, you must have a properly configured [Facebook app](https://developers.facebook.com/) and a [public page](https://www.facebook.com/pages/create/). Data fetched from the public page will be displayed at LUA Manager's start page.

For debugging purposes, you may run `python ./src/setup_debug.py`, and edit the `settings_debug.yaml` file with your real app information. Those files are .gitignore'd, so you need to change them prior to debugging whenever you clone the repository.

When pushing to production, please remember to update your files (database and yaml) accordingly. 

**DO NOT PUSH DEBUG FILES TO PRODUCTION!** Debug files have preference over non-debug files, and will be used in case they exist.


## Background
This system was born as an idea to improve the academic center of Economics. The basic idea is to give a stronger voice to the students, which can effectively participate on decisions that impact their academic lives, without having the burden of having to go to face-to-face meetings, which can be long and uninteresting.
