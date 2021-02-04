from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image

#  main window
root = Tk()
root.title("Tic Tac Toe")
root.wm_attributes('-fullscreen', 'true')
background_image = PhotoImage(file="love_tictactoe.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# starting variables
play1 = StringVar()
play2 = StringVar()

score1 = 0
score2 = 0

button = StringVar()
buttonclick = True
winner = " "
currentPlayer = StringVar()


def set_name():
    global player1, player2, p1
    score2 = 0
    score1 = 0

    # entry for player 1 and player 2 with default text
    player1 = Entry(root, width=30, textvariable=play1, font=12, bd=4)
    player1.delete(0, END)
    player1.insert(0, 'Enter your name')
    player1.place(relx=0.13, rely=0.1)
    player1_label = Label(root, text='Player 1', padx=5, relief="groove", font="Times 12 bold", bd=4, bg="#cce6ff")
    player1_label.place(relx=0.07, rely=0.1)

    player2 = Entry(root, width=30, textvariable=play2, font=12, bd=4)
    player2.delete(0, END)
    player2.insert(0, 'Enter your name')
    player2.place(relx=0.73, rely=0.1)
    player2_label = Label(root, text='Player 2', padx=5, relief="groove", font="Times 12 bold", bd=4, bg="#cce6ff")
    player2_label.place(relx=0.67, rely=0.1)

    # Enter button
    p1 = Button(root, text='Enter', command=run_enter_button, font="Times 14 bold", bg="yellow", relief="ridge", bd=4)
    p1.place(relx=0.47, rely=0.09, relwidth=0.1)

    # score labels
    score1lbl = Label(root, text="SCORE", font=14, bd=4, bg="white", relief="groove")
    score1lbl.place(relx=0.07, rely=0.15)
    score1_label = Label(root, text=score1, bd=4, bg="white", font=14, relief="sunken")
    score1_label.place(relx=0.13, rely=0.15, relwidth=0.05)

    score2lbl = Label(root, text="SCORE", font=14, bd=4, bg="white", relief="groove")
    score2lbl.place(relx=0.67, rely=0.15)
    score2_label = Label(root, text=score2, bd=4, bg="white", font=14, relief="sunken")
    score2_label.place(relx=0.73, rely=0.15, relwidth=0.05)

    start_button.destroy()


def run_enter_button():
    get_names()
    set_first_player()
    show_buttons()


# setting who is going to play first
def set_first_player():
    global turn
    turn = Tk()
    turn.title("tic tac toe")
    turn.configure(background="#00ffff")
    x = (turn.winfo_screenwidth() - 150) / 3
    y = (turn.winfo_screenheight() - 150) / 4
    turn.geometry("+%d+%d" % (x + 200, y + 100))
    first_player_label = Label(turn, text="Who is first?", bd=4, fg="#ffff1a", font="Times 14 bold", bg="grey",
                               relief="groove")
    first_player_label.place(relx=0.1, rely=0.1, relwidth=0.8)
    first_turn_player1 = Button(turn, text=play1.get(), command=lambda: first_player(value=play1.get()),
                                bd=4, fg="#ff9900", font="Times 14 bold", bg="black", relief="groove")
    first_turn_player1.place(relx=0.1, rely=0.3, relwidth=0.8)
    first_turn_player2 = Button(turn, text=play2.get(), command=lambda: first_player(value=play2.get()),
                                bd=4, fg="#ff9900", font="Times 14 bold", bg="black", relief="groove")
    first_turn_player2.place(relx=0.1, rely=0.5, relwidth=0.8)


# getting entered name and putting them in labels
def get_names():
    name1 = play1.get()
    player1.destroy()
    name1_lbl = Label(root, text=f'{name1}', width=25, anchor=W, padx=10, relief="groove", font="Times 12 bold", bd=4,
                      bg="#cce6ff")
    name1_lbl.place(relx=0.13, rely=0.1)
    p1.destroy()

    name2 = play2.get()
    player2.destroy()
    name2_lbl = Label(root, text=f'{name2}', width=25, anchor=W, padx=10, relief="groove", font="Times 12 bold", bd=4,
                      bg="#cce6ff")
    name2_lbl.place(relx=0.73, rely=0.1)


# getting name of first player and set label with it`s name
def first_player(value):
    global currentPlayer, first_move, player
    currentPlayer = value
    current_player_label = Label(root, text=currentPlayer + '`s turn', font="Times 14 bold",
                                 bd=4, fg="black", bg="#bfff00")
    current_player_label.place(relx=0.1, rely=0.9)
#    current_player_label.after(10000, current_player_label.destroy)
    first_move = current_player_label.cget("text")
    player = play1.get() + '`s turn'
    turn.destroy()


# changing name of current player in label and getting who`s turn is it to get the winner
def switch_player():
    global current_player_label, first_move, winner

    if first_move == player:
        current_player_label = Label(root, text=play2.get() + '`s turn',
                                     font="Times 14 bold",
                                     bd=4, fg="black", bg="#bfff00"
                                     )
        current_player_label.place(relx=0.1, rely=0.9)
        first_move = play2.get() + '`s turn'
        both_players = first_move
        winner, looser = both_players.split('`')

    else:
        current_player_label = Label(root, text=play1.get() + '`s turn',
                                     font="Times 14 bold",
                                     bd=4, fg="black", bg="#bfff00"
                                     )
        current_player_label.place(relx=0.1, rely=0.9)
        first_move = play1.get() + '`s turn'
        both_players = first_move
        winner, looser = both_players.split('`')


# most important part of functioning, heart of game
def click_button(button):
    global buttonclick
    if button["text"] == " " and buttonclick == True:
        button["text"] = "X"
        button.configure(state=DISABLED)
        buttonclick = False
        draw()
        check_for_win()
        switch_player()
    elif button["text"] == " " and buttonclick == False:
        button["text"] = "O"
        buttonclick = True
        button.configure(state=DISABLED)
        draw()
        check_for_win()
        switch_player()


# checking for win with both x and o and keep track of score
def check_for_win():
    global current_player_label, score1_label
    global score1, score2
    if button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or\
       button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or\
       button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or\
       button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or\
       button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or\
       button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or\
       button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or\
       button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X':

        winning_show()
        current_player_label.destroy()
        if winner == play1.get():
            score1 += 1
        else:
            score2 += 1

        score1_label = Label(root, text=score1, bd=4, bg="white", font=14, relief="sunken")
        score1_label.place(relx=0.13, rely=0.15, relwidth=0.05)

        score2_label = Label(root, text=score2, bd=4, bg="white", font=14, relief="sunken")
        score2_label.place(relx=0.73, rely=0.15, relwidth=0.05)


    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):

        winning_show()
        current_player_label.destroy()
        if winner == play1.get():
            score1 += 1
        else:
            score2 += 1

        score1_label = Label(root, text=score1, bd=4, bg="white", font=14, relief="sunken")
        score1_label.place(relx=0.13, rely=0.15, relwidth=0.05)

        score2_label = Label(root, text=score2, bd=4, bg="white", font=14, relief="sunken")
        score2_label.place(relx=0.73, rely=0.15, relwidth=0.05)


# draw definition
def draw():
    global again
    if button1.cget('state') == DISABLED and\
       button2.cget('state') == DISABLED and\
       button3.cget('state') == DISABLED and\
       button4.cget('state') == DISABLED and\
       button5.cget('state') == DISABLED and\
       button6.cget('state') == DISABLED and\
       button7.cget('state') == DISABLED and\
       button8.cget('state') == DISABLED and\
       button9.cget('state') == DISABLED:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
        again = Tk()
        again.title("Play again?")
        again.config(bg="#00ffbf")
        Left = (again.winfo_screenwidth() - 200) / 2
        Top = (again.winfo_screenheight() - 200) / 2
        again.geometry("%dx%d+%d+%d" % (200, 100, Left, Top))
        yes = Button(again, text="YES", command=yes_clicked, bd=5, bg="white", font="Helvetica 14 bold")
        yes.place(relx=0.2, rely=0.4, relwidth=0.3)
        no = Button(again, text="NO", command=no_clicked, bd=5, bg="white", font="Helvetica 14 bold")
        no.place(relx=0.6, rely=0.4, relwidth=0.3)


# defining buttons for game
def show_buttons():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    #  first row buttons
    button1 = Button(root, borderwidth=3, relief="solid", text=" ", font="Helvetica 70 bold",
                     command=lambda: click_button(button1))
    button1.place(relx=0.25, rely=0.3, relwidth=0.1, relheight=0.1)
    button2 = Button(root, borderwidth=3, relief="solid", text=" ",
                     font="Helvetica 70 bold", command=lambda: click_button(button2))
    button2.place(relx=0.45, rely=0.3, relwidth=0.1, relheight=0.1)
    button3 = Button(root, borderwidth=3, relief="solid", text=" ",
                     font="Helvetica 70 bold", command=lambda: click_button(button3))
    button3.place(relx=0.65, rely=0.3, relwidth=0.1, relheight=0.1)

    # second row buttons
    button4 = Button(root, borderwidth=3, relief="solid", text=" ",
                     font="Helvetica 70 bold", command=lambda: click_button(button4))
    button4.place(relx=0.25, rely=0.5, relwidth=0.1, relheight=0.1)
    button5 = Button(root, borderwidth=3, relief="solid", text=" ",
                     font="Helvetica 70 bold", command=lambda: click_button(button5))
    button5.place(relx=0.45, rely=0.5, relwidth=0.1, relheight=0.1)
    button6 = Button(root, borderwidth=3, relief="solid", text=" ",
                     font="Helvetica 70 bold", command=lambda: click_button(button6))
    button6.place(relx=0.65, rely=0.5, relwidth=0.1, relheight=0.1)

    # third row buttons
    button7 = Button(root, borderwidth=3, relief="solid", text=" ",
                     font="Helvetica 70 bold", command=lambda: click_button(button7))
    button7.place(relx=0.25, rely=0.7, relwidth=0.1, relheight=0.1)
    button8 = Button(root, borderwidth=3, relief="solid", text=" ",
                     font="Helvetica 70 bold", command=lambda: click_button(button8))
    button8.place(relx=0.45, rely=0.7, relwidth=0.1, relheight=0.1)
    button9 = Button(root, borderwidth=3, relief="solid", text=" ",
                     font="Helvetica 70 bold", command=lambda: click_button(button9))
    button9.place(relx=0.65, rely=0.7, relwidth=0.1, relheight=0.1)


# picture for winner, label with winner and continue button
def winning_show():
    global canvas
    IMAGE_PATH = 'congratulations.png'
    WIDTH, HEIGTH = 600, 450
    canvas = Canvas(root, width=WIDTH, height=HEIGTH)
    canvas.pack()
    l1 = Label(canvas, font=50, text="The WINNER is " + winner, bd=5, bg="yellow", fg="green")
    l1.place(relx=0.2, rely=0.6, relwidth=0.6)
    img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
    canvas.background = img
    canvas.create_image(0, 0, anchor=NW, image=img)
    _continue = Button(canvas, text="CONTINUE", command=play_again, bd=5, bg="#f2e6ff",
                       fg="#00001a", font="Times 14 bold")
    _continue.place(relx=0.4, rely=0.8)


# pop up window to play again, or not
def play_again():
    global again
    again = Tk()
    again.title("Play again?")
    again.config(bg="#00ffbf")
    Left = (again.winfo_screenwidth() - 200) / 2
    Top = (again.winfo_screenheight() - 200) / 2
    again.geometry("%dx%d+%d+%d" % (200, 100, Left, Top))
    yes = Button(again, text="YES", command=yes_clicked, bd=5, bg="white", font="Helvetica 14 bold")
    yes.place(relx=0.2, rely=0.4, relwidth=0.3)
    no = Button(again, text="NO", command=no_clicked, bd=5, bg="white", font="Helvetica 14 bold")
    no.place(relx=0.6, rely=0.4, relwidth=0.3)
    canvas.destroy()


def yes_clicked():
    show_buttons()
    set_first_player()
    again.destroy()


def no_clicked():
    set_name()
    again.destroy()


# def for quitting game
def _quit():
    global quit_window
    quit_window = Tk()
    quit_window.config(bg="grey")
    quit_window.title(" ")
    quit_left = (root.winfo_screenwidth() - 400) / 2
    quit_top = (root.winfo_screenheight() - 300) / 2
    quit_window.geometry("%dx%d+%d+%d" % (420, 100, quit_left, quit_top))
    quit_label = Label(quit_window, text="Are You Sure You Want To Quit?!", fg="red",
                       bg="#b3b3ff", font="Helvetica 16 bold", anchor="w")
    quit_label.place(relx=0.1, rely=0.1)
    yes_q = Button(quit_window, text="YES", command=yes_quit, bg="red", font="Times 14 bold")
    yes_q.place(relx=0.2, rely=0.4, relwidth=0.2)
    no_q = Button(quit_window, text="NO", command=no_quit, font="Times 14 bold", bg="green")
    no_q.place(relx=0.6, rely=0.4, relwidth=0.2)


def yes_quit():
    quit_window.destroy()
    root.destroy()
    try:
        turn.destroy()
        again.destroy()
    except:
        pass


def no_quit():
    quit_window.destroy()


# buttons reset, quit, start
quit_button = Button(root, text="QUIT", bg="red", bd=5, fg="black", command=_quit)
quit_button.place(relx=0.8, rely=0.9, relwidth=0.2)

# reset button
reset_button = Button(root, text='RESET', command=set_name, font="Helvetica 18 bold", bd=10, fg="#0040ff", bg="#00ff00")
reset_button.place(relx=0.5, rely=0.93, anchor=S, relwidth=0.2, relheight=0.1)

#  start button
start_button = Button(root, text='START', font="Helvetica 18 bold", command=set_name, bd=5, fg="blue", bg="#ffff00",
                      padx=5, pady=5)
start_button.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)

root.mainloop()
