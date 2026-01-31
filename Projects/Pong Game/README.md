# 🏓 Pong Game

A classic Pong clone built with Python’s `turtle` module.

## ✨ Features
- 🎮 Two-player paddle controls  
- ⚡ Ball bounce physics  
- 🧮 Score tracking  
- 🚀 Speed increase on paddle hits  

## ✅ Requirements
- 🐍 Python 3.x (includes `turtle`)

## ▶️ How to Run
From this folder:
```
python main.py
```

## 🎛️ Controls
- Right paddle: ⬆️ / ⬇️ arrows  
- Left paddle: **W** (up) / **S** (down)

## 📁 Files
- `main.py` — game loop and input bindings  
- `paddle.py` — paddle class  
- `ball.py` — ball movement and collision  
- `scoreboard.py` — score display  

## 📝 Notes
If the window doesn’t update smoothly, ensure the screen update call is enabled in the game loop (typically `screen.update()` when using `tracer(0)`).