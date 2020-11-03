#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
 
time = 1000
#n = 2                   #>=  2    Кол-во тел
dt = 0.01                 # временной шаг
t_g = 1
iter = int(time/dt) + 1
rmax = 1
f = 1

M = [20, 30]
n = len(M)
s = [[2, -2],
     [2, -1]]
c = [[0, 50],
     [0, 50]]

'''M = [20, 30, 60, 10, 500]
s = [[0, 0, 0, 0, 0],
     [2, 5, 6, 0, 0]]
c = [[70, 50, 30, 100, 0],
     [0, 0, 0, 0, 0]]'''
'''M=[10000,5, 40]
s =[[0,0, 50],
    [0,10, -50]]
c=[[0,2000, 0],
   [0,0, 50]]'''
g = 20
#X = np.zeros((n, iter))
#Y = np.zeros((n, iter))
#print(X)
 
class Space:
  def __init__ (self, body_num, start_speed, start_cordinate, G, mass):
    self.bn = body_num
    self.G = G
    self.M = mass
    self.SS = start_speed
    self.SC = start_cordinate
    self.S = np.array(self.SS, dtype='float', ndmin = 2)
    self.C = np.array(self.SC, dtype='float', ndmin = 2)
    self.X = np.zeros((n, iter))
    self.Y = np.zeros((n, iter))

  def Force (self):
    self.A = np.zeros((2, self.bn))
    global rmax
    #self.R = np.zeros(int(self.bn*(self.bn+1)/2))
    for a in range(self.bn):
      for i in range(self.bn):
        if i != a:
          self.r = np.sqrt((self.C[0, a] - self.C[0, i])**2 + (self.C[1, a] - self.C[1, i])**2)
          if self.r > rmax:
            rmax = self.r
          #self.r = np.sqrt((self.C[i] - self.C[a]) @ (self.C[i] - self.C[a]).T)
          self.A[0, a] += self.G * self.M[i] * (self.C[0, i] - self.C[0, a])/self.r**3
          self.A[1, a] += self.G * self.M[i] * (self.C[1, i] - self.C[1, a])/self.r**3
          #print(self.A[0, a])
          #self.A[:, a] += self.G * self.M[i] * (self.C[i] - self.C[a])/self.r**3
    #print(self.A)      
    return r

  def velocity(self):
    self.V = np.round(np.sqrt(self.S[0]**2 + self.S[1]**2), 2)
    return self.V

  def step (self, i, dt):
    global rmax
    rmax = sp.Force()
    self.S += self.A * dt
    self.C += self.S * dt
    #self.V = np.round(np.sqrt(self.S[0]**2 + self.S[1]**2), 2)
    self.X[:, i] = self.C[0]
    self.Y[:, i] = self.C[1]
    #return self.C

  def energy(self):
    self.Ek = np.zeros(n)
    self.Ep = 0
    V = sp.velocity()
    self.Ek = self.M * V**2 / 2
    for i in range(self.bn):
      for j in range(i+1,self.bn):
        self.r = np.sqrt((self.C[0, i] - self.C[0, j])**2 + (self.C[1, i] - self.C[1, j])**2)
        self.Ep -= self.G*self.M[i]*self.M[j]/self.r
    E = np.sum(self.Ek) + self.Ep
    return E

  #def graph(self, x, y, i):
  def graph(self, i):
    global n
    curve_с= ('g','r','b','m','c','y')
    fig, ax = plt.subplots()
    V = sp.velocity()
    for j in range(n):
      #print(x[j,:i+1])
      #ax.plot(x[j,:i+1], y[j,:i+1], curve_с[j%6], label=str(np.round(np.sqrt(self.S[0, j]**2 + self.S[1, j]**2), 2)))
      ax.plot(self.X[j,:i+1], self.Y[j,:i+1], curve_с[j%6], label=str(V[j]))
    legend = ax.legend(loc='upper right', shadow=0, fontsize=8)
    plt.title('time '+str(np.round(i*dt, 3)))
    plt.grid(1)
    plt.show()
 
sp = Space(n, s, c, g, M)

E0 = sp.energy()
print('Начальная энергия системы', E0)

for i in range(iter):
    sp.step(i, dt)
    #X[:, i] = ST[0]
    #Y[:, i] = ST[1]
    if rmax <= 0.99:
      print('Объекты сблизились на критическое расстояние')
      break
    elif rmax >= 10000: 
      print('Объекты отдалились на значительное рассотяние')
      break    
    if np.round(i*dt % t_g, 3) == 0 and f == 1:
      #sp.graph(X, Y, i)
      sp.graph(i)
      E = sp.energy()
      print('Энергия системы', E)
Ef = sp.energy()
print('Изменение энергии системы', Ef-E0)

