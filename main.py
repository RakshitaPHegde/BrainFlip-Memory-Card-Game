import tkinter as tk
import random


class BrainFlip:

    def __init__(self, window):

        self.window = window

        # ==================================================
        # WINDOW
        # ==================================================

        self.window.title("BrainFlip - Memory Challenge")
        self.window.geometry("1000x850")
        self.window.resizable(False, False)
        self.window.configure(bg="#EEF2FF")

        # ==================================================
        # LEVEL SETTINGS
        # ==================================================

        self.level = 1
        self.max_level = 100

        # ALWAYS 12 PAIRS = 24 CARDS
        self.pairs = 12

        # ==================================================
        # GAME VARIABLES
        # ==================================================

        self.cards = []
        self.card_widgets = []

        self.first_card = None
        self.second_card = None

        self.matched_cards = set()

        self.locked = False

        self.moves = 0
        self.matches = 0
        self.score = 0

        self.time_left = 90
        self.timer_running = False
        self.timer_id = None

        self.best_score = 0

        # ==================================================
        # 12 COLORFUL SYMBOLS
        # ==================================================

        self.symbols = [
            "apple",
            "star",
            "sun",
            "moon",
            "flower",
            "clover",
            "ball",
            "music",
            "rocket",
            "cat",
            "butterfly",
            "pizza"
        ]

        # ==================================================
        # CREATE GAME
        # ==================================================

        self.create_interface()

        self.start_game()

    # ======================================================
    # CREATE INTERFACE
    # ======================================================

    def create_interface(self):

        # TITLE

        title = tk.Label(
            self.window,
            text="BrainFlip",
            font=("Arial", 34, "bold"),
            bg="#EEF2FF",
            fg="#3949AB"
        )

        title.pack(pady=(12, 0))

        # SUBTITLE

        subtitle = tk.Label(
            self.window,
            text="The Ultimate Memory Challenge",
            font=("Arial", 14, "bold"),
            bg="#EEF2FF",
            fg="#636B8A"
        )

        subtitle.pack(pady=(0, 5))

        # LEVEL

        self.level_label = tk.Label(
            self.window,
            text="LEVEL 1",
            font=("Arial", 22, "bold"),
            bg="#EEF2FF",
            fg="#4CAF50"
        )

        self.level_label.pack(pady=4)

        # ==================================================
        # INFORMATION BAR
        # ==================================================

        info_frame = tk.Frame(
            self.window,
            bg="#EEF2FF"
        )

        info_frame.pack(pady=2)

        self.score_label = tk.Label(
            info_frame,
            text="Score: 0",
            font=("Arial", 13, "bold"),
            bg="#EEF2FF",
            fg="#E91E63"
        )

        self.score_label.grid(
            row=0,
            column=0,
            padx=25
        )

        self.moves_label = tk.Label(
            info_frame,
            text="Moves: 0",
            font=("Arial", 13, "bold"),
            bg="#EEF2FF",
            fg="#1565C0"
        )

        self.moves_label.grid(
            row=0,
            column=1,
            padx=25
        )

        self.timer_label = tk.Label(
            info_frame,
            text="Time: 90",
            font=("Arial", 13, "bold"),
            bg="#EEF2FF",
            fg="#F4511E"
        )

        self.timer_label.grid(
            row=0,
            column=2,
            padx=25
        )

        self.best_label = tk.Label(
            info_frame,
            text="Best: 0",
            font=("Arial", 13, "bold"),
            bg="#EEF2FF",
            fg="#673AB7"
        )

        self.best_label.grid(
            row=0,
            column=3,
            padx=25
        )

        # ==================================================
        # PROGRESS
        # ==================================================

        self.progress_label = tk.Label(
            self.window,
            text="Level 1 / 100",
            font=("Arial", 11, "bold"),
            bg="#EEF2FF",
            fg="#555577"
        )

        self.progress_label.pack(pady=2)

        # ==================================================
        # GAME BOARD
        # ==================================================

        self.board = tk.Frame(
            self.window,
            bg="#EEF2FF"
        )

        self.board.pack(pady=5)

        # ==================================================
        # RESTART BUTTON
        # ==================================================

        tk.Button(
            self.window,
            text="RESTART LEVEL",
            font=("Arial", 11, "bold"),
            width=20,
            bg="#3949AB",
            fg="white",
            activebackground="#283593",
            activeforeground="white",
            command=self.start_game
        ).pack(pady=5)

        # ==================================================
        # MESSAGE
        # ==================================================

        self.message_label = tk.Label(
            self.window,
            text="Find all 12 matching pairs!",
            font=("Arial", 12, "bold"),
            bg="#EEF2FF",
            fg="#555577"
        )

        self.message_label.pack(pady=2)

    # ======================================================
    # DIFFICULTY
    # ======================================================

    def calculate_time(self):

        if self.level <= 10:

            return 90

        elif self.level <= 25:

            return 80

        elif self.level <= 50:

            return 70

        elif self.level <= 75:

            return 60

        else:

            return 50

    # ======================================================
    # START GAME
    # ======================================================

    def start_game(self):

        # STOP OLD TIMER

        if self.timer_id is not None:

            try:

                self.window.after_cancel(
                    self.timer_id
                )

            except Exception:

                pass

            self.timer_id = None

        # RESET TIME

        self.time_left = self.calculate_time()

        # RESET GAME

        self.moves = 0
        self.matches = 0
        self.score = 0

        self.first_card = None
        self.second_card = None

        self.matched_cards = set()

        self.locked = False
        self.timer_running = False

        # LEVEL COLOR

        if self.level <= 10:

            level_color = "#4CAF50"

        elif self.level <= 25:

            level_color = "#FF9800"

        elif self.level <= 50:

            level_color = "#FF7043"

        elif self.level <= 75:

            level_color = "#E91E63"

        else:

            level_color = "#9C27B0"

        self.level_label.config(
            text=f"LEVEL {self.level}",
            fg=level_color
        )

        self.progress_label.config(
            text=f"Level {self.level} / {self.max_level}"
        )

        # REMOVE OLD CARDS

        for card in self.card_widgets:

            card.destroy()

        self.card_widgets = []

        # ==================================================
        # CREATE 12 PAIRS = 24 CARDS
        # ==================================================

        self.cards = self.symbols * 2

        random.shuffle(self.cards)

        # ==================================================
        # BOARD = 6 COLUMNS × 4 ROWS
        # ==================================================

        columns = 6

        # ==================================================
        # CREATE 24 CARDS
        # ==================================================

        for index, symbol in enumerate(self.cards):

            row = index // columns
            column = index % columns

            card = tk.Canvas(
                self.board,
                width=125,
                height=92,
                bg="white",
                highlightthickness=3,
                highlightbackground="#C5CAE9",
                cursor="hand2"
            )

            card.grid(
                row=row,
                column=column,
                padx=4,
                pady=4
            )

            self.draw_card_back(card)

            card.bind(
                "<Button-1>",
                lambda event, i=index:
                self.flip_card(i)
            )

            self.card_widgets.append(card)

        # UPDATE

        self.update_information()

        self.message_label.config(
            text="Find all 12 matching pairs!",
            fg="#555577"
        )

    # ======================================================
    # CARD BACK
    # ======================================================

    def draw_card_back(self, canvas):

        canvas.delete("all")

        # OUTER CARD

        canvas.create_rectangle(
            3,
            3,
            122,
            89,
            fill="#E8EAF6",
            outline="#5C6BC0",
            width=3
        )

        # INNER CARD

        canvas.create_rectangle(
            13,
            13,
            112,
            79,
            fill="#536DFE",
            outline="#303F9F",
            width=3
        )

        # DECORATION

        canvas.create_oval(
            45,
            25,
            80,
            60,
            outline="#9FA8DA",
            width=2
        )

        # QUESTION MARK

        canvas.create_text(
            62,
            43,
            text="?",
            font=("Arial", 30, "bold"),
            fill="white"
        )

    # ======================================================
    # FLIP CARD
    # ======================================================

    def flip_card(self, index):

        # GAME LOCKED

        if self.locked:

            return

        # ALREADY MATCHED

        if index in self.matched_cards:

            return

        # SAME CARD

        if self.first_card == index:

            return

        # SHOW CARD

        self.draw_card_front(
            self.card_widgets[index],
            self.cards[index]
        )

        # FIRST CARD

        if self.first_card is None:

            self.first_card = index

            if not self.timer_running:

                self.timer_running = True

                self.update_timer()

            return

        # SECOND CARD

        self.second_card = index

        self.moves += 1

        self.locked = True

        self.update_information()

        self.window.after(
            600,
            self.check_match
        )

    # ======================================================
    # CARD FRONT
    # ======================================================

    def draw_card_front(self, canvas, symbol):

        canvas.delete("all")

        canvas.create_rectangle(
            3,
            3,
            122,
            89,
            fill="white",
            outline="#7986CB",
            width=3
        )

        self.draw_symbol(
            canvas,
            symbol
        )

    # ======================================================
    # DRAW COLORFUL SYMBOLS
    # ======================================================

    def draw_symbol(self, canvas, symbol):

        # APPLE

        if symbol == "apple":

            canvas.create_oval(
                38, 30, 83, 75,
                fill="#EF5350",
                outline="#C62828",
                width=2
            )

            canvas.create_oval(
                67, 20, 87, 38,
                fill="#66BB6A"
            )

            canvas.create_line(
                67, 31, 65, 18,
                fill="#795548",
                width=4
            )

        # STAR

        elif symbol == "star":

            points = [
                62, 10,
                72, 36,
                100, 36,
                78, 52,
                86, 82,
                62, 64,
                38, 82,
                46, 52,
                24, 36,
                52, 36
            ]

            canvas.create_polygon(
                points,
                fill="#FFD54F",
                outline="#FF8F00",
                width=3
            )

        # SUN

        elif symbol == "sun":

            canvas.create_oval(
                40, 25, 85, 70,
                fill="#FFD54F",
                outline="#FF9800",
                width=3
            )

            rays = [
                (62, 7, 62, 20),
                (62, 75, 62, 88),
                (18, 48, 32, 48),
                (92, 48, 106, 48),
                (30, 18, 40, 28),
                (84, 68, 94, 78),
                (84, 18, 94, 28),
                (30, 68, 40, 78)
            ]

            for x1, y1, x2, y2 in rays:

                canvas.create_line(
                    x1, y1, x2, y2,
                    fill="#FF9800",
                    width=3
                )

        # MOON

        elif symbol == "moon":

            canvas.create_oval(
                35, 18, 90, 73,
                fill="#FFD54F",
                outline="#F9A825",
                width=2
            )

            canvas.create_oval(
                55, 13, 93, 60,
                fill="white",
                outline="white"
            )

        # FLOWER

        elif symbol == "flower":

            petals = [
                (48, 18, 75, 45, "#EC407A"),
                (30, 34, 57, 61, "#AB47BC"),
                (68, 34, 95, 61, "#42A5F5"),
                (48, 50, 75, 77, "#FF7043")
            ]

            for x1, y1, x2, y2, color in petals:

                canvas.create_oval(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=color
                )

            canvas.create_oval(
                55,
                38,
                68,
                51,
                fill="#FFD54F"
            )

        # CLOVER

        elif symbol == "clover":

            positions = [
                (30, 22, 58, 50),
                (66, 22, 94, 50),
                (30, 45, 58, 73),
                (66, 45, 94, 73)
            ]

            colors = [
                "#66BB6A",
                "#43A047",
                "#2E7D32",
                "#81C784"
            ]

            for position, color in zip(
                positions,
                colors
            ):

                canvas.create_oval(
                    *position,
                    fill=color
                )

            canvas.create_rectangle(
                60,
                58,
                66,
                84,
                fill="#795548",
                outline="#795548"
            )

        # BALL

        elif symbol == "ball":

            canvas.create_oval(
                30, 15, 94, 79,
                fill="#42A5F5",
                outline="#1565C0",
                width=3
            )

            canvas.create_polygon(
                62, 29,
                75, 39,
                71, 54,
                53, 54,
                49, 39,
                fill="white",
                outline="#1565C0"
            )

        # MUSIC

        elif symbol == "music":

            canvas.create_oval(
                35, 62, 57, 78,
                fill="#AB47BC"
            )

            canvas.create_line(
                54, 68, 54, 20,
                fill="#6A1B9A",
                width=6
            )

            canvas.create_line(
                54, 20, 83, 28,
                fill="#6A1B9A",
                width=6
            )

            canvas.create_line(
                83, 28, 83, 55,
                fill="#6A1B9A",
                width=6
            )

            canvas.create_oval(
                72, 50, 92, 66,
                fill="#E91E63"
            )

        # ROCKET

        elif symbol == "rocket":

            canvas.create_oval(
                45, 10, 80, 68,
                fill="#EF5350",
                outline="#B71C1C",
                width=2
            )

            canvas.create_polygon(
                45, 47,
                28, 62,
                47, 61,
                fill="#42A5F5"
            )

            canvas.create_polygon(
                80, 47,
                97, 62,
                78, 61,
                fill="#42A5F5"
            )

            canvas.create_oval(
                54, 25, 70, 41,
                fill="#90CAF9",
                outline="#1565C0"
            )

            canvas.create_polygon(
                52, 65,
                62, 86,
                72, 65,
                fill="#FF9800"
            )

        # CAT

        elif symbol == "cat":

            canvas.create_oval(
                37, 28, 88, 76,
                fill="#FFB74D",
                outline="#EF6C00",
                width=2
            )

            canvas.create_polygon(
                39, 35,
                36, 12,
                54, 27,
                fill="#FFB74D",
                outline="#EF6C00"
            )

            canvas.create_polygon(
                70, 27,
                89, 12,
                86, 35,
                fill="#FFB74D",
                outline="#EF6C00"
            )

            canvas.create_oval(
                49, 43, 55, 50,
                fill="black"
            )

            canvas.create_oval(
                70, 43, 76, 50,
                fill="black"
            )

            canvas.create_oval(
                59, 53, 66, 59,
                fill="#E91E63"
            )

        # BUTTERFLY

        elif symbol == "butterfly":

            canvas.create_oval(
                23, 23, 56, 55,
                fill="#EC407A",
                outline="#AD1457",
                width=2
            )

            canvas.create_oval(
                68, 23, 101, 55,
                fill="#7E57C2",
                outline="#4527A0",
                width=2
            )

            canvas.create_oval(
                25, 50, 55, 75,
                fill="#42A5F5",
                outline="#1565C0",
                width=2
            )

            canvas.create_oval(
                69, 50, 99, 75,
                fill="#26C6DA",
                outline="#00838F",
                width=2
            )

            canvas.create_rectangle(
                59, 31, 66, 75,
                fill="#5D4037"
            )

        # PIZZA

        elif symbol == "pizza":

            canvas.create_polygon(
                25, 18,
                100, 30,
                48, 82,
                fill="#FFD54F",
                outline="#F57C00",
                width=3
            )

            canvas.create_line(
                25, 18,
                100, 30,
                fill="#D84315",
                width=9
            )

            canvas.create_oval(
                51, 40, 62, 51,
                fill="#E53935"
            )

            canvas.create_oval(
                69, 51, 80, 62,
                fill="#E53935"
            )

            canvas.create_oval(
                43, 56, 54, 67,
                fill="#E53935"
            )

    # ======================================================
    # CHECK MATCH
    # ======================================================

    def check_match(self):

        first = self.first_card
        second = self.second_card

        if first is None or second is None:

            self.locked = False

            return

        # MATCH

        if self.cards[first] == self.cards[second]:

            self.matched_cards.add(first)
            self.matched_cards.add(second)

            self.card_widgets[first].configure(
                highlightbackground="#4CAF50"
            )

            self.card_widgets[second].configure(
                highlightbackground="#4CAF50"
            )

            self.matches += 1

            self.score += 10

            self.message_label.config(
                text="MATCH FOUND!",
                fg="#2E7D32"
            )

        # NOT MATCH

        else:

            self.draw_card_back(
                self.card_widgets[first]
            )

            self.draw_card_back(
                self.card_widgets[second]
            )

            self.message_label.config(
                text="Not a match. Try again!",
                fg="#D84315"
            )

        self.first_card = None
        self.second_card = None

        self.locked = False

        self.update_information()

        # ALL 12 PAIRS FOUND

        if self.matches == self.pairs:

            self.level_completed()

    # ======================================================
    # TIMER
    # ======================================================

    def update_timer(self):

        if not self.timer_running:

            return

        if self.time_left > 0:

            self.time_left -= 1

            self.timer_label.config(
                text=f"Time: {self.time_left}"
            )

            self.timer_id = self.window.after(
                1000,
                self.update_timer
            )

        else:

            self.timer_running = False

            self.timer_id = None

            self.locked = True

            for card in self.card_widgets:

                card.unbind(
                    "<Button-1>"
                )

            self.show_time_up_popup()

    # ======================================================
    # UPDATE INFORMATION
    # ======================================================

    def update_information(self):

        self.score_label.config(
            text=f"Score: {self.score}"
        )

        self.moves_label.config(
            text=f"Moves: {self.moves}"
        )

        self.timer_label.config(
            text=f"Time: {self.time_left}"
        )

        self.best_label.config(
            text=f"Best: {self.best_score}"
        )

    # ======================================================
    # CALCULATE STARS
    # ======================================================

    def calculate_stars(self):

        if self.moves <= 15:

            return 3

        elif self.moves <= 24:

            return 2

        else:

            return 1

    # ======================================================
    # LEVEL COMPLETED
    # ======================================================

    def level_completed(self):

        self.timer_running = False

        if self.timer_id is not None:

            try:

                self.window.after_cancel(
                    self.timer_id
                )

            except Exception:

                pass

            self.timer_id = None

        # TIME BONUS

        self.score += self.time_left

        # BEST SCORE

        if self.score > self.best_score:

            self.best_score = self.score

        self.update_information()

        # DISABLE CARDS

        for card in self.card_widgets:

            card.unbind(
                "<Button-1>"
            )

        stars = self.calculate_stars()

        self.show_level_complete_popup(
            stars
        )

    # ======================================================
    # CENTER POPUP
    # ======================================================

    def center_popup(self, popup, width, height):

        self.window.update_idletasks()

        main_x = self.window.winfo_x()
        main_y = self.window.winfo_y()

        main_width = self.window.winfo_width()
        main_height = self.window.winfo_height()

        x = main_x + (main_width - width) // 2
        y = main_y + (main_height - height) // 2

        popup.geometry(
            f"{width}x{height}+{x}+{y}"
        )

    # ======================================================
    # CONGRATULATIONS POPUP
    # ======================================================

    def show_level_complete_popup(self, stars):

        popup = tk.Toplevel(
            self.window
        )

        popup.title(
            "Congratulations!"
        )

        popup.resizable(
            False,
            False
        )

        popup.configure(
            bg="#FFF8E1"
        )

        popup.transient(
            self.window
        )

        # CENTER POPUP

        self.center_popup(
            popup,
            620,
            560
        )

        popup.grab_set()

        # ==================================================
        # HEADER
        # ==================================================

        header = tk.Frame(
            popup,
            bg="#5E35B1",
            height=115
        )

        header.pack(
            fill="x"
        )

        tk.Label(
            header,
            text="CONGRATULATIONS!",
            font=("Arial", 28, "bold"),
            bg="#5E35B1",
            fg="white"
        ).pack(
            pady=34
        )

        # ==================================================
        # LEVEL COMPLETE
        # ==================================================

        tk.Label(
            popup,
            text=f"LEVEL {self.level} COMPLETED!",
            font=("Arial", 22, "bold"),
            bg="#FFF8E1",
            fg="#E65100"
        ).pack(
            pady=(20, 5)
        )

        # ==================================================
        # STARS
        # ==================================================

        star_text = "★" * stars

        tk.Label(
            popup,
            text=star_text,
            font=("Arial", 42, "bold"),
            bg="#FFF8E1",
            fg="#FFB300"
        ).pack(
            pady=2
        )

        # ==================================================
        # REWARD
        # ==================================================

        if stars == 3:

            reward = "PERFECT! 3-STAR CHAMPION!"

        elif stars == 2:

            reward = "GREAT JOB! 2-STAR PLAYER!"

        else:

            reward = "GOOD JOB! 1-STAR PLAYER!"

        tk.Label(
            popup,
            text=reward,
            font=("Arial", 15, "bold"),
            bg="#FFF8E1",
            fg="#3949AB"
        ).pack(
            pady=2
        )

        # ==================================================
        # STATISTICS BOX
        # ==================================================

        stats = tk.Frame(
            popup,
            bg="white",
            bd=2,
            relief="ridge"
        )

        stats.pack(
            padx=70,
            pady=15,
            fill="x"
        )

        tk.Label(
            stats,
            text=f"Score: {self.score}",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#E91E63"
        ).pack(
            pady=4
        )

        tk.Label(
            stats,
            text=f"Moves: {self.moves}",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#1565C0"
        ).pack(
            pady=4
        )

        tk.Label(
            stats,
            text=f"Time Left: {self.time_left} seconds",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#F4511E"
        ).pack(
            pady=4
        )

        tk.Label(
            stats,
            text="12 Pairs • 24 Cards",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#673AB7"
        ).pack(
            pady=4
        )

        # ==================================================
        # NEXT LEVEL
        # ==================================================

        if self.level < self.max_level:

            tk.Button(
                popup,
                text=f"NEXT LEVEL {self.level + 1}",
                font=("Arial", 15, "bold"),
                width=25,
                height=1,
                bg="#4CAF50",
                fg="white",
                activebackground="#388E3C",
                activeforeground="white",
                command=lambda:
                self.next_level(popup)
            ).pack(
                pady=15
            )

        # ==================================================
        # LEVEL 100
        # ==================================================

        else:

            tk.Label(
                popup,
                text="YOU ARE A BRAINFLIP MASTER!",
                font=("Arial", 16, "bold"),
                bg="#FFF8E1",
                fg="#9C27B0"
            ).pack(
                pady=8
            )

            tk.Button(
                popup,
                text="PLAY AGAIN",
                font=("Arial", 15, "bold"),
                width=25,
                bg="#E91E63",
                fg="white",
                activebackground="#C2185B",
                activeforeground="white",
                command=lambda:
                self.play_again(popup)
            ).pack(
                pady=10
            )

    # ======================================================
    # NEXT LEVEL
    # ======================================================

    def next_level(self, popup):

        popup.grab_release()

        popup.destroy()

        self.level += 1

        self.start_game()

    # ======================================================
    # PLAY AGAIN
    # ======================================================

    def play_again(self, popup):

        popup.grab_release()

        popup.destroy()

        self.level = 1

        self.start_game()

    # ======================================================
    # TIME UP POPUP
    # ======================================================

    def show_time_up_popup(self):

        popup = tk.Toplevel(
            self.window
        )

        popup.title(
            "Time's Up!"
        )

        popup.resizable(
            False,
            False
        )

        popup.configure(
            bg="#FFEBEE"
        )

        popup.transient(
            self.window
        )

        # CENTER

        self.center_popup(
            popup,
            500,
            330
        )

        popup.grab_set()

        tk.Label(
            popup,
            text="TIME'S UP!",
            font=("Arial", 30, "bold"),
            bg="#FFEBEE",
            fg="#D32F2F"
        ).pack(
            pady=35
        )

        tk.Label(
            popup,
            text=f"Level {self.level}",
            font=("Arial", 18, "bold"),
            bg="#FFEBEE",
            fg="#555555"
        ).pack()

        tk.Label(
            popup,
            text="Don't give up! Try again.",
            font=("Arial", 14),
            bg="#FFEBEE",
            fg="#555555"
        ).pack(
            pady=10
        )

        tk.Button(
            popup,
            text="TRY AGAIN",
            font=("Arial", 13, "bold"),
            width=18,
            bg="#3949AB",
            fg="white",
            command=lambda:
            self.close_time_popup(popup)
        ).pack(
            pady=15
        )

    # ======================================================
    # CLOSE TIME POPUP
    # ======================================================

    def close_time_popup(self, popup):

        popup.grab_release()

        popup.destroy()

        self.start_game()


# ==========================================================
# START PROGRAM
# ==========================================================

if __name__ == "__main__":

    window = tk.Tk()

    game = BrainFlip(window)

    window.mainloop()