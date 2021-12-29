import numpy as np
import pandas as pd
import scipy.optimize as opt
import scipy.interpolate as interp

def ro_daily(df):
    """
    Receives a dataframe with daily closed prices and returns the daily return
    Calculates the daily rate of return of a portfolio
    """
    d0 = df.pct_change().dropna(axis=0, how='any')

    return d0

def log_ro_daily(df):
    """
    Receives a dataframe with daily closed prices and returns the daily logarithmic return
    Calculates the daily rate of return of a portfolio
    """
    d0 = df.pct_change().dropna(axis=0, how='any')
    d0 = np.log(df) - np.log(df.shift(1))

    return d0
