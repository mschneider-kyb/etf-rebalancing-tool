import customtkinter as ctk


def get_rebalancing_etf1(current_value1: float, price1: float, current_value2: float,
                         _, deposit: float, weight1: int) -> float:
    weight1_percent = weight1 / 100.0
    numerator = weight1_percent * (
            deposit + current_value1 + current_value2) - current_value1
    return numerator / price1


def get_rebalancing_etf2(current_value1: float, _, current_value2: float,
                         price2: float, deposit: float, weight1: int) -> float:
    weight1_percent = weight1 / 100.0
    numerator = ((deposit + current_value1) * (1.0 - weight1_percent)) - (
            weight1_percent * current_value2)
    return numerator / price2


def get_break_even(current_value1: float, _, current_value2: float, __, ___,
                   weight1: int, share1: float, share2: float) -> float:
    weight1_percent = weight1 / 100.0
    if share1 < 0 and weight1_percent != 0.0:
        return (current_value1 / weight1_percent) - current_value1 - current_value2
    elif share2 < 0 and weight1_percent != 0.0:
        return ((weight1_percent * current_value2) / (
                1.0 - weight1_percent)) - current_value1
    else:
        return 0.0


def calculate() -> None:
    try:
        # get values and compute result
        entry_values = [float(entry.get().replace(",", ".")) for entry in
                        entry_entities]

        # validate values
        if any(n < 0 for n in entry_values):
            label_result.configure(text="Fehler: Werte dürfen nicht negativ sein!",
                                   text_color="red")
            return

        # do calculations
        share1 = get_rebalancing_etf1(*entry_values, slider.get())
        share2 = get_rebalancing_etf2(*entry_values, slider.get())
        break_even = get_break_even(*entry_values, slider.get(), share1, share2)

        # show result
        if break_even > 0.0:
            label_result.configure(
                text=f"Ergebnis (neg = verkaufen, pos = kaufen):\nAnteil ETF 1 = "
                     f"{share1:.2f}\nAnteil ETF 2 = {share2:.2f}\nFür break-even muss "
                     f"mindestens {break_even: .2f} investiert werden.",
                text_color="white")
        else:
            label_result.configure(
                text=f"Ergebnis (neg = verkaufen, pos = kaufen):\nAnteil ETF 1 = "
                     f"{share1:.2f}\nAnteil ETF 2 = {share2:.2f}", text_color="white")

    except ValueError:
        label_result.configure(text="Fehler: Bitte nur Zahlen!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ctk.set_appearance_mode("System")

    app = ctk.CTk()
    app.title("Rebalancing for two ETFs")
    app.geometry("600x550")

    # show text for description, entry fields and slider
    all_texts = ["ETF 1 Wert:", "ETF 1 Kurs:", "ETF 2 Wert:", "ETF 2 Kurs:",
                 "Einzahlung:", "Anteil (Gewichtung) ETF 1:"]
    entry_entities = []
    slider_var = ctk.IntVar(value=70)

    for i in range(0, len(all_texts)):
        ctk.CTkLabel(app, text=all_texts[i]).grid(row=i, column=0, padx=20, pady=10)

        if i != (len(all_texts) - 1):
            entry = ctk.CTkEntry(app)
            entry.grid(row=i, column=1, padx=20, pady=10)
            entry_entities.append(entry)
        else:
            slider = ctk.CTkSlider(app, from_=0, to=100, number_of_steps=100,
                                   variable=slider_var)
            slider.grid(row=5, column=1, padx=20, pady=10)

            label_slider_value = ctk.CTkLabel(app, textvariable=slider_var)
            label_slider_value.grid(row=5, column=2, padx=10)

    label_slider_value = ctk.CTkLabel(app, textvariable=slider_var)
    label_slider_value.grid(row=5, column=2, padx=10)

    # calculate Button
    btn_calc = ctk.CTkButton(app, text="Berechnen", command=calculate)
    btn_calc.grid(row=6, column=0, columnspan=2, pady=20)

    # show result
    label_result = ctk.CTkLabel(app, text="Ergebnis (neg = verkaufen, pos = kaufen): -",
                                font=("Arial", 16, "bold"))
    label_result.grid(row=7, column=0, columnspan=2, pady=25)

    app.mainloop()
