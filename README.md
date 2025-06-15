# Space Invaders (Python & Pygame)

A Python recreation of the classic *Space Invaders* arcade game built using the Pygame library.

## Overview

This project is a functional clone of the Space Invaders game, featuring:  
- Player-controlled spaceship moving horizontally with **A** and **D** keys  
- Bullet firing using the **spacebar**  
- Multiple enemy invaders moving horizontally and descending gradually  
- Collision detection between bullets and enemies  
- Score tracking and a game over screen when enemies reach the player’s position  
- Background music and sound effects for shooting and game over events  

## Features & Learning Outcomes

- Game window created with **Pygame** (resolution: 1500x900)  
- Real-time player input handling and movement  
- Enemy invader fleet with randomized starting positions and dynamic movement  
- Collision detection implemented using distance calculation between sprites  
- Score display with Pygame’s font rendering  
- Sound management with background music and event-triggered effects  
- Basic game state management (running, firing bullet, game over)  

## How to Run

1. Ensure Python 3.x and Pygame are installed (`pip install pygame`).  
2. Place image assets (`player1.png`, `enemy1.png`, `bullet.png`) and audio files (`bg music.mp3`, `shoot.wav`, `game over.wav`) in the same folder as the script or adjust paths accordingly.  
3. Run the script:  
   ```bash
   python space_invaders.py
4. Use keys A and D to move left and right, and spacebar to shoot.
5. Try to shoot all enemies before they descend too far.

## file Structure

space-invaders-python/
│
├── space_invaders.py       # Main game script
├── player1.png             # Player spaceship image
├── enemy1.png              # Enemy invader image
├── bullet.png              # Bullet image
├── bg music.mp3            # Background music
├── shoot.wav               # Shooting sound effect
├── game over.wav           # Game over sound effect
├── README.md               # This file

## About Me
Adrika Bordoloi! :)
IGCSE Student | Aspiring Quantitative Finance Analyst and Investment Banker
Connect with me on [LinkedIn](https://www.linkedin.com/in/adrika-bordoloi-083443255/)

## Disclaimer
This project is created purely for educational purposes and does not infringe on the original Space Invaders intellectual property. All assets used are placeholders or self-created.
