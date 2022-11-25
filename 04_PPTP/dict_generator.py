allowedCharacters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
"""
f = open("dictionary.txt", "w")

for i in allowedCharacters:
	for j in allowedCharacters:
		for k in allowedCharacters:
			for l in allowedCharacters:
				for m in allowedCharacters:
					for n in allowedCharacters:
							entry = i + j + k + l + m + n +"\n"
							print(entry)
							f.write(entry)

f.close()
"""

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

# all possible P1 bis P6
with open("dictionary.txt", "w") as outfile:
   for c1 in char_range('a', 'z'):
        for c2 in char_range('a', 'z'):
            for c3 in char_range('a', 'z'):
                for c4 in char_range('a', 'z'):
                    for c5 in char_range('a', 'z'):
                        for c6 in char_range('a', 'z'):
                            newPassword = c1.upper() + c2.upper() + c3.upper() + c4.upper() + c5.upper() + c6.upper()
                            print(newPassword)
                            outfile.write(newPassword + "\n")
