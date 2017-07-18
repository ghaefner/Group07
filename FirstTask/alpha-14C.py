import numpy as np

# Constant input
esq = 1.440 # e^2 [MeV fm] (= hc/2pi * fine structure constant)
hc = 197.327 # hc/2pi [MeV fm]

Am = 223 # mass number of mother nucleus
Zm = 88 # atomic number of mother nucleus



# calculate half life of alpha decay
Ae = 4 # mass number of emitted nucleus
Ze = 2 # atomic number of emitted nucleus

Ad = Am - Ae # mass number of daughter nucleus
Zd = Zm - Ze # atomic number of daughter nucleus

mu = Ad*Ae/(Ad+Ae)*931.494 # reduced mass [MeV/c^2]

Q = 5.979 # Q-value [MeV]

Rt = 1.35*Am**(1./3.) # the radius of the strong interaction [fm] (modify from Alex's lecture note p67 to reproduce alpha decay half life)
Rc = Ze*Zd*esq/Q # the classical turning radius [fm]

x = np.sqrt(Rt/Rc)

Wc = np.sqrt(Q/(2.*Rt**2.*mu))*(3.*10**(23)) # decay rate [s] (Alex's lecture note p67)
P = np.exp(-2.*Zd*Ze*esq*np.sqrt(2.*mu/(Q*hc**2.)) * (np.arccos(x) - x*np.sqrt(1.-x**2.)) ) # Tunneling probability (Alex's lecture note p68(7.17))

aT12 = np.log(2.)/Wc/P # half life of alpha decay
DRa = 1./aT12 # decay rate [1/s]

print("Alpha decay half life of 223Ra")
print(aT12, "s")
print(aT12/60., "m")
print(aT12/60./60., "h")
print(aT12/60./60./24., "d")
print("Experimental half life = 11.431 d")
print()



# calculate half life of 14C decay with parameters which approximately reproduce alpha decay half life
Ae = 14 # mass number of emitted nucleus
Ze = 6 # atomic number of emitted nucleus

Ad = Am - Ae # mass number of daughter nucleus
Zd = Zm - Ze # atomic number of daughter nucleus

mu = Ad*Ae/(Ad+Ae)*931.494 # reduced mass [MeV/c^2]

Q = 31.828 # Q-value [MeV]

Rt = 1.35*Am**(1./3.) # the radius of the strong interaction [fm] (modify from Alex's lecture note p67 to reproduce alpha decay half life)
Rc = Ze*Zd*esq/Q # the classical turning radius [fm]

x = np.sqrt(Rt/Rc)

Wc = np.sqrt(Q/(2.*Rt**2.*mu))*(3.*10**(23)) # decay rate [s] (Alex's lecture note p67)
P = np.exp(-2.*Zd*Ze*esq*np.sqrt(2.*mu/(Q*hc**2.)) * (np.arccos(x) - x*np.sqrt(1.-x**2.)) ) # Tunneling probability (Alex's lecture note p68(7.17))

C14T12 = np.log(2.)/Wc/P # half life of 14C decay
DRC14 = 1./C14T12 # decay rate [1/s]

print("14C decay half life of 223Ra")
print(C14T12, "s")
print(C14T12/60., "m")
print(C14T12/60./60., "h")
print(C14T12/60./60./24., "d")
print(C14T12/60./60./24./365., "y")
print()



# Calculate branching ratio (assume that alpha and 14C decay are the only possible decay)
print("BR = ", DRC14/(DRa + DRC14))
