import customtkinter as ctk


def get_rebalancing_etf1(current_value1: float, price_1: float, current_value2: float,
                         _, deposit: float, weight_1: int) -> float:
    weight1_percent = weight_1 / 100.0
    numerator = weight1_percent * (
            deposit + current_value1 + current_value2) - current_value1
    return numerator / price_1


def get_rebalancing_etf2(current_value1: float, _, current_value2: float,
                         price_2: float, deposit: float, weight_1: int) -> float:
    weight1_percent = weight_1 / 100.0
    numerator = ((deposit + current_value1) * (1.0 - weight1_percent)) - (
            weight_1 * current_value2)
    return numerator / price_2


def calculate_rebalancing() -> None:
    try:
        entry_values = [float(entry.get()) for entry in entry_entities]
        share_1 = get_rebalancing_etf1(*entry_values, slider.get())
        share_2 = get_rebalancing_etf2(*entry_values, slider.get())
        # Ergebnis in der GUI anzeigen
        label_result.configure(
            text=f"Ergebnis (neg = verkaufen, pos = kaufen): Anteil ETF 1 = "
                 f"{share_1:.2f}, Anteil ETF 2 = {share_2:.2f}")

    except ValueError:
        label_result.configure(text="Fehler: Bitte nur Zahlen!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ctk.set_appearance_mode("System")

    app = ctk.CTk()
    app.title("Rebalancing for two ETFs")
    app.geometry("500x400")

    # Show text for description, entry fields and slider
    all_texts = ["ETF 1 Wert:", "ETF 1 Kurs:", "ETF 2 Wert:", "ETF 2 Kurs:",
                 "Einzahlung:", "Anteil (Gewichtung) ETF 1:"]
    entry_entities = []
    slider_var = ctk.IntVar(value=50)

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

    # Calculate Button
    btn_calc = ctk.CTkButton(app, text="Berechnen", command=calculate_rebalancing)
    btn_calc.grid(row=6, column=0, columnspan=2, pady=20)

    # Show result
    label_result = ctk.CTkLabel(app, text="Ergebnis (neg = verkaufen, pos = kaufen): -",
                                font=("Arial", 16, "bold"))
    label_result.grid(row=7, column=0, columnspan=2, pady=10)

    app.mainloop()
