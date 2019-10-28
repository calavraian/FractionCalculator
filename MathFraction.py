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
    """
    A class to represent fraction objects with or without wholes.
    
    Attributes:
        whole: <int> the whole number of the fraction
        numerator: <int> the numerator number of the fraction
        denominator: <int> the denominator number of the fraction
    """

    def __init__(self, whole, numerator, denominator):
        self.whole = whole
        self.numerator = numerator
        self.denominator = abs(denominator)
    
    def description(self):
        return "{{ Whole: {}, Numerator: {}, Denominator: {} }}".format(self.whole, self.numerator, self.denominator)

    def improper(self):
        return Fraction(0, self.denominator*self.whole+self.numerator, self.denominator)
    
    def shorten(self):
        nwhole = self.whole + (self.numerator // self.denominator)
        nnumerator = abs(self.numerator) % self.denominator
        ndenominator = self.denominator

        return Fraction(nwhole, nnumerator, ndenominator)

    def __str__(self):
        if self.numerator == 0:
            return "{}".format(self.whole)

        if self.whole == 0:
            return "{}/{}".format(self.numerator, self.denominator)

        return "{}_{}/{}".format(self.whole, self.numerator, self.denominator)

class Operations():
    """
    Class on charge to handle the valid operation supported with fractions,
    all methods are static.
    
    Methods:
        add: Sum two Fraction instance and return a reduced fraction object
        subtract: Rest the second fraction to first first fraction parameters
        multiply: Multiply the two fractions specified
        divide: Divide the first fraction (dividend) by the second (divisor)
    """
    
    @staticmethod
    def add(frac1, frac2):
        impFrac1 = frac1.improper()
        impFrac2 = frac2.improper()
        
        numerator = (impFrac1.numerator*impFrac2.denominator) + (impFrac1.denominator*impFrac2.numerator)
        denominator = impFrac1.denominator*impFrac2.denominator
        
        return Fraction(0, numerator, denominator).shorten()

    @staticmethod
    def subtract(frac1, frac2):
        impFrac1 = frac1.improper()
        impFrac2 = frac2.improper()
        
        numerator = (impFrac1.numerator*impFrac2.denominator) - (impFrac1.denominator*impFrac2.numerator)
        denominator = impFrac1.denominator*impFrac2.denominator
        
        return Fraction(0, numerator, denominator).shorten()

def error(errorText="Invalid sequence operation"):
    print("Error: {}, execution terminated...".format(errorText))
    raise SystemExit
    
def createFraction(element):
    """
    Creates a Fraction instance from a given string, the valid format of an input is:
        <int>/<int> for fraction
        <int>_<int>/<int> for whole with fractions
        <int> just for a whole representation
    If not valid fraction is received then it raises and error with the problem found.
    
    Parameters:
        element: <str> a single fraction representation
    Return:
        Return a <Fractions> instance
    """

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
    """
    Creates a valid operation sequence with Fraction and Operators instance,
    this function also clean an extra operators at the end or beginning of the
    sequence, if not valid sequence is found then it raises and error with the
    problem found.
    
    Parameters:
        listItems: <list> of <str> list of all operands and operators as a string objects
    Return:
        Return a <list> of <Fractions> and <Operators>
    """

    if not listItems:
        error("No operation sequence specified")
    
    if len(listItems) < 3:
        error("Operation sequence not valid, only {} elements found, expected 3 at least".format(len(listItems)))
    
    while len(listItems) > 2 and listItems[0] in Operators.ALL.value:
        del listItems[0]
    
    while len(listItems) > 2 and listItems[-1] in Operators.ALL.value:
        del listItems[-1]

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
    print(Operations.subtract(sequence[0], sequence[2]))

if __name__ == '__main__':
    main()
