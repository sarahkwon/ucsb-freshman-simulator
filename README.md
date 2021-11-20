# UCSB Freshman Simulator

Text-based adventure game that represents the life of a typical student at UCSB with a focus on the protagonist's psychology and the brutality and frustration of the everyday struggle.

Theme: Opposing Forces: School work against free time, fighting the natural entropy of life 

“Living in between the two opposing forces. Existing on the edge of life and work.”

You are a first-year student at University of Santa Barbara, It is your first time away from home living on your own. How you choose to spend your time is wholly up to you. Do as you please but be aware that the forces of work and nature are out to destroy you should you choose not to act. 

# Overview

Engine: Python, Pygames

Objective: Survive for as much time as possible until a game over or a certain ending. 

The main gameplay loop is choosing which activities to do and events to visit, considering all of the available resources as well as mental and physical states of the character.

# Team

* Elly - writer
* Andy Wu - programmer
* Sarah Kwon - programmer
* Nick Nosov - programmer

# Mechanics:

Name entry: 
* Naming your player
* Naming your major

The name typed for your “player name” will insert for all scenarios that mention your name 

The name typed for “Major” will insert for all scenarios that mention a class or subject or major. 
* Ex: “You are a [Biology] student. You are late to your [Biology] class. Next week is the [Biology] final.”


Activities have estimates of how much time and energy they are going to take, however they are highly unreliable, but get better with time.

Events: Some activities will force the player into a random scenario where they must make a decision that will have an impact on their stats, time, money, status or progress certain ending flags or game overs. Increasing your stats through activities are the best way to survive these random scenario encounters so that you may have a more favorable outcome.

Types of events/activities:
* SE - scheduled events, you choose to attend
* RE - random events that affect you
* Activities - something that you choose to do

