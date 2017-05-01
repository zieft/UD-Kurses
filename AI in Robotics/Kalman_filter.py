from math import *


def f(mu, sigma2, x):
    """
    Gaussian function.
    """
    return 1. / sqrt(2. * pi * sigma2) * exp(-0.5 * (x - mu) ** 2. / sigma2)


print(f(10., 4., 8.))


def update(mean1, var1, mean2, var2):
    """
    Karman filter mesurement update.
    """
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1 / (1 / var1 + 1 / var2)

    return [new_mean, new_var]


def predict(mean1, var1, mean2, var2):
    """
    Karman filter predictions(move updeate).
    :param mean1: 
    :param var1: 
    :param mean2: 
    :param var3: 
    :return: 
    """
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]



### Example: A full kalman filter in 1-D ###
measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

for i in range(len(measurements)):
    Update = update(mu, sig, measurements[i], measurement_sig)
    print('update: ', Update)
    Pridiction = predict(mu, sig, motion[i], motion_sig)
    print('pridict: ', Pridiction)
### Example End ###
