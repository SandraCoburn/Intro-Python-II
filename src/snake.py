import time, curses


#wrapper
def main(screen):
    screen = curses.initscr()
    curses.curs_set(0) #hide cursor
    screen.nodelay(True) #don't block I/O calls

    directions = {
        curses.KEY_UP: (-1, 0),
        curses.KEY_DOWN: (1, 0),
        curses.KEY_LEFT: (0, -1),
        curses.KEY_RIGHT: (0, 1)
    }
    direction = directions[curses.KEY_RIGHT]

    snake = [(0,i) for i in reversed(range(20))]

    while True:
        screen.erase()
        #draw the snake
        screen.addstr(*snake[0], '@')
        for segment in snake[1:]:
            screen.addstr(*segment, '*')

        #move the snake:
        snake.pop()
        snake.insert(0, tuple(map(sum, zip(snake[0], direction))))

        #change direction on arrow keystrokes:
        direction = directions.get(screen.getch(), direction)

        screen.refresh()
        time.sleep(0.1)
if __name__ == '__main__':
        #screen = curses.initscr()
    curses.wrapper(main) 
    #main(1)
#main(1)