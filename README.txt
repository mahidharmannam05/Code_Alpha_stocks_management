============================================================
STOCKS MANAGEMENT - README
============================================================

DESCRIPTION
-----------
A simple Python program that calculates the total investment
value of a set of stocks. The user enters how many stocks they
want to calculate, then the name and quantity of each stock.
The program looks up each stock's price from a built-in price
list and prints the total investment amount.


FILE
----
stocks_management.py


REQUIREMENTS
------------
- Python 3.6 or higher (uses f-strings)
- No external libraries needed


AVAILABLE STOCKS AND PRICES
---------------------------
Stock Name    Price per Share
----------    ---------------
APPLE         180
GOOGLE        130
TATA          140

(Prices are stored in the 'stocks' dictionary at the top of
the script and can be edited or extended.)


HOW TO RUN
----------
1. Open a terminal or command prompt.
2. Go to the folder containing the file.
3. Run:

       python stocks_management.py


HOW IT WORKS
------------
1. The program asks for the number of stocks to enter.
2. For each stock, it asks for:
   - The stock name (not case-sensitive; it is converted to
     uppercase automatically)
   - The quantity purchased
3. If the stock exists in the price list, it calculates
   (price x quantity) and adds it to the investment list.
4. If the stock is not found, it prints "Stocks not found!"
   and moves on to the next entry.
5. At the end, it prints the sum of all valid investments.


EXAMPLE
-------
Input:
    Enter no of stocks:2
    Enter name of stock:apple
    Enter quantity APPLE:10
    Enter name of stock:tata
    Enter quantity TATA:5

Output:
    Total investment
    ----------------
    2500

Calculation: (180 x 10) + (140 x 5) = 1800 + 700 = 2500


NOTES AND LIMITATIONS
---------------------
- Stock prices are fixed (hard-coded) and are not fetched
  from the internet.
- Entering a non-numeric value for the number of stocks or
  the quantity will cause the program to stop with an error.
- A stock that is not found still uses up one of the entries
  you specified at the start.


POSSIBLE IMPROVEMENTS
---------------------
- Add input validation for numbers.
- Let the user add or update stock prices.
- Show a per-stock breakdown along with the total.
- Fetch live stock prices from an API.


============================================================
