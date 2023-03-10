"""
This module is an implementation of the book Quantitative Investment Analysis, DeFusco, McLeavey, Pinto, Runkle, Second Edition, CFA Institute Investment Series, Wiley Publishing.
You can find the 3rd edition of this book available here: https://www.wiley.com/en-gb/Quantitative+Investment+Analysis%2C+3rd+Edition-p-9781119104599
"""
import panel as pn
import pandas as pd
import numpy as np
import holoviews as hv
import param as pm
import math



# Chapter 1 The Time Value of Money
from qia.interest_rate import InterestRate
from qia.cashflow import CashFlow, CompoundingCashFlow


# Chapter 2 Discounted Cash Flow Operations
from qia.net_present_value import NetPresentValue