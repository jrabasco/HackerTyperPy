#!/usr/bin/python3

import curses
import random
import argparse


def main():
    parser = argparse.ArgumentParser(description="Hacker typer to impress your friends !")
    parser.add_argument("-t", "--test", action="store_true", help="Testing mode, uses a shorter file and a shorter"
                                                                  "window.")
    parser.add_argument("-s", "--speed", help="Typing speed, i.e. number of characters per key"
                                              "stroke.", required=False, default=4, type=int)
    args = parser.parse_args()

    if args.test:
        input_file = "test"
    else:
        input_file = "in" + str(random.randint(1, 8))
    speed = args.speed
    default_screen = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    default_screen.clear()
    max_xy = default_screen.getmaxyx()
    y_dim = max_xy[0]
    if args.test and y_dim > 10:
        y_dim = 10
    x_dim = max_xy[1]
    pad = curses.newpad(y_dim, x_dim)
    pad.attrset(curses.color_pair(1))
    pad.refresh(0, 0, 0, 0, y_dim - 1, x_dim - 1)
    text_file = open(input_file)
    if not args.test:
        text_file.seek(random.randrange(30000))

    exit_program = False
    try:
        pos = 0
        while True:
            key = pad.getch()
            if key == 27:
                exit_program = True
                break

            out_of_chars = False

            for i in range(speed):
                char = text_file.read(1)
                if not char:
                    out_of_chars = True
                    break
                try:
                    pad.addstr(char)
                except curses.error:
                    pos += 1
                    pad.resize(y_dim + pos, x_dim)
                    pad.addstr(char)

            pad.refresh(pos, 0, 0, 0, y_dim - 1, x_dim - 1)
            if out_of_chars:
                break
        if not exit_program:
            pad.erase()
            default_screen.refresh()
            pad.resize(3, 8)
            pad.addstr(1, 0, " HACKED ")
            pad.border()
            pad.refresh(0, 0, 0, 0, 2, 7)
            while pad.getch() != 27:
                i = 0

    finally:
        text_file.close()
        curses.endwin()


if __name__ == "__main__":
    main()
