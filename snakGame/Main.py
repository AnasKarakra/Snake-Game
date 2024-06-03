import random
import curses

screen = curses.initscr()  # initialzation the window
curses.curs_set(
    0)  # delete the curser form window Set the cursor state. visibility can be set to 0, 1, or 2, for invisible, normal, or very visible. If the terminal supports the visibility requested, return the previous cursor state; otherwise raise an exception. On many terminals, the “visible” mode is an underline cursor and the “very visible” mode is a block cursor.
hight, width = screen.getmaxyx()
window = curses.newwin(hight, width, 0, 0)  # the size of window
# window.getch()
window.keypad(True)  # allow the window to take an input form keyboard
window.timeout(100)
# -------------------------------------------------------
snak_x = width // 4
snak_y = hight // 2
snake = [[snak_y, snak_x],
         [snak_y, snak_x - 1],
         [snak_y, snak_x - 2]]

food = [hight // 2, width // 2]
window.addch(food[0], food[1], curses.ACS_PI)
key = curses.KEY_RIGHT
# =========================================================
while True:
    nextKey = window.getch()
    key = key if nextKey == -1 else nextKey
    if snake[0][0] in [0, hight] or snake[0][1] in [0, width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    newHead = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWN:
        newHead[0] += 1
    elif key == curses.KEY_UP:
        newHead[0] -= 1
    elif key == curses.KEY_LEFT:
        newHead[1] -= 1
    else:
        newHead[1] += 1

    snake.insert(0, newHead)

    if snake[0] == food:
        food = None
        while food is None:
            # food_y = random.randint(1, hight - 1)
            # food_x = random.randint(1, width - 1)
            # newFood = [food_y, food_x]
            newFood = [random.randint(1, hight - 1), random.randint(1, width - 1)]
            if newFood not in snake:

                food = newFood
            else:
                food = None
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], " ")

    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
