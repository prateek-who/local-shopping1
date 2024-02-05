import customtkinter as ct
import tkinter as tk
from PIL import Image as Im
import backendforact2 as bk
import time


class App(ct.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ct.set_default_color_theme("green")
        ct.set_appearance_mode("dark")
        self.login()

    def login(self):
        self.geometry("400x600+100+200")
        self.resizable(False, False)
        self.title("ABG")

        logo_width = 300
        logo_height = 200

        logo_img = ct.CTkImage(Im.open("images\\logo_route.jpg"), size=(logo_width, logo_height))

        mainframe = ct.CTkFrame(master=self, width=400, height=600, corner_radius=0, fg_color="#000000")
        mainframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        login_frame = ct.CTkFrame(master=mainframe, width=400, height=600, corner_radius=0, fg_color="#000000")
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # logo and stuff
        comp_log = ct.CTkLabel(master=login_frame, width=logo_width, height=logo_height, corner_radius=0, text="",
                               image=logo_img)
        comp_log.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        # login
        txt_color1 = "#A1EEBD"
        txt_color = "#FFC0D9"
        self.username = ct.CTkEntry(master=login_frame, width=200, height=45, placeholder_text="Username",
                                    font=("Normal", 18),
                                    corner_radius=10, placeholder_text_color=txt_color, text_color=txt_color,
                                    fg_color="#000000",
                                    border_color=txt_color)
        self.username.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.password = ct.CTkEntry(master=login_frame, width=200, height=45, placeholder_text="Password",
                                    font=("Normal", 18), corner_radius=10, show="*",
                                    placeholder_text_color=txt_color1, text_color=txt_color1, fg_color="#000000",
                                    border_color=txt_color1)
        self.password.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        login_button = ct.CTkButton(master=login_frame, width=100, height=38, text="Login", corner_radius=10,
                                    font=("Normal", 18), text_color="#000000", fg_color="#F2BE22",
                                    hover_color="#22A699",
                                    command=self.login_opp)
        login_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        self.bind("<Return>", lambda event: login_button.invoke())

    def login_opp(self):
        username = self.username.get()
        password = self.password.get()

        check, name = mybackend.login_check(username, password)
        if check:
            self.destroy()
            main = Main()
            main.mainloop()


class Main(ct.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ct.set_default_color_theme("green")
        ct.set_appearance_mode("dark")
        self.main()

    def main(self):
        self.geometry("1200x600+100+200")
        self.resizable(False, False)
        self.title("ABG")

        font_style = "Segoe UI"
        info_dict = {}
        final_total = {}
        update_dict = {}

        bottom_frame_color = "#000000"
        bottom_frame = ct.CTkFrame(master=self, width=1200, height=600, corner_radius=0,
                                   fg_color=bottom_frame_color)
        bottom_frame.pack(padx=0, pady=0)

        # Left-top frame stuff here
        left_frame_top = ct.CTkFrame(master=bottom_frame, width=250, height=100, corner_radius=10, fg_color="#121212")
        left_frame_top.place(relx=0.108, rely=0.09, anchor=tk.CENTER)

        # Middle frame
        midframe = ct.CTkFrame(master=self, width=930, height=542, fg_color="#FFFFFF", corner_radius=10,
                               bg_color="#000000")
        midframe.place(relx=0.607, rely=0.537, anchor=tk.CENTER)

        # profile stuff
        wid = 249
        hei = 100
        prof_bg_img = ct.CTkImage(Im.open("images\\image.png"), size=(wid, hei))
        prof_fg_img = ct.CTkImage(Im.open("images\\ast.jpg"), size=(65, 65))
        my_profile_bg = ct.CTkLabel(master=left_frame_top, width=wid, height=hei, corner_radius=10, image=prof_bg_img,
                                    text="")
        my_profile_bg.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Add to cart, call this everywhere
        def add_to_cart(frame_name):
            add_to_cart_button = ct.CTkButton(master=self, width=200, height=50, corner_radius=0,
                                              text="Add to cart", font=("Segoe UI Semibold", 26),
                                              fg_color="#121212", hover_color="#282828")

            match frame_name:
                case "fru_veg":
                    add_to_cart_button.configure(command=fru_frame_func)
                case "meats":
                    add_to_cart_button.configure(command=meat_func)
                case "packaged_foods":
                    add_to_cart_button.configure(command=pack_func)
                case "home_essentials":
                    add_to_cart_button.configure(command=home_ess)
                case "makeup":
                    add_to_cart_button.configure(command=makeup_func)
            return add_to_cart_button.place(relx=0.59, rely=0.938, anchor=tk.CENTER)
            # if frame_name == "fru_veg":
            #     add_to_cart_button.configure(command=fru_frame_func)
            # if frame_name == "meats":
            #     add_to_cart_button.configure(command=meat_func)
            # if frame_name == "packaged_foods":
            #     add_to_cart_button.configure(command=pack_func)
            # if frame_name == "home_essentials":
            #     add_to_cart_button.configure(command=home_ess)
            # if frame_name == "makeup":
            #     add_to_cart_button.configure(command=makeup_func)
            # return add_to_cart_button.place(relx=0.59, rely=0.938, anchor=tk.CENTER)

        def fru_frame_func():
            fruits = ['mango', 'grape', 'banana', 'apple', 'orange']

            for fruit in fruits:
                fruit_quantity = f"{fruit}_quantity"
                if hasattr(self, fruit_quantity) and getattr(self, fruit_quantity).winfo_exists():
                    quan_str = getattr(self, fruit_quantity).get()
                    if quan_str != "":
                        if int(quan_str) > 0 or quan_str.isdigit():
                            info_dict[fruit] = int(quan_str)
                    else:
                        for k in list(info_dict.keys()):
                            if k == fruit:
                                del info_dict[fruit]

            # if hasattr(self, 'grape_quantity') and self.grape_quantity.winfo_exists():
            #     gra = self.grape_quantity.get()
            #     if gra != "" and (int(gra) > 0 or gra.isdigit()):
            #         info_dict['grape'] = int(gra)
            #
            # if hasattr(self, 'banana_quantity') and self.banana_quantity.winfo_exists():
            #     ban = self.banana_quantity.get()
            #     if ban != "" and (int(ban) > 0 or ban.isdigit()):
            #         info_dict['banana'] = int(ban)
            #
            # if hasattr(self, 'apple_quantity') and self.apple_quantity.winfo_exists():
            #     apl = self.apple_quantity.get()
            #     if apl != "" and (int(apl) > 0 or apl.isdigit()):
            #         info_dict['apple'] = int(apl)
            #
            # if hasattr(self, 'orange_quantity') and self.orange_quantity.winfo_exists():
            #     ora = self.orange_quantity.get()
            #     if ora != "" and (int(ora) > 0 or ora.isdigit()):
            #         info_dict['orange'] = int(ora)

            print(info_dict)

        def meat_func():
            meat_list = ['chicken', 'mutton', 'fish', 'shrimp', 'egg']

            for meatz in meat_list:
                meatz_quantity = f"{meatz}_quantity"
                if hasattr(self, meatz_quantity) and getattr(self, meatz_quantity).winfo_exists():
                    quan_str = getattr(self, meatz_quantity).get()
                    if quan_str != "":
                        if int(quan_str) > 0 or quan_str.isdigit():
                            info_dict[meatz] = int(quan_str)
                    else:
                        for k in list(info_dict.keys()):
                            if k == meatz:
                                del info_dict[meatz]
            print(info_dict)

        def pack_func():
            packedfood_list = ['bourbon', 'dairy milk', 'gulab jamoon', 'tomato soup', 'lays']

            for fds in packedfood_list:
                packedfoods_quantity = f"{fds}_quantity"
                if hasattr(self, packedfoods_quantity) and getattr(self, packedfoods_quantity).winfo_exists():
                    quan_str = getattr(self, packedfoods_quantity).get()
                    if quan_str != "":
                        if int(quan_str) > 0 or quan_str.isdigit():
                            info_dict[fds] = int(quan_str)
                    else:
                        for k in list(info_dict.keys()):
                            if k == fds:
                                del info_dict[fds]
            print(info_dict)

        def home_ess():
            home_essen_list = ['soap', 'hand wash', 'paper towel', 'toothpaste', 'paper plate']

            for products in home_essen_list:
                product_quantity = f"{products}_quantity"
                if hasattr(self, product_quantity) and getattr(self, product_quantity).winfo_exists():
                    quan_str = getattr(self, product_quantity).get()
                    if quan_str != "":
                        if int(quan_str) > 0 or quan_str.isdigit():
                            info_dict[products] = int(quan_str)
                    else:
                        for k in list(info_dict.keys()):
                            if k == products:
                                del info_dict[products]
            print(info_dict)

        def makeup_func():
            makeup_list = ['blush', 'foundation', 'lipstick', 'mascara', 'perfume']

            for tube in makeup_list:
                tube_quantity = f"{tube}_quantity"
                if hasattr(self, tube_quantity) and getattr(self, tube_quantity).winfo_exists():
                    quan_str = getattr(self, tube_quantity).get()
                    if quan_str != "":
                        if int(quan_str) > 0 or quan_str.isdigit():
                            info_dict[tube] = int(quan_str)
                    else:
                        for k in list(info_dict.keys()):
                            if k == tube:
                                del info_dict[tube]
            print(info_dict)



        def my_profile():
            profile_frame = ct.CTkFrame(master=self, width=930, height=542, fg_color="#000000", corner_radius=10,
                                        bg_color="#000000")
            profile_frame.place(relx=0.607, rely=0.537, anchor=tk.CENTER)

            # Profile stuff

        my_profile_fg = ct.CTkButton(master=my_profile_bg, width=65, height=65, corner_radius=0, image=prof_fg_img,
                                     text="", border_spacing=0, border_width=0, fg_color="#000000",
                                     hover_color="#4555AC", command=my_profile)
        my_profile_fg.place(relx=0.2, rely=0.55, anchor=tk.CENTER)

        # Left_bot frame stuff
        the_background_grey = "#000000"
        left_frame_bot = ct.CTkFrame(master=bottom_frame, width=250, height=487, corner_radius=0,
                                     fg_color=the_background_grey)
        left_frame_bot.place(relx=0.108, rely=0.586, anchor=tk.CENTER)

        # Fruits & Vegetables side stuff
        def fruveg():
            if hasattr(self, 'fru_frame') and self.fru_frame.winfo_exists():
                self.fru_frame.destroy()

            xaxe = 0.12
            minus_placement_x = 0.058
            plus_placement_x = 0.181
            text_box_placement_x = 0.12
            # name_list = ["Mango", "Grapes", "Banana", "Apple", "Orange"]
            # image_list = ["mango.png", "grapes.png", "banana.png", "apple.png", "orange.png"]
            # price_list = [40, 50, 60, 70, 80]
            # namelabel_dict = {}
            # imagelabel_dict = {}
            # bgcolor = "#181818"

            self.fru_frame = ct.CTkFrame(master=self, width=930, height=542, fg_color="#121212", corner_radius=10,
                                    bg_color="#000000")
            self.fru_frame.place(relx=0.607, rely=0.537, anchor=tk.CENTER)

            # for name, image, price in zip(name_list, image_list, price_list):
            #     imagelabel_dict[f"{name}_img"] = ct.CTkImage(Im.open(f"images\\fruvegss\\{image}"), size=(150, 150))
            #     namelabel_dict[f"{name}_label"] = ct.CTkLabel(master=fru_frame, width=150, height=150, fg_color=bgcolor, text="", image=imagelabel_dict[f"{name}_img"])
            #     namelabel_dict[f"{name}_label"].place(relx=xaxe, rely=0.19, anchor=tk.CENTER)
            #     namelabel_dict[f"{name}_text"] = ct.CTkLabel(master=fru_frame, width=150, height=50, text=f"{name}\n₹{price}/kg", font=("Normal", 18),
            #                          bg_color="#000000")
            #     namelabel_dict[f"{name}_text"].place(relx=xaxe, rely=0.38, anchor=tk.CENTER)
            #     namelabel_dict[f"{name}_minus"] = ct.CTkButton(master=fru_frame, width=35, height=40, text="-", font=("Normal", 18),
            #                                fg_color="#121212", hover_color="#FF2B2B")
            #     namelabel_dict[f"{name}_minus"].place(relx=minus_placement_x, rely=0.47, anchor=tk.CENTER)
            #     namelabel_dict[f"{name}_plus"] = ct.CTkButton(master=fru_frame, width=35, height=40, text="+", font=("Normal", 18),
            #                               fg_color="#121212", command=onclickplus)
            #     namelabel_dict[f"{name}_plus"].place(relx=plus_placement_x, rely=0.47, anchor=tk.CENTER)
            #     namelabel_dict[f"{name}_quantity"] = ct.CTkEntry(master=fru_frame, width=65, height=40, state="disabled", justify="center", font=("normal", 24))
            #     namelabel_dict[f"{name}_quantity"].place(relx=text_box_placement_x, rely=0.47, anchor=tk.CENTER)
            #     xaxe += 0.19
            #     minus_placement_x += 0.19
            #     plus_placement_x += 0.19
            #     text_box_placement_x += 0.19

            def create_fruit_widgets(fruit_name, image_path):
                current_num = 0
                for key in info_dict:
                    if fruit_name.lower() == key:
                        current_num = info_dict.get(key)

                def onclick_minus():
                    nonlocal current_num
                    if current_num > 0:
                        current_num -= 1
                        entry.configure(state="normal")
                        entry.delete(0, "end")
                        entry.insert(0, current_num)
                        entry.configure(state="disabled")
                        if current_num == 0:
                            entry.configure(state="normal")
                            entry.delete(0, "end")
                            entry.configure(state="disabled")

                def onclick_plus():
                    nonlocal current_num
                    if current_num < 15:
                        current_num += 1
                        entry.configure(state="normal")
                        entry.delete(0, "end")
                        entry.insert(0, current_num)
                        entry.configure(state="disabled")

                def update_quantity():
                    for ke in info_dict:
                        if fruit_name.lower() == ke:
                            entry.configure(state="normal")
                            entry.delete(0, "end")
                            entry.insert(0, info_dict.get(ke))
                            entry.configure(state="disabled")

                img = ct.CTkImage(Im.open(image_path), size=(150, 150))
                text = ct.CTkLabel(master=self.fru_frame, width=150, height=50,
                                   text=f"{fruit_name}\n₹{mybackend.item_list(fruit_name.lower())}/kg",
                                   font=(font_style, 18), bg_color="#000000")
                text.place(relx=xaxe, rely=0.38, anchor=tk.CENTER)
                minus_button = ct.CTkButton(master=self.fru_frame, width=35, height=40, text="-", font=(font_style, 18),
                                            fg_color="#121212", hover_color="#FF2B2B", command=onclick_minus)
                minus_button.place(relx=minus_placement_x, rely=0.47, anchor=tk.CENTER)
                plus_button = ct.CTkButton(master=self.fru_frame, width=35, height=40, text="+", font=(font_style, 18),
                                           fg_color="#121212", command=onclick_plus)
                plus_button.place(relx=plus_placement_x, rely=0.47, anchor=tk.CENTER)
                label = ct.CTkLabel(master=self.fru_frame, width=150, height=150, fg_color="#181818", text="",
                                    image=img)
                label.place(relx=xaxe, rely=0.19, anchor=tk.CENTER)
                entry = ct.CTkEntry(master=self.fru_frame, width=65, height=40, state="disabled", justify="center",
                                    font=("normal", 24), border_width=0, corner_radius=0)
                entry.place(relx=text_box_placement_x, rely=0.47, anchor=tk.CENTER)
                update_quantity()

                return current_num, entry

            fruits = [
                {"name": "Mango", "image_path": "images\\fruvegss\\mango_fixed.jpg"},
                {"name": "Grape", "image_path": "images\\fruvegss\\grapes_fixed.png"},
                {"name": "Banana", "image_path": "images\\fruvegss\\banana_fixed.png"},
                {"name": "Apple", "image_path": "images\\fruvegss\\apple_fixed.png"},
                {"name": "Orange", "image_path": "images\\fruvegss\\orange_fixed.png"}
            ]

            # Create widgets for each fruit
            for fruit in fruits:
                current_num, quantity_entry = create_fruit_widgets(fruit["name"], fruit["image_path"])
                setattr(self, f"current_num_{fruit['name'].lower()}", current_num)
                setattr(self, f"{fruit['name'].lower()}_quantity", quantity_entry)

                xaxe += 0.19
                minus_placement_x += 0.19
                plus_placement_x += 0.19
                text_box_placement_x += 0.19

            add_to_cart("fru_veg")
            # -----------------------------------------------------------------------
            # self.current_num_mango = 0
            # def mango_onclickminus():
            #     if self.current_num_mango > 0:
            #         self.current_num_mango -= 1
            #         self.mango_quantity.configure(state="normal")
            #         self.mango_quantity.delete(0, "end")
            #         self.mango_quantity.insert(0, self.current_num_mango)
            #         self.mango_quantity.configure(state="disabled")
            #         if self.current_num_mango == 0:
            #             self.mango_quantity.configure(state="normal")
            #             self.mango_quantity.delete(0, "end")
            #             self.mango_quantity.configure(state="disabled")
            #
            # def mango_onclickplus():
            #     if self.current_num_mango < 15:
            #         self.current_num_mango += 1
            #         self.mango_quantity.configure(state="normal")
            #         self.mango_quantity.delete(0, "end")
            #         self.mango_quantity.insert(0, self.current_num_mango)
            #         self.mango_quantity.configure(state="disabled")
            #
            # mango_img = ct.CTkImage(Im.open("images\\fruvegss\\mango_fixed.jpg"), size=(150, 150))
            # mangoes_label = ct.CTkLabel(master=self.fru_frame, width=150, height=150, fg_color="#181818", text="",
            #                             image=mango_img)
            # mangoes_label.place(relx=xaxe, rely=0.19, anchor=tk.CENTER)
            # mango_text = ct.CTkLabel(master=self.fru_frame, width=150, height=50, text="Mango\n₹40/kg", font=(font_style, 18),
            #                          bg_color="#000000")
            # mango_text.place(relx=xaxe, rely=0.38, anchor=tk.CENTER)
            # mango_minus = ct.CTkButton(master=self.fru_frame, width=35, height=40, text="-", font=(font_style, 18),
            #                            fg_color="#121212", hover_color="#FF2B2B", command=mango_onclickminus)
            # mango_minus.place(relx=minus_placement_x, rely=0.47, anchor=tk.CENTER)
            # mango_plus = ct.CTkButton(master=self.fru_frame, width=35, height=40, text="+", font=(font_style, 18),
            #                           fg_color="#121212", command=mango_onclickplus)
            # mango_plus.place(relx=plus_placement_x, rely=0.47, anchor=tk.CENTER)
            # self.mango_quantity = ct.CTkEntry(master=self.fru_frame, width=65, height=40, state="disabled",
            #                              justify="center", font=("normal", 24), border_width=0,
            #                              corner_radius=0)
            # self.mango_quantity.place(relx=text_box_placement_x, rely=0.47, anchor=tk.CENTER)
            # xaxe += 0.19
            # minus_placement_x += 0.19
            # plus_placement_x += 0.19
            # text_box_placement_x += 0.19
            #
            #
            #
            # self.current_num_grape = 0
            #
            # def grape_onclickminus():
            #     if self.current_num_grape > 0:
            #         self.current_num_grape -= 1
            #         self.grape_quantity.configure(state="normal")
            #         self.grape_quantity.delete(0, "end")
            #         self.grape_quantity.insert(0, self.current_num_grape)
            #         self.grape_quantity.configure(state="disabled")
            #         if self.current_num_grape == 0:
            #             self.grape_quantity.configure(state="normal")
            #             self.grape_quantity.delete(0, "end")
            #             self.grape_quantity.configure(state="disabled")
            #
            # def grape_onclickplus():
            #     if self.current_num_grape < 15:
            #         self.current_num_grape += 1
            #         self.grape_quantity.configure(state="normal")
            #         self.grape_quantity.delete(0, "end")
            #         self.grape_quantity.insert(0, self.current_num_grape)
            #         self.grape_quantity.configure(state="disabled")
            #
            # grape_img = ct.CTkImage(Im.open("images\\fruvegss\\grapes_fixed.png"), size=(150, 150))
            # grape_text = ct.CTkLabel(master=self.fru_frame, width=150, height=50, text="Grapes\n₹20/kg", font=(font_style, 18),
            #                          bg_color="#000000")
            # grape_text.place(relx=xaxe, rely=0.38, anchor=tk.CENTER)
            # grape_minus = ct.CTkButton(master=self.fru_frame, width=35, height=40, text="-", font=(font_style, 18),
            #                            fg_color="#121212", hover_color="#FF2B2B", command=grape_onclickminus)
            # grape_minus.place(relx=minus_placement_x, rely=0.47, anchor=tk.CENTER)
            # grape_plus = ct.CTkButton(master=self.fru_frame, width=35, height=40, text="+", font=(font_style, 18),
            #                           fg_color="#121212", command=grape_onclickplus)
            # grape_plus.place(relx=plus_placement_x, rely=0.47, anchor=tk.CENTER)
            # grape_label = ct.CTkLabel(master=self.fru_frame, width=150, height=150, fg_color="#181818", text="",
            #                            image=grape_img)
            # grape_label.place(relx=xaxe, rely=0.19, anchor=tk.CENTER)
            # self.grape_quantity = ct.CTkEntry(master=self.fru_frame, width=65, height=40, state="disabled",
            #                              justify="center", font=("normal", 24), border_width=0,
            #                              corner_radius=0)
            # self.grape_quantity.place(relx=text_box_placement_x, rely=0.47, anchor=tk.CENTER)
            # xaxe += 0.19
            # minus_placement_x += 0.19
            # plus_placement_x += 0.19
            # text_box_placement_x += 0.19
            #
            # self.current_num_banana = 0
            #
            # def banana_onclickminus():
            #     if self.current_num_banana > 0:
            #         self.current_num_banana -= 1
            #         self.banana_quantity.configure(state="normal")
            #         self.banana_quantity.delete(0, "end")
            #         self.banana_quantity.insert(0, self.current_num_banana)
            #         self.banana_quantity.configure(state="disabled")
            #         if self.current_num_banana == 0:
            #             self.banana_quantity.configure(state="normal")
            #             self.banana_quantity.delete(0, "end")
            #             self.banana_quantity.configure(state="disabled")
            #
            # def banana_onclickplus():
            #     if self.current_num_banana < 15:
            #         self.current_num_banana += 1
            #         self.banana_quantity.configure(state="normal")
            #         self.banana_quantity.delete(0, "end")
            #         self.banana_quantity.insert(0, self.current_num_banana)
            #         self.banana_quantity.configure(state="disabled")
            #
            # banana_img = ct.CTkImage(Im.open("images\\fruvegss\\banana_fixed.png"), size=(150, 150))
            # banana_text = ct.CTkLabel(master=self.fru_frame, width=150, height=50, text="Banana\n₹70/kg",
            #                           font=(font_style, 18),
            #                           bg_color="#000000")
            # banana_text.place(relx=xaxe, rely=0.38, anchor=tk.CENTER)
            # banana_minus = ct.CTkButton(master=self.fru_frame, width=35, height=40, text="-", font=(font_style, 18),
            #                             fg_color="#121212", hover_color="#FF2B2B", command=banana_onclickminus)
            # banana_minus.place(relx=minus_placement_x, rely=0.47, anchor=tk.CENTER)
            # banana_plus = ct.CTkButton(master=self.fru_frame, width=35, height=40, text="+", font=(font_style, 18),
            #                            fg_color="#121212", command=banana_onclickplus)
            # banana_plus.place(relx=plus_placement_x, rely=0.47, anchor=tk.CENTER)
            # banana_label = ct.CTkLabel(master=self.fru_frame, width=150, height=150, fg_color="#181818", text="",
            #                            image=banana_img)
            # banana_label.place(relx=xaxe, rely=0.19, anchor=tk.CENTER)
            # self.banana_quantity = ct.CTkEntry(master=self.fru_frame, width=65, height=40, state="disabled",
            #                              justify="center", font=("normal", 24), border_width=0,
            #                              corner_radius=0)
            # self.banana_quantity.place(relx=text_box_placement_x, rely=0.47, anchor=tk.CENTER)
            # xaxe += 0.19
            # minus_placement_x += 0.19
            # plus_placement_x += 0.19
            # text_box_placement_x += 0.19
            #
            #
            #
            # self.current_num_apple = 0
            #
            # def apple_onclickminus():
            #     if self.current_num_apple > 0:
            #         self.current_num_apple -= 1
            #         self.apple_quantity.configure(state="normal")
            #         self.apple_quantity.delete(0, "end")
            #         self.apple_quantity.insert(0, self.current_num_apple)
            #         self.apple_quantity.configure(state="disabled")
            #         if self.current_num_apple == 0:
            #             self.apple_quantity.configure(state="normal")
            #             self.apple_quantity.delete(0, "end")
            #             self.apple_quantity.configure(state="disabled")
            #
            # def apple_onclickplus():
            #     if self.current_num_apple < 15:
            #         self.current_num_apple += 1
            #         self.apple_quantity.configure(state="normal")
            #         self.apple_quantity.delete(0, "end")
            #         self.apple_quantity.insert(0, self.current_num_apple)
            #         self.apple_quantity.configure(state="disabled")
            #
            # apple_img = ct.CTkImage(Im.open("images\\fruvegss\\apple_fixed.png"), size=(150, 150))
            # apple_text = ct.CTkLabel(master=self.fru_frame, width=150, height=50, text="Apple\n₹35/kg",
            #                          font=(font_style, 18),
            #                          bg_color="#000000")
            # apple_text.place(relx=xaxe, rely=0.38, anchor=tk.CENTER)
            # apple_minus = ct.CTkButton(master=self.fru_frame, width=35, height=40, text="-", font=(font_style, 18),
            #                            fg_color="#121212", hover_color="#FF2B2B", command=apple_onclickminus)
            # apple_minus.place(relx=minus_placement_x, rely=0.47, anchor=tk.CENTER)
            # apple_plus = ct.CTkButton(master=self.fru_frame, width=35, height=40, text="+", font=(font_style, 18),
            #                           fg_color="#121212", command=apple_onclickplus)
            # apple_plus.place(relx=plus_placement_x, rely=0.47, anchor=tk.CENTER)
            # apple_label = ct.CTkLabel(master=self.fru_frame, width=150, height=150, fg_color="#181818", text="",
            #                           image=apple_img)
            # apple_label.place(relx=xaxe, rely=0.19, anchor=tk.CENTER)
            # self.apple_quantity = ct.CTkEntry(master=self.fru_frame, width=65, height=40, state="disabled",
            #                               justify="center", font=("normal", 24), border_width=0,
            #                               corner_radius=0)
            # self.apple_quantity.place(relx=text_box_placement_x, rely=0.47, anchor=tk.CENTER)
            # xaxe += 0.19
            # minus_placement_x += 0.19
            # plus_placement_x += 0.19
            # text_box_placement_x += 0.19
            #
            #
            #
            #
            #
            # self.current_num_orange = 0
            #
            # def orange_onclickminus():
            #     if self.current_num_orange > 0:
            #         self.current_num_orange -= 1
            #         self.orange_quantity.configure(state="normal")
            #         self.orange_quantity.delete(0, "end")
            #         self.orange_quantity.insert(0, self.current_num_orange)
            #         self.orange_quantity.configure(state="disabled")
            #         if self.current_num_orange == 0:
            #             self.orange_quantity.configure(state="normal")
            #             self.orange_quantity.delete(0, "end")
            #             self.orange_quantity.configure(state="disabled")
            #
            # def orange_onclickplus():
            #     if self.current_num_orange < 15:
            #         self.current_num_orange += 1
            #         self.orange_quantity.configure(state="normal")
            #         self.orange_quantity.delete(0, "end")
            #         self.orange_quantity.insert(0, self.current_num_orange)
            #         self.orange_quantity.configure(state="disabled")
            #
            # orange_img = ct.CTkImage(Im.open("images\\fruvegss\\orange_fixed.png"), size=(150, 150))
            # orange_text = ct.CTkLabel(master=self.fru_frame, width=150, height=50, text="Orange\n₹80/kg",
            #                           font=(font_style, 18),
            #                           bg_color="#000000")
            # orange_text.place(relx=xaxe, rely=0.38, anchor=tk.CENTER)
            # orange_minus = ct.CTkButton(master=self.fru_frame, width=35, height=40, text="-", font=(font_style, 18),
            #                             fg_color="#121212", hover_color="#FF2B2B", command=orange_onclickminus)
            # orange_minus.place(relx=minus_placement_x, rely=0.47, anchor=tk.CENTER)
            # orange_plus = ct.CTkButton(master=self.fru_frame, width=35, height=40, text="+", font=(font_style, 18),
            #                            fg_color="#121212", command=orange_onclickplus)
            # orange_plus.place(relx=plus_placement_x, rely=0.47, anchor=tk.CENTER)
            # orange_label = ct.CTkLabel(master=self.fru_frame, width=150, height=150, fg_color="#181818", text="",
            #                            image=orange_img)
            # orange_label.place(relx=xaxe, rely=0.19, anchor=tk.CENTER)
            # self.orange_quantity = ct.CTkEntry(master=self.fru_frame, width=65, height=40, state="disabled",
            #                              justify="center", font=("normal", 24), border_width=0,
            #                              corner_radius=0)
            # self.orange_quantity.place(relx=text_box_placement_x, rely=0.47, anchor=tk.CENTER)

        fru_veg_img = ct.CTkImage(Im.open("images\\fnl_fruvegs.png"), size=(240, 80))
        fru_veg = ct.CTkButton(master=left_frame_bot, width=250, height=70, corner_radius=10, text="",
                               fg_color=the_background_grey, hover_color="#282828", image=fru_veg_img,
                               border_spacing=0, command=fruveg)
        fru_veg.place(relx=0.5, rely=0.09, anchor=tk.CENTER)
        # Meats side stuff
        def meats():
            if hasattr(self, 'meat_frame') and self.meat_frame.winfo_exists():
                self.meat_frame.destroy()

            xaxe = 0.12
            minus_placement_x = 0.058
            plus_placement_x = 0.181
            text_box_placement_x = 0.12

            self.meat_frame = ct.CTkFrame(master=self, width=930, height=542, fg_color="#121212", corner_radius=10,
                                    bg_color="#000000")
            self.meat_frame.place(relx=0.607, rely=0.537, anchor=tk.CENTER)

            def create_meats_widgets(meat_name, image_path):
                current_num = 0
                for key in info_dict:
                    if meat_name.lower() == key:
                        current_num = info_dict.get(key)

                def onclick_minus():
                    nonlocal current_num
                    if current_num > 0:
                        current_num -= 1
                        entry.configure(state="normal")
                        entry.delete(0, "end")
                        entry.insert(0, current_num)
                        entry.configure(state="disabled")
                        if current_num == 0:
                            entry.configure(state="normal")
                            entry.delete(0, "end")
                            entry.configure(state="disabled")

                def onclick_plus():
                    nonlocal current_num
                    if current_num < 15:
                        current_num += 1
                        entry.configure(state="normal")
                        entry.delete(0, "end")
                        entry.insert(0, current_num)
                        entry.configure(state="disabled")

                def update_quantity():
                    for ke in info_dict:
                        if meat_name.lower() == ke:
                            entry.configure(state="normal")
                            entry.delete(0, "end")
                            entry.insert(0, info_dict.get(ke))
                            entry.configure(state="disabled")

                img = ct.CTkImage(Im.open(image_path), size=(150, 150))
                text = ct.CTkLabel(master=self.meat_frame, width=150, height=50,
                                   text=f"{meat_name}\n₹{mybackend.item_list(meat_name.lower())}/ 10 pcs" if meat_name.lower() == "egg" else f"{meat_name}\n₹{mybackend.item_list(meat_name.lower())}/kg",
                                   font=(font_style, 18), bg_color="#000000")
                text.place(relx=xaxe, rely=0.38, anchor=tk.CENTER)
                minus_button = ct.CTkButton(master=self.meat_frame, width=35, height=40, text="-", font=(font_style, 18),
                                            fg_color="#121212", hover_color="#FF2B2B", command=onclick_minus)
                minus_button.place(relx=minus_placement_x, rely=0.47, anchor=tk.CENTER)
                plus_button = ct.CTkButton(master=self.meat_frame, width=35, height=40, text="+", font=(font_style, 18),
                                           fg_color="#121212", command=onclick_plus)
                plus_button.place(relx=plus_placement_x, rely=0.47, anchor=tk.CENTER)
                label = ct.CTkLabel(master=self.meat_frame, width=150, height=150, fg_color="#181818", text="",
                                    image=img)
                label.place(relx=xaxe, rely=0.19, anchor=tk.CENTER)
                entry = ct.CTkEntry(master=self.meat_frame, width=65, height=40, state="disabled", justify="center",
                                    font=("normal", 24), border_width=0, corner_radius=0)
                entry.place(relx=text_box_placement_x, rely=0.47, anchor=tk.CENTER)
                update_quantity()

                return current_num, entry

            # Define fruits
            meats_info = [
                {"name": "Chicken", "image_path": "images\\meats\\chicken_fixed.png"},
                {"name": "Mutton", "image_path": "images\\meats\\mutton_fixed.png"},
                {"name": "Fish", "image_path": "images\\meats\\fish_fixed.png"},
                {"name": "Shrimp", "image_path": "images\\meats\\shrimps_fixed.png"},
                {"name": "Egg", "image_path": "images\\meats\\eggs_fixed.png"}
            ]

            # Create widgets for each fruit
            for meatss in meats_info:
                current_num, quantity_entry = create_meats_widgets(meatss["name"], meatss["image_path"])
                setattr(self, f"current_num_{meatss['name'].lower()}", current_num)
                setattr(self, f"{meatss['name'].lower()}_quantity", quantity_entry)

                xaxe += 0.19
                minus_placement_x += 0.19
                plus_placement_x += 0.19
                text_box_placement_x += 0.19

            add_to_cart("meats")

        meat_img = ct.CTkImage(Im.open("images\\meats.jpg"), size=(240, 80))
        meat = ct.CTkButton(master=left_frame_bot, width=250, height=70, corner_radius=10, text="",
                            fg_color=the_background_grey, hover_color="#282828", image=meat_img,
                            border_spacing=0, command=meats)
        meat.place(relx=0.5, rely=0.27, anchor=tk.CENTER)

        # Packaged Food side stuff
        def packfoods():
            if hasattr(self, 'packfood_frame') and self.packfood_frame.winfo_exists():
                self.packfood_frame.destroy()

            xaxe = 0.12
            minus_placement_x = 0.058
            plus_placement_x = 0.181
            text_box_placement_x = 0.12

            self.packfood_frame = ct.CTkFrame(master=self, width=930, height=542, fg_color="#121212", corner_radius=10,
                                         bg_color="#000000")
            self.packfood_frame.place(relx=0.607, rely=0.537, anchor=tk.CENTER)

            def create_packfoods_widgets(packaged_name, image_path):
                current_num = 0
                for key in info_dict:
                    if packaged_name.lower() == key:
                        current_num = info_dict.get(key)

                def onclick_minus():
                    nonlocal current_num
                    if current_num > 0:
                        current_num -= 1
                        entry.configure(state="normal")
                        entry.delete(0, "end")
                        entry.insert(0, current_num)
                        entry.configure(state="disabled")
                        if current_num == 0:
                            entry.configure(state="normal")
                            entry.delete(0, "end")
                            entry.configure(state="disabled")

                def onclick_plus():
                    nonlocal current_num
                    if current_num < 15:
                        current_num += 1
                        entry.configure(state="normal")
                        entry.delete(0, "end")
                        entry.insert(0, current_num)
                        entry.configure(state="disabled")

                def update_quantity():
                    for ke in info_dict:
                        if packaged_name.lower() == ke:
                            entry.configure(state="normal")
                            entry.delete(0, "end")
                            entry.insert(0, info_dict.get(ke))
                            entry.configure(state="disabled")

                img = ct.CTkImage(Im.open(image_path), size=(150, 150))
                text = ct.CTkLabel(master=self.packfood_frame, width=150, height=50,
                                   text=f"{packaged_name}\n₹{mybackend.item_list(packaged_name.lower())}",
                                   font=(font_style, 18), bg_color="#000000")
                text.place(relx=xaxe, rely=0.38, anchor=tk.CENTER)
                minus_button = ct.CTkButton(master=self.packfood_frame, width=35, height=40, text="-", font=(font_style, 18),
                                            fg_color="#121212", hover_color="#FF2B2B", command=onclick_minus)
                minus_button.place(relx=minus_placement_x, rely=0.47, anchor=tk.CENTER)
                plus_button = ct.CTkButton(master=self.packfood_frame, width=35, height=40, text="+", font=(font_style, 18),
                                           fg_color="#121212", command=onclick_plus)
                plus_button.place(relx=plus_placement_x, rely=0.47, anchor=tk.CENTER)
                label = ct.CTkLabel(master=self.packfood_frame, width=150, height=150, fg_color="#181818", text="",
                                    image=img)
                label.place(relx=xaxe, rely=0.19, anchor=tk.CENTER)
                entry = ct.CTkEntry(master=self.packfood_frame, width=65, height=40, state="disabled", justify="center",
                                    font=("normal", 24), border_width=0, corner_radius=0)
                entry.place(relx=text_box_placement_x, rely=0.47, anchor=tk.CENTER)
                update_quantity()

                return current_num, entry

            packed_foods_info = [
                {"name": "Bourbon", "image_path": "images\\packaged_foods\\bourbon_fixed.png",},
                {"name": "Dairy Milk", "image_path": "images\\packaged_foods\\dm_fixed.png",},
                {"name": "Gulab Jamoon", "image_path": "images\\packaged_foods\\gj_fixed.png",},
                {"name": "Tomato Soup", "image_path": "images\\packaged_foods\\ks_fixed.png",},
                {"name": "Lays", "image_path": "images\\packaged_foods\\lays_fixed.png",}
            ]

            # Create widgets for each fruit
            for foods in packed_foods_info:
                current_num, quantity_entry = create_packfoods_widgets(foods["name"], foods["image_path"])
                setattr(self, f"current_num_{foods['name'].lower()}", current_num)
                setattr(self, f"{foods['name'].lower()}_quantity", quantity_entry)

                xaxe += 0.19
                minus_placement_x += 0.19
                plus_placement_x += 0.19
                text_box_placement_x += 0.19

            add_to_cart("packaged_foods")

        packaged_img = ct.CTkImage(Im.open("images\\packaged.png"), size=(240, 80))
        packaged_foods = ct.CTkButton(master=left_frame_bot, width=250, height=70, corner_radius=10, text="",
                                      fg_color=the_background_grey, hover_color="#282828", image=packaged_img,
                                      border_spacing=0, command=packfoods)
        packaged_foods.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        def home_essen():
            if hasattr(self, 'home_essentials_frame') and self.home_essentials_frame.winfo_exists():
                self.home_essentials_frame.destroy()

            xaxe = 0.12
            minus_placement_x = 0.058
            plus_placement_x = 0.181
            text_box_placement_x = 0.12

            self.home_essentials_frame = ct.CTkFrame(master=self, width=930, height=542, fg_color="#121212",
                                                corner_radius=10,
                                                bg_color="#000000")
            self.home_essentials_frame.place(relx=0.607, rely=0.537, anchor=tk.CENTER)

            def create_home_essentials_widgets(packaged_name, image_path):
                current_num = 0
                for key in info_dict:
                    if packaged_name.lower() == key:
                        current_num = info_dict.get(key)

                def onclick_minus():
                    nonlocal current_num
                    if current_num > 0:
                        current_num -= 1
                        entry.configure(state="normal")
                        entry.delete(0, "end")
                        entry.insert(0, current_num)
                        entry.configure(state="disabled")
                        if current_num == 0:
                            entry.configure(state="normal")
                            entry.delete(0, "end")
                            entry.configure(state="disabled")

                def onclick_plus():
                    nonlocal current_num
                    if current_num < 15:
                        current_num += 1
                        entry.configure(state="normal")
                        entry.delete(0, "end")
                        entry.insert(0, current_num)
                        entry.configure(state="disabled")

                def update_quantity():
                    for ke in info_dict:
                        if packaged_name.lower() == ke:
                            entry.configure(state="normal")
                            entry.delete(0, "end")
                            entry.insert(0, info_dict.get(ke))
                            entry.configure(state="disabled")

                img = ct.CTkImage(Im.open(image_path), size=(150, 150))
                text = ct.CTkLabel(master=self.home_essentials_frame, width=150, height=50,
                                   text=f"{packaged_name}\n₹{mybackend.item_list(packaged_name.lower())}/125 g" if packaged_name.lower() == "soap"
                                   else f"{packaged_name}\n₹{mybackend.item_list(packaged_name.lower())}/250 ml" if packaged_name.lower() == "hand wash"
                                   else f"{packaged_name}\n₹{mybackend.item_list(packaged_name.lower())}/200 pieces" if packaged_name.lower() == "paper towel"
                                   else f"{packaged_name}\n₹{mybackend.item_list(packaged_name.lower())}/200 g" if packaged_name.lower() == "toothpaste"
                                   else f"{packaged_name}\n₹{mybackend.item_list(packaged_name.lower())}/10 pieces",
                                   font=(font_style, 18), bg_color="#000000")
                text.place(relx=xaxe, rely=0.38, anchor=tk.CENTER)
                minus_button = ct.CTkButton(master=self.home_essentials_frame, width=35, height=40, text="-", font=(font_style, 18),
                                            fg_color="#121212", hover_color="#FF2B2B", command=onclick_minus)
                minus_button.place(relx=minus_placement_x, rely=0.47, anchor=tk.CENTER)
                plus_button = ct.CTkButton(master=self.home_essentials_frame, width=35, height=40, text="+", font=(font_style, 18),
                                           fg_color="#121212", command=onclick_plus)
                plus_button.place(relx=plus_placement_x, rely=0.47, anchor=tk.CENTER)
                label = ct.CTkLabel(master=self.home_essentials_frame, width=150, height=150, fg_color="#181818", text="",
                                    image=img)
                label.place(relx=xaxe, rely=0.19, anchor=tk.CENTER)
                entry = ct.CTkEntry(master=self.home_essentials_frame, width=65, height=40, state="disabled", justify="center",
                                    font=("normal", 24), border_width=0, corner_radius=0)
                entry.place(relx=text_box_placement_x, rely=0.47, anchor=tk.CENTER)
                update_quantity()

                return current_num, entry

            home_products_info = [
                {"name": "Soap", "image_path": "images\\home_essentials\\dove_fixed.png"},
                {"name": "Hand Wash", "image_path": "images\\home_essentials\\handwash_fixed.png"},
                {"name": "Paper Towel", "image_path": "images\\home_essentials\\paper_towels_fixed.png"},
                {"name": "Toothpaste", "image_path": "images\\home_essentials\\toothpaste_fixed.png"},
                {"name": "Paper Plate", "image_path": "images\\home_essentials\\paper_plates_fixed.png"}
            ]

            for product in home_products_info:
                current_num, quantity_entry = create_home_essentials_widgets(product["name"], product["image_path"])
                setattr(self, f"current_num_{product['name'].lower()}", current_num)
                setattr(self, f"{product['name'].lower()}_quantity", quantity_entry)

                xaxe += 0.19
                minus_placement_x += 0.19
                plus_placement_x += 0.19
                text_box_placement_x += 0.19

            add_to_cart("home_essentials")

        # Home Essentials side stuff
        home_img = ct.CTkImage(Im.open("images\\home.png"), size=(240, 80))
        home_essentials = ct.CTkButton(master=left_frame_bot, width=250, height=70, corner_radius=10, text="",
                                       fg_color=the_background_grey, hover_color="#282828", image=home_img,
                                       border_spacing=0, command=home_essen)
        home_essentials.place(relx=0.5, rely=0.63, anchor=tk.CENTER)

        # Makeup and Bodycare side stuff
        def makeup():
            if hasattr(self, 'makeup_frame') and self.makeup_frame.winfo_exists():
                self.makeup_frame.destroy()

            xaxe = 0.12
            minus_placement_x = 0.058
            plus_placement_x = 0.181
            text_box_placement_x = 0.12

            self.makeup_frame = ct.CTkFrame(master=self, width=930, height=542, fg_color="#121212", corner_radius=10,
                                       bg_color="#000000")
            self.makeup_frame.place(relx=0.607, rely=0.537, anchor=tk.CENTER)

            def create_makeup_widgets(packaged_name, image_path):
                current_num = 0
                for key in info_dict:
                    if packaged_name.lower() == key:
                        current_num = info_dict.get(key)

                def onclick_minus():
                    nonlocal current_num
                    if current_num > 0:
                        current_num -= 1
                        entry.configure(state="normal")
                        entry.delete(0, "end")
                        entry.insert(0, current_num)
                        entry.configure(state="disabled")
                        if current_num == 0:
                            entry.configure(state="normal")
                            entry.delete(0, "end")
                            entry.configure(state="disabled")

                def onclick_plus():
                    nonlocal current_num
                    if current_num < 15:
                        current_num += 1
                        entry.configure(state="normal")
                        entry.delete(0, "end")
                        entry.insert(0, current_num)
                        entry.configure(state="disabled")

                def update_quantity():
                    for ke in info_dict:
                        if packaged_name.lower() == ke:
                            entry.configure(state="normal")
                            entry.delete(0, "end")
                            entry.insert(0, info_dict.get(ke))
                            entry.configure(state="disabled")


                img = ct.CTkImage(Im.open(image_path), size=(150, 150))
                text = ct.CTkLabel(master=self.makeup_frame, width=150, height=50,
                                   text=f"{packaged_name}\n₹{mybackend.item_list(packaged_name.lower())}/1.5 ml" if packaged_name.lower() == "blush"
                                   else f"{packaged_name}\n₹{mybackend.item_list(packaged_name.lower())}/15 ml" if packaged_name.lower() == "foundation"
                                   else f"{packaged_name}\n₹{mybackend.item_list(packaged_name.lower())}/3.6 g" if packaged_name.lower() == "lipstick"
                                   else f"{packaged_name}\n₹{mybackend.item_list(packaged_name.lower())}/9 ml" if packaged_name.lower() == "mascara"
                                   else f"{packaged_name}\n₹{mybackend.item_list(packaged_name.lower())}/100 ml",
                                   font=(font_style, 18), bg_color="#000000")
                text.place(relx=xaxe, rely=0.38, anchor=tk.CENTER)
                minus_button = ct.CTkButton(master=self.makeup_frame, width=35, height=40, text="-",
                                            font=(font_style, 18),
                                            fg_color="#121212", hover_color="#FF2B2B", command=onclick_minus)
                minus_button.place(relx=minus_placement_x, rely=0.47, anchor=tk.CENTER)
                plus_button = ct.CTkButton(master=self.makeup_frame, width=35, height=40, text="+",
                                           font=(font_style, 18),
                                           fg_color="#121212", command=onclick_plus)
                plus_button.place(relx=plus_placement_x, rely=0.47, anchor=tk.CENTER)
                label = ct.CTkLabel(master=self.makeup_frame, width=150, height=150, fg_color="#181818", text="",
                                    image=img)
                label.place(relx=xaxe, rely=0.19, anchor=tk.CENTER)
                entry = ct.CTkEntry(master=self.makeup_frame, width=65, height=40, state="disabled", justify="center",
                                    font=("normal", 24), border_width=0, corner_radius=0)
                entry.place(relx=text_box_placement_x, rely=0.47, anchor=tk.CENTER)
                update_quantity()

                update_dict[packaged_name.lower()] = current_num
                return current_num, entry

            makeup_info = [
                {"name": "Blush", "image_path": "images\\makeup\\blu_fixed.png"},
                {"name": "Foundation", "image_path": "images\\makeup\\foundation_fixed.png"},
                {"name": "Lipstick", "image_path": "images\\makeup\\lipstick_fixed.png"},
                {"name": "Mascara", "image_path": "images\\makeup\\mascara_fixed.png"},
                {"name": "Perfume", "image_path": "images\\makeup\\perfume_fixed.png"}
            ]

            for makess in makeup_info:
                current_num, quantity_entry = create_makeup_widgets(makess["name"], makess["image_path"])
                setattr(self, f"current_num_{makess['name'].lower()}", current_num)
                setattr(self, f"{makess['name'].lower()}_quantity", quantity_entry)

                xaxe += 0.19
                minus_placement_x += 0.19
                plus_placement_x += 0.19
                text_box_placement_x += 0.19

            add_to_cart("makeup")

        makeup_img = ct.CTkImage(Im.open("images\\makeup.png"), size=(240, 80))
        makeup_bodycare = ct.CTkButton(master=left_frame_bot, width=250, height=70, corner_radius=10, text="",
                                       fg_color=the_background_grey, hover_color="#282828", image=makeup_img,
                                       border_spacing=0, command=makeup)
        makeup_bodycare.place(relx=0.5, rely=0.812, anchor=tk.CENTER)

        # Cart button stuff
        def cart_gui():
            if hasattr(self, 'cart_frame') and self.cart_frame.winfo_exists():
                self.cart_frame.destroy()

            self.cart_frame = ct.CTkFrame(master=self, width=930, height=542, fg_color="#121212", corner_radius=0,
                                            bg_color="#000000")
            self.cart_frame.place(relx=0.607, rely=0.537, anchor=tk.CENTER)

            self.big_outer_frame = ct.CTkFrame(master=self.cart_frame, width=630, height=542, fg_color="#e5f7fa", corner_radius=0,
                                          bg_color="#000000")
            self.big_outer_frame.place(relx=0.339, rely=0.5, anchor=tk.CENTER)

            self.indvidual_item_cart_frame = ct.CTkScrollableFrame(master=self.big_outer_frame, width=620, height=540, fg_color="#FFFFFF", corner_radius=0,
                                          bg_color="#000000", scrollbar_fg_color="#FFFFFF", scrollbar_button_color="#FFFFFF")
            self.indvidual_item_cart_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            # inner_frame = ct.CTkFrame(master=self.indvidual_item_cart_frame)
            # inner_frame.pack(anchor="center")

            # All headings
            text_label = ["PRODUCT", "PRICE", "QTY", "TOTAL"]

            for col_change, lab in enumerate(text_label):
                heading_label = ct.CTkLabel(master=self.indvidual_item_cart_frame, 
                                            width=190 if lab == "PRODUCT" else 130 if lab == "PRICE" else 120 if lab == "QTY" else 100,
                                            height=50,
                                            fg_color="#FFFFFF", text=lab,
                                            text_color="#000000", font=("Leelawadee", 20))
                heading_label.grid(row=0, column=col_change, padx=20 if col_change == 0 else 0, pady=0)

            # The invis fixx was the friends we made along the way
            # column_headers = ["product", "price", "qty", "total"]
            # for col, header in enumerate(column_headers):
            #     filler_label = ct.CTkLabel(master=self.indvidual_item_cart_frame,
            #                                width=190 if header == "product" else 130 if header == "price" else 150 if header == "qty" else 150,
            #                                height=50,
            #                                fg_color="#FFFFFF",
            #                                text="", text_color="#000000", font=("Yu Gothic", 14))
            #
            #     filler_label.grid(row=1, column=col)

            # product_filler = ct.CTkLabel(master=self.indvidual_item_cart_frame, width=190, height=50,
            #                                     fg_color="#FF5F12",
            #                                     text="",
            #                                   text_color="#000000", font=("Yu Gothic", 14))
            # product_filler.grid(row=1, column=0)
            #
            # price_filler = ct.CTkLabel(master=self.indvidual_item_cart_frame, width=130, height=50,
            #                              fg_color="#FF1212",
            #                              text="",
            #                              text_color="#000000", font=("Yu Gothic", 14))
            # price_filler.grid(row=1, column=1)
            #
            # qty_filler = ct.CTkLabel(master=self.indvidual_item_cart_frame, width=150, height=50,
            #                            fg_color="#FFAEBB",
            #                            text="",
            #                            text_color="#000000", font=("Yu Gothic", 14))
            # qty_filler.grid(row=1, column=2)
            #
            # total_filler = ct.CTkLabel(master=self.indvidual_item_cart_frame, width=150, height=50,
            #                          fg_color="#FF1289",
            #                          text="",
            #                          text_color="#000000", font=("Yu Gothic", 14))
            # total_filler.grid(row=1, column=3)

            def price_insert(item_name, call):
                price = mybackend.item_list(item_name)
                item_price_label.configure(state="normal")
                item_price_label.delete(0, "end")
                item_price_label.insert(0, f"₹{price}")
                item_price_label.configure(state="disabled")
                if call == "special":
                    return price
                
            def qty_insert(item_name, call):
                if int(info_dict.get(item_name)) > 0:
                    quantity = info_dict.get(item_name)
                    print(quantity)
                    item_qty_label.configure(state="normal")
                    item_qty_label.delete(0, "end")
                    item_qty_label.insert(0, quantity)
                    item_qty_label.configure(state="disabled")
                    if call == "special":
                        return quantity
                
            def total_insert(item_name, item_num):
                print(qty_insert(item_name, "special"))
                total = int(price_insert(item_name, "special")) * int(qty_insert(item_name, "special"))
                item_total_label.configure(state="normal")
                item_total_label.delete(0, "end")
                item_total_label.insert(0, f"₹{total}")
                item_total_label.configure(state="disabled")
                final_total[item_num] = total

            def plus():
                pass

            def minus():
                pass

            for row_change, item in enumerate(info_dict):
                item_name_label = ct.CTkLabel(master=self.indvidual_item_cart_frame,
                                              width=100, height=50, fg_color="#FFFFFF",
                                              text=f"{item.capitalize()}", text_color="#000000", font=("Yu Gothic", 14))
                item_name_label.grid(row=row_change+1, column=0, pady=5)

                item_price_label = ct.CTkEntry(master=self.indvidual_item_cart_frame, border_width=0,
                                               width=100, height=50, fg_color="#FFFFFF", justify="center",
                                               text_color="#000000", font=("Yu Gothic", 14))
                item_price_label.grid(row=row_change+1, column=1, pady=5)
                price_insert(item, call="reg")

                item_qty_label = ct.CTkEntry(master=self.indvidual_item_cart_frame, border_width=0,
                                             width=60, height=50, fg_color="#FFFFFF", justify="center",
                                             text_color="#000000", font=("Yu Gothic", 14))
                item_qty_label.grid(row=row_change+1, column=2, pady=5)
                qty_insert(item, call="reg")

                item_total_label = ct.CTkEntry(master=self.indvidual_item_cart_frame, border_width=0,
                                               width=100, height=50, fg_color="#FFFFFF", justify="center",
                                               text_color="#000000", font=("Yu Gothic", 14))
                item_total_label.grid(row=row_change+1, column=3, pady=5)
                total_insert(item, row_change+1)
            print(sum(final_total.values()))

            self.total_cart_frame = ct.CTkFrame(master=self.cart_frame, width=300, height=542, fg_color="#FAE8E5", corner_radius=0,
                                                bg_color="#000000")
            self.total_cart_frame.place(relx=0.839, rely=0.5, anchor=tk.CENTER)

            total_cart_label = ct.CTkLabel(master=self.total_cart_frame, width=100, height=52,
                                           text="Grand Total", font=("Century Gothic", 18), text_color="#000000")
            total_cart_label.place(relx=0.3, rely=0.2, anchor=tk.CENTER)

            if not info_dict:
                for kz in list(final_total.keys()):
                    del final_total[kz]

            ffff = sum(final_total.values())
            total_price_label = ct.CTkLabel(master=self.total_cart_frame, width=50, height=62,
                                            text=f"₹{ffff}", font=("Yu Gothic", 26), text_color="#000000")
            total_price_label.place(relx=0.7, rely=0.2, anchor=tk.CENTER)

            bullshit_label = ct.CTkLabel(master=self.total_cart_frame, width=50, height=22,
                                         text="*Shipping & taxes calculated at checkout",
                                         font=("Century Gothic", 12), text_color="#000000")
            bullshit_label.place(relx=0.55, rely=0.25, anchor=tk.CENTER)

            checkout_button = ct.CTkButton(master=self.total_cart_frame, width=170, height=55, corner_radius=30,
                                           text="CHECKOUT", font=("Yu Gothic", 14), hover_color="#282828",
                                           text_color="#FFFFFF", fg_color="#000000")
            checkout_button.place(relx=0.38, rely=0.45, anchor=tk.CENTER)

        cart_img = ct.CTkImage(Im.open("images\\cart_fnl.png"), size=(240, 40))
        cart_btn = ct.CTkButton(master=left_frame_bot, width=240, height=40, corner_radius=0,
                                text="", image=cart_img,
                                fg_color=the_background_grey, hover_color="#4950AA",
                                border_spacing=0, command=cart_gui)
        cart_btn.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        # Right frame stuff
        right_frame = ct.CTkFrame(master=bottom_frame, width=940, height=592,
                                  fg_color="#000000", corner_radius=0)
        right_frame.place(relx=0.607, rely=0.5, anchor=tk.CENTER)

        # Search bar stuff
        search_bar = ct.CTkEntry(master=right_frame, width=760, height=40,
                                 corner_radius=30, border_color="#282828",
                                 placeholder_text="Search for any product!",
                                 fg_color="#121212",
                                 font=("Normal", 15))
        search_bar.place(relx=0.819, rely=0.035, anchor=tk.E)
        search_btn = ct.CTkButton(master=right_frame, width=150, height=40, corner_radius=30,
                                  text="Search", text_color="#FFFFFF", font=("Normal", 15),
                                  fg_color="#121212", hover_color="#282828")
        search_btn.place(relx=0.83, rely=0.035, anchor=tk.W)

    # On open middle frame

    # cart_img = ct.CTkImage(Im.open("images\\cart.png"), size=(240, 50))
    # cart_btn = ct.CTkButton(master=left_frame_bot, width=240, height=50, corner_radius=0,
    #                         text="", image=cart_img,
    #                         fg_color="#363159", hover_color="#4950aa",
    #                         border_spacing=0)
    # cart_btn.place(relx=0.5, rely=0.96, anchor=tk.CENTER)

    # veg_label = ct.CTkLabel(master=vegies, width=230, height=70, text="", image=vegies_img)
    # veg_label.place(relx=0.2, rely=0.5, anchor=tk.CENTER)

    #
    # # 2st side tab
    # fruits_img = ct.CTkImage(Im.open("images\\vegetables.png"), size=(45, 45))
    # fruits = ct.CTkButton(master=left_frame, width=210, height=70, corner_radius=10,
    #                       text="    Fruits     ", font=("Normal", 28), image=fruits_img,
    #                       fg_color="#000000")
    # fruits.place(relx=0.5, rely=0.4, anchor=tk.CENTER)


app = Main()
mybackend = bk.Backend()
app.mainloop()