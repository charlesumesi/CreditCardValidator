# CreditCardValidator
A short code for validating a credit card number
```python
def credit_card_validator():
    
    '''Based on the Luhn formula'''
    '''This version uses https://en.wikipedia.org/wiki/Luhn_algorithm'''
    
    # Entering of credit card number
    enter_number = input('Enter credit card number (with no spaces) : ')
    
    # Implementing formula
    l = [k for k in enter_number]
    ...
```
