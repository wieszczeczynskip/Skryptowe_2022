from tkinter import *
from tkinter import messagebox
from Loader import Loader


def gui():
    loader = Loader()
    okno = Tk()

    okno.title("Wersja 2")
    okno.geometry("800x600")

    label0 = Label(okno, text="Odczyt danych", font=("Calibri Bold", 40))
    label0.grid()

    label1 = Label(okno, text="Zgony czy zachorowania?")
    label1.grid()
    isZgonyE = Entry(okno)
    isZgonyE.grid()

    label2 = Label(okno, text="Z którego kraju dane chcesz uzyskać? (po angielsku)")
    label2.grid()
    krajE = Entry(okno)
    krajE.grid()

    label3 = Label(
        okno, text="Z którego miesiąca dane chcesz uzyskać? (numer miesiąca)"
    )
    label3.grid()
    miesiacE = Entry(okno)
    miesiacE.grid()

    label4 = Label(okno, text="Od którego dnia chcesz uzyskać dane?")
    label4.grid()
    dzien1E = Entry(okno)
    dzien1E.grid()

    label5 = Label(okno, text="Do którego dnia chcesz uzyskać dane?")
    label5.grid()
    dzien2E = Entry(okno)
    dzien2E.grid()

    def getData():
        kraj = None if krajE.get() == "" else krajE.get()
        miesiac = None if miesiacE.get() == "" else int(miesiacE.get())
        dzien1 = None if dzien1E.get() == "" else int(dzien1E.get())
        dzien2 = None if dzien2E.get() == "" else int(dzien2E.get())
        isZgony = isZgonyE.get().lower()
        match isZgony:
            case "zgony":
                isZgony = 1
            case "zachorowania":
                isZgony = 0
            case _:
                isZgony = None

        counter = 0
        if isZgony == 1 or isZgony == 0:
            for x in range(dzien1, dzien2 + 1):
                counter = counter + loader.getData(isZgony, 2020, x, miesiac, kraj)
            counter = str(counter)
        else:
            counter = "Błąd"

        messagebox.showinfo("Ilość", counter)

    btn = Button(okno, text="Zatwierdź", command=getData)
    btn.grid()

    okno.mainloop()


if __name__ == "__main__":
    gui()
