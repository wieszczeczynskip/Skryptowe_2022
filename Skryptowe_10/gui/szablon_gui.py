"""
Created on 2021-03-22

@author: Andrzej
"""

import configparser
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import NSEW
import os
from Loader import Loader

dane_konfig = "config.txt"


class BazoweGui(tk.Frame):
    def __init__(self, master=None):
        self.konfig = configparser.ConfigParser()
        self.konfig.read(dane_konfig, "UTF8")
        tk.Frame.__init__(self, master)
        self.parent = master
        self.parent.protocol("WM_DELETE_WINDOW", self.file_quit)
        domyslne = self.konfig["DEFAULT"]
        self.geometria_baza = domyslne["bazowa_geometria"]
        self.parent.geometry(self.geometria_baza)
        self.utworz_bazowe_menu()
        self.utworz_pasek_narzedzi()
        self.utworz_status()
        self.utworz_okno_robocze()
        self.dodaj_menu_custom()
        self.dodaj_menu_help()
        self.utworz_dodatki()
        self.parent.columnconfigure(0, weight=999)
        self.parent.columnconfigure(1, weight=1)
        self.parent.rowconfigure(0, weight=1)
        self.parent.rowconfigure(1, weight=9999)
        self.parent.rowconfigure(2, weight=1)
        self.loader = Loader()
        self.kraj = domyslne["last_kraj"]
        self.miesiac = int(domyslne["last_miesiac"])
        self.dzien1 = int(domyslne["last_dzien1"])
        self.dzien2 = int(domyslne["last_dzien1"])
        self.isZgony = domyslne["last_isZgony"]
        match self.isZgony:
            case "zgony":
                self.isZgony = 1
            case "zachorowania":
                self.isZgony = 0
            case _:
                self.isZgony = None

    def utworz_pasek_narzedzi(self):
        self.toolbar_images = []  # muszą być pamiętane stale
        self.toolbar = tk.Frame(self.parent)
        for image, command in (
            ("images/editdelete.gif", self.file_usun),
            ("images/filenew.gif", self.file_new),
            ("images/fileopen.gif", self.file_open),
            ("images/filesave.gif", self.file_save),
        ):
            image = os.path.join(os.path.dirname(__file__), image)
            try:
                image = tkinter.PhotoImage(file=image)
                self.toolbar_images.append(image)
                button = tkinter.Button(self.toolbar, image=image, command=command)
                button.grid(
                    row=0, column=len(self.toolbar_images) - 1
                )  # KOLEJNE ELEMENTY
            except tkinter.TclError as err:
                print(err)  # gdy kłopoty z odczytaniem pliku
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky=tkinter.NSEW)

    def utworz_dodatki(self):
        pass

    def utworz_status(self):
        self.statusbar = tk.Label(
            self.parent, text='Program działa - kliknij "Zatwierdź" aby uzyskać dane', anchor=tkinter.W
        )
        self.statusbar.grid(row=2, column=0, columnspan=2, sticky=tkinter.EW)
        pass

    def ustawStatusBar(self, txt):
        self.statusbar["text"] = txt

    def clearStatusBar(self):
        self.statusbar["text"] = ""

    def utworz_bazowe_menu(self):
        self.menubar = tk.Menu(self.parent)
        self.parent["menu"] = self.menubar
        fileMenu = tk.Menu(self.menubar)
        for label, command, shortcut_text, shortcut in (
            ("New...", self.file_new, "Ctrl+N", "<Control-n>"),
            ("Open...", self.file_open, "Ctrl+O", "<Control-o>"),
            ("Save", self.file_save, "Ctrl+S", "<Control-s>"),
            (None, None, None, None),
            ("Quit", self.file_quit, "Ctrl+Q", "<Control-q>"),
        ):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(
                    label=label, underline=0, command=command, accelerator=shortcut_text
                )
                self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="File", menu=fileMenu, underline=0)
        pass

    def dodaj_menu_help(self):
        fileMenu = tk.Menu(self.menubar)
        for label, command, shortcut_text, shortcut in (
            ("New...", self.file_new, "Ctrl+N", "<Control-n>"),
            ("Open...", self.file_open, "Ctrl+O", "<Control-o>"),
            ("Save", self.file_save, "Ctrl+S", "<Control-s>"),
            (None, None, None, None),
            ("Quit", self.file_quit, "Ctrl+Q", "<Control-q>"),
        ):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(
                    label=label, underline=0, command=command, accelerator=shortcut_text
                )
                self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="Help", menu=fileMenu, underline=0)
        pass

    def file_quit(self, event=None):
        reply = tkinter.messagebox.askyesno(
            "koniec pracy", "naprawdę kończysz?", parent=self.parent
        )
        event = event
        if reply:
            geometria = self.parent.winfo_geometry()
            self.konfig["DEFAULT"]["bazowa_geometria"] = geometria
            self.konfig["DEFAULT"]["last_kraj"] = self.kraj
            self.konfig["DEFAULT"]["last_miesiac"] = str(self.miesiac)
            self.konfig["DEFAULT"]["last_dzien1"] = str(self.dzien1)
            self.konfig["DEFAULT"]["last_dzien2"] = str(self.dzien2)
            match self.isZgony:
                case 1:
                    self.konfig["DEFAULT"]["last_isZgony"] = "zgony"
                case 0:
                    self.konfig["DEFAULT"]["last_isZgony"] = "zachorowania"
                case _:
                    self.konfig["DEFAULT"]["last_isZgony"] = ""

            with open(dane_konfig, "w") as konfig_plik:
                self.konfig.write(konfig_plik)
            self.parent.destroy()
        pass

    def dodaj_menu_custom(self, event=None):
        pass

    def file_usun(self):
        pass

    def file_new(self, event=None):
        event = event
        pass

    def file_open(self, event=None):
        event = event
        pass

    def file_save(self, event=None):
        event = event
        pass

    def utworz_okno_robocze(self):
        domyslne = self.konfig["DEFAULT"]
        self.robocze = tk.Frame(self.parent, background="#00704A")
        self.robocze.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NSEW)

        label0 = tk.Label(self.robocze, text="Odczyt danych", font=("Calibri Bold", 40))
        label0.grid()

        label1 = tk.Label(self.robocze, text="Zgony czy zachorowania?")
        label1.grid()
        isZgonyE = tk.Entry(self.robocze)
        isZgonyE.insert(0, domyslne["last_isZgony"])
        isZgonyE.grid()

        label2 = tk.Label(
            self.robocze, text="Z którego kraju dane chcesz uzyskać? (po angielsku)"
        )
        label2.grid()
        krajE = tk.Entry(self.robocze)
        krajE.insert(0, domyslne["last_kraj"])
        krajE.grid()

        label3 = tk.Label(
            self.robocze,
            text="Z którego miesiąca dane chcesz uzyskać? (numer miesiąca)",
        )
        label3.grid()
        miesiacE = tk.Entry(self.robocze)
        miesiacE.insert(0, domyslne["last_miesiac"])
        miesiacE.grid()

        label4 = tk.Label(self.robocze, text="Od którego dnia chcesz uzyskać dane?")
        label4.grid()
        dzien1E = tk.Entry(self.robocze)
        dzien1E.insert(0, domyslne["last_dzien1"])
        dzien1E.grid()

        label5 = tk.Label(self.robocze, text="Do którego dnia chcesz uzyskać dane?")
        label5.grid()
        dzien2E = tk.Entry(self.robocze)
        dzien2E.insert(0, domyslne["last_dzien2"])
        dzien2E.grid()

        def getData():
            self.kraj = None if krajE.get() == "" else krajE.get()
            self.miesiac = None if miesiacE.get() == "" else int(miesiacE.get())
            self.dzien1 = None if dzien1E.get() == "" else int(dzien1E.get())
            self.dzien2 = None if dzien2E.get() == "" else int(dzien2E.get())
            self.isZgony = isZgonyE.get().lower()
            match self.isZgony:
                case "zgony":
                    self.isZgony = 1
                case "zachorowania":
                    self.isZgony = 0
                case _:
                    self.isZgony = None

            counter = 0
            if self.isZgony == 1 or self.isZgony == 0:
                for x in range(self.dzien1, self.dzien2 + 1):
                    counter = counter + self.loader.getData(
                        self.isZgony, 2020, x, self.miesiac, self.kraj
                    )
                counter = str(counter)
            else:
                counter = "Błąd"

            tkinter.messagebox.showinfo("Ilość", counter)

        btn = tk.Button(self.robocze, text="Zatwierdź", command=getData)
        btn.grid()


if __name__ == "__main__":
    root = tk.Tk()
    app = BazoweGui(master=root)
    app.mainloop()
    pass
