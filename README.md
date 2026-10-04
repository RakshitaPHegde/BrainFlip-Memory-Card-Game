# 🧠 BrainFlip - Memory Card Game

BrainFlip is an interactive memory card game developed using **Python and Tkinter**. The game challenges players to find matching pairs while completing progressively challenging levels within a countdown timer.

## 🎮 Features

- 🃏 Up to 24 cards with 12 matching pairs
- 🎯 100 progressive levels
- ⏱️ Countdown timer
- 🏆 Score system
- ⭐ 1-star, 2-star and 3-star rewards
- 🔀 Randomized card arrangement
- 🎨 Colorful graphical card designs
- 🎉 Congratulations popup after completing a level
- ➡️ Next Level option
- ⏰ Time's Up and Try Again option
- 🔄 Restart Level option
- 🏅 Best score tracking
- 💻 Desktop graphical user interface

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter**
- **Random module**

## 🧩 How the Game Works

1. The game displays a set of cards containing matching pairs.
2. The player selects two cards.
3. If the cards match, they remain visible.
4. If the cards do not match, they are flipped back.
5. The player continues until all pairs are matched.
6. The player must complete the level before the timer reaches zero.
7. After completing a level, the player receives a score and star rating.
8. The player can click **Next Level** to continue.
9. The difficulty increases as the player progresses through the 100 levels.

## 📈 Level Progression

The game contains **100 levels** with increasing difficulty.

| Levels | Cards | Pairs | Time |
|--------|------:|------:|-----:|
| 1–10 | 8 | 4 | 60 seconds |
| 11–25 | 12 | 6 | 65 seconds |
| 26–50 | 16 | 8 | 70 seconds |
| 51–75 | 20 | 10 | 75 seconds |
| 76–100 | 24 | 12 | 80 seconds |

The number of cards increases as the player progresses, making the memory challenge more difficult.

## ⭐ Scoring System

Players receive points for finding matching pairs and receive a time bonus when completing a level.

The game awards stars based on the number of moves:

- ⭐⭐⭐ 3 Stars — Excellent performance
- ⭐⭐ 2 Stars — Great performance
- ⭐ 1 Star — Good effort

## 🎉 Level Completion

After completing a level, a congratulations window displays:

- Level completed
- Star rating
- Score
- Number of moves
- Remaining time
- Number of pairs
- Next Level button

After completing **Level 100**, the player receives a final BrainFlip Master message and can choose to play again.

## ⏰ Time-Up System

If the timer reaches zero before all pairs are matched:

- The game stops accepting card selections.
- A **Time's Up!** message is displayed.
- The player can choose **Try Again** to restart the current level.

## ▶️ How to Run

### Requirements

- Python 3.x
- Tkinter

### Run the Game

Open a terminal in the project folder and run:

```bash
python main.py
## 📸 Screenshots

### 🎮 Game Board
![BrainFlip Game Board](SCREENSHOT%203.jpeg)

### 🏆 Level Completed
![Level Completed](SCREENSHOT%201.jpeg)

### ⏰ Time Up / Try Again
![Time Up](SCREENSHOT%202.jpeg)
