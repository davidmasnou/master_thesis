#!/home/apmlab/Software/anaconda3/bin/python3

import sys

box_volume = float(sys.argv[1]) #Read volume of the box from terminal (in A)

#Converting volume from A to L
A_to_L = 10*(10**-28) 
volume = box_volume*A_to_L #Final volume in L

#Calculating the number of ions needed to add to that volume (150 mmol)
n_ions = volume*(9.03*(10**22))
rounded_n_ions = round(n_ions)

print("Add %f (%i) Na and Cl atoms to the system" %(n_ions, rounded_n_ions))


