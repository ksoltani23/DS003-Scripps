# FUNCTIONS
#     correlation(xs: List[float], ys: List[float]) -> float
#         Measures how much xs and ys vary in tandem about their means

# def correlation(xs,ys):
def correlation(xs: List[float], ys: List[float]) -> float:
    """Measures how much xs and ys vary in tandem about their means"""
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0    # if no variation, correlation is zero


#     covariance(xs: List[float], ys: List[float]) -> float


def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys), "xs and ys must have same number of elements"
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)


#
#     data_range(xs: List[float]) -> float
#         # "range" already means something in Python, so we'll use a different name

# "range" already means something in Python, so we'll use a different name
def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)

#
#     de_mean(xs: List[float]) -> List[float]
#         Translate xs by subtracting its mean (so the result has mean 0)

def de_mean(xs: List[float]) -> List[float]:
    """Translate xs by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

#
#     interquartile_range(xs: List[float]) -> float
#         Returns the difference between the 75%-ile and the 25%-ile

def interquartile_range(xs: List[float]) -> float:
    """Returns the difference between the 75%-ile and the 25%-ile"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)

#
#     mean(xs: List[float]) -> float
#

def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)



# The underscores indicate that these are "private" functions, as they're
# intended to be called by our median function but not by other people
# using our statistics library.
def _median_odd(xs: List[float]) -> float:
    """If len(xs) is odd, the median is the middle element"""
    return sorted(xs)[len(xs) // 2]

def _median_even(xs: List[float]) -> float:
    """If len(xs) is even, it's the average of the middle two elements"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2  # e.g. length 4 => hi_midpoint 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2


#     median(v: List[float]) -> float
#         Finds the 'middle-most' value of v

def median(v: List[float]) -> float:
    return None


#
#     mode(x: List[float]) -> List[float]
#         Returns a list, since there might be more than one mode

def mode(x: List[float]) -> List[float]:
    return None


#
#     quantile(xs: List[float], p: float) -> float
#         Returns the pth-percentile value in x

def quantile(xs: List[float], p: float) -> float:
    """Returns the pth-percentile value in x"""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

#
#     standard_deviation(xs: List[float]) -> float
#         The standard deviation is the square root of the variance

def standard_deviation(xs: List[float]) -> float:
    """The standard deviation is the square root of the variance"""
    return math.sqrt(variance(xs))


#
#     variance(xs: List[float]) -> float
#         Almost the average squared deviation from the mean
#

def variance(xs: List[float]) -> float:
    """Almost the average squared deviation from the mean"""
    assert len(xs) >= 2, "variance requires at least two elements"
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)
