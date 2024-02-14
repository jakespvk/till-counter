from flask import Flask
from flask import request
from markupsafe import escape
import math

app = Flask(__name__)

#TOTAL_DOLLARS: int;
#TOTAL_ONES: int;
#TOTAL_FIVES: int;
#TOTAL_TENS: int;
#TOTAL_TWENTIES: int;
#TOTAL_FIFTIES: int;
#TOTAL_HUNDREDS: int;

def totalOnes(num: int):
    return 1 * num;

def totalFives(num: int):
    return 5 * num;

def totalTens(num: int):
    return 10 * num;

def totalTwenties(num: int):
    return 20 * num;

def totalFifties(num: int):
    return 50 * num;

def totalHundreds(num: int):
    return 100 * num;

@app.route("/")
def index():
    ones = str(escape(request.args.get("ones", "")))
    if (ones == ''):
        ones = 0
    fives = str(escape(request.args.get("fives", "")))
    if (fives == ''):
        fives = 0
    tens = str(escape(request.args.get("tens", "")))
    if (tens == ''):
        tens = 0
    twenties = str(escape(request.args.get("twenties", "")))
    if (twenties == ''):
        twenties = 0
    fifties = str(escape(request.args.get("fifties", "")))
    if (fifties == ''):
        fifties = 0
    hundreds = str(escape(request.args.get("hundreds", "")))
    if (hundreds == ''):
        hundreds = 0
    return ("""<form action="" method="get">
                <h1>Till Counter</h1>
                <label>One Dollar Bills:</label>
                <input type="text" name="ones"><br>
                <label>Five Dollar Bills:</label>
                <input type="text" name="fives"><br>
                <label>Ten Dollar Bills:</label>
                <input type="text" name="tens"><br>
                <label>Twenty Dollar Bills:</label>
                <input type="text" name="twenties"><br>
                <label>Fifty Dollar Bills:</label>
                <input type="text" name="fifties"><br>
                <label>Hundred Dollar Bills:</label>
                <input type="text" name="hundreds"><br>
                <input type="submit" value="Total"><br>
              </form>"""
            + "Total: $"
            + getTotal(ones, fives, tens, twenties, fifties, hundreds)
            )

@app.route("/<int:ones><int:fives><int:tens><int:twenties><int:fifties><int:hundreds>")
def getTotal(ones, fives, tens, twenties, fifties, hundreds):
    return str(totalOnes(int(ones)) + totalFives(int(fives)) + totalTens(int(tens)) + 
               totalTwenties(int(twenties)) + totalFifties(int(fifties)) + 
               totalFifties(int(fifties)) + totalHundreds(int(hundreds)))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
