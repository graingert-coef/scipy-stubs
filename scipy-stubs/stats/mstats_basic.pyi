# This module is not meant for public use and will be removed in SciPy v2.0.0.
from typing_extensions import deprecated

__all__ = [
    "argstoarray",
    "brunnermunzel",
    "count_tied_groups",
    "describe",
    "f_oneway",
    "find_repeats",
    "friedmanchisquare",
    "kendalltau",
    "kendalltau_seasonal",
    "kruskal",
    "kruskalwallis",
    "ks_1samp",
    "ks_2samp",
    "ks_twosamp",
    "kstest",
    "kurtosis",
    "kurtosistest",
    "linregress",
    "mannwhitneyu",
    "meppf",
    "mode",
    "moment",
    "mquantiles",
    "msign",
    "normaltest",
    "obrientransform",
    "pearsonr",
    "plotting_positions",
    "pointbiserialr",
    "rankdata",
    "scoreatpercentile",
    "sem",
    "sen_seasonal_slopes",
    "siegelslopes",
    "skew",
    "skewtest",
    "spearmanr",
    "theilslopes",
    "tmax",
    "tmean",
    "tmin",
    "trim",
    "trima",
    "trimboth",
    "trimmed_mean",
    "trimmed_std",
    "trimmed_stde",
    "trimmed_var",
    "trimr",
    "trimtail",
    "tsem",
    "ttest_1samp",
    "ttest_ind",
    "ttest_onesamp",
    "ttest_rel",
    "tvar",
    "variation",
    "winsorize",
]

@deprecated("will be removed in SciPy v2.0.0")
def argstoarray(*args: object) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def find_repeats(arr: object) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def count_tied_groups(x: object, use_missing: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def rankdata(data: object, axis: object = ..., use_missing: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def mode(a: object, axis: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def msign(x: object) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def pearsonr(x: object, y: object) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def spearmanr(
    x: object,
    y: object = ...,
    use_ties: object = ...,
    axis: object = ...,
    nan_policy: object = ...,
    alternative: object = ...,
) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def kendalltau(
    x: object,
    y: object,
    use_ties: object = ...,
    use_missing: object = ...,
    method: object = ...,
    alternative: object = ...,
) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def kendalltau_seasonal(x: object) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def pointbiserialr(x: object, y: object) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def linregress(x: object, y: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def theilslopes(y: object, x: object = ..., alpha: object = ..., method: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def siegelslopes(y: object, x: object = ..., method: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def sen_seasonal_slopes(x: object) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def ttest_onesamp(a: object, popmean: object, axis: object = ..., alternative: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def ttest_1samp(a: object, popmean: object, axis: object = ..., alternative: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def ttest_ind(a: object, b: object, axis: object = ..., equal_var: object = ..., alternative: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def ttest_rel(a: object, b: object, axis: object = ..., alternative: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def mannwhitneyu(x: object, y: object, use_continuity: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def kruskal(*args: object) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def kruskalwallis(*args: object) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def ks_1samp(x: object, cdf: object, args: object = ..., alternative: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def ks_2samp(data1: object, data2: object, alternative: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def ks_twosamp(data1: object, data2: object, alternative: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def kstest(data1: object, data2: object, args: object = ..., alternative: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def trima(a: object, limits: object = ..., inclusive: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def trimr(a: object, limits: object = ..., inclusive: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def trim(
    a: object,
    limits: object = ...,
    inclusive: object = ...,
    relative: object = ...,
    axis: object = ...,
) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def trimboth(data: object, proportiontocut: object = ..., inclusive: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def trimtail(
    data: object,
    proportiontocut: object = ...,
    tail: object = ...,
    inclusive: object = ...,
    axis: object = ...,
) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def trimmed_mean(a: object, limits: object = ..., inclusive: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def trimmed_var(
    a: object,
    limits: object = ...,
    inclusive: object = ...,
    relative: object = ...,
    axis: object = ...,
    ddof: object = ...,
) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def trimmed_std(
    a: object,
    limits: object = ...,
    inclusive: object = ...,
    relative: object = ...,
    axis: object = ...,
    ddof: object = ...,
) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def trimmed_stde(a: object, limits: object = ..., inclusive: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def tmean(a: object, limits: object = ..., inclusive: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def tvar(a: object, limits: object = ..., inclusive: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def tmin(a: object, lowerlimit: object = ..., axis: object = ..., inclusive: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def tmax(a: object, upperlimit: object = ..., axis: object = ..., inclusive: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def tsem(a: object, limits: object = ..., inclusive: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def winsorize(
    a: object,
    limits: object = ...,
    inclusive: object = ...,
    inplace: object = ...,
    axis: object = ...,
    nan_policy: object = ...,
) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def moment(a: object, moment: object = ..., axis: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def variation(a: object, axis: object = ..., ddof: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def skew(a: object, axis: object = ..., bias: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def kurtosis(a: object, axis: object = ..., fisher: object = ..., bias: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def describe(a: object, axis: object = ..., ddof: object = ..., bias: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def stde_median(data: object, axis: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def skewtest(a: object, axis: object = ..., alternative: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def kurtosistest(a: object, axis: object = ..., alternative: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def normaltest(a: object, axis: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def mquantiles(
    a: object,
    prob: object = ...,
    alphap: object = ...,
    betap: object = ...,
    axis: object = ...,
    limit: object = ...,
) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def scoreatpercentile(data: object, per: object, limit: object = ..., alphap: object = ..., betap: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def meppf(data: object, alpha: object = ..., beta: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def plotting_positions(data: object, alpha: object = ..., beta: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def obrientransform(*args: object) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def sem(a: object, axis: object = ..., ddof: object = ...) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def f_oneway(*args: object) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def friedmanchisquare(*args: object) -> object: ...
@deprecated("will be removed in SciPy v2.0.0")
def brunnermunzel(x: object, y: object, alternative: object = ...) -> object: ...
