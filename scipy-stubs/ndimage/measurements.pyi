# This module is not meant for public use and will be removed in SciPy v2.0.0.
from typing_extensions import deprecated

__all__ = [
    "center_of_mass",
    "extrema",
    "find_objects",
    "histogram",
    "label",
    "labeled_comprehension",
    "maximum",
    "maximum_position",
    "mean",
    "median",
    "minimum",
    "minimum_position",
    "standard_deviation",
    "sum",
    "sum_labels",
    "variance",
    "watershed_ift",
]

@deprecated("will be removed in SciPy v2.0.0")
def label(input: object, structure: object = ..., output: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def find_objects(input: object, max_label: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def labeled_comprehension(
    input: object,
    labels: object,
    index: object,
    func: object,
    out_dtype: object,
    default: object,
    pass_positions: object = ...,
) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def sum(input: object, labels: object = ..., index: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def sum_labels(input: object, labels: object = ..., index: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def mean(input: object, labels: object = ..., index: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def variance(input: object, labels: object = ..., index: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def standard_deviation(input: object, labels: object = ..., index: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def minimum(input: object, labels: object = ..., index: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def maximum(input: object, labels: object = ..., index: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def median(input: object, labels: object = ..., index: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def minimum_position(input: object, labels: object = ..., index: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def maximum_position(input: object, labels: object = ..., index: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def extrema(input: object, labels: object = ..., index: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def center_of_mass(input: object, labels: object = ..., index: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def histogram(input: object, min: object, max: object, bins: object, labels: object = ..., index: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def watershed_ift(input: object, markers: object, structure: object = ..., output: object = ...) -> object: ...
