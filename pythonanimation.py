import matplotlib.pyplot as plt # type: ignore
import matplotlib.animation as animation # type: ignore
import matplotlib.gridspec as gridspec # type: ignore
import numpy as np


t_0 = 0
t_end = 2
t_delta = 0.005

time = np.arange(t_0, t_end + t_delta, t_delta)
altitude = 2

x = 800 * time # distance traveled
y = np.ones(len(time)) * altitude


frame_amount = len(time)
def update_plot(num):
    plane_trajectory.set_data(x[0:num],y[0:num])
    plane_body.set_data([x[num]-40, x[num]+20],[y[num],y[num]])
    
    return plane_trajectory, plane_body

fig = plt.figure(figsize=(10,9), dpi=120, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)

ax0 = fig.add_subplot(gs[0,:], facecolor=(0.9, 0.9, 0.9))
plane_trajectory, = ax0.plot([],[], 'g', linewidth=1)
plane_body, = ax0.plot([],[], 'k', linewidth=7)


anim = animation.FuncAnimation(fig=fig,func=update_plot,frames=frame_amount, interval=20, repeat=True, blit=True)
plt.xlim(x[0], x[-1])
plt.ylim(0, y[0] + 1)
plt.show()