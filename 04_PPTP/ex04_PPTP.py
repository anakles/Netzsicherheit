import hashlib

capturedHash = 'bb1ecd0d331bf33ada81e2aec716b990'

# Malte
#capturedHash = '327d324a11d868591251a986fb3db06b'

constant = 'NetSec1'

useValues = False

def md5(password, constant):
	# print(f"Debug: '{password + constant}'")
	m = hashlib.md5()
	m.update(str.encode(password + constant))
	return m.hexdigest()

def lmh(password, constant):
	while len(password) <= 14:
		password = password + "0"
	password = password.upper()
	return md5(password[:7], constant)[:16] + md5(password[7:14], constant)[:16]

def getPassword(leftPw, rightPw):
	return str(leftPw) + str(rightPw)

def controlPassword(password):
	controlHash = lmh(password, constant)
	print(f" == Control Output: {capturedHash} == {controlHash}")

	if controlHash == capturedHash:
		print(" = Hashes match")
	else:
		print(" = [!!!] Hashed don't match [!!!]")

# = Found candidate 97 with hash da81e2aec716b990
def crackRightHash():
	rightHash = capturedHash[16:]
	print(" == Trying to figure out the password for: ", rightHash)

	for i in range(0, 100):
		tempHash = md5(str(i) + "00000", constant)[:16]
		# print(f" === Cracking hash for {i}: {tempHash}")

		if tempHash == rightHash:
			print(f" = Found candidate {i} with hash {tempHash}")
			return str(i) 

# = Found candidate 2767694 with hash bb1ecd0d331bf33a
def crackLeftHash():
	leftHash = capturedHash[:16]
	print(" == Trying to figure out the password for: ", leftHash)

	for i in range(1000000, 10000000):
		tempHash = md5(str(i), constant)[:16]
		# print(f" === Cracking hash for {i}: {tempHash}")

		if tempHash == leftHash:
			print(f" = Found candidate {i} with hash {tempHash}")
			return str(i)
			
# == Main Function ==

if not(useValues):
	print(' = Starting breaking hashes...')
	
	rightPw = crackRightHash()
	print(" = Right part of the password is: ", rightPw)

	leftPw = crackLeftHash()
	print(" = The password candidate is: ", getPassword(leftPw, rightPw))

else:
	print(" == Starting with preset values.")
	rightPw = '97'
	leftPw = '2767694'

# Control the results
password = getPassword(leftPw, rightPw)
controlPassword(password)
