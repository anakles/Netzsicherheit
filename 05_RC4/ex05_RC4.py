k = [35, 54, 155, 213, 167, 47, 16, 31]
s = []
l = len(k)

def ksa():
	#Initialisierung:
	for i in range(0, 256-1):
		s.append(i)
	# print(s)

	j=0

	# Scambling
	for i in range(0,256-1):
		j = (j + s[i] + k[i % l]) % 255
		
		# print(f"Iteration {i} with j={j}")
		swap(s[i], s[j])

def swap(i, j):
	# print(f"Swapping {s[i]} with {s[j]}")
	tmp = s[j]
	s[j] = s[i]
	s[i] = tmp


# == MAIN FUNCTION ==

# First initiialize the array S[]
ksa()
# print(s)

# Generate the first x amount of outputs:
x = 20
keygen_i = 0
keygen_j = 0

for iterator in range(0, x):

	keygen_i = (keygen_i + 1) % 255
	keygen_j = (keygen_j + s[keygen_i]) % 255
	swap(s[keygen_i], s[keygen_j])

	z = s[(s[keygen_i] + s[keygen_j]) % 255]
	print(f"The i={iterator+1} output is: {z}")

"""
The i=1 output is: 206
The i=2 output is: 170
The i=3 output is: 251
The i=4 output is: 232
The i=5 output is: 181
The i=6 output is: 164
The i=7 output is: 102
The i=8 output is: 14
The i=9 output is: 163
The i=10 output is: 196
The i=11 output is: 197
The i=12 output is: 134
The i=13 output is: 107
The i=14 output is: 54
The i=15 output is: 183
The i=16 output is: 196
The i=17 output is: 201
The i=18 output is: 174
The i=19 output is: 254
The i=20 output is: 96
"""