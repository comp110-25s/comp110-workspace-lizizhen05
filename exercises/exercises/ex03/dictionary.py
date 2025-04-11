"""Functions for Dictionary Functions"""

__author__: str = "730667645"

from typing import List, Dict, Set


def invert(d: dict[str, str]) -> dict[str, str]:
    result: Dict[str, str] = {}
    for key in d:
        value = d[key]
        if value in result:
            raise KeyError("Duplicate key!")
        result[value] = key
    return result


def count(xs: list[str]) -> dict[str, int]:
    result: Dict[str, int] = {}
    for item in xs:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(colors: dict[str, str]) -> str:
    color_counts: Dict[str, int] = {}
    for name in colors:
        color = colors[name]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
    max_count = 0
    most_common = ""
    for color in color_counts:
        if color_counts[color] > max_count or (color_counts[color] == max_count and most_common == ""):
            max_count = color_counts[color]
            most_common = color
    return most_common


def bin_len(xs: list[str]) -> dict[int, set[str]]:
    result: Dict[int, Set[str]] = {}
    for item in xs:
        length = len(item)
        if length in result:
            result[length].add(item)
        else:
            result[length] = {item}
    return result
