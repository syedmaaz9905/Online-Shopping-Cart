# ************************************ELEGANCE************************************

from tkinter import *
from csv import *
import os
import csv
# import cv2
from tkinter.messagebox import showerror, showinfo
from PIL import ImageTk, Image
from abc import ABC, abstractmethod


class GUI(Tk):  # Inherited from Tk
    lst = []  # Empty list

    def __init__(self):  # constructor initiated/allows the user to sign in if he/she already has an account
        super().__init__()  # method overriding ( tk )
        self.title("PROJECT 1")
        self.geometry("1280x830")
        self.minsize(800, 400)
        self.maxsize(1400, 1000)

        self.resizable(FALSE, FALSE)
        self.bg = ImageTk.PhotoImage(file="CS20014_13.jpg")
        self.bg_image = Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        frame_login = Frame(self, bg="cornsilk2")
        frame_login.place(x=400, y=150, width=500, height=500)
        title = Label(frame_login, text="WELCOME TO ELEGANCE", font=("Times New Roman", 25, "bold"), bg="cornsilk2",
                      fg="grey18").place(x=30, y=30)
        subtitle = Label(frame_login, text="Account Login Page", font=("Times New Roman", 19, "bold"), bg="cornsilk2",
                         fg="grey18").place(x=25, y=100)

        self.username = StringVar()  # instance attribute/stringvar converts username into string
        self.password = StringVar()  # instance attribute/stringvar converts username into string

        self.l1 = Label(frame_login, text="Enter your username:", font=("Times New Roman", 15, "bold"), bg="cornsilk2",
                        fg="#666565").place(x=30, y=150)
        self.e1 = Entry(frame_login, textvar=self.username, font=("Times New Roman", 15), bg="#E7E6E6")
        self.e1.place(x=30, y=190, width=250)

        self.l2 = Label(frame_login, text="Enter your password:", font=("Times New Roman", 15, "bold"), bg="cornsilk2",
                        fg="#666565").place(x=30, y=230)
        self.e2 = Entry(frame_login, textvar=self.password, font=("Times New Roman", 15), bg="#E7E6E6")
        self.e2.place(x=30, y=270, width=250)

        self.b1 = Button(frame_login, text="Sign In", font=("Times New Roman", 15, "bold"), bd="5", bg="cornsilk2",
                         fg="#666565", command=self.sign_in).place(x=30, y=330)

        self.b2 = Button(frame_login, text="Sign Up", font=("Times New Roman", 15, "bold"), bd="5", bg="cornsilk2",
                         fg="#666565", command=self.sign_up).place(x=150, y=330)

    def sign_up(self):  # This instance method is creating the user account
        self.destroy()
        super().__init__()
        self.title("Sign Up Page")
        self.geometry("1280x800")
        self.minsize(800, 400)
        self.maxsize(1400, 1000)
        self.resizable(FALSE, FALSE)
        self.wm_iconbitmap("CS20014_2.ico")

        self.bg = ImageTk.PhotoImage(file="CS20014_14.jpg")
        self.bg_image = Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        frame_signup = Frame(self, bg="gray10")
        frame_signup.place(x=400, y=75, width=450, height=640)
        title = Label(frame_signup, text="SIGN UP", font=("Times New Roman", 25, "bold"), bg="gray10",
                      fg="DodgerBlue4").place(x=30, y=30)

        self.first_name = StringVar()
        self.last_name = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.email_address = StringVar()
        self.address = StringVar()

        self.l3 = Label(frame_signup, text="Enter Your First Name:", font=("Times New Roman", 15, "bold"), bg="gray10",
                        fg="#666565").place(x=30, y=80)
        self.e3 = Entry(frame_signup, textvar=self.first_name, font=("Times New Roman", 15), bg="#adaaaa")
        self.e3.place(x=30, y=120, width=250)

        self.l4 = Label(frame_signup, text="Enter Your Last Name:", font=("Times New Roman", 15, "bold"), bg="gray10",
                        fg="#666565").place(x=30, y=160)
        self.e4 = Entry(frame_signup, textvar=self.last_name, font=("Times New Roman", 15), bg="#adaaaa")
        self.e4.place(x=30, y=200, width=250)

        self.l5 = Label(frame_signup, text="Enter Your Username:", font=("Times New Roman", 15, "bold"), bg="gray10",
                        fg="#666565").place(x=30, y=240)
        self.e5 = Entry(frame_signup, textvar=self.username, font=("Times New Roman", 15), bg="#adaaaa")
        self.e5.place(x=30, y=280, width=250)

        self.l6 = Label(frame_signup, text="Enter Your Password:", font=("Times New Roman", 15, "bold"), bg="gray10",
                        fg="#666565").place(x=30, y=320)
        self.e6 = Entry(frame_signup, textvar=self.password, font=("Times New Roman", 15), bg="#adaaaa")
        self.e6.place(x=30, y=360, width=250)

        self.l7 = Label(frame_signup, text="Enter Your Email Address:", font=("Times New Roman", 15, "bold"),
                        bg="gray10", fg="#666565").place(x=30, y=400)
        self.e7 = Entry(frame_signup, textvar=self.email_address, font=("Times New Roman", 15), bg="#adaaaa")
        self.e7.place(x=30, y=440, width=250)

        self.l8 = Label(frame_signup, text="Enter Your Address:", font=("Times New Roman", 15, "bold"), bg="gray10",
                        fg="#666565").place(x=30, y=480)
        self.e8 = Entry(frame_signup, textvar=self.address, font=("Times New Roman", 15), bg="#adaaaa")
        self.e8.place(x=30, y=520, width=250)

        self.b3 = Button(frame_signup, text="Create An Account", font=("Times New Roman", 15, "bold"), bd="5",
                         bg="gray10", fg="DodgerBlue4",
                         command=lambda: [self.save_user(), self.account_verification()]).place(x=170, y=570, width=250)

    def sign_in(self):  # verifies whether username or password exists in the accounts file
        if os.path.exists("account.csv"):
            with open("account.csv") as f:
                reader = csv.reader(f)
                data_read = [row for row in reader]
                count = 0
                for i in data_read:
                    if self.username.get() in i and self.password.get() in i:
                        self.destroy()
                        GUI.lst.append(self.username.get())  # appends username to the GUI list
                        self.a = Main_Menu()
                        count += 1
                    else:
                        continue
                if count != 0:
                    pass
                else:
                    showerror("Error", "Something is wrong")
        else:  # gives an error if username or password is invalid
            showerror("Error", "Enter Valid Username and Password")

    def save_user(self):  # creates the file and stores the information of a user upon account creation
        if self.first_name.get() != "" and self.last_name.get() != "" and self.username.get() != "" and self.password.get() != "" and self.email_address.get() != "" and self.address.get() != "":
            try:
                if os.path.exists("account.csv"):
                    with open("account.csv", "a+") as f:
                        write = writer(f)
                        write.writerow([self.first_name.get(), " ", self.last_name.get(), " ", self.username.get(), " ",
                                        self.password.get(), " ", self.email_address.get(), " ", self.address.get()])
                else:
                    with open("account.csv", "a+") as f:
                        write = writer(f)
                        write.writerow(
                            ["First Name", " ", "Last Name", " ", "Username", " ", "Password", " ", "Email Address",
                             " ", "Address"])
                    with open("account.csv", "a+") as f:
                        write = writer(f)
                        write.writerow([self.first_name.get(), " ", self.last_name.get(), " ", self.username.get(), " ",
                                        self.password.get(), " ", self.email_address.get(), " ", self.address.get()])
            except:
                showerror("Error", "Something is Missing")
        else:
            if self.first_name.get() == "" or self.last_name.get() == "" or self.username.get() == "" or self.password.get() == "" or self.email_address.get() == "" or self.address.get() == "":
                showerror("Error", "Something is Missing")

    def account_verification(self):  # verifies if all the entries are entered and takes you back to the GUI window
        if self.first_name.get() == "" or self.last_name.get() == "" or self.username.get() == "" or self.password.get() == "" or self.email_address.get() == "" or self.address.get() == "":
            showerror("Error", "Something is missing")
        elif self.first_name.get() != "" and self.last_name.get() != "" and self.username.get() != "" and self.password.get() != "" and self.email_address.get() != "" and self.address.get() != "":
            showinfo("Info", "Your account has been created.")
            self.destroy()
            self.a = GUI()


class Main_Menu(Tk):  # user is given options to shop or view shopping history or to exit the application
    def __init__(self):
        super().__init__()
        self.title("MAIN MENU")
        self.geometry("1000x830")
        self.minsize(800, 600)
        self.maxsize(1200, 800)
        self.wm_iconbitmap("CS20014_2.ico")

        self.bg = Label(self, bg="gray12").place(x=0, y=0, relwidth=1, relheight=1)

        frame_mainmenu = Frame(self, bg="#ffffff")
        frame_mainmenu.place(x=250, y=100, width=500, height=500)

        image = Image.open("CS20014_15.jpg")
        new_image = image.resize((500, 500))
        self.image = ImageTk.PhotoImage(new_image)
        self.label = Label(frame_mainmenu, image=self.image)
        self.label.place(x=0, y=0)

        self.products_menu = Button(frame_mainmenu, text="Products Menu", font=("Times New Roman", 15, "bold"), bd="5",
                                    bg="RosyBrown1", command=self.product_menu1).place(x=30, y=170, width=140,
                                                                                       height=55)

        self.shopping_history = Button(frame_mainmenu, text="Shopping History", font=("Times New Roman", 15, "bold"),
                                       bd="5", bg="RosyBrown1", command=self.shopping_history).place(x=330, y=160,
                                                                                                     width=155,
                                                                                                     height=55)

        self.exit = Button(frame_mainmenu, text="EXIT", font=("Times New Roman", 15, "bold"), bd="5", bg="RosyBrown1",
                           command=self.exit).place(x=330, y=450, width=145, height=45)

    def exit(self):  # terminated the application
        self.destroy()

    def shopping_history(self):  # inserts the data from the user shopping history file into a listbox
        self.destroy()
        super().__init__()
        self.title("Shopping History")
        self.wm_iconbitmap("CS20014_2.ico")
        self.geometry("950x800")
        self.minsize(800, 600)
        self.maxsize(1000, 800)
        self.listbox = Listbox(self, width=50, height=25)
        self.listbox.pack()
        if os.path.exists(GUI.lst[0] + ".csv"):
            with open(GUI.lst[0] + ".csv", "r+") as f:
                reader = csv.reader(f, delimiter=' ', quotechar='|')
                your_list = list(reader)
                self.original = f.read()
                for item in your_list:
                    self.listbox.insert(END, item)
                    f.close()

        self.b4 = Button(self, text="Go Back To Main Menu", font=("Times New Roman", 10, "bold"), bd="5",
                         relief="groove", padx=10,
                         pady=5, command=self.back_to_menu)
        self.b4.pack()

    def back_to_menu(self):  # this method lets the user go back to main menu from shopping history
        self.destroy()
        self.a = Main_Menu()

    def product_menu1(self):  # opens the products menu page 1
        self.destroy()
        super().__init__()
        self.title("Product's Menu")
        self.wm_iconbitmap("CS20014_2.ico")
        self.geometry("950x800")
        self.minsize(750, 600)
        self.maxsize(1000, 800)
        # self.resizable(FALSE, FALSE)

        self.l21 = Label(self, text="ELEGANCE", font=("Times New Roman", 30), bd="3", padx=10, pady=10)
        self.l21.grid(row=0, column=1)

        self.p1 = Image.open("CS20014_3.png")
        self.p1 = self.p1.resize((125, 125), Image.ANTIALIAS)
        self.my_p1 = ImageTk.PhotoImage(self.p1)
        my_p1 = Label(image=self.my_p1)
        my_p1.grid(row=1, column=0, padx=10, pady=10)
        self.l12 = Label(self, text="-->One piece stitched cotton Kurta\n-->PKR.2000",
                         font=("Times New Roman", 15), bd="3", padx=10, pady=10)
        self.l12.grid(row=2, column=0)
        self.slider1 = Scale(self, from_=0, to=10, orient=HORIZONTAL)
        self.slider1.grid(row=3, column=0)

        self.b5 = Button(self, text='Add', font=("Times New Roman", 15, "bold"), bd="5", relief="groove", padx=10,
                         pady=5, command=self.add_item1)
        self.b5.grid(row=4, column=0, padx=10, pady=5)

        self.p2 = Image.open("CS20014_4.png")
        self.p2 = self.p2.resize((125, 125), Image.ANTIALIAS)
        self.my_p2 = ImageTk.PhotoImage(self.p2)
        my_p2 = Label(image=self.my_p2)
        my_p2.grid(row=1, column=1, padx=10, pady=10)
        self.l13 = Label(self, text="-->Three piece stitched Lawn Suit\n-->PKR.3000",
                         font=("Times New Roman", 15), bd="3", padx=10, pady=10)
        self.l13.grid(row=2, column=1)
        self.slider2 = Scale(self, from_=0, to=10, orient=HORIZONTAL)
        self.slider2.grid(row=3, column=1)

        self.b6 = Button(self, text="Add ", font=("Times New Roman", 15, "bold"), bd="5", relief="groove", padx=10,
                         pady=5, command=self.add_item2)
        self.b6.grid(row=4, column=1, padx=10, pady=5)

        self.p3 = Image.open("CS20014_5.png")
        self.p3 = self.p3.resize((125, 125), Image.ANTIALIAS)
        self.my_p3 = ImageTk.PhotoImage(self.p3)
        my_p3 = Label(image=self.my_p3)
        my_p3.grid(row=1, column=2, padx=10, pady=10)
        self.l14 = Label(self, text="-->Embroidered Cambric Kurta\n-->PKR.Rs.1500",
                         font=("Times New Roman", 15), bd="3", padx=10, pady=10)
        self.l14.grid(row=2, column=2)
        self.slider3 = Scale(self, from_=0, to=10, orient=HORIZONTAL)
        self.slider3.grid(row=3, column=2)

        self.b7 = Button(self, text="Add ", font=("Times New Roman", 15, "bold"), bd="5", relief="groove", padx=10,
                         pady=5, command=self.add_item3)
        self.b7.grid(row=4, column=2, padx=10, pady=5)

        self.p4 = Image.open("CS20014_6.png")
        self.p4 = self.p4.resize((125, 125), Image.ANTIALIAS)
        self.my_p4 = ImageTk.PhotoImage(self.p4)
        my_p4 = Label(image=self.my_p4)
        my_p4.grid(row=5, column=0, padx=10, pady=10)
        self.l15 = Label(self, text="-->Embroidered lawn Kurta\n-->PKR.1800", font=("Times New Roman", 15),
                         bd="3", padx=10, pady=10)
        self.l15.grid(row=6, column=0)
        self.slider4 = Scale(self, from_=0, to=10, orient=HORIZONTAL)
        self.slider4.grid(row=7, column=0)

        self.b8 = Button(self, text="Add", font=("Times New Roman", 15, "bold"), bd="5", relief="groove", padx=10,
                         pady=5, command=self.add_item4)
        self.b8.grid(row=8, column=0, padx=10, pady=5)

        self.p5 = Image.open("CS20014_7.png")
        self.p5 = self.p5.resize((125, 125), Image.ANTIALIAS)
        self.my_p5 = ImageTk.PhotoImage(self.p5)
        my_p5 = Label(image=self.my_p5)
        my_p5.grid(row=5, column=1, padx=10, pady=10)
        self.l16 = Label(self, text="-->Printed silk Kurta\n-->PKR.2500", font=("Times New Roman", 15),
                         bd="3", padx=10, pady=10)
        self.l16.grid(row=6, column=1)
        self.slider5 = Scale(self, from_=0, to=10, orient=HORIZONTAL)
        self.slider5.grid(row=7, column=1)

        self.b9 = Button(self, text="Add", font=("Times New Roman", 15, "bold"), bd="5", relief="groove", padx=10,
                         pady=5, command=self.add_item5)
        self.b9.grid(row=8, column=1, padx=10, pady=5)

        self.p1 = Image.open("CS20014_16.png")
        resized = self.p1.resize((25, 25), Image.ANTIALIAS)
        self.pic = ImageTk.PhotoImage(resized)
        self.b10 = Button(self, image=self.pic, command=self.open_cart)
        self.b10.grid(row=0, column=2)

        self.b11 = Button(self, text="NEXT", font=("Times New Roman", 10, "bold"), bd="5", relief="groove", padx=10,
                          pady=5, command=self.product_menu2)
        self.b11.grid(row=5, column=2, padx=10, pady=5)

        self.b12 = Button(self, text="CHECKOUT", font=("Times New Roman", 10, "bold"), bd="5", relief="groove", padx=10,
                          pady=5, command=lambda: [self.ct(), self.mm()])
        self.b12.grid(row=6, column=2, padx=10, pady=5)

        self.b = Button(self, text="Go Back", font=("Times New Roman", 10, "bold"), bd="5", relief="groove", padx=10,
                        pady=5, command=self.mm)
        self.b.grid(row=7, column=2, padx=10, pady=5)

    def add_item1(self):  # adds the item details into the current cart file
        self.name = "Light Blue Kurta"
        self.quantity = self.slider1.get()
        self.price = 2000
        self.total_price = self.quantity * self.price
        self.cart = Cart()
        self.cart.add_cart(self.name, self.price, self.quantity, self.total_price)
        with open("cart.csv", "a+") as f:
            write = writer(f)
            write.writerow([GUI.lst[0], self.name, self.quantity, self.price, self.total_price])

    def add_item2(self):
        self.name = "Red Suit"
        self.quantity = self.slider2.get()
        self.price = 3000
        self.total_price = self.quantity * self.price
        self.cart = Cart()
        self.cart.add_cart(self.name, self.price, self.quantity, self.total_price)
        with open("cart.csv", "a+") as f:
            write = writer(f)
            write.writerow([GUI.lst[0], self.name, self.quantity, self.price, self.total_price])

    def add_item3(self):
        self.name = "Navy Blue Kurta"
        self.quantity = self.slider3.get()
        self.price = 1500
        self.total_price = self.quantity * self.price
        self.cart = Cart()
        self.cart.add_cart(self.name, self.price, self.quantity, self.total_price)
        with open("cart.csv", "a+") as f:
            write = writer(f)
            write.writerow([GUI.lst[0], self.name, self.quantity, self.price, self.total_price])

    def add_item4(self):
        self.name = "Beige Kurta"
        self.quantity = self.slider4.get()
        self.price = 1800
        self.total_price = self.quantity * self.price
        self.cart = Cart()
        self.cart.add_cart(self.name, self.price, self.quantity, self.total_price)
        with open("cart.csv", "a+") as f:
            write = writer(f)
            write.writerow([GUI.lst[0], self.name, self.quantity, self.price, self.total_price])

    def add_item5(self):
        self.name = "Royal Blue"
        self.quantity = self.slider5.get()
        self.price = 2500
        self.total_price = self.quantity * self.price
        self.cart = Cart()
        self.cart.add_cart(self.name, self.price, self.quantity, self.total_price)
        with open("cart.csv", "a+") as f:
            write = writer(f)
            write.writerow([GUI.lst[0], self.name, self.quantity, self.price, self.total_price])

    def open_cart(self):  # association/creates an object of the Show_cart class
        self.b = Show_cart()

    def mm(self):  # association
        self.destroy()  # it will destory product menu window
        self.a = Main_Menu()  # it will open main menu

    def ct(self):  # association/creates an object of Checkout class
        self.c = Checkout()
        self.c.checkout()
        self.c.remove_cart_history()

    def product_menu2(self):  # opens the products menu page 1
        self.destroy()
        super().__init__()
        self.title("Product's Menu")
        self.wm_iconbitmap("CS20014_2.ico")
        self.geometry("950x800")
        self.minsize(800, 600)
        self.maxsize(1000, 800)
        # self.resizable(FALSE, FALSE)

        self.l21 = Label(self, text="ELEGANCE", font=("Times New Roman", 30), bd="3", padx=10, pady=10)
        self.l21.grid(row=0, column=1)

        self.p6 = Image.open("CS20014_8.png")
        self.p6 = self.p6.resize((125, 125), Image.ANTIALIAS)
        self.my_p6 = ImageTk.PhotoImage(self.p6)
        my_p6 = Label(image=self.my_p6)
        my_p6.grid(row=1, column=0, padx=10, pady=10)
        self.l17 = Label(self, text="-->Plain cotton Kameez\n-->PKR.1200", font=("Times New Roman", 15),
                         bd="3", padx=10, pady=10)
        self.l17.grid(row=2, column=0)
        self.slider6 = Scale(self, from_=0, to=10, orient=HORIZONTAL)
        self.slider6.grid(row=3, column=0)

        self.b13 = Button(self, text="Add", font=("Times New Roman", 15, "bold"), bd="5", relief="groove", padx=10,
                          pady=5, command=self.add_item6)
        self.b13.grid(row=4, column=0, padx=10, pady=5)

        self.p7 = Image.open("CS20014_9.png")
        self.p7 = self.p7.resize((125, 125), Image.ANTIALIAS)
        self.my_p7 = ImageTk.PhotoImage(self.p7)
        my_p7 = Label(image=self.my_p7)
        my_p7.grid(row=1, column=1, padx=10, pady=10)
        self.l18 = Label(self, text="-->Lawn Kameez & Shalwar\n-->PKR.2000", font=("Times New Roman", 15),
                         bd="3", padx=10, pady=10)
        self.l18.grid(row=2, column=1)
        self.slider7 = Scale(self, from_=0, to=10, orient=HORIZONTAL)
        self.slider7.grid(row=3, column=1)

        self.b14 = Button(self, text="Add", font=("Times New Roman", 15, "bold"), bd="5", relief="groove", padx=10,
                          pady=5, command=self.add_item7)
        self.b14.grid(row=4, column=1, padx=10, pady=5)

        self.p8 = Image.open("CS20014_10.png")
        self.p8 = self.p8.resize((125, 125), Image.ANTIALIAS)
        self.my_p8 = ImageTk.PhotoImage(self.p8)
        my_p8 = Label(image=self.my_p8)
        my_p8.grid(row=1, column=2, padx=10, pady=10)
        self.l19 = Label(self, text="-->Broadcloth Shirt\n-->PKR.1400", font=("Times New Roman", 15),
                         bd="3", padx=10, pady=10)
        self.l19.grid(row=2, column=2)
        self.slider8 = Scale(self, from_=0, to=10, orient=HORIZONTAL)
        self.slider8.grid(row=3, column=2)

        self.b15 = Button(self, text="Add", font=("Times New Roman", 15, "bold"), bd="5", relief="groove", padx=10,
                          pady=5, command=self.add_item8)
        self.b15.grid(row=4, column=2, padx=10, pady=5)

        self.p9 = Image.open("CS20014_11.png")
        self.p9 = self.p9.resize((125, 125), Image.ANTIALIAS)
        self.my_p9 = ImageTk.PhotoImage(self.p9)
        my_p9 = Label(image=self.my_p9)
        my_p9.grid(row=5, column=0, padx=10, pady=10)
        self.l20 = Label(self, text="-->Plain Blue Broadcloth Kameez\n-->PKR.900",
                         font=("Times New Roman", 15), bd="3", padx=10, pady=10)
        self.l20.grid(row=6, column=0)
        self.slider9 = Scale(self, from_=0, to=10, orient=HORIZONTAL)
        self.slider9.grid(row=7, column=0)

        self.b16 = Button(self, text="Add", font=("Times New Roman", 15, "bold"), bd="5", relief="groove", padx=10,
                          pady=5, command=self.add_item9)
        self.b16.grid(row=8, column=0, padx=10, pady=5)

        self.p10 = Image.open("CS20014_12.png")
        self.p10 = self.p10.resize((125, 125), Image.ANTIALIAS)
        self.my_p10 = ImageTk.PhotoImage(self.p10)
        my_p10 = Label(image=self.my_p10)
        my_p10.grid(row=5, column=1, padx=10, pady=10)
        self.l21 = Label(self, text="-->Three Piece Cotton, Silk & Broad Cloth Suit\n-->PKR.4000",
                         font=("Times New Roman", 15), bd="3", padx=10, pady=10)
        self.l21.grid(row=6, column=1)
        self.slider10 = Scale(self, from_=0, to=10, orient=HORIZONTAL)
        self.slider10.grid(row=7, column=1)

        self.b17 = Button(self, text="Add", font=("Times New Roman", 15, "bold"), bd="5", relief="groove", padx=10,
                          pady=5, command=self.add_item10)
        self.b17.grid(row=8, column=1, padx=10, pady=5)

        self.p1 = Image.open("CS20014_16.png")
        resized = self.p1.resize((25, 25), Image.ANTIALIAS)
        self.pic = ImageTk.PhotoImage(resized)
        self.b18 = Button(self, image=self.pic, command=self.open_cart)
        self.b18.grid(row=0, column=2)

        self.b19 = Button(self, text="BACK", font=("Times New Roman", 10, "bold"), bd="5", relief="groove", padx=10,
                          pady=5, command=self.product_menu1)
        self.b19.grid(row=5, column=2, padx=10, pady=5)

        self.b20 = Button(self, text="CHECKOUT", font=("Times New Roman", 10, "bold"), bd="5", relief="groove", padx=10,
                          pady=5, command=lambda: [self.ct(), self.mm()])
        self.b20.grid(row=6, column=2, padx=10, pady=5)

    def add_item6(self):
        self.name = "Denim Kameez"
        self.quantity = self.slider6.get()
        self.price = 1200
        self.total_price = self.quantity * self.price
        self.cart = Cart()
        self.cart.add_cart(self.name, self.price, self.quantity, self.total_price)
        with open("cart.csv", "a+") as f:
            write = writer(f)
            write.writerow([GUI.lst[0], self.name, self.quantity, self.price, self.total_price])

    def add_item7(self):
        self.name = "Kameez & Shalwar"
        self.quantity = self.slider7.get()
        self.price = 2000
        self.total_price = self.quantity * self.price
        self.cart = Cart()
        self.cart.add_cart(self.name, self.price, self.quantity, self.total_price)
        with open("cart.csv", "a+") as f:
            write = writer(f)
            write.writerow([GUI.lst[0], self.name, self.quantity, self.price, self.total_price])

    def add_item8(self):
        self.name = "Prussian Blue Shirt"
        self.quantity = self.slider8.get()
        self.price = 1400
        self.total_price = self.quantity * self.price
        self.cart = Cart()
        self.cart.add_cart(self.name, self.price, self.quantity, self.total_price)
        with open("cart.csv", "a+") as f:
            write = writer(f)
            write.writerow([GUI.lst[0], self.name, self.quantity, self.price, self.total_price])

    def add_item9(self):
        self.name = "Blue Kameez Shalwar"
        self.quantity = self.slider9.get()
        self.price = 900
        self.total_price = self.quantity * self.price
        self.cart = Cart()
        self.cart.add_cart(self.name, self.price, self.quantity, self.total_price)
        with open("cart.csv", "a+") as f:
            write = writer(f)
            write.writerow([GUI.lst[0], self.name, self.quantity, self.price, self.total_price])

    def add_item10(self):
        self.name = "Grey Suit"
        self.quantity = self.slider10.get()
        self.price = 4000
        self.total_price = self.quantity * self.price
        self.cart = Cart()
        self.cart.add_cart(self.name, self.price, self.quantity, self.total_price)
        with open("cart.csv", "a+") as f:
            write = writer(f)
            write.writerow([GUI.lst[0], self.name, self.quantity, self.price, self.total_price])


class Trolley(ABC):  # Abstarct Class
    cart = [["Product Name", "Product Price", "Product Quantity", "Total Price"]]
    price = 0

    @abstractmethod
    def add_cart(self):
        pass

class Cart(Trolley):  # makes the list of the details of the products that a user adds to the cart, child class of abstract class
    def add_cart(self, name, price, quantity, total_price):
        Cart.cart.append([name, price, quantity, total_price])

class Total_price:  # telling the total price of all the items present in the cart
    def updated_price(self):
        with open("cart.csv", 'r') as csvfile:
            NewPrice = 0
            reader = csv.reader(csvfile, dialect='excel', delimiter=",")
            for row in reader:
                if row != []:
                    NewPrice += int(row[4])
            Cart.price = NewPrice

        self.l24 = Label(self, text="The total price is " + str(Cart.price))
        self.l24.pack()


class Checkout():
    def checkout(self):  # transfers the data from the current cart file to the shopping history file of each user
        checkout = GUI.lst[0] + ".csv"
        if os.path.exists(checkout):
            try:
                with open(checkout, "a+") as f:  # it will create a shopping history file with the username of the user
                    output = open(checkout, "a+")
                    with open("cart.csv", "rt", encoding='ascii') as f:
                        for row in f:
                            # print(row)
                            output.write(row)
            except:
                showerror("Error", "No such directory 'Account.csv' found")
        else:
            checkout = GUI.lst[0] + ".csv"
            output = open(checkout, 'a+')
            with open('cart.csv', 'rt', encoding='ascii') as f:
                for row in f:
                    # print(row)
                    output.write(row)

    def remove_cart_history(self):  # it deletes the current cart file
        os.remove('cart.csv')


class Show_cart(Toplevel, Cart, Checkout, Total_price):  # inserts the current cart file data into a listbox
    def __init__(self):
        # Toplevel=Tk()
        super().__init__()
        super().geometry("800x800")
        super().minsize(800, 600)
        super().maxsize(1000, 800)
        self.wm_iconbitmap("CS20014_2.ico")
        super().title("Current Cart List")
        self.label = Label(self, text=f"You are signed in as {GUI.lst[0]}")
        self.label.pack()
        self.listbox = Listbox(self, width=50, height=25)
        self.listbox.pack()
        self.listbox.insert(1)
        with open("cart.csv", "a+") as f:
            reader = csv.reader(f, delimiter=' ', quotechar='|')
            f.seek(0)
            your_list = list(reader)
            for item in your_list:
                self.listbox.insert(END, item)

        self.b21 = Button(self, text="REMOVE", font=("Times New Roman", 10, "bold"), bd="5", relief="groove", padx=10,
                          pady=5, command=self.remove_button)
        self.b21.pack()

        self.b22 = Button(self, text="Total Price", font=("Times New Roman", 10, "bold"), bd="5", relief="groove",
                          padx=10, pady=5, command=self.updated_price)
        self.b22.pack()

    def remove_button(self):  # allow's the user tor remove an item from the listbox as well as the file
        with open("cart.csv", 'r') as f:
            removed_items = self.listbox.curselection()
            lines = f.readlines()
        f.close()
        with open("cart.csv", 'w') as f:
            write = writer(f, delimiter=',')
            for i, line in enumerate(lines):
                if i not in removed_items:
                    f.write(line)
        self.listbox.delete(ANCHOR)
        f.close()


# driver code
if __name__ == "__main__":
    r = GUI()
    r.wm_iconbitmap("CS20014_2.ico")
    r.mainloop()
