import typing as tp

import numpy as np

from lib import Interval, merge_list_of_intervals, solve_equation


def main():
    As = Interval(*[float(a) for a in input("Write interval borders for coef 'a' coef: ").split()])  # exmpl: 1, 2
    Bs = Interval(*[float(b) for b in input("Write interval borders for coef 'b' coef: ").split()])  # exmpl: 4, 6
    Cs = Interval(*[float(c) for c in input("Write interval borders for coef 'c' coef: ").split()])  # exmpl: -8, -5

    p = int(input("Number of splits: "))

    _locals = locals()
    borders = {
        var: np.linspace(
            start=_locals[var].left_border,
            stop=_locals[var].right_border,
            num=p+1
        )
        for var in ["As", "Bs", "Cs"]
    }

    intervals_dict = [
        {
            var: Interval(borders[var][i], borders[var][i+1])
            for var in ["As", "Bs", "Cs"]
        }
        for i in range(p)
    ]

    X1: tp.List[Interval] = []
    X2: tp.List[Interval] = []

    for i in range(p):
        for j in range(p):
            for k in range(p):
                As_i = intervals_dict[i]["As"]
                Bs_j = intervals_dict[j]["Bs"]
                Cs_k = intervals_dict[k]["Cs"]
                
                X1s, X2s = solve_equation(As_i, Bs_j, Cs_k)
                X1.append(X1s)
                X2.append(X2s)

    X1s: tp.Interval = merge_list_of_intervals(X1)
    X2s: tp.Interval = merge_list_of_intervals(X2)

    print("Analitic solution:")
    print("x1: ", X1s)
    print("x2: ", X2s)


if __name__ == "__main__":
    main() 
