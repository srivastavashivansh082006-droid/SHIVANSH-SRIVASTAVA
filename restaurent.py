import time
import os

# ---------- COLORS ----------
RESET = "\033[0m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"


# ---------- CLEAR SCREEN ----------
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ---------- HEADER ----------
def header():
    print(MAGENTA + "============================================")
    print("         WELCOME TO SAI KRISHNA RESTAURANT")
    print("============================================" + RESET)


# ---------- DISPLAY MENU ----------
def display_menu():
    print(CYAN + "\n----------- OUR MENU -----------" + RESET)
    print(" 1. DABBANG Burger            ₹120")
    print(" 2. UP 63 Pizza             ₹250")
    print(" 3.  WHITE SAUCE Pasta             ₹180")
    print(" 4. Cold Drink        ₹60")
    print(" 5. Coffee            ₹80")
    print("----------------------------------")


# ---------- MAIN BILLING SYSTEM ----------
def restaurant_billing():

    clear()
    header()
    display_menu()

    print(YELLOW + '\nEnter total bill amount (after adding food items from menu):' + RESET)
    amount = float(input(" → ₹ "))

    senior = input("\nIs the customer a senior citizen? (yes/no): ").lower()

    # ----- DISCOUNT -----
    discount = 0
    if senior == "yes":
        discount = amount * 0.50

    # ----- TAX AND SERVICE CHARGE -----
    gst = amount * 0.05       # 5% GST
    service_charge = amount * 0.03  # 3% service charge

    total_amount = amount - discount + gst + service_charge

    # ----- COMPLIMENTARY ITEMS -----
    complimentary = []

    if amount > 700:
        complimentary.append("French Fries (₹90)")
        complimentary.append('Ice Cream (₹50)')
    elif amount > 500:
        complimentary.append("Ice Cream(₹50)")

    # ----- PRINTING BILL -----
    clear()
    header()
    print(BLUE + "--------------- BILL SUMMARY ---------------" + RESET)
    print(f"Original Bill Amount      : ₹{amount:.2f}")
    print(f"Senior Discount (50%)     : ₹{discount:.2f}")
    print(f"GST (5%)                  : ₹{gst:.2f}")
    print(f"Service Charge (3%)       : ₹{service_charge:.2f}")
    print("--------------------------------------------")
    print(GREEN + f"FINAL AMOUNT TO PAY       : ₹{total_amount:.2f}" + RESET)
    print("--------------------------------------------\n")

    print(CYAN + "Complimentary Items :" + RESET)
    if complimentary:
        for item in complimentary:
            print(GREEN + f" ✔ {item}" + RESET)
    else:
        print(RED + "  ❌ No complimentary items." + RESET)

    print(MAGENTA + "\nThank you for  VISITING SAI KRISHNA  Restaurant!")
    print('😊😊😊 Please visit again 😊😊😊' + RESET)


# ---------- RUN PROGRAM ----------
restaurant_billing()
