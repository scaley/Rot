from numpy import *
from math import *

import numpy as np
m = matrix

CTF_FNAME = 'NC07-14AMap1proc-LGp50m1pg.ctf'

def read_ctf(fname=CTF_FNAME):

	eang = []
	for line in open(fname).readlines()[18:]:
		tmp = line.strip().split('\t')

		eang.append([float(x) for x in tmp[5:8]])

	return np.array(eang)

print read_ctf()[10, 0]

def atan2_(a, b, theta):
	return np.arctan2(a/np.cos(theta), b/np.cos(theta))

def get_euler(R):
	if np.abs(R[2,0]) <> 1:
		theta = (-np.arcsin(R[2, 0]), np.pi + np.arcsin(R[2, 0]))
		psi = (atan2_(R[2, 1], R[2, 2], theta[0]), atan2_(R[2, 1], R[2, 2], theta[1]))
		phi = (atan2_(R[1, 0], R[0, 0], theta[0]), atan2_(R[1, 0], R[0, 0], theta[1]))

		return (theta[0], psi[0], phi[0]), (theta[1], psi[1], phi[1])
	else:
		phi = 0

		if R[2, 0] == 1:
			theta = np.pi/2
			psi = phi + np.arctan2(R[0, 1], R[0, 2])
		else:
			theta = -np.pi/2
			psi = -phi + np.arctan2(-R[0, 1], -R[0, 2])

		return (theta, psi, phi)

def get_euler2(R):	

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

			return (Theta, Psi, Phi)

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

		return (Theta1, Psi1, Phi1), (Theta2, Psi2, Phi2)

if __name__ == '__main__':
	#Define the rotation matrix
	R = m([[0,0,-0.5],[0,1,0],[0.5,0,0]])
	#R = m([[0.5,-0.1464,0.8536],[0.5,0.8536,-0.1464],[-0.7071,0.5,0.5]])

	print get_euler(R)
	print get_euler2(R)
