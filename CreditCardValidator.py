# -*- coding: utf-8 -*-
"""
Created on 16 Feb 2020; edited on 22 Jun 2020
Name: CreditCardValidator.py
Purpose: Determines whether a number is a valid credit card number (Luhn's algorithm)
@author: Charles Umesi (charlesumesi)
"""

def credit_card_validator():
    
    '''Based on the Luhn formula'''
    '''This version uses https://en.wikipedia.org/wiki/Luhn_algorithm'''
    
    # Entering of credit card number
    enter_number = input('Enter credit card number (with no spaces) : ')
    
    # Implementing formula
    l = [k for k in enter_number]
    m = l[::-1]
    n = [str(2*int(i)) for i in m[1::2]]
    o = m[0::2]
    p = ''.join(n)
    q = [j for j in p]
       
    r = 9*(sum(list(map(int, q))) + sum(list(map(int, o))))
        
    if r%10 == 0: print('The number entered is a valid credit card number.')
    else: print('The number entered is not a valid credit card number.')
    del(l,m,n,o,p,q)

if __name__ == '__main__':
    credit_card_validator()
