# Ajumma's Fast Food Ordering System (CLI)

[![Check](https://github.com/jadenchua-dot/python-terminal-shop/actions/workflows/check.yml/badge.svg)](https://github.com/jadenchua-dot/python-terminal-shop/actions/workflows/check.yml)

A command-line ordering app for a fast food counter, written in plain Python 3. You browse a categorised menu, build a cart, edit it, apply a discount and pay with 9% GST, then get a shot at a lucky draw.

## Features

- **Menu by category:** burgers, sides, drinks, desserts and combos, each item with a short code (`B01`, `S03`, `C02`...).
- **Cart:** add items in any quantity. Ordering the same item again adds to its existing line instead of creating a duplicate.
- **Edit the cart:** change a quantity by item code, or set it to 0 to remove the item.
- **Discounts and GST:** student 10%, staff 8% or loyalty member 5%, then 9% GST on the discounted amount.
- **Lucky draw:** after an order is placed, guess a number from 1 to 10 to win free fries.
- **Input checks:** every prompt rejects invalid choices, codes and quantities and asks again.

## Run it

Needs Python 3.10 or newer. No packages to install.

```bash
git clone https://github.com/jadenchua-dot/python-terminal-shop.git
cd python-terminal-shop
python3 shopping_cart.py
```

On Windows, use `python shopping_cart.py` (or `py shopping_cart.py`).

## Example

```text
---FAST FOOD ORDERING SYSTEM---
Welcome to Ajumma's Shop
1. Add items into cart
2. View Menu
3. View Shopping Cart
4. Exit

------------------ CHECK OUT ---------------------
       Qty  Item Name               Price(Each)
--------------------------------------------------
   1.  3x  Classic Beef Burger      $5.50
--------------------------------------------------
Subtotal (before discount & GST):   $16.50
Discount Amount:                    $1.65
GST Amount (9% GST):                $1.34
Final Payable Amount:               $16.19
```

## How the code is organised

| Function | What it does |
|---|---|
| `final()` | Main loop: shows the main menu and routes each option |
| `view_menu()`, `print_category()` | Browse the menu without ordering |
| `choose_cat()`, `item()` | Pick a category, then an item code and quantity, and add it to the cart |
| `add_shopping_bag()`, `for_cart()` | Show the cart and its options (edit, keep shopping, check out) |
| `for_editing_cart()` | Change or remove a cart line by item code |
| `check_out()` | Discount, GST, final total and order confirmation |
| `lucky_draw()` | The number-guessing mini game |

The menu is one nested dictionary at the top of `shopping_cart.py`, so adding an item or a category only means adding an entry there.

## Tests

GitHub Actions places a scripted order on Python 3.10 to 3.13 on every push and checks the cart and the final amount ([workflow](.github/workflows/check.yml)).
