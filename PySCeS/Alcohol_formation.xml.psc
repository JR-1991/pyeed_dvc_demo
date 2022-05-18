# Generated by PySCeS 1.0.2 (2022-05-18 10:04)
 
# Keywords
Description: Alcohol formation
Modelname: Alcohol formation
Output_In_Conc: True
Species_In_Conc: True
 
# GlobalUnitDefinitions
UnitSubstance: mole, 1.0, 0, 1
UnitVolume: litre, 1.0, 0, 1
UnitTime: second, 1.0, 0, 1
UnitLength: metre, 1.0, 0, 1
UnitArea: metre, 1.0, 0, 2
 
# Compartments
Compartment: v0, 10.0, 3 
 
# Reactions
r0@v0:
    s1 > s0
    r0_kcat*p0*s1/(s1+r0_Km)
# r0 has modifier(s): p0  

r1@v0:
    s0 > s2
    r1_kcat*p1*s0/(s0+r1_Kp+r1_Km)
# r1 has modifier(s): p1  
 
# Fixed species
 
# Variable species
p0@v0 = 10.0
p1@v0 = 20.0
s0@v0 = 0.0
s1@v0 = 10.0
s2@v0 = 0.0
s3@v0 = 0.0
 
# Parameters
r0_Km = 20.0
r0_kcat = 5.0
r1_Km = 50.0
r1_kcat = 3.0
r1_Kp = 3.0
 

