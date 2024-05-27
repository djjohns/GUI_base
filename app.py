import customtkinter
from modules.buttons.button1 import button1
from modules.buttons.button2 import button2
from modules.dropdown_menus.change_options_menu1 import change_options_menu1
from modules.dropdown_menus.change_appearance_mode import change_appearance_mode


customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):

    APP_NAME = "GUI Base App"
    WIDTH = 800
    HEIGHT = 500

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand("tk::mac::Quit", self.on_closing)

        self.marker_list = []

        # --------------- Create two CTkFrames --------------------------------

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Left Frame
        self.frame_left = customtkinter.CTkFrame(
            master=self, width=150, corner_radius=0, fg_color=None
        )
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        # Right Frame
        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        # ------------------- Left frame config begin -------------------------
        self.frame_left.grid_rowconfigure(2, weight=1)

        # Button 1
        self.button_1 = customtkinter.CTkButton(
            master=self.frame_left, text="Button 1", command=button1
        )

        self.button_1.grid(pady=(20, 0), padx=(20, 20), row=0, column=0)

        # Button 2
        self.button_2 = customtkinter.CTkButton(
            master=self.frame_left,
            text="Button 2",
            command=button2,
        )

        self.button_2.grid(pady=(20, 0), padx=(20, 20), row=1, column=0)

        # options_menu1 Title
        self.map_label = customtkinter.CTkLabel(
            self.frame_left, text="Option Menu 1 Title:", anchor="w"
        )
        self.map_label.grid(row=3, column=0, padx=(20, 20), pady=(20, 0))

        # options_menu1
        self.map_option_menu = customtkinter.CTkOptionMenu(
            self.frame_left,
            values=["Option 1", "Option 2", "Option 3", "Option 4"],
            command=change_options_menu1,
        )
        self.map_option_menu.grid(row=4, column=0, padx=(20, 20), pady=(10, 0))

        # Appearance mode
        self.appearance_mode_label = customtkinter.CTkLabel(
            self.frame_left, text="Appearance Mode:", anchor="w"
        )

        self.appearance_mode_label.grid(row=5, column=0, padx=(20, 20), pady=(20, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self.frame_left,
            values=["Light", "Dark", "System"],
            command=change_appearance_mode,
        )

        self.appearance_mode_optionemenu.grid(
            row=6, column=0, padx=(20, 20), pady=(10, 20)
        )

        # Set appearance default to dark mode.
        self.appearance_mode_optionemenu.set("Dark")

        # ------------------- Left frame config end ---------------------------

        # ------------------- Right frame config begin ------------------------
        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        # Entry Field
        self.entry = customtkinter.CTkEntry(
            master=self.frame_right, placeholder_text="Search"
        )
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        self.entry.bind("<Return>", self.search)

        # Button 3
        self.button_3 = customtkinter.CTkButton(
            master=self.frame_right,
            text="Button 3",
            width=90,
            command=self.search,
        )
        self.button_3.grid(row=0, column=1, sticky="w", padx=(12, 0), pady=12)

        # ------------------- Right frame config end ------------------------

    def search(self, event=None):
        """
        Since I want to do something with the content provided by the user in the entry field, the easiest and fastest way is to define that function inside of the app.py file. There are other ways to abstract this into it's own module for cleaner code but this is just a example.
        """
        user_input = self.entry.get()
        print(f"User wants to Search for: {user_input}")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
