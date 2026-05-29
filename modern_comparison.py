import numpy as np
import matplotlib.pyplot as plt


class Adrc:
    g = 9.81
    L = 0.12
    k_p = 100.0
    k_d = 10.0
    lem_1 = 10.0
    lem_2 = 120.0
    lem_3 = 4000.0
    dt = 0.01

    def __init__(
        self,
        u: float,
        x1: float,
        x2: float,
        d: float,
        x1ob: float,
        x2ob: float,
    ):

        self.u = u
        self.x1 = x1
        self.x2 = x2
        self.d = d
        self.x1_ob = x1ob
        self.x2_ob = x2ob

    def controller(self, x1_ref, x2_ref):
        k_p1 = self.k_p
        k_d1 = self.k_d
        self.u = k_p1 * (x1_ref - self.x1_ob) + k_d1 * (x2_ref - self.x2_ob) - self.d

    def sysdyn(
        self,
    ):
        x1_dot = self.x2_ob
        x2_dot = self.u - (self.g / self.L) * np.sin(self.x1_ob) + self.d
        self.x2 = x2_dot * self.dt + self.x2_ob
        self.x1 = x1_dot * self.dt + self.x1_ob

    def extobs(self, d_in):
        lem_11 = self.lem_1
        lem_21 = self.lem_2
        lem_31 = self.lem_3
        self.d = d_in
        dx1_ob = self.x2 + lem_11 * (self.x1 - self.x1_ob)
        dx2_ob = self.u + lem_21 * (self.x1 - self.x1_ob) + self.d
        dz = lem_31 * (self.x1 - self.x1_ob)
        self.x1_ob += dx1_ob * self.dt
        self.x2_ob += dx2_ob * self.dt
        self.d += dz * self.dt


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


def extobs(x1, x2, x1_ob, x2_ob, u, z, dt):
    lem_1 = 10.0
    lem_2 = 120.0
    lem_3 = 4000.0
    dx1_ob = x2 + lem_1 * (x1 - x1_ob)
    dx2_ob = u + lem_2 * (x1 - x1_ob) + z
    dz = lem_3 * (x1 - x1_ob)
    x1_ob1 = dx1_ob * dt + x1_ob
    x2_ob1 = dx2_ob * dt + x2_ob
    z1 = dz * dt + z
    return x1_ob1, x2_ob1, z1


sys1 = Adrc(
    u=0.0,
    x1=0.0,
    x2=0.0,
    d=0.0,
    x1ob=0.0,
    x2ob=0.0,
)
dt = sys1.dt
t = 0
t1 = []
x11 = []
x12 = []
x13 = []
x21 = []
x22 = []
z11 = []
z12 = []
x1 = 0
x2 = 0
u = 0
x1_ob = 0
x2_ob = 0
while t < 5000 * dt:
    x1_ref = 0.3 * np.sin(t)
    x2_ref = 0.3 * np.cos(t)
    z = 0.34 * np.random.rand()
    sys1.extobs(z)
    [x1_ob, x2_ob, z_1] = extobs(x1, x2, x1_ob, x2_ob, u, z, dt)
    print(x1_ob)
    print(sys1.x1_ob)
    sys1.controller(x1_ref, x2_ref)
    u = controller(x1_ref, x2_ref, x1_ob, x2_ob, z_1)
    print(u)
    print(sys1.u)
    sys1.sysdyn()
    [x1, x2] = sysdyn(x1_ob, x2_ob, u, z_1, dt)
    print(sys1.x1)
    print(x1)

    x11.append(sys1.x1)
    x12.append(x1_ref)
    x13.append(x1)
    x21.append(sys1.x2)
    x22.append(x2_ref)
    z11.append(z_1)
    z12.append(z)
    t1.append(t)
    t += dt
plt.plot(t1, x11, "r", t1, x12, "b", t1, x21, "k", t1, x22, "g")
plt.show()
