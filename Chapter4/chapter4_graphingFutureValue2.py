# futval_graph2.py

from graphics import *


def main():
    # Introduction
    print("This program plots the growth of a 10-year investment.")

    # Get principal and interest rate
    wininput = GraphWin("Enter your numbers", 500, 500)
    wininput.setCoords(0, 0, 100, 100)
    wininput.setBackground("grey")
    Text(Point(30, 70), "Enter the principal: ").draw(wininput)
    Text(Point(30, 40), "Enter the interest rate: ").draw(wininput)
    get_principal = Entry(Point(60, 70), 5)
    get_principal.setText("0.0")
    get_principal.draw(wininput)
    get_apr = Entry(Point(60, 40), 5)
    get_apr.setText("0.0")
    get_apr.draw(wininput)

    wininput.getMouse()

    principal = float(get_principal.getText())
    apr = float(get_apr.getText())

    wininput.close()

    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 640, 480)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), " 0.0K").draw(win)
    Text(Point(-1, 2500), " 2.5K").draw(win)
    Text(Point(-1, 5000), " 5.0K").draw(win)
    Text(Point(-1, 7500), " 7.5K").draw(win)
    Text(Point(-1, 10000), " 10.0K").draw(win)

    # draw bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw a bar for each subsequent year
    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

#    input("Press <Enter> to quit")
    win.getMouse()


main()
