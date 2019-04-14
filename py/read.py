import numpy as np
import matplotlib.pyplot as plt

data_dir = '../data/'

f = open(data_dir+'nd.dac','r')
nd = int(f.read().split()[0])
f.close()

f = open(data_dir+'params.dac','r')
params = f.read().split()
f.close()

nx = int(params[0])
xmax = float(params[1])
xmin = float(params[2])

dx = (xmax - xmin)/nx
x = np.linspace(xmin + 0.5*dx, xmax - 0.5*dx,nx)

endian = '<'

plt.clf()
for n in range(0,nd+1):
    f = open(data_dir+'t.dac.'+'{0:08d}'.format(n),"rb")
    t = np.fromfile(f,endian+'d',1)
    f.close()
    t = t.reshape(1,order='F')[0]

    dtype = np.dtype([("qq",endian+str(nx)+"d")])
    f = open(data_dir+'qq.dac.'+'{0:08d}'.format(n),"rb")
    qq = np.fromfile(f,dtype=dtype,count=1)
    qq = qq["qq"].reshape(nx,order='F')

    plt.plot(x,qq)
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.pause(0.1)
    print(t)
