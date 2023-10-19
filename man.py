# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2023/10/19 16:54

from sympy import *
from sympy.parsing.latex import parse_latex

latex_str = r"\frac{x^2 + \sqrt{5}}{\log y}"
expr = parse_latex(latex_str)
result = sympify(expr)
print(result)