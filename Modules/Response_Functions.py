import numpy as np


class GM_ResFunc():
    def __init__(self):
        pass

    def compute(self, params, t, x_0):
        a = params[0]
        b = params[1]
        x1_pred = (x_0 - b / a) * np.exp(-a * t) + b / a
        return x1_pred


class NGM_ResFunc():
    def __init__(self):
        pass

    def compute(self, params, t, x_0):
        a = params[0]
        b = params[1]
        x1_pred = (x_0 - b / a + b / a / a) * np.exp(-a * t) + b * (t + 1) / a - b / a / a
        return x1_pred


class BernoulliGM_ResFunc():
    def __init__(self):
        pass

    def compute(self, params, t, x_0, N):
        a = params[0]
        b = params[1]
        x1_pred = ((x_0 ** (1 - N) - b / a) * np.exp(-a * (1 - N) * t) + b / a) ** (1 / (1 - N))
        return x1_pred


class DGM_ResFunc():
    def __init__(self):
        pass

    def compute(self, params, t, x_0):
        a = params[0]
        b = params[1]
        x1_pred = (a ** t) * (x_0 - (b / (1 - a))) + b / (1 - a)
        return x1_pred


class GMN_ResFunc():
    def __init__(self):
        pass

    def compute(self, params, t, x1):
        a = params[0]
        b = params[1:]
        lens_0 = len(np.array(x1[0:, 0]))
        c = np.zeros(11)
        for i in range(0, lens_0):
            c[i] = sum(b * x1[i, 1:])
        x1_pred = (x1[0][0] - c / a) / np.exp(a * t) + c / a
        return x1_pred


class DGMN_ResFunc():
    def __init__(self):
        pass

    def compute(self, params, t, x1):
        a = params[0]
        u = params[-1]
        b = params[1:-1]
        lens = len(t)
        c = []
        for k in range(0, 11):
            for m in range(0, k):
                for i in range(1, 5):
                    c[k] = sum((a**m)*(sum(b * x1[])))