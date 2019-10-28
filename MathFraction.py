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

def createSequence(listItems):
    if not listItems:
        error("No operation sequence specified")
    
    if len(listItems) < 3:
        error("Operation sequence not valid, only {} elements found, expected 3 at least".format(len(listItems)))
    
    lookingOp = False
    sequence = []
    for item in listItems:
        if lookingOp:
            if item not in Operators.ALL.value:
                error("Invalid operator: {}".format(item))
            sequence.append(Operators(item))
            lookingOp = False
        else:
            sequence.append(createFraction(item))
            lookingOp = True
    
    return sequence

def main():
    opElements = list(filter(lambda x: x.strip(), input("Operation> ").split(" ")))
    sequence = createSequence(opElements)
    for elem in sequence:
        print(elem)

if __name__ == '__main__':
    main()
