import curses

def init_curses():
    scr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    scr.nodelay(True)
    scr.keypad(True)
    scr.idcok(False)
    scr.idlok(False)
    curses.curs_set(0)
    return scr

def terminate_curses(scr):
    scr.clear()
    scr.refresh()
    curses.echo()
    curses.nocbreak()
    scr.keypad(False)
    curses.curs_set(1)
    curses.endwin()
