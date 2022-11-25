import math

#k = [3,7,2,5,1]
k = [4, 7, 4, 5, 4]
s = []
l = 5
n = pow(2,3)

def ksa():
	#Initialisierung:
	for i in range(0, n-1):
		s.append(i)
	# print(s)

	j=0

	# Scambling
	for i in range(0,n-1):
		j = (j + s[i] + k[i % l]) % (n-1)
		
		# print(f"Iteration {i} with j={j}")
		swap(s[i], s[j])

def swap(i, j):
	# print(f"Swapping {s[i]} with {s[j]}")
	tmp = s[j]
	s[j] = s[i]
	s[i] = tmp


# == MAIN FUNCTION ==
print("Using Key: ", k)

# First initiialize the array S[]
ksa()
# print(s)

# Generate the first x amount of outputs:
x = 5
keygen_i = 0
keygen_j = 0

for iterator in range(0, x):

	keygen_i = (keygen_i + 1) % (n-1)
	keygen_j = (keygen_j + s[keygen_i]) % (n-1)
	swap(s[keygen_i], s[keygen_j])

	z = s[(s[keygen_i] + s[keygen_j]) % (n-1)]
	print(f"The i={iterator+1} output is: {z}")
