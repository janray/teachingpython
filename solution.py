import matplotlib.pyplot as plt
import numpy as np

# 0 ≤ θ ≤ 2π

sin_x_start = -4 * np.pi
sin_x_stop = 4 * np.pi

cos_x_start = -2 * np.pi
cos_x_stop = 2 * np.pi

x_increment = 0.005

x_sin_data = np.arange(sin_x_start, sin_x_stop, x_increment)
y_sin_data = np.sin(x_sin_data)

x_cos_data = np.arange(cos_x_start, cos_x_stop, x_increment)
y_cos_data = np.cos(x_cos_data)

figure = plt.figure(figsize=(16,9), dpi=120, facecolor=(0.8,0.8,0.8))

sinplot = figure.add_subplot(2,1,1)
sinplot.axis([sin_x_start, sin_x_stop, -1, 1])
sinplot.grid()
sinplot.plot(x_sin_data, y_sin_data, 'r')
sinplot.title.set_text('Sine Wave')


cosplot = figure.add_subplot(2,1,2)
cosplot.axis([cos_x_start, cos_x_stop, -2, 2])
cosplot.grid()
cosplot.plot(x_cos_data, y_cos_data, 'g')
cosplot.title.set_text('Cosine Wave')



plt.show()