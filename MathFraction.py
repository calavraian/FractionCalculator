'''
Created on Oct 28, 2019

@author: calavraian
'''

class Fraction():
    def __init__(self, whole, numerator, denominator):
        self.whole = whole
        self.numerator = numerator
        self.denominator = abs(denominator)
    
    def __str__(self):
        return "{}_{}/{}".format(self.whole, self.numerator, self.denominator)

def main():
    opElements = list(filter(lambda x: x.strip(), input("Operation> ").split(" ")))
    print(opElements)

if __name__ == '__main__':
    main()
