from matplotlib import pyplot as pl

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 4, 2, 1]

total_error = [x + y for x, y in zip(variance, bias_squared)]

xs = [i for i, _ in enumerate(variance)]

pl.plot(xs, variance, 'g-', label='variance')
pl.plot(xs, variance, 'r-', label='bias^2')
pl.plot(xs, variance, 'b-', label='total_error')

pl.legend(loc= 9)
pl.xlabel("model complexity")
pl.title("The bias-Variance TradeOff")
pl.show()
