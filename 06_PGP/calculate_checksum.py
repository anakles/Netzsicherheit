# Calculate the checksum by modulo 
def calculateChecksum(paramSum):
	modul = 0x10000 	# >>> hex(65536) = '0x10000'
	public_p = 0xb805375d6e629284275483eff61a39e9134737a07fd2685bf5166de3663f0cf3f53be8602ee75b7da3d9899fa1ca7b94073797bc4e49da7980d0dfa78e3e09cb95d8a45b6b904ecc58de9a8cb942ec1d4509ca78638e260d51474718c69d0dfe6607d693cdf9af34fb8f8f9885f96f62935a9c0f397a99c39d0df12e130dcea7
	public_q = 0xabc0b5a1ef7421ca0771d1bd84b191ad9707fdff
	public_g = 0xa7f76232d0785854bc014fc7a95a7dc3f27716bc20f1ba3c6e34017a94dcbfb4dde553db6cffc648d07ea07bb7aef24f1d1ba6ca56886946c007e95c9948aa6d4229140703c0e0b5347dd30d6320f71cc090b0b3e24c62c0dddbc4d636c5224577bc4c9789c4e75a27eb6c893c8c96140ab5c2ad7161e7b82b6af74f98dbd6aa
	public_y = 0x0529d2917e0545c1d4ee93c25ee8c5d95ce4b37d3b99b6ea1c01eb02feb15858ea3495acba279e4b1a0119d1d04f0bda8409bacc6ed700028a591e40f817cac130cec8c0c253dc2b529e9bb2915944a72f995516a7db80e59918fa547a061f73a966d03d42cc064ddbaae5450f2aeb7065161f1a3c8c70bbdc90cda8c7c128ed

	return (public_p + public_q + public_g + public_y + paramSum) % modul


new_x = 0xb0b0dead

# First verify the old checksum:
old_x = 0x8d5d6a83d840ed591623768bb89e60602529651a
checksumOld = 0x08f2


temp = hex(calculateChecksum(old_x))
if hex(checksumOld) == temp:
	print('Successfully verified the old checksum')
else:
	print(f'Could not verify the old checksum -> Result differs {temp}')

# Calculate the checksum for the new x:
print(f"New checksum for x={hex(new_x)}: {hex(calculateChecksum(new_x))}")