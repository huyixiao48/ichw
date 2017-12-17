#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

__author__ = "胡奕潇"
__pkuid__  = "1700011716"
__email__  = "1700011716@pku.edu.cn"
"""


"""Part A Currency Query."""


def analysis(currency_from, currency_to, amount_from):
    """Return: a JSON string contains all the information we need.
    
    Parameter currency_from: the currency on hand.
    Precondition: currency_from is a string.
    
    Parameter currency_to: the currency to convert to.
    Precondition: currency_to is a string.
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a string but can be some 
    other things like a float."""
    str_amount_from = str(amount_from)
    web = "http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=" + \
    currency_from + "&to=" + currency_to + "&amt=" + str_amount_from
    from urllib.request import urlopen
    doc = urlopen(web)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return(jstr)


"""Part B Processing a JSON String"""


def valid(js):
    """judge whether the datas input is valid.
    Parameter js: 
    in the form'{"from":"*","to":"*","success": *, "error":"*"}'
    """
    if "invalid" not in js:
        return(cal(js))
    else:
        return(oput(js))
    
    
def cal(js):
    """Return: amount of currency received in the given exchange.
    The value returned has type float.
    
    Parameter js: 
    in the form
    '{"from":"<old-amt>","to":"<new-amt>","success": true, "error":""}'
    """
    L = len(js)
    J = js[:(L-34)]+" }"
    j = eval(J)
    jfinal = j["to"]
    K = jfinal.split()
    k = float(K[0])
    return(k)


def oput(js):
    """Return: problem reports.
    
    Paramter js:
    in the form
    '{"from":"","to":"","success":false,"error":"* is invalid."}'"""
    if "Source currency code is invalid." in js:
        return("Source currency code is invalid.")
    elif "Currency amount is invalid." in js:
        return("Currency amount is invalid.")
    elif "Exchange currency code is invalid." in js:
        return("Exchange currency code is invalid.")
    else:
        return("unknow problems")

    
"""Part C Currency Exchange"""


def main():   
    cfrom = input("the currency on hand")
    cto = input("the currency convert to")
    afrom = input("amount of currency to convert"))
    fij = analysis(cfrom, cto, afrom)
    print(valid(fij))
    

if __name__ == '__main__':
    main()

    
"""Part D Test"""

def exchange(currency_from, currency_to, amount_from):
    """As is required by the problem given by the teacher.
    Also provide a way to test the functions.
    
    Returns: amount of currency received in the given exchange.
    
    The value returned has type float. 

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    x = analysis(currency_from, currency_to, amount_from)
    return(cal(x))


def invalidproblem(currency_from, currency_to, amount_from):
    """Provide a way to test the functions.
    Returns: problem reports."""
    x = analysis(currency_from, currency_to, amount_from)
    return(oput(x))


def test_exchange1():
    assert(2.0952375 == exchange("USD","EUR", 2.5))

    
def test_exchange2():
    assert(1 == exchange("CNY","CNY", 1))

    
def test_invalidproblem():
    assert("Currency amount is invalid." == \
           invalidproblem("USD","CNY","PIG"))
    
    
def test_all():
    """test all cases"""
    test_exchange1()
    test_exchange2()
    test_invalidproblem()
    print("All tests passed")