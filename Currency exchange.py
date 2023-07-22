from tkinter import *
import requests

master = Tk()
txt = StringVar(master)
cu = StringVar(master)
currencies = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "SGD", "HKD", "CNY", "KRW"]
MYR = ["MYR"]

# connect to open exchange endpoint to get real-time exchange rate.

API_ENDPOINT = ""
API_KEY = ""

entry = Entry(master)


def exchange():
    response = requests.get(API_ENDPOINT, params={"app_id": API_KEY})
    if response.status_code != 200:
        return "Error in getting the last exchange rate."

    exchange_rates = response.json().get("rates")
    if not exchange_rates:
        return "Error in getting the exchange rate."
    c_value = entry.get()
    if not c_value.replace('.', '', 1).isdigit():
        txt.set("Please make sure you enter numeric values")  # control the user input
    else:
        c_value = float(c_value) / exchange_rates.get(MYR[0])  # convert from MYR to USD

    if cu.get() == currencies[0]:
        value = c_value * exchange_rates.get(currencies[0])
    elif cu.get() == currencies[1]:
        value = c_value * exchange_rates.get(currencies[1])
    elif cu.get() == currencies[2]:
        value = c_value * exchange_rates.get(currencies[2])
    elif cu.get() == currencies[3]:
        value = c_value * exchange_rates.get(currencies[3])
    elif cu.get() == currencies[4]:
        value = c_value * exchange_rates.get(currencies[4])
    elif cu.get() == currencies[5]:
        value = c_value * exchange_rates.get(currencies[5])
    elif cu.get() == currencies[6]:
        value = c_value * exchange_rates.get(currencies[6])
    elif cu.get() == currencies[7]:
        value = c_value * exchange_rates.get(currencies[7])
    elif cu.get() == currencies[8]:
        value = c_value * exchange_rates.get(currencies[8])
    else:
        value = c_value * exchange_rates.get(currencies[9])
    txt.set(f"The value of exchange is: {round(value, 1)} {cu.get()}")


def gui():
    cu.set(currencies[0])
    w = OptionMenu(master, cu, *currencies)
    master.title("Currency Exchange")
    master.geometry("450x200")
    Label(master, text=" Select the currency: ", padx=10, font=("Arial", 12)).grid(row=0, sticky=W)
    Label(master, text=" Enter the value: ", padx=10, font=("Arial", 12)).grid(row=1, sticky=W)
    Label(master, text=" MYR ", padx=10, font=("Arial", 8)).grid(row=1, column=2, sticky=W)
    Click_result = Button(master, text="Exchange", command=exchange, bg='blue', fg='white', font=("Arial", 12))
    result = Label(master, text="", textvariable=txt)
    w.grid(row=0, column=1, sticky=W)
    entry.grid(row=1, column=1, sticky=W)
    Click_result.grid(row=2, column=1, sticky=W)
    result.grid(row=3, column=1, sticky=W)
    mainloop()


if __name__ == "__main__":
    gui()
