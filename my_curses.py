import curses

def init_curses():
    scr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    scr.nodelay(True)
    scr.keypad(True)
    curses.curs_set(0)
    return scr

def terminate_curses(scr):
    scr.clear()
    scr.refresh()
    curses.curs_set(1)
    scr.keypad(False)
    scr.nodelay(False)
    curses.nocbreak()
    curses.echo()
    curses.endwin()
