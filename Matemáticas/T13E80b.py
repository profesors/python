import random
import curses

stdscr = curses.initscr()
stdscr.keypad(True)
curses.noecho()
curses.curs_set(0)

intentos = 100000.0
aciertos = 0

for contador in range(int(intentos)):
	bolsa = ["f","f","f","f","f","f","f","f","m","m","m","m","l","l","l","l","l","l"]

	x = random.choice(bolsa)
	bolsa.remove(x)

	y = random.choice(bolsa)
	bolsa.remove(y)

	stdscr.addstr(1, 5, "Intentos         Probabilidad")
	stdscr.addstr(2, 5, "--------         ------------")
	stdscr.addstr(3, 6, str(contador+1))
	stdscr.addstr(3, 25, str(aciertos/intentos))
	stdscr.addstr(4, 0, "")
	stdscr.refresh()

	if (y != "f"):
		aciertos = aciertos + 1



stdscr.getkey()
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
