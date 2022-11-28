import math

message = 'NetSeC'
letters = []
n = 585209

for c in message:
	letters.append(bin(ord(c)))

print(letters)

# build ascii value for word
word = ''

for l in letters:
	word = word + str(l)[2:]

print(word)

# convert back to decimal
number = int(word, 2)
print(number)

# perform modulo operation
m = number % n # = 31778
print(m)
print()

# -------------------------------------------------------
# calculate s'^e mod n

s = 357672
e = 7

inv_s = pow(s, e) % n
print(inv_s) # = 61769
print()

# -------------------------------------------------------
# calculate ggt(m−s′^e,n) 

def getGgt(x,y):
	if(y == 0):
		return abs(x)
	else:
		return getGgt(y, x % y)


p = getGgt(m - inv_s, n)	# = 769
print(p)
print()

# -------------------------------------------------------
# calculate q = n/p

q = n/p 	# 761
print(q)
print()