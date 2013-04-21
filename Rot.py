from numpy import *
from math import *
m = matrix

#Define the rotation matrix
R = m([[0,0,-0.5],[0,1,0],[0.5,0,0]])
#R = m([[0.5,-0.1464,0.8536],[0.5,0.8536,-0.1464],[-0.7071,0.5,0.5]])

print R

var = R[2,0]

if var == 1 or var == -1:
	print 'Ok, we have to do this the hard way...'
	Phi = 0 # anything (can set to zero)
	
	if var == -1:
		Theta = pi/2
		Psi = Phi + atan2(R[0,1], R[0,2])
		
		E = m([Psi*180/pi, Theta*180/pi, Phi*180/pi])
		print 'Your Euler angles of rotation are:', E
		
	else:
		Theta = -pi/2
		Psi = -Phi + atan2(-R[0,1], -R[0,2])
		
		E = m([Psi*180/pi, Theta*180/pi, Phi*180/pi])
		print 'Your Euler angles of rotation are:', E

else:
	print 'Your 3,1 matrix value is', R[2,0]
	print 'Going the easy method...'
	
	Theta1 = -asin(R[2,0])
	Theta2 = pi - Theta1
	print 'Theta1 =', Theta1
	print 'Theta1 =', Theta2

	#Find the corresponding angles of Psi
	Psi1 = atan2(R[2,1]/cos(Theta1), R[2,2]/cos(Theta1))
	Psi2 = atan2(R[2,1]/cos(Theta2), R[2,2]/cos(Theta2))
	print 'Psi1 =', Psi1
	print 'Psi2 =', Psi2

	#Find the corresponding angles of Phi
	Phi1 = atan2(R[1,0]/cos(Theta1), R[0,0]/cos(Theta1))
	Phi2 = atan2(R[1,0]/cos(Theta2), R[0,0]/cos(Theta2))
	print 'Phi1 =', Phi1
	print 'Phi1 =', Phi2

#Output in radians...
	E1 = m([Psi1, Theta1, Phi1])
	E2 = m([Psi2, Theta2, Phi2])
#Output in degrees...
#	E1 = m([Psi1*180/pi, Theta1*180/pi, Phi1*180/pi])
#	E2 = m([Psi2*180/pi, Theta2*180/pi, Phi2*180/pi])
	print 'Your possible Euler angles of rotation, which are equivalent are:'
	print 'Euler angle set 1 = ', E1
	print 'Euler angle set 2 = ', E2
