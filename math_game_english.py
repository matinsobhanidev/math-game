import random
from tkinter import *
import time

result = 0
ts = 0
alamat = ""
ts2 = 0
ch = 1
crang = "#eb0000"
equal = 0
ll1 = 0
ll2 = 0
ll3 = 0
ll4 = 0
random2 = 0
emt = 0


def creatq():
    # Create a question
    global result
    global alamat

    min1 = min.get()
    min1 = min1.strip()

    max2 = max.get()
    max2 = max2.strip()

    ty = grrr.get()

    if min1 == "":
        showq.config(text="Minimum is not specified")

    elif max2 == "":
        showq.config(text="Maximum is not specified")

    elif min1.isdigit() == False:
        showq.config(text="Minimum must be a number")

    elif max2.isdigit() == False:
        showq.config(text="Maximum must be a number")

    elif int(min1) >= int(max2):
        showq.config(text="Minimum must be smaller than maximum")

    else:
        rand1 = random.randint(int(min1), int(max2))
        rand2 = random.randint(int(min1), int(max2))

        if ty == 1:
            result = rand1 + rand2
            alamat = "+"

        elif ty == 2:
            result = rand1 - rand2
            alamat = "-"

        elif ty == 3:
            result = rand1 * rand2
            alamat = "*"

        elif ty == 4:
            result = rand1 / rand2
            alamat = "/"

        showq.config(text="{} {} {} = ?".format(rand1, alamat, rand2))


def cans():
    # Check the answer
    global result
    global ts
    global ts2

    ans1 = ans.get()
    ans1 = ans1.strip()

    if ans1 == "":
        showans.config(text="You did not enter an answer")

    elif ans1.isdigit() == False:
        showans.config(text="Please enter a number")

    elif float(ans1) == result:
        showans.config(text="Your answer is correct")

        ts += 1

        tedad.config(
            text="Correct answers: {}".format(ts)
        )

    else:
        showans.config(text="Incorrect")

        ts2 += 1

        tedad2.config(
            text="Incorrect answers: {}".format(ts2)
        )

    if ans1 == "":
        showans.config(text="You did not enter an answer")

    elif ans1.isdigit() == False:
        showans.config(text="Please enter a number")

    elif float(ans1) == result:
        creatq()

    else:
        pass


def rahnama():
    # Help
    rahnama = Toplevel()
    rahnama.geometry("500x300")
    rahnama.configure(bg="#121212")

    ll = Label(
        rahnama,
        text=
        "First, specify the range.\n"
        "Then enter the minimum value, for example: 10\n"
        "After that, enter the maximum value, for example: 50\n"
        "Choose one of the operators and click Create Question.\n"
        "Then enter the answer to the generated question in the Answer field.",
        fg="#eb0000",
        bg="#121212",
        font=25
    )

    ll.pack()


def tem():
    # Change theme
    global ch
    global crang

    rang = [
        "#eb0000",
        "#eb0000",
        "#2a81fe",
        "#07ff20",
        "white"
    ]

    if ch == 4:
        ch = 0

    ch += 1
    crang = rang[ch]

    min.config(bg=crang)
    max.config(bg=crang)
    showq.config(fg=crang)
    showans.config(fg=crang)
    tedad.config(fg=crang)
    tedad2.config(fg=crang)
    rr.config(fg=crang)
    rr2.config(fg=crang)
    rr3.config(fg=crang)
    rr4.config(fg=crang)
    l1.config(fg=crang)
    b1.config(bg=crang)
    b2.config(bg=crang)
    ans.config(bg=crang)
    b3.config(bg=crang)
    l2.config(fg=crang)
    l3.config(fg=crang)
    b4.config(bg=crang)
    l4.config(fg=crang)
    b6.config(bg=crang)


def timi():
    # Timed game
    def countdown():

        for i in range(10, 0, -1):
            t1.config(text=i)
            time.sleep(1)
            print(i)

    timi = Toplevel()
    timi.geometry("400x600")
    timi.configure(bg="#121212")

    second = 10

    t1 = Label(timi, text=second)
    t1.pack()

    Button(
        timi,
        text="Start",
        command=countdown
    ).pack()


def quez():
    # Quiz game
    global equal
    global ll1
    global ll2
    global ll3
    global ll4
    global random2
    global emt

    def kar1():
        # Check answer 1
        global ll1
        global random2
        global emt

        if ll1 == random2:
            emt += 1

            ted.config(
                text="Correct answers: {}".format(emt)
            )

            q1()

        else:
            q1()

    def kar2():
        # Check answer 2
        global ll2
        global random2
        global emt

        if ll2 == random2:
            emt += 1

            ted.config(
                text="Correct answers: {}".format(emt)
            )

            q1()

        else:
            q1()

    def kar3():
        # Check answer 3
        global ll3
        global random2
        global emt

        if ll3 == random2:
            emt += 1

            ted.config(
                text="Correct answers: {}".format(emt)
            )

            q1()

        else:
            q1()

    def kar4():
        # Check answer 4
        global ll4
        global random2
        global emt

        if ll4 == random2:
            emt += 1

            ted.config(
                text="Correct answers: {}".format(emt)
            )

            q1()

        else:
            q1()

    def q1():
        # Generate a quiz question
        global equal
        global ll1
        global ll2
        global ll3
        global ll4
        global random2
        global emt

        ted.config(
            text="Correct answers: {}".format(emt)
        )

        def randsaz(random2, random3, random4, random5):
            global ll1
            global ll2
            global ll3
            global ll4

            # Randomize the answer buttons
            listrand = [
                random2,
                random3,
                random4,
                random5
            ]

            ll1 = random.sample(listrand, 1)
            ll2 = random.sample(listrand, 1)
            ll3 = random.sample(listrand, 1)
            ll4 = random.sample(listrand, 1)

            ll1 = ll1[0]
            ll2 = ll2[0]
            ll3 = ll3[0]
            ll4 = ll4[0]

            if (
                ll1 == ll2
                or ll1 == ll3
                or ll1 == ll4
                or ll2 == ll3
                or ll2 == ll4
                or ll3 == ll4
                or ll1 == ll2 == ll3
                or ll1 == ll2 == ll4
                or ll1 == ll3 == ll4
                or ll2 == ll3 == ll4
                or ll1 == ll2 == ll3 == ll4
            ):
                randsaz(
                    random2,
                    random3,
                    random4,
                    random5
                )

            else:
                bu1.config(text=ll1)
                bu2.config(text=ll2)
                bu3.config(text=ll3)
                bu4.config(text=ll4)

        random1 = random.randint(0, 100)
        random2 = random.randint(0, 100)
        random3 = random.randint(0, 100)
        random4 = random.randint(0, 100)
        random5 = random.randint(0, 100)

        listrand = [
            random2,
            random3,
            random4,
            random5
        ]

        ll1 = random.sample(listrand, 1)
        ll2 = random.sample(listrand, 1)
        ll3 = random.sample(listrand, 1)
        ll4 = random.sample(listrand, 1)

        ll1 = ll1[0]
        ll2 = ll2[0]
        ll3 = ll3[0]
        ll4 = ll4[0]

        alamrrand = ["+", "-"]

        arand = random.sample(
            alamrrand,
            1
        )

        arand = "".join(arand)

        if arand == "+":
            equal = random1 + random2

        elif arand == "-":
            equal = random1 - random2

        lab.config(
            text="{} {} ? = {}".format(
                random1,
                arand,
                equal
            )
        )

        if (
            ll1 == ll2
            or ll1 == ll3
            or ll1 == ll4
            or ll2 == ll3
            or ll2 == ll4
            or ll3 == ll4
            or ll1 == ll2 == ll3
            or ll1 == ll2 == ll4
            or ll1 == ll3 == ll4
            or ll2 == ll3 == ll4
            or ll1 == ll2 == ll3 == ll4
        ):
            randsaz(
                random2,
                random3,
                random4,
                random5
            )

        else:
            bu1.config(text=ll1)
            bu2.config(text=ll2)
            bu3.config(text=ll3)
            bu4.config(text=ll4)

    quez = Toplevel()
    quez.geometry("400x600")
    quez.configure(bg="#121212")

    Button(
        quez,
        text="Start",
        bg="#ff0000",
        command=q1,
        font=50
    ).pack(pady=5)

    lab = Label(
        quez,
        text="",
        fg="#eb0000",
        bg="#121212",
        font=200
    )

    lab.pack(pady=20)

    bu1 = Button(
        quez,
        text="",
        bg="#ff0000",
        command=kar1,
        font=50
    )

    bu1.pack()

    bu2 = Button(
        quez,
        text="",
        bg="#ff0000",
        command=kar2,
        font=50
    )

    bu2.pack()

    bu3 = Button(
        quez,
        text="",
        bg="#ff0000",
        command=kar3,
        font=50
    )

    bu3.pack()

    bu4 = Button(
        quez,
        text="",
        bg="#ff0000",
        command=kar4,
        font=50
    )

    bu4.pack()

    ted = Label(
        quez,
        text="Correct answers: {}".format(emt),
        fg="#eb0000",
        bg="#121212",
        font=25
    )

    ted.pack(pady=5)


window = Tk()

window.title("Math Game")
window.geometry("400x600")
window.configure(bg="#121212")

frame = Frame(
    window,
    bg="#121212"
)

frame.pack(
    side="right",
    anchor="n"
)

l1 = Label(
    window,
    text="Minimum:",
    fg=crang,
    bg="#121212",
    font=25
)

l1.pack(pady=5)

b1 = Button(
    frame,
    text="Help",
    bg="#ff0000",
    command=rahnama
)

b1.pack(pady=10)

b2 = Button(
    frame,
    text="Change Theme",
    bg="#ff0000",
    command=tem
)

b2.pack()

min = Entry(
    window,
    bg="#eb0000"
)

min.pack(pady=5)

l2 = Label(
    window,
    text="Maximum:",
    fg="#eb0000",
    bg="#121212",
    font=25
)

l2.pack(pady=5)

max = Entry(
    window,
    bg="#eb0000"
)

max.pack(pady=5)

s = ["+", "-", "*", "/"]

g = 0
grrr = IntVar()
grrr.set(1)
d = 1

rr = Radiobutton(
    window,
    text=s[g],
    variable=grrr,
    value=d,
    fg=crang,
    bg="#121212",
    font=20
)

rr.pack(pady=5)

g += 1
d += 1

rr2 = Radiobutton(
    window,
    text=s[g],
    variable=grrr,
    value=d,
    fg=crang,
    bg="#121212",
    font=20
)

rr2.pack(pady=5)

g += 1
d += 1

rr3 = Radiobutton(
    window,
    text=s[g],
    variable=grrr,
    value=d,
    fg=crang,
    bg="#121212",
    font=20
)

rr3.pack(pady=5)

g += 1
d += 1

rr4 = Radiobutton(
    window,
    text=s[g],
    variable=grrr,
    value=d,
    fg=crang,
    bg="#121212",
    font=20
)

rr4.pack(pady=5)

g += 1
d += 1

b3 = Button(
    window,
    text="Create Question",
    command=creatq,
    bg="#ff0000"
)

b3.pack(pady=5)

showq = Label(
    window,
    text="Question",
    fg="#eb0000",
    bg="#121212",
    font=25
)

showq.pack(pady=5)

l3 = Label(
    window,
    text="Answer:",
    fg="#eb0000",
    bg="#121212",
    font=25
)

l3.pack(pady=5)

ans = Entry(
    window,
    bg="#eb0000"
)

ans.pack(pady=5)

b4 = Button(
    window,
    text="Submit",
    command=cans,
    bg="#ff0000"
)

b4.pack(pady=5)

showans = Label(
    window,
    fg="#eb0000",
    bg="#121212",
    font=25
)

showans.pack(pady=5)

l4 = Label(
    window,
    text="-*-" * 20,
    fg="#eb0000",
    bg="#121212",
    font=20
)

l4.pack()

tedad = Label(
    window,
    text="Correct answers: 0",
    fg="#eb0000",
    bg="#121212",
    font=25
)

tedad.pack(pady=5)

tedad2 = Label(
    window,
    text="Incorrect answers: 0",
    fg="#eb0000",
    bg="#121212",
    font=25
)

tedad2.pack(pady=5)

# b5 = Button(
#     frame,
#     text="Timed Game",
#     bg="#ff0000",
#     command=timi
# )
# b5.pack(pady=5)

b6 = Button(
    frame,
    text="Quiz Game",
    command=quez,
    bg="#ff0000"
)

b6.pack(pady=5)
creator = Label(
    window,
    text="Created by Matin Sobhani",
    fg="#777777",
    bg="#121212",

)

creator.pack(side="bottom", pady=5)

window.mainloop()