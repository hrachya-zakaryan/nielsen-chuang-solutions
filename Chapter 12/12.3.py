import numpy as np

E=np.sqrt(1/3)*np.array([np.sqrt(3)*np.array([1,0]),np.array([1,np.sqrt(2)]),
np.array([1,np.sqrt(2)*np.power(np.e,2*np.pi*1j/3)]),np.array([1,np.sqrt(2)*np.power(np.e,4*np.pi*1j/3)])])
F=np.sqrt(1/3)*np.array([np.sqrt(3)*np.array([0,1]),np.array([np.sqrt(2)*np.power(np.e,np.pi*1j/3),1]),
np.array([np.sqrt(2)*np.power(np.e,np.pi*1j),1]),np.array([np.sqrt(2)*np.power(np.e,5*np.pi*1j/3),1])])
rho_i=np.zeros((4,2,2), dtype=complex)
for i in range(4):
    rho_i[i]=np.outer(E[i],np.conjugate(E[i]))
povm_E=0.5*rho_i


Hy=0
Hyx=0
for i in range(4):
    temp_y=0
    temp_yx=0
    for j in range(4):
        temp_trace=np.trace(np.dot(rho_i[j],povm_E[i]))
        temp_y=temp_y+0.25*temp_trace
        temp_yx=temp_yx+0.25*temp_trace*np.log2(temp_trace)
    Hy=Hy+temp_y*np.log2(temp_y)
    Hyx=Hyx+temp_yx
Hy=-Hy
Hyx=-Hyx
Hxy=Hy-Hyx
print(Hxy.real)


povm_F=np.zeros((4,2,2), dtype=complex)
for i in range(4):
    povm_F[i]=0.5*np.outer(F[i],np.conjugate(F[i]))

Hy=0
Hyx=0
for i in range(4):
    temp_y=0
    temp_yx=0
    for j in range(4):
        temp_trace=np.trace(np.dot(rho_i[i],povm_F[j]))
        temp_y=temp_y+0.25*temp_trace
        if temp_trace!=0:
            temp_yx=temp_yx+0.25*temp_trace*np.log2(temp_trace)
    Hy=Hy+temp_y*np.log2(temp_y)
    Hyx=Hyx+temp_yx
Hy=-Hy
Hyx=-Hyx
Hxy=Hy-Hyx

print(Hxy.real)