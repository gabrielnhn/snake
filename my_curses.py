import curses

def init_curses():
    scr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    scr.keypad(True)
    return scr

def terminate_curses(scr):
    scr.clear()
    scr.refresh()
    curses.curs_set(1)
    curses.echo()
    curses.nocbreak()
    scr.keypad(False)
    curses.endwin()
