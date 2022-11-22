import re

def checkInput():
    x = input("Enter a number: ")
    if x.isdigit():
        return num2rom(int(x))
    else:
        if bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", x)):
            return rom2int(x)
        else:
            print("Incorrect value")

slownik1 = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}      

def num2rom(x):
    result = ''

    while x > 0:
        for i, j in slownik1.items():
            while x >= i:
                result += j
                x -= i
    return result

slownik2 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def rom2int(x):
        wynik = 0

        for i in range(len(x)):
            if i > 0 and slownik2[x[i]] > slownik2[x[i - 1]]:
                wynik += slownik2[x[i]] - 2 * slownik2[x[i - 1]]
            else:
                wynik += slownik2[x[i]]
        return wynik

print(checkInput())