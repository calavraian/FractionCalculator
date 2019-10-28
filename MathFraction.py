'''
Created on Oct 28, 2019

@author: calavraian
'''

from enum import Enum


class Operators(Enum):
    PLUS = "+"
    MINUS = "-"
    TIMES = "*"
    SLASH = "/"
    ALL = "+-*/"

class Fraction():
    def __init__(self, whole, numerator, denominator):
        self.whole = whole
        self.numerator = numerator
        self.denominator = abs(denominator)
    
    def description(self):
        return "{{ Whole: {}, Numerator: {}, Denominator: {} }}".format(self.whole, self.numerator, self.denominator)

    def improper(self):
        return Fraction(0, self.denominator*self.whole+self.numerator, self.denominator)
    
    def __str__(self):
        if self.whole == 0:
            return "{}/{}".format(self.numerator, self.denominator)

        return "{}_{}/{}".format(self.whole, self.numerator, self.denominator)

def error(errorText="Invalid sequence operation"):
    print("Error: {}, execution terminated...".format(errorText))
    raise SystemExit
    
def createFraction(element):
    if not element:
        error("No fraction specified")
    
    wholeSplit = element.split("_")
    try:
        wholeValue = int(wholeSplit[0])
        if len(wholeSplit) == 1:
            return Fraction(wholeValue, 0, 1)
        elif len(wholeSplit) > 2:
            error()
        del wholeSplit[0]
    except ValueError:
        wholeValue = 0
    
    fracItems = wholeSplit[0].split("/")
    if len(fracItems) != 2:
        error()
    
    try:
        numerator = int(fracItems[0])
        denominator = int(fracItems[1])
    except ValueError:
        error()
        
    return Fraction(wholeValue, numerator, denominator)

def main():
    opElements = list(filter(lambda x: x.strip(), input("Operation> ").split(" ")))
    fraction = createFraction(opElements[0])
    print(type(fraction))
    print(fraction)

if __name__ == '__main__':
    main()
