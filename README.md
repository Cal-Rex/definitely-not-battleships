# QWETHT

[amiresponsive](#amiresponsive immage)

### The adventure game that goes beyond your wildest dreams. If your dreams were relatively unimaginative

---

## Table of Contents
1. [INTRODUCTION](#introduction)
2. [DESIGN](#design)
- [UX](#ux)
  - [Research](#research)
- [Development Planes](#development-planes)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure) 
  - [Skeleton](#skeleton)
- [Colour Scheme](#colour-scheme)
- [Typography](#typography)
- [Imagery](#imagery)

3. [FEATURES](#features)
- [Design Features](#design-features)
- [Visual Features](#visual-features)
- [Gameplay + JS Features](#gameplay-features)
- [404 and 500 Features](#404-and-500-error-pages)
- [Features to Implement in Future](#features-to-implement-in-future)

4. [BUGS](#bugs)
- [Resolved Bugs](#resolved-bugs)

5. [TECHNOLOGIES](#technologies)
- [Languages Used](#languages-used)
- [Frameworks](#frameworks--libraries--programs)
- [Libraries](#frameworks--libraries--programs)
- [Programs](#frameworks--libraries--programs)

6. [TESTING](testing.md)

Contained as a seperate document [here](testing.md)

7. [DEPLOYMENT](#deployment)

Step-by-step guide on how to deploy

8. [CREDITS](#credits)

9. [ACKNOWLEDGEMENTS](#acknolwedgments)

---

# Introduction

```
        ___________ _____ _____ _______    ____ _________ ______________
       /          //    //    //   _   \  /    \\    _   \\             \
      /          //    //    //   //   / /  /\  \\   \\   \\             \   
     /     _____//    //    //    '   / /  /  \  \\   \\   \\   \\   \\   \   
    /          //     '    //    _   | /  /   /  / \   \\   \\   \\   \\   \   
   /______    //          //    //   //  /___/  /   \   `    \\   \\   \\   \  
  /          //__________//_________//_________/     \________\\___\\   \\   \ 
 /          /  M   A   R   I   N   E ████ I   N   A   T   I   O   N  \   \\   \
/__________/ █████████████████████████████████████████████████████████\___\\___\

```

`S U B M A R I N E ██ D O M I N A T I O N`, is an iteration on a classic game of "Battleships", in a terminal using Python on the command line.

```

████████████████████████████████████████████████████████████████████████████████
█                 █                                          █                 █
█   WELCOME TO    █ +| A B C D E F G H || A B C D E F G H |+ █        THIS IS  █
█   SUBMARINE     █ -|-----------------||-----------------|- █  AN EXAMPLE OF  █
█   DOMINATION    █ 1| ~ @ ~ ~ @ ~ ~ ~ || ~ ~ X ~ ~ ~ ~ ~ |1 █  THE SIMULATED  █
█   SIMULATION    █ 2| ~ ~ ~ ~ ~ ~ @ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |2 █          ARENA  █
█   COMMANDER     █ 3| ~ ~ ~ ~ ~ ~ ~ ~ || ~ ~ ~ ~ . ~ ~ ~ |3 █                 █
█                 █ 4| ~ ~ ~ X ~ ~ ~ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |4 █    ENEMY SUBS   █
█ [LEFT] IS YOUR  █ 5| ~ . ~ ~ ~ ~ @ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |5 █ARE HIDDEN[RIGHT]█
█      ZONE       █ -|-----------------||-----------------|- █ . = MISSED SHOT █
█ @ = YOUR SHIPS  █ +| A B C D E F G H || A B C D E F G H |+ █  X = SUNK SUB   █
█                 █                                          █                 █
████████████████████████████████████████████████████████████████████████████████

```

The idea to shift the characteristics of the game to be _submarines_ instead of _battleships_ due to the nature that the player can see board boards simoultaneously.

When the program begins to run, players are asked to position 5 Submarines on the board:

```

AT THE START OF THE GAME, YOU WILL BE ASKED TO POSITION 5 SUBS
              LIKE THIS:
                     pick a lettered column between A - H:
              THEN LIKE THIS:
                      pick a numbered row between 1 - 5:

```

Once all 5 submarines are positioned, the game employs the same function to guess the coordinates of the computer's hidden submarines (it also has 5 submarines).

once a player's /computer's submarines have all been targeted, the game is over and a win/loss message is generated, supplemented with the otpion to start a new game.

**This project is the third of the five projects to be created for the Diploma in Full Stack Software Development (Common Curriculum)**

Based on the Learning outcomes of the section of the Diploma, this project aims to:

1. Create an interactive game through a _"given algorithm as a computer program"_ that projects  
2. Run a game of ` S U B M A R I N E ██ D O M I N A T I O N ` by _"Adapting and combining algorithms"_ to solve the processes and problem solving operations generated by the game's programming
3. Utilise _"standard programming constructs: repetition, selection, functions, composition, modules, aggregated data (arrays, lists, etc.)"_ to effictively run the game
4. _"Explain what the given program does"_ in it's code through effective commenting and docstrings
5. Using the project creation process to _"Identify and repair coding errors in a program"_
6. Create a Project that uses _"library software for building a graphical user interface, or command-line interface, or web application, or mathematical software"_
7. create a project that _"implements a data model, application features and business logic"_ and utilises these to generate easily recognisable responses and outcomes for users/players.
8. Create a Project that is developed through a documented process _"through a version control system such as **GitHub©**"_
9. Be Deployed on **Heroku©**


---

# Design

## UX

### **Research**

This project was designed to be a Minimally Viable Project (MVP). Therefore it aligns as-close-as-possible to the design brief. Of course, as the code developed, personal flair was intertwined with core conepts. But the primary focus of the project (to meet the design brief) was constantly at the forefront of design during development.

the following sources were viewed for the conept of UI visual layout **ONLY**:

| [Code Institute Project brief video](https://www.youtube.com/embed/4sqtzZQpDJE) |
|--------------------------------------------------------------------------------- |
| ![Battleships Example 3](assets/images/readme/battleships-ex3.png) |

| [trinket.io](https://trinket.io/python/051179b6d3) | [copyassignment.com](https://copyassignment.com/battleship-game-code-in-python/) |
| ------------------------------------ | ------------------ |
| ![battleships example 1](assets/images/readme/battleships-ex1.png) | ![battleships example 2](assets/images/readme/battleships-ex2.png) |

The following points were picked up by comparing the visual elements of the following 3 sources:
- UI is very narrow and bunched together
- The constraints of the UI makes User interface very bland and cluttered
- The visual representation for the "computer" playing the game is limited

Taking this into account. When the code for this project is developed. there will be focus drawn to making the command-line messages and interface more _game-like_.
<br>
<br>
<br>

## **Development Planes**

## Structure Plane
<br>


### **User Stories**

The following user stories were created based off of the following design brief set out in The [Portfolio Project 3 Assessment Guide](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/2?activate_block_id=block-v1%3ACodeInstitute%2BPE_PAGPPF%2B2021_Q2%2Btype%40vertical%2Bblock%403db2c53014c24243a11d471769df21e7):

    The Battleships game is played on grids on which each player's fleet of battleships are marked. The locations of the fleets are concealed from the other player. Players call shots at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.

    The application provides a working battleships game for a single user to play against the computer.

    Potential features to include:

      The ability for the user to set the grid size
      Warn the user if their guess is off-grid

      External user’s goal:
      The application user wants to play a logic game

The learning outcomes below hae also been taken as a point of reference for the project. sourced directly from The [Portfolio Project 3 Assessment Guide](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/2?activate_block_id=block-v1%3ACodeInstitute%2BPE_PAGPPF%2B2021_Q2%2Btype%40vertical%2Bblock%403db2c53014c24243a11d471769df21e7):

| Learning outcomes |
|-------------------|
|**LO1**	Implement a given algorithm as a computer program|
|**LO2**	Adapt and combine algorithms to solve a given problem|
|**LO3**	Adequately use standard programming constructs: repetition, selection, functions, composition, modules, aggregated data (arrays, lists, etc.)|
|**LO4**	Explain what a given program does|
|**LO5**	Identify and repair coding errors in a program|
|**LO6**	Use library software for building a graphical user interface, or command-line interface, or web application, or mathematical software|
|**LO7**	Implement a data model, application features and business logic to manage, query and manipulate data to meet given needs in a particular real-world domain.|
|**LO8**	Demonstrate and document the development process through a version control system such as GitHub|
|**L09**	Deploy a command-line application to a cloud-based platform|
<br>

After reviewing this information, the following user-stories were created:

1. _"As a user, i want to play a simple game of battleships"_
2. _"As a user, i want to play some kind of logic game"_
3. _"As a user, i want to be able to position my own ships to allow for own personal strategy"_
4. _"As a user, i want to play against a 'computer' player"_
5. _"As a user, i want to be able to make my own choices when trying to guess the position of enemy ships"_
6. _"As a user, i want to be notified if i accidentally pick the same coordinate twice"_
7. _"As a user, i want to be prompted if enter invalid coordinates"_ 
8. _"As a user, i want to feel like my choices matter against the 'computer' player, and that i won't win if i just select each coordinate in sequential order"_
<br>
<br>

### **Project Goals**

Based on the criteria outlined above, the following project goals have been divided into User Goals and Developer Goals. These have been listed below:

**User Goals:**
<br>
Based on the user stories, User goals are defined as:
- create a command line game that is easy to follow
- the UI must be readable and friendly within the given limitations
- Employ code that simulates players playing against a chellenging AI opponent
- Allow for elements of personal choice when positioning ships and targeting enemy ships
- have contingencies in place if a mistake is made during an input error
- not punish the user for not enetering EXACT coordinates information

**Developer Goals:**
<br>
Based on Project research and design brief, Developer Goals are defined as:
- Have a command line game deployed and playable on the internet via Heroku©
- Develop a version of the game _"Battleships"_ in the coding language: Python
- implement use of python libraries to enhance the UX of The terminal based game
- Make use of ASCII Art to add more of a visual element to the game
- create a program that only requires game narrative input from the user, no knowledge of working from a command line should be required to play the game.
<br>
<br>

## Scope Plane
<br>


Based on the results yielded from refining the design brief and research in the previous section, the following features will be developed for the project:

1. **Horizontal Game board and Center Aligned HUD design**
    - Given the terminal is wider than it is in height, the print statements for the game will be created to accomodate free lateral real estate in the terminal
2. **Classic Battleships Coordinates**
    - To elaborate on the focus of a user friendly feel, the coordinates used will be similar to that of the original _"Battleships"_, where players would target an area on the board by a letter and a number
3. **Game-like Narrative**
    - Flipping the concept of taking the terminal as a limitation to style and turning it into a style choice, create a narrative in the language of the interface to make the game mimic the style of gimmicky vintage war game
4. **Anticipated error handling on user input**
    - ensure that input field data isn't case sensetive
    - If invalid field data is parsed into the terminal, the programme can recognise how the data is invalid, notify the user, then let them retry inputting a value without crashing the programme or punishing the user
5. **Responsive Terminal**
    - The terminal will routinely clear and update game-state information, to prevent scrolling and simulate that of an interactive game
    - the gameboard in the terminal will update every time a turn or change has been made to the game board
6. **How to Play Section**
    - An option will be present at the start menu that will explian the rules of the game to the user
<br>
<br>

## Structure Plane
<br>

In Terms of web layout, the project is hosted entirely through the project template after being deployed to Heroku©

[Link to the template used to create the Repo for this project](https://github.com/Code-Institute-Org/python-essentials-template)
<br>

The page itself acts as an index, and has no further functionality as this is out-of-scope for this project

Regarding the terminal, the amount of `rows` was increased from `24` to `30` accomodate some additional descriptions within print statements and remove the need for scrolling.

in terms of game structure, the following flowchart was drafted on [LucidChart](https://www.lucidchart.com/):

![flowchart of programme designed in lucid.app](assets/images/readme/Flowcharts.png)
<br>
<br>

## Skeleton & Design Planes
<br>

Due to the nature of this project, both of these planes have been merged.

As this project was to run entirely of of a terminal. Notepad on Windows was the optimal choice to create mockups define the structure for each section. Transcript lisfted directly from planning and quoted in codeblock below:

```

80 columns x 24 rows
https://ascii.co.uk/art/submarine
https://ascii.co.uk/art/explosiv
.
                                  |`-:_
         ,----....____            |    `+.
        (             ````----....|___   |            - (sub art by Shimrod)
         \     _                      ````----....____
          \    _)                                     ```---.._
           \                                                   \
         )`.\  )`.   )`.   )`.   )`.   )`.   )`.   )`.   )`.   )`.   )`.
       -'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `


████████████████████████████████████████████████████████████████████████████████
████   /          //    //    //   _   \  /    \\    _   \\             \   ████
███   /          //    //    //   //   / /  /\  \\   \\   \\             \   ███
██   /     _____//    //    //    '   / /  /  \  \\   \\   \\   \\   \\   \   ██
█   /          //     '    //    _   | /  /   /  / \   \\   \\   \\   \\   \   █
█  /______    //          //    //   //  /___/  /   \   `    \\   \\   \\   \  █
█ /          //__________//_________//_________/     \________\\___\\   \\   \ █
█/          /█ M   A   R   I   N   E ████ I   N   A   T   I   O   N █\   \\   \█
█__________/ █████████████████████████████████████████████████████████\___\\___█
████████████████████████████████████████████████████████████████████████████████
                                      ____
                              __,-~~/~    `---.
                            _/_,---(      ,    )
                        __ /        <    /   )  \___
         - ------===;;;'====------------------===;;;===----- -  -
                           \/  ~"~"~"~"~"~\~"~)~"/   Nuclear
                           (_ (   \  (     >    \)   Explosion
                            \_( _ <         >_>'     Mushroom
                               ~ `-i' ::>|--"        - by Bill March
                                   I;|.|.|
                                  <|i::|i|`.
                                 (` ^'"`-' ")
         ------------------------------------------------------------------

███████████████████ +| A B C D E F G H || A B C D E F G H |+ ███████████████████
███████████████████ -|-----------------||-----------------|- ███████████████████
███████████████████ 1| ~ ~ ~ ~ ~ ~ ~ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |1 ███████████████████
███████████████████ 2| ~ ~ ~ ~ ~ ~ ~ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |2 ███████████████████
███████████████████ 3| ~ ~ ~ ~ ~ ~ ~ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |3 ███████████████████
███████████████████ 4| ~ ~ ~ ~ ~ ~ ~ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |4 ███████████████████
███████████████████ 5| ~ ~ ~ ~ ~ ~ ~ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |5 ███████████████████
███████████████████ -|-----------------||-----------------|- ███████████████████
███████████████████ +| A B C D E F G H || A B C D E F G H |+ ███████████████████


████████████████████████████████████████████████████████████████████████████████
█                 █                                          █                 █
█   WELCOME TO    █ +| A B C D E F G H || A B C D E F G H |+ █        THIS IS  █
█   SUBMARINE     █ -|-----------------||-----------------|- █  AN EXAMPLE OF  █
█   DOMINATION    █ 1| ~ @ ~ ~ @ ~ ~ ~ || ~ ~ X ~ ~ ~ ~ ~ |1 █  THE SIMULATED  █
█   SIMULATION    █ 2| ~ ~ ~ ~ ~ ~ @ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |2 █          ARENA  █
█   COMMANDER     █ 3| ~ ~ ~ ~ ~ ~ ~ ~ || ~ ~ ~ ~ . ~ ~ ~ |3 █                 █
█                 █ 4| ~ ~ ~ X ~ ~ ~ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |4 █    ENEMY SUBS   █
█ [LEFT] IS YOUR  █ 5| ~ . ~ ~ ~ ~ @ ~ || ~ ~ ~ ~ ~ ~ ~ ~ |5 █ARE HIDDEN[RIGHT]█
█      ZONE       █ -|-----------------||-----------------|- █ . = MISSED SHOT █
█ @ = YOUR SHIPS  █ +| A B C D E F G H || A B C D E F G H |+ █  X = SUNK SUB   █
█                 █                                          █                 █
████████████████████████████████████████████████████████████████████████████████
         AT THE START OF THE GAME, YOU WILL BE ASKED TO POSITION 5 SUBS
              LIKE THIS:
                     pick a lettered column between A - H:
              THEN LIKE THIS:
                      pick a numbered row between 1 - 5:
████████████████████████████████████████████████████████████████████████████████
      YOU WILL THEN USE THIS SAME PROCESS TO PREDICT ENEMY SUB PLACEMENT
    THE HIGHLY ADVANCED AI WILL IN-TURN ATTEMPT TO PREDICT YOUR HIDDEN SUBS
          SIMULATION STEPS REPEAT UNTIL ALL 5 ENEMY SUBS ARE DOMINATED
                      OR ENEMY DOMINATES ALL 5 OF YOUR SUBS
           +| N: New Game || I: How to Play || X: close simulation |+
pick a lettered option listed above: 

                    ---POSITION SUB NUMBER  1, COMMANDER---
                       DESIGNATE RADAR COLUMN, COMMANDER
 pick a lettered column between A - H: 
 pick a numbered row between 1 - 5: 

```
<br>

### **Colour Scheme**
<br>

As the Terminal is black, the `HTML` template used was appended with a style rule to change thepage background to black, to immerse with the style of the game and improve visual effect

the python library `termcolor` was used to color text in the terminal to raise importance of certain messages and increase readability

### **Typography**

Typography generated and unedited by Terminal

### **Imagery**

As seen in the Notepad block above. Art was sketched out on the notepad manually. for more complex shapes, ASCII art was sourced from [ASCII.co.uk](https://ascii.co.uk).
Original artists are credited above as appropriate

when building the board, an active choice was made to characterise blank spaces on the board with `~`, as this effectively represent waves on a body of water.

`@` signs were employed as player subs, as it was the closest thing to imagine as a periscope sticking out of the water.

`.` was used for a miss, as it was to emphasise stillness in the water but be more identifiable than `-`

`X` was used to mark a hit on the board for both sides, as an `X` is synonymous with negative outcomes. Also, sinking a sub is a relatively negative thing (if you are on board).

<br>
<br>

---


# Features

## **Visual Features**

- webpage
    - houses the terminal to be used. coloured black to stylize itself with the terminal

- Upon page load (and inevitably, terminal load) users are presented with the Title art along with instructions. Design is minimalistic and driects users to pick one of 2 options immediately:
    - New Game
        - Entering "N" will start a new game
    - How to Play
        - Entering "I" will clear the board and display the game rules

- How To Play
    - when activated, clears the terminal then displays an example of the board, bookended with terminology to understand the game items
    - further explanation of how to enter coordinates and rules of the game are then displayed directly below

- New Game
    - Displays a blank board and gives prompts to begin entering in coordinates for users to position their own subs
    - every time a set of coordinates is entered, the terminal clears and an update of the board is printed.
    - because of the low amount of data parsed, the terminal clear and repopulation appears instantaneous. simulating a running game and not a terminal.

- winning conditions
    - If a player beats the computer, then the terminal is cleared and ASCII art of a submarine with a congratulatory message appears
    - From here, players have the option to start a new game, or return to the title screen

- losing conditions
    - If the programme guesses all the player's sub positions, the terminal is cleared and modified ASCII art appears of a nuclear explosion over water
    - a game over message is printed underneath, with the option for players to start a new game or return to the title screen

- during gameplay
    - With each turn, the terminal is cleared and the gameboard is updated to reflect the current state of play
    - if there are any errors in coordinates, the terminal also refreshes and displays the current state of the game to display up to date messages without the user having to scroll

<br>
<br>

## **Gameplay/Code Features**

## Gameplay Loop

<br>

![Gameplay loop flow chart](assets/images/readme/battleships-flowchart.png)

<br>

1. Title function Loads
    - `prints` title art and welcome message
    - `input` field appears to select option
    - player picks "new game"
    - player picks "how to play"
2. Player Picks "How to play"
    - `game_info` function called
    - clears terminal
    - `prints` explanation on how to play with examples
    - `input` option given, options given to return to title or start new game
3. Return to title
    - calls `title` function and repeats step 1
4. Player picks "new game"
    - calls `main` function
    - `main` function establishes important variables
    - `prints` new game board to terminal
    - sets a `boolean variable` that determines state of the game
    - calls function that assigns values for Comps subs in the background
    - calls position_subs function, parses in state of the game variable to determine messages to print
    - Position_subs function, calls pick_coords function to allow user to input coords. returns coords to dict
    - `boolean variable` value updated to change game messgaes when calling functions
    - upon function conclusion, dict is unpacked into 2 lists
5. Core Gameplay loop begins
    - housed within a `while loop`
    - calls `fire_torpedo` function, which in-turn uses `pick_coords` function to target a coordinate on the board
    - value from `pick_coords` returned to `fire_torpedo` and compared against Comp's sub coordinates
    - depending on hit or miss, the coordinate is updates on the board with "`X`" or "`.`"
    - back in the `while loop`, `main` function takes the updated value of the coordinate, and depending on the value, reduces the comp_shipcount by `1` or `0`
    - process is repeated using neighbouring functions for comp's turn
    - The `turn` variable is incrementally increased by `1`, keeping track of the amount of turns played
    - A message is printed detailing the current score of lives between the player and computer
    - `While loop` loops back to top `if` comp's shipcount is > `0` and player's shipcount is > `0`
6. `hit_checker` function called during all `fire_torpedo` functions
    - this checks to make sure that coordinates selected have not been picked before, or if a submarine has already sunk at this position
    - if either above outcomes is `true` a relevant statement is `printed` to the terminal. The player is then required to pick a new coordinate
7. step 5 repeats
    - `if` `3`, `7`, `11`, `15` or `18` turns pass, the comp will automatically guess a predesignated player's submarine
    - This is to prevent plays's from "cheesing" a victory by just entering every coordinate sequentially 1 after the other
8. Winning
    - `if` the `comp_shipcount` variable is reduced to `0`, the loop ends
    - the `player_win` function is called
    - the function generates relevant ASCII art, congratulating player on their victory
    - offers then to start a new game
    - if they accpet, `main` is called again
    - if they choose no, `title` is called instead
8. Losing
    - `if` the `player_shipcount` variable is reduced to `0`, the loop `break`s
    - the `player_lose` function is called
    - the function generates relevant ASCII art, letting them know they have lost
    - offers then to start a new game
    - if they accpet, `main` is called again
    - if they choose no, `title` is called instead

<br>
<br>

## **Features to Implement in the future**

Upon reading the brief, there was room for further features that were overlooked to prioritise project delivery on deadline. instead they will be features that will be implemented in the future

1. allowing player to select bot difficulty
    - this would increase/reduce the amount of turns it would take for the programme to guess all of the player's coordinates
2. Allowing player to determine board size
    - increase or shrink boardsize
    - contain different styles of boards to reflect this
3. Allow player to enter their own name
4. create a scroeboard by linking a google sheet to the programme
    - this would allow creation of a global scoreboard that could be displayed at the end of each game, displaying how many turns it took to win, at selected difficulty

***After hearing feedback from testers the following features were suggested for the future:***

1. "if a player has selected all coordinates or a row/column, error should be raised before player is allowed to put in second part of coordinate, reducing amount of unnecessary steps for player" 

<br>
<br>

---

# Bugs

**Resolved Bugs**

1. Global variable PLAYER_SUBS not logging all positions from player
    - The dict that was packing all input data was overiting and value on a key that had already been entered instead of making a new key: value pair.
    This meant that if players picked the same row for more than one Sub the loop would just overrite the value for that row
    - This was refactored out by making the return value of the position_subs() function to a tuple which unpacks to 3 variables (game_start, p_rows, p_columns), which now produces the desired end result

| Omercan Cirit |
| ------------- |
|_"Bug!... 5 subs, then at one point i think i lost 3 of them"_|
| ![Bug 1 image 1](assets/images/readme/omercan-bug-id.jpeg) |

2. Since debugging, this error has not been replicated. it was suspected that; upon defeat by the computer, the program would not exit the `while loop` that ran the core gameplay loop, resulting in an error throwing when it was trying to run the `while loop` on values which no longer had a value as the game had been restarted:

| Joe Collins |
|---------------|
|_"Just had a little play looks great but did encounter an error that kicked me out. I think the coordinate i hit to get this was C1. I have added  a screenshot of the IndexError this caused."_|

| screenshot 1 | Screenshot 2 | 
| -------- | -------- | 
|![bug image 1](assets/images/readme/j-collins-screenshot-20221205-1.png)|![bug image 2](assets/images/readme/j-collins-screenshot-20221205-2.png)|
Joe Collins:

| Cheryl Phillips: |
| ---------------- |
|_"G1 here... This was the state of play at the time:"_|

| Screenshot 1 | Screenshot 2 |
| ------------ | ------------ |
| ![bug image 1](assets/images/readme/c-phillips-screenshot-20221205-1.png)|![bug image 2](assets/images/readme/c-phillips-screenshot-20221205-2.png)|

After consultation with The project mentor (Seun Owonikoko), the above explanation was expected. at this stage, the bug has been removed by implementing a `break` of the `loop` upon `player_shipcount` decreasing to `0`

<br>
<br>

---

# Testing

### Testing is housed in the following appendix: [TESTING.md]()

<br>
<br>

---

# Technologies

## **Languages used**

Given the nature of this project, other languages were used to build the suitable platform to deploy the project.

## languages used by author:

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Markdown](https://en.wikipedia.org/wiki/Markdown)

## Languages used in template pack:

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

## Python Modules:

- [Random](https://docs.python.org/3/library/random.html) - To create random numbers
- [OS](https://www.tutorialsteacher.com/python/os-module#:~:text=The%20OS%20module%20in%20Python,with%20the%20underlying%20operating%20system.) - to create a function that clears the terminal
- [colorterm](https://pypi.org/project/colorterm/) - to color terminal print statements
- [Pylint](https://www.pylint.org/) - to ensure that code follows PEP8 guidance.
- [pdb](https://realpython.com/lessons/getting-started-pdb/#:~:text=It's%20import%20pdb%3B%20pdb.,where%20we%20call%20set_trace()%20.) - `import pdb; pdb.set_trace()` used to manually debug code mid-run of program at specific intervals

## Frameworks | Libraries | Programs:

- [GitHub](https://github.com/) - Used to store, deploy and publish site.
- [GitPod](https://gitpod.io/) - Used to write and preview code, commit and push to GitHub.
- [Google Chrome](https://www.google.co.uk/chrome) - Used to run GitPod in browser, test deployment, and google search etc.
- [Mozilla Firefox](https://www.mozilla.org/en-GB/firefox/new/) - Used to test UX
- [Microsoft Edge](https://www.microsoft.com/en-us/edge?form=MA13FJ) - Used to test UX
- [Safari on Mac and iOS](https://www.apple.com/uk/safari/) - Used to test UX
- [Opera](https://www.opera.com/) - Used to test UX
- [Google Chrome on Android](https://support.google.com/chrome/answer/95346?hl=en&co=GENIE.Platform%3DAndroid) - Used to test UX
- [LucidChart](https://www.lucidchart.com/) - Used to create Structure plane flowchart
- [Python Tutor](https://pythontutor.com/) - Used to simulate isolated blocks of code during build
- [Diffchecker](https://www.diffchecker.com/diff/) - used to check for differences in code against reference structures
- [Cloud Converter](https://cloudconvert.com/mp4-to-gif) - Used to create all GIFs in README

<br>

- [MS Notepad](https://en.wikipedia.org/wiki/Windows_Notepad) - Used to initially sketch own ASCII art and ideas
- [MS Powerpoint](https://en.wikipedia.org/wiki/Microsoft_PowerPoint) - Used to create features flowchart
- [MS Clipchamp](https://www.microsoft.com/en-us/microsoft-365/clipchamp) - Used to create all GIFs in README
- [Zoom Screen recording](https://zoom.us/) - Used to create all GIFs in README

<br>
<br>

---

# Deployment

Upon creation of the project in GitHub/GitPod, the project was launched externally on Heroku

below are the following steps one should take to deploy this project on Heroku:

![How to deploy to Heroku](assets/images/readme/how-to-deploy-to-heroku.gif)

1. Log in/Sign up for an account with Heroku
3. Upon logging in, at the dashboard select "create new app".
    - if you have previously created projects on Heroku, this option can be accessed from the "new" buttonat the top right corner of the screen
4. Give your project a unique name. You cannot name your project with a name that's already in use
5. select the region you wish to deploy your project to
6. click "create app"
7. select the deployment method, in this scenario, we are using GitHub
8. upon page refresh, enter the name of the repo you want to link up to Heroku
    - If you have not done so, you will need to ollow the steps to link your GitHub account to your Heroku account
    - You must seach for the correct repo name of your project in the field given. misplellings will result in Heroku being unable to find your repo
9. Set up your prject to automatcally deploy on every push update
10. deploy your project
    - Allow time for Heroku to deploy the project(the video here is sped up)
11. click to iew your deployment!

additional steps specific to this project **Before Deploying**:

1. Once you have created the project, you will also have to install Buildpacks
2. this can be done in the settings tab of the project, along the top of the page.
the following 2 buildpacks need to be added for this project to function. they must be added in the following order:
    - Python
    - NodeJS
3. in it's current state, this project does not have any CREDS required to run the project. However, in the futre, should this be needed. the contents of the creds.json file in the repo would need to be copied to the configvars of the project in Heroku, with the creds.json file also being added to .gitignore in the repo.

# Credits

resources for creating code:

 - [digitalocean.com](https://www.digitalocean.com/community/tutorials/python-remove-character-from-string)
 - [thispointer.com](https://thispointer.com/python-how-to-get-last-n-characters-in-a-string/)
 - [askpython.com](https://www.askpython.com/python/string/remove-character-from-string-python)
 - [bobbyhadz.com](https://bobbyhadz.com/blog/python-add-items-to-dictionary-in-loop#:~:text=If%20the%20key%20is%20already%20in%20the%20dictionary%2C%20we%20use,update()%20method)
 - [simplilearn.com](https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python#:~:text=To%20convert%20a%20list%20to%20a%20string%2C%20use%20Python%20List,and%20return%20it%20as%20output)
 - [w3schools](https://www.w3schools.com/)
    - [resource 1](https://www.w3schools.com/python/python_conditions.asp)
    - [resource 2](https://www.w3schools.com/python/ref_random_randint.asp)
 - [Stack Overflow](https://stackoverflow.com)
    - [resource 1](https://stackoverflow.com/questions/4528982/convert-alphabet-letters-to-number-in-python)
    - [resource 2](https://stackoverflow.com/questions/58086435/how-to-select-a-specific-returned-variable-from-a-number-of-returned-variable-in)
    - [resource 3](https://stackoverflow.com/questions/53105185/creating-a-list-of-random-numbers-without-duplicates-in-python)
    - [resource 4](https://stackoverflow.com/questions/423379/using-global-variables-in-a-function#:~:text=If%20you%20want%20to%20refer,declare%20which%20variables%20are%20global)
    - [resource 5](https://stackoverflow.com/questions/42165091/how-to-target-a-specific-key-in-a-dictionary)
 - [scaler.com](https://www.scaler.com/topics/how-to-clear-screen-in-python/) 
 - [folkstalk.com](https://www.folkstalk.com/2022/10/python-loop-certain-number-of-times-with-code-examples.html)
 - [freecodecamp.org](https://www.freecodecamp.org/news/python-break-and-python-continue-how-to-skip-to-the-next-function/#:~:text=You%20can%20use%20the%20continue,move%20onto%20the%20next%20iteration.)
 - [codeacademy.com](https://discuss.codecademy.com/t/how-can-i-determine-if-a-dictionary-is-empty/352838)
 - [geeksforgeeks.org](https://www.geeksforgeeks.org)
    - [resource 2](https://www.geeksforgeeks.org/iterate-over-a-dictionary-in-python/)
    - [resource 1](https://www.geeksforgeeks.org/python-extract-key-value-of-dictionary-in-variables/)
 - [ascii.co.uk](https://ascii.co.uk/art/)
 - [zetcode.com](https://zetcode.com/python/add-string/#:~:text=Python%20add%20strings%20with%20%2B%20operator,that%20the%20operator%20is%20overloaded.&text=Two%20strings%20are%20added%20using%20the%20%2B%20operator.)
 - [includehelp.com](https://www.includehelp.com/python/ignoring-escape-sequences-in-the-string.aspx#:~:text=To%20ignoring%20escape%20sequences%20in,%22r%22%20before%20the%20string.)
