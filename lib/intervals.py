import random
import typing as tp

import numpy as np


class Interval:
    def __init__(self, left_border: float, right_border: float):
        assert left_border <= right_border
        self._left_border = left_border
        self._right_border = right_border

    def __neg__(self) -> "Interval":
        return Interval(
            left_border=-self._right_border,
            right_border=-self._left_border
        )

    def __add__(
            self, 
            other: tp.Union["Interval", float]
    ) -> tp.Union["Interval", float]:
        if isinstance(other, Interval):
            return Interval(
                left_border=self._left_border + other._left_border,
                right_border=self._right_border + other._right_border
            )
        elif isinstance(other, float):
            return Interval(
                left_border=self._left_border + other,
                right_border=self._right_border + other
            )

    def __radd__(
            self, 
            other: tp.Union["Interval", float]
    ) -> tp.Union["Interval", float]:
        return self.__add__(other)

    def __sub__(
            self, 
            other: tp.Union["Interval", float]
    ) -> tp.Union["Interval", float]:
        return self.__add__(-other)

    def __rsub__(
            self, 
            other: tp.Union["Interval", float]
    ) -> tp.Union["Interval", float]:
        return self.__sub__(other)

    def __mul__(
            self, 
            other: tp.Union["Interval", float]
    ) -> tp.Union["Interval", float]:
        if isinstance(other, Interval):
            return Interval(
                left_border=min(
                    self._left_border * other._left_border,
                    self._left_border * other._right_border,
                    self._right_border * other._left_border,
                    self._right_border * other._right_border
                ),
                right_border=max(
                    self._left_border * other._left_border,
                    self._left_border * other._right_border,
                    self._right_border * other._left_border,
                    self._right_border * other._right_border
                )
            )
        elif isinstance(other, float):
            if other > 0.0:
                return Interval(
                    left_border=self._left_border * other,
                    right_border=self._right_border * other
                )
            else:
                return Interval(
                    left_border=self._right_border * other,
                    right_border=self._left_border * other
                )

    def __rmul__(
            self, 
            other: tp.Union["Interval", float]
    ) -> tp.Union["Interval", float]:
        return self.__mul__(other)

    def __truediv__(
            self, 
            other: tp.Union["Interval", float]
    ) -> tp.Union["Interval", float]:
        if isinstance(other, Interval):
            return self * Interval(
                left_border=1.0 / other._right_border,
                right_border=1.0 / other._left_border
            )
        elif isinstance(other, float):
            return Interval(
                left_border=self._left_border / other,
                right_border=self._right_border / other
            )
    
    def __rtruediv__(
            self, 
            other: tp.Union["Interval", float]
    ) -> tp.Union["Interval", float]:
        return self.__truediv__(other)
            
    def sqr(self) -> "Interval":
        left_border_value = min(
                    self._left_border ** 2, 
                    self._right_border ** 2
        ) if self._left_border * self._right_border >= 0.0 else 0.0
        
        return Interval(
            left_border=left_border_value,
            right_border=max(
                    self._left_border ** 2, 
                    self._right_border ** 2
            )
        )

    def sqrt(self) -> "Interval":
        assert self._left_border >= 0.0
        assert self._right_border >= 0.0
        return Interval(
            left_border=self._left_border ** 0.5,
            right_border=self._right_border ** 0.5
        )

    def __pow__(self, power: float) -> "Interval":
        if np.isclose(power, 2.0):
            return self.sqr()
        elif np.isclose(power, 0.5):
            return self.sqrt()

    def sample(self) -> float:
        return random.uniform(self._left_border, self._right_border)

    def __str__(self) -> str:
        return f"({self._left_border}, {self._right_border})"

    def __repr__(self) -> str:
        return str(self)

    @property
    def left_border(self):
        return self._left_border

    @property
    def right_border(self):
        return self._right_border

    def __iter__(self):
        return [self._left_border, self._right_border]
