import customtkinter as ctk


def get_rebalancing_etf1(price_1: float, deposit: float, current_value1: float,
                         current_value2: float, weight_1: int) -> float:
    weight1_percent = weight_1 / 100.0
    numerator = weight1_percent * (
            deposit + current_value1 + current_value2) - current_value1
    return numerator / price_1


def get_rebalancing_etf2(price_2: float, deposit: float, current_value1: float,
                         current_value2: float, weight_1: int) -> float:
    weight1_percent = weight_1 / 100.0
    numerator = ((deposit + current_value1) * (1.0 - weight1_percent)) - (
            weight_1 * current_value2)
    return numerator / price_2


def update_slider_label(value: float) -> None:
    ganze_zahl = int(value)
    label_slider_value.configure(text=f"{ganze_zahl} %")


# def calculate_rebalancing():


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ctk.set_appearance_mode("System")

    app = ctk.CTk()
    app.title("Rebalancing for two ETFs")
    app.geometry("500x400")

    # Show text for description, entry fields and slider
    all_texts = ["ETF 1 Wert:", "ETF 1 Kurs:", "ETF 2 Wert:", "ETF 2 Kurs:",
                 "Einzahlung:", "Anteil (Gewichtung) ETF 1:"]
    entry_values = [0] * 7
    for i in range(0, len(all_texts)):
        ctk.CTkLabel(app, text=all_texts[i]).grid(row=i, column=0, padx=20, pady=10)

        if i != (len(all_texts) - 1):
            entry_values[i] = ctk.CTkEntry(app)
            entry_values[i].grid(row=i, column=1, padx=20, pady=10)
        else:
            slider = ctk.CTkSlider(app, from_=0, to=100, command=update_slider_label)
            slider.grid(row=5, column=1, padx=20, pady=10)
            slider.set(50)  # Startwert auf 50 setzen

    label_slider_value = ctk.CTkLabel(app, text="50 %")
    label_slider_value.grid(row=5, column=2, padx=10)

    # Calculate Button
    btn_calc = ctk.CTkButton(app, text="Berechnen", command=calculate)
    btn_calc.grid(row=6, column=0, columnspan=2, pady=20)

    # Show result
    label_result = ctk.CTkLabel(app, text="Ergebnis: -", font=("Arial", 16, "bold"))
    label_result.grid(row=7, column=0, columnspan=2, pady=10)

    app.mainloop()
