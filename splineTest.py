from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline
import numpy as np
import matplotlib.pyplot as plt

# # x = np.linspace(0, 10, num=11, endpoint=True)
# # y = np.cos(-x**2/9.0)
# # y = x
x = np.array([0, 1, 20, 50, 100])
y = np.array([0, 10, 300, 500, 800])
f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')

xnew = np.linspace(0, 100, num=50, endpoint=False)
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()

# Test UnivariateSpline - this needs a uniform x range to work
# x = np.array([1, 2, 3, 4, 5])
# spl = UnivariateSpline(x, y)
# spl.set_smoothing_factor(0.5)
# plt.plot(x, spl(x), 'b', lw=3)
# plt.show()

# x = np.linspace(-3, 3, 50)
# y = np.exp(-x**2) + 0.1 * np.random.randn(50)
# plt.plot(x, y, 'ro', ms=5)

# spl = UnivariateSpline(x, y)
# xs = np.linspace(-3, 3, 1000)
# plt.plot(xs, spl(xs), 'g', lw=3)

# spl.set_smoothing_factor(0.5)
# plt.plot(xs, spl(xs), 'b', lw=3)
# plt.show()
