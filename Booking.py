import tkinter as tk
from tkinter import ttk

screens = ["Screens 1", "Screens 2", "Screens 3", "Screens 4", "Screens 5", "Screens 6"]

movies = {
    "Horror": ["Hereditary", "A Quiet Place", "The Conjuring 2", "The Grudge", "Annabelle Comes Home"],
    "Action": ["Avengers Endgame", "John Wick Chapter 3", "Aquaman", "Black Panther", "Mission Impossible"],
    "Drama": ["Joker", "Spotlight", "Little Women", "The Irishman", "A Star is Born"],
    "Comedy": ["Step Brothers", "Booksmart", "Horrible Bosses", "The Other Guys", "Superbad"],
    "Sci-Fi": ["Star Wars", "Annihilation", "Arrival", "Interstellar", "The Martian"],
    "Romance": ["The Fault in Our Stars", "The Notebook", "The Tourist", "Titanic", "Crazy Rich Asians"]
}

times = ["10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30",
         "14:00", "14:30", "15:00", "15:30", "16:00", "16:30"]

seatList = []
seatSelected = []

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cinema Booking")
        self.createWidgets()

    def updateMovies(self, event=None):
        genre = self.genreCombo.get()
        self.movieCombo['values'] = movies.get(genre, [])
        self.movieCombo.set("Select Movie")

    def createWidgets(self):
        headingLabel = tk.Label(self, text="Cinema Seat Bookings", font="Arial 12 bold")
        headingLabel.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="w")

        ttk.Separator(self, orient="horizontal").grid(row=1, column=0, columnspan=5, sticky="ew")

        day = tk.Frame(self)
        tk.Label(day, text="____").pack()
        tk.Label(day, text="Today", font="Arial 10 underline").pack()
        tk.Label(day, text="").pack()
        day.grid(row=2, column=0, padx=10)

        tk.Label(self, text="Genre: ").grid(row=2, column=1, padx=(10, 0))
        self.genreCombo = ttk.Combobox(self, width=15, values=list(movies.keys()), state="readonly")
        self.genreCombo.set("Select Genre")
        self.genreCombo.bind('<<ComboboxSelected>>', self.updateMovies)
        self.genreCombo.grid(row=2, column=2)

        tk.Label(self, text="Movies: ").grid(row=2, column=3, padx=(10, 0))
        self.movieCombo = ttk.Combobox(self, width=15, state="readonly")
        self.movieCombo.set("Select Movie")
        self.movieCombo.grid(row=2, column=4, padx=(10, 0))
        self.movieCombo.bind('<<ComboboxSelected>>', self.createTimeButtons)

        ttk.Separator(self, orient="horizontal").grid(row=3, column=0, columnspan=5, sticky='ew')

    def createTimeButtons(self, event=None):
        tk.Label(self, text="Select Time Slot", font="Arial 11 bold underline").grid(
            row=4, column=2, columnspan=2, pady=5
        )
        Time = tk.Frame(self)
        Time.grid(row=5, column=0, columnspan=5)
        for i in range(14):
            tk.Button(Time, text=times[i], command=self.seatSelection).grid(row=i//7, column=i%7, padx=5, pady=5)

    def seatSelection(self):
        window = tk.Toplevel()
        window.title("Select your Seat")
        checkoutHeading = tk.Label(window, text="Seat(s) Selection", font="Arial 12")
        checkoutHeading.grid(row=0, column=0, columnspan=5, padx=10, pady=(10, 0), sticky="w")

        infer = tk.Frame(window)
        infer.grid(row=1, column=0)
        tk.Label(infer, text='BLUE = SELECTED', fg='blue').grid(row=0, column=0, padx=10)
        tk.Label(infer, text='RED = BOOKED', fg='brown').grid(row=0, column=1, padx=10)
        tk.Label(infer, text='GREEN = AVAILABLE', fg='green').grid(row=0, column=2, padx=10)
        ttk.Separator(window, orient="horizontal").grid(row=2, column=0, pady=(0, 5), sticky="ew")

        w = tk.Canvas(window, width=500, height=15)
        w.create_rectangle(10, 0, 490, 10, fill='black')
        w.grid(row=3, column=0)
        tk.Label(window, text="SCREEN").grid(row=4, column=0, pady=(0, 10))

        seats = tk.Frame(window)
        seats.grid(row=5, column=0)
        seatList.clear()
        seatSelected.clear()
        for i in range(4):
            temp = []
            for j in range(15):
                but = tk.Button(seats, bd=2, bg='green', activebackground='forestGreen',
                                command=lambda x=i, y=j: self.selected(x, y))
                temp.append(but)
                but.grid(row=i, column=j, padx=5, pady=5)
            seatList.append(temp)

        tk.Button(window, text="Book Seats", bg='black', fg="white", command=self.bookSeat).grid(
            row=6, column=0, pady=10
        )

    def selected(self, i, j):
        if seatList[i][j]['bg'] == 'blue':
            seatList[i][j]['bg'] = 'green'
            seatList[i][j]['activebackground'] = "forestGreen"
            seatSelected.remove((i, j))
        else:
            seatList[i][j]['bg'] = 'blue'
            seatList[i][j]['activebackground'] = 'blue'
            seatSelected.append((i, j))

    def bookSeat(self):
        for i in seatSelected:
            seatList[i[0]][i[1]]['bg'] = 'brown'
            seatList[i[0]][i[1]]['activebackground'] = 'brown'
            seatList[i[0]][i[1]]['relief'] = 'sunken'

app = Application()
app.mainloop()

