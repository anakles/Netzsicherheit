"""
Now calculate the message signed by the email server from the DKIM signature by 
exponentiating the value of the signature with the public RSA exponent 
(modulus the public RSA modulus). You can use the Python function pow(basis, exponent, modulus) 
to do this.
"""
modulus = 0x5b8e9197201d654bc2c674ba3ff23bb833f95ee719393d0a535082c9f
pub_exponent = 0x10001 	# hex(65537)

signature = 'efaKslYarrtXPmISSPU3w72uTVEq83CsYNnGsl4SnFgNZYsYmdFgNUgmGZA169VxLRs/8d6gFS8btBjELOzSafcla8gQhxnAGyhh9w/ZxJBsJaJjEafkt8iToDJGnhgLAUUsH8zqxmC2f7uPJ0VqeReBkvkhHzrF2i3xfchgUrk='

