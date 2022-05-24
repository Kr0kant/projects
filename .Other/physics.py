from math import sqrt

L_p = 99.79 * (10**(-3))
M_p = 7.8 * (10**(-3))

L_dl = 128.98 * (10**(-3))

L_sm = 50.03 * (10**(-3))
M_sm = 2.5 * (10**(-3))

M_g = 0.7 * (10**(-3))
M_b = 0.9 * (10**(-3))

a = 0.0175
g = 9.8195

M = M_p + M_sm + (M_g + M_b)*2
L = L_p*0.8 + L_sm 

d = ( (M_p + M_sm)*(L/2) + (M_g + M_b)*(0.95*L_p) + (M_g + M_b)*(0.85*L_p) )/M

J = 1/3*M*(L)**2 + (M_g + M_b)*(0.95*L_p)**2 + (M_g + M_b)*(0.85*L_p)**2

L_priv = J/(M*d)
gamma = 1/a * sqrt(2*g*L_priv)

print(L_priv) 
print(gamma)
