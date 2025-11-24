# SHIVANSH-SRIVASTAVA
This Python script simulates the Sai Krishna Restaurant Billing System. It manages menu display, bill calculation, and conditional offers. The system grants a 50% discount to senior citizens, calculates 5% GST and 3% service charges, and provides complimentary items (e.g., Ice Cream) based on the total bill, all with clear, colorful console output.
# 🍔 SAI KRISHNA RESTAURANT BILLING SYSTEM

This is a simple console-based restaurant billing system developed in Python. It calculates the final bill amount, including GST and a service charge, and applies a significant discount for senior citizens. It also offers complimentary items based on the total bill amount.

## ✨ Features

* **Colorful Console Output:** Uses ANSI escape codes to enhance readability with colors.
* **Menu Display:** Shows a static menu of food items and their prices.
* **Senior Citizen Discount:** Automatically applies a **50% discount** to the original bill amount for senior citizens.
* **Tax Calculation:** Applies **5% GST** and a **3% Service Charge** to the original bill amount.
* **Complimentary Items:** Provides free items based on the total bill amount:
    * Bill > ₹500: **Ice Cream**
    * Bill > ₹700: **French Fries** and **Ice Cream**
* **Clear Output:** Clears the console screen before displaying the header and the final bill summary for a clean interface.

## 🛠️ Requirements

* **Python 3.x**
* This script uses the `os` and `time` standard Python libraries, which are generally available on most systems.

## 🚀 How to Run

1.  **Save the Code:** Save the provided Python code into a file named `billing_system.py`.
2.  **Open Terminal:** Open your terminal or command prompt.
3.  **Execute the Script:** Run the file using the Python interpreter:

    ```bash
    python billing_system.py
    ```

4.  **Follow Prompts:** The system will guide you through the billing process:
    * Enter the **total bill amount** (you'll need to manually calculate this based on the menu and quantity).
    * Answer whether the customer is a **senior citizen** (`yes` or `no`).

## ⚙️ Logic Summary

The core logic of the `restaurant_billing` function is as follows:

| Calculation | Formula / Condition | Notes |
| :--- | :--- | :--- |
| **Discount** | `amount * 0.50` if Senior Citizen is 'yes' | 50% discount on the original amount. |
| **GST** | `amount * 0.05` | 5% tax applied to the original amount. |
| **Service Charge** | `amount * 0.03` | 3% service charge applied to the original amount. |
| **Final Amount** | `amount - discount + gst + service_charge` | The final total the customer must pay. |
| **Complimentary** | If `amount > 700`: French Fries & Ice Cream | Based on the pre-discount original bill amount. |
| **Complimentary** | If `amount > 500`: Ice Cream | Based on the pre-discount original bill amount. |

## 📁 File Structure
billing_system.py # The main Python script

## 🧑‍💻 Code Snippets (Key Functions)

### Header Function

```python
def header():
    print(MAGENTA + "============================================")
    print("      WELCOME TO SAI KRISHNA RESTAURANT")
    print("============================================" + RESET)
Main Billing Logic
Python
def restaurant_billing():
    # ... code ...
    # ----- DISCOUNT -----
    discount = 0
    if senior == "yes":
        discount = amount * 0.50

    # ----- TAX AND SERVICE CHARGE -----
    gst = amount * 0.05       # 5% GST
    service_charge = amount * 0.03  # 3% service charge

    total_amount = amount - discount + gst + service_charge
    # ... code ...

