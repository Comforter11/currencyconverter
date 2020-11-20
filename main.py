from tkinter import *
import requests


windows = Tk()
windows.title("CURRENCY CONVERTOR ")
windows.geometry("500x500")
windows.config(background="purple")


url = "https://v6.exchangerate-api.com/v6/6e5bfadc9d72fef355f3be14/latest/USD"


req = requests.get(url)

result = req.json()

rates = result['conversion_rates'].keys()


def convertor():

    amount = float(amount_entry.get())

    new_amount = amount * result['conversion_rates'][lst.get(ACTIVE)]

    answer['text'] = new_amount


l1_convertor = Label(windows, text="Converting US Currency To Others", bg="grey", fg="black", font=("bold", 12))
l1_convertor.grid(row=0, column=6)

currency = IntVar(windows)
currency1 = IntVar(windows)

amount = Label(text="Amount:", bg="pink", fg="black", font=("bold", 12))
amount.grid(row=3, column=0)

amount_entry = Entry(windows)
amount_entry.grid(row=3, column=6)


currency = Label(text="To Currency:", bg="pink", fg="black", font=("bold", 12))
currency.grid(row=5, column=0)
lst = Listbox(windows, width=20)
for i in rates:
    lst.insert(END, str(i))
lst.grid(row=5, column=6)

btn = Button(windows, text="Convert", font=("bold", 12), command=convertor)
btn.grid(row=6, column=6)

answer = Label(windows, font=('bold', 12))
answer.grid(row=8, column=6)


windows.mainloop()
