import numpy as np
import matplotlib.pyplot as plt
# print(np.random.rand())
# def uniforme (a, b):
#     r = np.random.rand()
#     return a + (b-a)*r
uniforme = []
exponencial = []
gamma = []
normal = []

for i in range(0,999):
    uniforme.append(np.random.uniform())

    exponencial.append(np.random.exponential())
    
    gamma.append(np.random.gamma(12))
    
    normal.append(np.random.normal())

plt.figure(1)
plt.title('uniforme')
plt.hist(uniforme)
plt.figure(2)
plt.title('exponencial')
plt.plot(exponencial)
plt.figure(3)
plt.title('gamma')
plt.hist(gamma)
plt.figure(4)
plt.title('normal')
plt.hist(normal)


plt.show()