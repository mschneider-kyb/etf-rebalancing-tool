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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ctk.set_appearance_mode("System")

    app = ctk.CTk()
    app.title("Rebalancing for two ETFs")
    app.geometry("500x400")

    # First entry

    app.mainloop()
