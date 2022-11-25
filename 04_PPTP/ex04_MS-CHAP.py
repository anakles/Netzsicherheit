"""
### Informationstext
In this task, you are to reproduce the attack against MS-CHAP in MS-PPTPv1 and perform it yourself. 
For this purpose, we have created a modified version of MS-CHAP that also uses MD5 instead of 
DES. You have eavesdropped on an authentication using this modification of the MS-CHAP 
protocol and recorded the challenge and response. Now you have to calculate the password used 
for authentication. Proceed as described in the lecture.

Tip: Try the attack on a password you know first; 
this will help you find bugs in your implementation of the attack. 
On a machine that can do 2^25 MD5 evaluations per minute, the attack takes about 10 minutes. 
Bruteforce, on the other hand, takes about 22 days. Note that strings instead of bytes are 
processed here in some places and specify the password in correct notation (i.e. case-sensitive) 
at the end.

You know that the password is 9 characters long, the first character is a "w" and all following 
8 characters are upper- and lowercase letters. The following values are given (as commented in 
the supplied code):
"""

import hashlib
from itertools import product

allowedLiterals = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
allowedCharacters = ['0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# dictionary = r"C:\Users\nikla\MEGA\Dokumente\Applied IT-Security Ma\Modul 05 - Netzsicherheit\Exercises\04_PPTP\temp_dictionary2.txt"
dictionary = r"C:\Users\nikla\MEGA\Dokumente\Applied IT-Security Ma\Modul 05 - Netzsicherheit\Exercises\04_PPTP\dictionary.txt"

constant = 'NetSec1'
challenge = 'GoodLuck!'
response = '77430cc47afc904c254020cf7d7fbe3432ba1d4938a1550b19ea0bca6f759f23cba562e96465026b0b98bae0417627cc' # Exercise response
# response = '8cc59222e199d0cd291a7a424042f0b114652e00301514ce7972fefc99990b2f21273f67490ec17f4eac6f065b3d4b3b' # Exercise von Malte
# response = '62e967056fc0a0bb901ee3b0a084e92f39c29257d5d6078a358f047049425f9bd51ecc26f8ec992e371437ba4c20befd' # this is the response for "password"
# response = '62e967056fc0a0bb901ee3b0a084e92f39c29257d5d6078a7463f183386dabc8c68e8125047ca6ded35c02404da4492c' # this is the response for "passWorD"
# response = '82270e6702e1b13099d425d199fa6ab7630677989b267c7106cec120d3e68dc5e26f7510aa2521b5089978c7657aa085' # this is the response for "testtest"
# response = '3d913e855f32d580fdc097e01f4fa36c39c29257d5d6078a1edb21ecc5dddb2e172a19e8747aedefdb804b2311008436' # this is the response for "WortWord"
# response = 'f8cd67d50411e848927d5670819d78ada2f481932093725893a1110de19ccd4732e8d969012bd9358fa9d34d84ee3e8c' # this is the response fpr "Wsrghserq"

startingLetter = "W"

# List of candidates
candidatesRes1 = []
candidatesRes2 = []
candidatesRes3 = []
candidatesRightLmh = []
candidatesLeftLmh = []


leftPasswordHalve = ""
rightPasswordHalve = ""

# Additional toggles
verbose = False

# Control the input parameters
def controlInput():
	# Control prameters of the response:
	print(" ==== Checking input parameters ====")
	print(" => Challenge: ", challenge)
	print(" => Constant: ", constant)
	print(" => Response: ", response)
	print(" => Password starts wiht the letter: ", startingLetter)

	if len(response) == (6*16):
		print(" => == PASSED == Length of response is ", len(response))
	else:
		print(" => == FAILED == Length of response is ", len(response))


# Calculate "DES" for password and constant
def md5(md5Password, md5Constant):
	m = hashlib.md5()
	m.update(str.encode(md5Password + md5Constant))
	return m.hexdigest()


# Calculate the LMH hash for password and constant
def lmh(lhmPassword, lhmConstant):
	while len(lhmPassword) <= 14:
		lhmPassword = lhmPassword + "0"
	lhmPassword = lhmPassword.upper()
	return md5(lhmPassword[:7], lhmConstant)[:16] + md5(lhmPassword[7:14], lhmConstant)[:16]


def wnth(password, constant):
	while len(password) <= 14:
		password = password + "0"
	return md5(password, constant)[:32]


# Crack the RES3
def crackRes3(res3):
	print(" ==== Starting cracking RES3 ====")
	print(" => RES3: ", res3)

	# Brute force the possible 
	#for i in allowedLiterals:
	# 	for j in allowedLiterals:
	for i in range(0x0, 0x10000):
		candidate = hex(i)[2:] + "0000000000"
		candidateHash = md5(candidate, challenge)[:16]
		
		if verbose:
			print(f" == [RES3] > ({candidate}) == {candidateHash}")

		if candidateHash == res3:
			print("")
			print(f" == [RES3] > Found a candidate for RES3")
			print(f" == [RES3] > ({candidate}) == {candidateHash}")
			
			# Append candidate to the list of candidates
			candidatesRes3.append(candidate)
			# return


# Crack the RES2
def crackRes2(res2):
	print(" ==== Starting cracking RES2 ====")
	print(" => RES2: ", res2)

	# For every candidate that was found for RES3:
	for c in candidatesRes3:
		print(f" == [LMH] > Testing for candidate ({c})")

		# First brute forcing the last password part (2 numbers, caps only, padded with 0s)	
		for i in allowedCharacters:
			for j in allowedCharacters:

				# Join to candidate with format ##00000
				candidate = i + j + "00000"
				candidateHash = md5(candidate, constant)[:16]

				if verbose:
					print(f" == [LMH] > ({candidate}) == {candidateHash}")

				# Compate, if the last 4 characters match
				# if candidateHash[(len(candidateHash)-4):] == c.replace("0", ""):
				if candidateHash[(len(candidateHash)-4):] == c[:4]:
					print("")
					print(f" == [LMH] > Found a candidate for left password halve")
					print(f" == [LMH] > ({candidate}) == {candidateHash}")
					
					# Append candidate to the list of candidates
					candidatesRightLmh.append(candidate)


	# Test if a candidate results in RES2
	for c in candidatesRightLmh:
		print("")
		print(f" == [RES2] > Testing all possible password candidates")

		candidateHash = md5(c, constant)[:16]
		print(f" == [RES2] > Testing candidate ({c}) == {candidateHash}")

		# any string for the first 7 Byte of the LMH input and the candidate as the second value for LMH
		inputLmh = "AAAAAAA" + c

		# Only the middle part of the lmh hash is hashed into the RES2, so only byte 14-28 are relevant
		result = (lmh(inputLmh, constant) + "0000000000")
		# Also stripping the first 2 characters away, because we want to brute force them now
		result = result[16:28]

		# The first 2 bit are still unknown and must be bruteforced:
		for c1 in allowedLiterals:
			for c2 in allowedLiterals:
				# Only the first 14 Byte are hashed with DES/MD5, the first two byte are still unknown.
				candidate = (c1 + c2 + result)
				# print("This should now be a 16 byte candidate: ", len(candidateHash))

				# calculate the DES md5 sum:
				tmpRes2 = md5(candidate,challenge)[:16]		
				
				if verbose:
					print(f" == [RES2] > ({candidate}) == {tmpRes2}")

				if tmpRes2 == res2:
					print("")
					print(f" == [RES2] > Found a candidate for RES2")
					print(f" == [RES2] > ({c}) == {tmpRes2}")
							
					# Append candidate to the list of candidates
					candidatesRes2.append(candidate)

					# We can return here, because we have found an exact match
					return c


# Crack the RES1
def crackRes1(res1, targetHash, rightPasswordHalve):
	print(" ==== Starting cracking RES1 ====")
	print(" => RES1: ", res1)
	print("")
	print(f" == [RES1] > Testing all possible password halves")

	# for each in dictionary check:
	# lhm(leftPassword + rightPassword)):
	# 	if (last 2 characters H15 & H16 match to the first 2 chars of the candidate of res2)
	# 	then: found a valid password

	with open(dictionary, 'r') as f:
		# print("Loaded dictionary file: ", str(f))

		ctr = 0

		for line in f.readlines():
			line = line.rstrip()
			ctr += 1

			# Create a new candidate (temp P) + brute force + found left password halve
			candidate = startingLetter + line + rightPasswordHalve
			# Convert word from dictionary to hash:
			hashedWord = lmh(candidate, constant)

			if (ctr % 1000000) == 1:
				print(f" == [RES1] > Currently trying word #{ctr}")

			if verbose:
				print(f" == [RES1] > Trying word: {startingLetter}|{line}|{rightPasswordHalve} ({hashedWord})")

			# print(f"{hashedWord[14:16]} == {targetHash[:2]}")

			# Break if the last 2 characters of the hash match with the first 2 of the res2 ur-image
			if hashedWord[14:16] == targetHash[:2]:
				print("")
				print(f" == [LMH] > Found a candidate for RES1: ({line}) == {hashedWord}")
				print(f" == [LHM] > Tryed {ctr} candidates so far")
				#candidatesLeftLmh.append(line)

				# For every candidate we can now check, if the RES1 would be the same:
				passwordCandidate = startingLetter + line
				fullPassword = passwordCandidate + rightPasswordHalve

				tempLmh = lmh(fullPassword, constant)
				tempRes1 = md5(tempLmh[:14], challenge)[:16]

				if verbose:
					print(f" == [RES1] > Verifying candidate ({passwordCandidate}) with resulting RES1 {tempRes1}")
			
				# If the resulting res1 from the candidate matches the given RES1, a valid password was found
				if tempRes1 == res1:
					print(f" == [RES1] > Found a valid candidate for RES1")
					print(f" == [RES1] > ({passwordCandidate}) == {tempRes1}")

					# Return the valid password candidate for the right password halve
					return passwordCandidate


def getCaseInsensitivePassword(passwordCandidate, fullResponse):
	print(f" == [PASSWORD] > Trying all case-sensitive possiblities for ({passwordCandidate})")

	# first strip away all "0"
	passwordCandidate = passwordCandidate.replace("0", "")

	# turn candidate into an array to enumerate over:

	candidateArray = getAllCandidates(passwordCandidate)
	# print(candidateArray)

	for finalPassword in candidateArray:

		# Calculate response for candidate:
		firstHash = lmh(finalPassword, constant) + "0000000000"
		secondHash = wnth(finalPassword, constant) + "0000000000"

		res1 = md5(firstHash[:14],challenge)[:16]
		res2 = md5(firstHash[14:28],challenge)[:16]
		res3 = md5(firstHash[28:42],challenge)[:16]
		res4 = md5(secondHash[:14],challenge)[:16]
		res5 = md5(secondHash[14:28],challenge)[:16]
		res6 = md5(secondHash[28:42],challenge)[:16]

		tempResponse = res1 + res2 + res3 + res4 + res5 + res6

		if verbose:
			print(f"== [PASSWORD] > Trying ({finalPassword}) ...")

		# if the responses match, the valid password was found
		if tempResponse == fullResponse:
			print(f" == [RES1] > Found a valid candidate for RES1")
			print(f" == [RES1] > ({finalPassword}) == {tempResponse}")

			return finalPassword


# Stolen from StackOverflow
def getAllCandidates(istr):
    l = [(c, c.upper()) if not c.isdigit() else (c,) for c in istr.lower()]
    return ["".join(item) for item in product(*l)]


# == Main Function ==
controlInput()

# First trim the response into the 6 different response values
res1 = response[:16]
res2 = response[16:(2*16)]
res3 = response[(2*16):(3*16)]
res4 = response[(3*16):(4*16)]
res5 = response[(4*16):(5*16)]
res6 = response[(5*16):]

print("")
print(f" ===> RES1 = {res1}")
print(f" ===> RES2 = {res2}")
print(f" ===> RES3 = {res3}")
print(f" ===> RES4 = {res4}")
print(f" ===> RES5 = {res5}")
print(f" ===> RES6 = {res6}")
print("")

# Cracking the first hash RES3
# RES3 = MD5(LMH(password)||00000)
crackRes3(res3)

# Cracking the second hash RES2
# res2 = md5(firstHash[14:28],challenge)[:16]
rightPasswordHalve = crackRes2(res2)

# Cracking the third hash RES1
# res1 = md5(firstHash[:14],challenge)[:16]
leftPasswordHalve = crackRes1(res1, candidatesRes2[0], rightPasswordHalve)

if leftPasswordHalve == None:
	print(f" == [PASSWORD] > ERROR: Could not find a valid password candidate")
else:
	print(f" == [PASSWORD] > The (case-insensitive) password is: {leftPasswordHalve}{rightPasswordHalve}")

	# finally get the case-sensitive password:
	password = getCaseInsensitivePassword(leftPasswordHalve + rightPasswordHalve, response)
	print(f" == [PASSWORD] > The (case-sensitive) password is: {password}")
	print(f" == [FINISHED] == ")


