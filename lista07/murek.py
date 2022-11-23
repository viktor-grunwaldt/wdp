import turtle as t

colors = {
    "❤️": "red",
    "🧡": "orange",
    "💛": "yellow",
    "💚": "green",
    "💙": "blue",
    "💜": "purple",
    "🤎": "brown",
    "🖤": "black",
    "🤍": "white",
}


def kwadrat(bok):
    t.begin_fill()
    for i in range(4):
        t.fd(bok)
        t.rt(90)
    t.end_fill()


def murek(s, bok):
    for a in s:
        match a:
            case "f":
                kwadrat(bok)
                t.fd(bok)
            case "b":
                kwadrat(bok)
                t.fd(bok)
            case "l":
                t.bk(bok)
                t.lt(90)
            case "r":
                t.rt(90)
                t.fd(bok)
            case _:
                if a in colors:
                    t.color("black", colors[a])


t.color("black", "yellow")

t.ht()

t.tracer(0, 0)  # szybkie rysowanie
murek("fffffffffrffffff🧡fffflfffffffffrfffffl", 10)
murek(4 * "fffffr", 14)
t.update()  # uaktualnienie rysunku

t.mainloop()
