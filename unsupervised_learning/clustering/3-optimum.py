# #!/usr/bin/env python3

# """
# a function that tests for the optimum
# number of clusters by variance
# """


# import numpy as np
# kmeans = __import__('1-kmeans').kmeans
# variance = __import__('2-variance').variance


# def optimum_k(X, kmin=1, kmax=None, iterations=1000):
#     '''
#     A function that tests for the optimum
#     '''
#     if not isinstance(X, np.ndarray) or len(X.shape) != 2:
#         return None, None
#     if not isinstance(kmin, int) or kmin <= 0:
#         return None, None
#     if not isinstance(kmax, int) or kmax <= 0:
#         return None, None
#     if kmin >= kmax:
#         return None, None
#     if not isinstance(iterations, int) or iterations <= 0:
#         return None, None
#     if kmax is None:
#         kmax = X.shape[0]

#     results = []
#     d_vars = []
#     var = float('inf')
#     for k in range(kmin, kmax + 1):
#         C, clss = kmeans(X, k, iterations)
#         results.append((C, clss))
#         new_var = variance(X, C)
#         if k == kmin:
#             var = new_var
#         d_vars.append(var - new_var)
#     return results, d_vars


#!/usr/bin/env python3
"""[summary]

Returns:
    [type]: [description]
"""
import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """[summary]

    Args:
        X ([type]): [description]
        kmin (int, optional): [description]. Defaults to 1.
        kmax ([type], optional): [description]. Defaults to None.
        iterations (int, optional): [description]. Defaults to 1000.

    Returns:
        [type]: [description]
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None
    if kmax is None:
        kmax = X.shape[0]
    if type(kmin) != int or kmin <= 0 or kmin >= X.shape[0]:
        return None, None
    if type(kmax) != int or kmax <= 0 or kmax > X.shape[0]:
        return None, None
    if kmin >= kmax:
        return None, None
    if type(iterations) != int or iterations <= 0:
        return None, None
    results = []
    d_vars = []
    for k in range(kmin, kmax + 1):
        C, clss = kmeans(X, k, iterations)
        results.append((C, clss))
        if k == kmin:
            varm = variance(X, C)
        d_vars.append(varm - variance(X, C))
    return results, d_vars
