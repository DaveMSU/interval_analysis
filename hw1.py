from lib import Interval, solve_equation


def main():
    As = Interval(*[float(a) for a in input("Write interval borders for coef 'a' coef: ").split()])  # exmpl: 1, 2
    Bs = Interval(*[float(b) for b in input("Write interval borders for coef 'b' coef: ").split()])  # exmpl: 4, 6
    Cs = Interval(*[float(c) for c in input("Write interval borders for coef 'c' coef: ").split()])  # exmpl: -8, -5

    X1s, X2s = solve_equation(As, Bs, Cs)

    print("Analitic solution:")
    print("x1:", X1s)
    print("x2:", X2s)

    N = int(input("Number of sampels in aproximity steps: "))  # 10, 100, 1000, 10000
    x1_history, x2_history = [], []
    for _ in range(N):
        a = As.sample()
        b = Bs.sample()
        c = Cs.sample()

        x1, x2 = solve_equation(a, b, c)

        x1_history.append(x1)
        x2_history.append(x2)

    print("Aproximity solution:")
    print("x1:", min(x1_history), max(x1_history))    
    print("x2:", min(x2_history), max(x2_history))    


if __name__ == "__main__":
    main()
