'''
Created on Oct 28, 2019

@author: calavraian
'''

def main():
    opElements = list(filter(lambda x: x.strip(), input("Operation> ").split(" ")))
    print(opElements)

if __name__ == '__main__':
    main()
