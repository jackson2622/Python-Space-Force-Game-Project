# Simple Pygame Shooter Game

## Overview

This project is a simple 2D shooter game created using Python and the `pygame` library.The player controls a green rectangle at the bottom of the screen and must shoot down falling red enemies while avoiding collisions. Over time, the game increases in difficulty as enemies spawn more frequently and move faster.

---

## Features

- **Player Movement**: Use the arrow keys to move the player left and right across the screen.
- **Shooting**: Press the spacebar to shoot white bullets upward to destroy red enemies.
- **Enemies**: Red enemies fall from the top of the screen and must be avoided or destroyed.
- **Scoring System**: Gain points by shooting enemies.
- **Increasing Difficulty**: The game dynamically increases difficulty over time by:
  1. Decreasing the enemy spawn rate.
  2. Increasing the enemy speed.
- **Game Over**: The game ends when an enemy collides with the player.

---

## Prerequisites

Ensure you have the following installed before running the game:

- Python 3.x
- `pygame` library

Install `pygame` using the following command:


---

## How to Play

**Run the Game**:
   - Use the command below to execute the Python script:
2. **Controls**:
   - **Move Left**: Press the Left Arrow key.
   - **Move Right**: Press the Right Arrow key.
   - **Shoot**: Press the Spacebar to fire bullets.
   - **Exit Game**: Press the Escape key to quit.

3. **Objective**:
   - Shoot as many enemies as possible to earn points.
   - Avoid getting hit by falling enemies.

---

## Code Details

The main functionalities of the game are described below:

1. **Player**:
   - A green rectangle controlled by the player to dodge and shoot enemies.
2. **Bullets**:
   - White bullets originate from the player's position when the spacebar is pressed.
   - Bullets disappear when they move off-screen or hit an enemy.
3. **Enemies**:
   - Red enemies spawn at random positions at the top of the screen and move down.
   - Enemies increase in number and speed as time progresses.

4. **Difficulty Adjustment**:
   - **Spawn Rate**: Starts high but decreases over time.
   - **Speed**: Gradually increases to make the game more challenging.

5. **Score Display**:
   - Displayed at the top-left corner of the game screen.

---

## Future Improvements

- **Enhancements**:
  - Add more complex enemy movement patterns.
  - Include power-ups or bonus items.
  - Implement multiple levels of difficulty.
- **UI Improvements**:
  - Add a start menu and game-over screen.
  - Design better graphics and animations.
- **Sound Effects**:
  - Add sound effects for shooting and collisions.

---

## License

This project is open source and free to use under the MIT License.