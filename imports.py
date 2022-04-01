# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 17:31:05 2022

@author: Sergio
"""
import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat, unumpy as unp
from uncertainties.unumpy import nominal_values as nv, std_devs as sd
from uncertainties.umath import *
from scipy.optimize import curve_fit as cf
from scipy.optimize import curve_fit as cf
from scipy.odr import ODR, Model, RealData
import pandas as pd
import time
from tqdm import tqdm
from numpy.linalg import norm
import matplotlib.axes as axes
from uncertainties import ufloat, unumpy
from uncertainties import nominal_value as nv, std_dev as sd
