import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation

##### CALCULATIONS / MATH #########
time_start = 0
time_end = 5 * np.pi
time_delta = 0.05

time = np.arange(time_start, time_end, time_delta)

y = np.sin(time) #y = sin(time)

####### END MATH ####################

##### START ANIMATION ######
figure = plt.figure(figsize=(10,9), facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)

sinsubplot = figure.add_subplot(gs[0,:], facecolor=(0.9, 0.9, 0.9))


frame_amount = len(time)
def update_func(num):
    sinwave_dot.set_data([time[num], time[num]], [y[num], y[num]])
    sinwave_green.set_data(time[0:num], y[0:num])
    
    return sinwave_green, sinwave_dot 

sinwave_dot, = sinsubplot.plot([], [], 'r:o', linewidth=1)
sinwave_green, = sinsubplot.plot([], [], 'g:o', lw=1)
tindug, = sinsubplot.plot([4,4],[0,1], color='black', linewidth=5, solid_capstyle='butt')

sinanimation = animation.FuncAnimation(fig=figure, func=update_func, interval=10, frames=frame_amount, blit=True, repeat=True)


plt.axhline(y=0, linewidth=1, linestyle='--', color='black')
plt.xlim(time[0], max(time))
plt.ylim(min(y)-0.5, max(y)+0.5)
plt.grid(True)
plt.plot(time, y)

plt.show()