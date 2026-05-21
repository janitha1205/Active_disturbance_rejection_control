import numpy as np
import matplotlib.pyplot as plt


def controller(x1_ref, x2_ref, x1_ob, x2_ob, z):
    k_p = 100.0
    k_d = 10.0
    u_c = k_p * (x1_ref - x1_ob) + k_d * (x2_ref - x2_ob) - z
    return u_c


def sysdyn(x1, x2, u, d, dt):
    g = 9.81
    L = 0.12
    x1_dot = x2
    x2_dot = u - (g / L) * np.sin(x1) + d
    x2 += x2_dot * dt
    x1 += x1_dot * dt
    return x1, x2


def extobs(x1, x1_ob, x2_ob, u, z, dt):
    lem_1 = 10.0
    lem_2 = 120.0
    lem_3 = 4000.0
    dx1_ob = x2_ob + lem_1 * (x1 - x1_ob)
    dx2_ob = u + lem_2 * (x1 - x1_ob) + z
    dz = lem_3 * (x1 - x1_ob)
    x1_ob1 = dx1_ob * dt + x1_ob
    x2_ob1 = dx2_ob * dt + x2_ob
    z1 = dz * dt + z
    return x1_ob1, x2_ob1, z1


dt = 0.001
t = 0
t1 = []
x11 = []
x12 = []
x21 = []
x22 = []
z11 = []
z12 = []
x1 = 0
x2 = 0
u = 0
x1_ob = 0
x2_ob = 0
while t < 30:
    x1_ref = 20.3 * np.sin(t)
    x2_ref = 20.3 * np.cos(t)
    z = 0.3 * np.sin(7 * t) + 0.7 * np.cos(2 * t)

    [x1_ob, x2_ob, z_1] = extobs(x1, x1_ob, x2_ob, u, z, dt)
    u = controller(x1_ref, x2_ref, x1_ob, x2_ob, z_1)
    [x1, x2] = sysdyn(x1_ob, x2_ob, u, z, dt)

    x11.append(x1)
    x12.append(x1_ref)
    x21.append(x2)
    x22.append(x2_ref)
    z11.append(z_1)
    z12.append(z)
    t1.append(t)
    t += dt
plt.plot(t1, x11, t1, x12, t1, x21, t1, x22, t1, z11, t1, z12)
plt.show()
