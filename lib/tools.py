import typing as tp

from .intervals import Interval


def merge_list_of_intervals(
    intervals_list: tp.List[Interval],
    test_coverage: bool = True
) -> Interval:
    """
    [(2.0, 3.0), (1.5, 2.5), (2.99, 5.1)] -> 
     -> (1.5, 5.1)
    """
    
    if test_coverage:
        sorted_intervals_list = sorted(
            intervals_list,
            key=lambda scope: scope.left_border
        )
        curr_right_border = sorted_intervals_list[0].right_border
        for interval in sorted_intervals_list[1:]:
            assert interval.left_border < curr_right_border
            curr_right_border = interval.right_border

    most_left_border = intervals_list[0].left_border
    most_right_border = intervals_list[0].right_border

    for interval in intervals_list:
        most_left_border = min(most_left_border, interval.left_border)
        most_right_border = max(most_right_border, interval.right_border)

    return Interval(
        left_border=most_left_border,
        right_border=most_right_border
    )
        

def solve_equation(
        a: tp.Union[Interval, float],
        b: tp.Union[Interval, float],
        c: tp.Union[Interval, float]
) -> tp.Tuple[tp.Union[Interval, float], tp.Union[Interval, float]]:
    """
    a*x^2 + b*x + c = 0
    :return: x1, x2
    """
    D = (b**2.0 - 4.0*a*c)**0.5
    x1 = -(D + b) / 2.0 / a
    x2 = (D - b) / 2.0 / a
    return [x1, x2]
