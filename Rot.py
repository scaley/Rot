from numpy import *
from math import *
m = matrix

__doc__ = """
if (R31 6= ±1)
θ1 = −asin(R31)
θ2 = π − θ1
ψ1 = atan2
R32
cosθ1
,
R33
cosθ1

ψ2 = atan2
R32
cosθ2
,
R33
cosθ2

φ1 = atan2
R21
cosθ1
,
R11
cosθ1

φ2 = atan2
R21
cosθ2
,
R11
cosθ2

else
φ = anything; can set to 0
if (R31 = −1)
θ = π/2
ψ = φ + atan2(R12, R13)
else
θ = −π/2
ψ = −φ + atan2(−R12, −R13)
end if
end if
"""

def atan2_(a, b, theta):
	return np.atan2(a/np.cos(theta), b/np.cos(theta))

def get_euler(R):
	if np.abs(R[2,0]) == 1:
		theta = (-np.asin(R[2, 0]), np.pi + np.asin(R[2, 0]))
		psi = (atan2_(R[2, 1], R[2, 2], theta[0]), atan2_(R[2, 1], R[2, 2], theta[1]))
		phi = (atan2_(R[1, 0], R[0, 0], theta[0]), atan2_(R[1, 0], R[0, 0], theta[1]))
	else:
		phi = 0

		if R[2, 0] == 1:
			theta = np.pi/2
			psi = phi + np.atan2(R[0, 1], R[0, 2])
		else:
			theta = -np.pi/2
			psi = -phi + np.atan2(-R[0, 1], -R[0, 2])






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
