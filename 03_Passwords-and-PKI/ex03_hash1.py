import hashlib

# targetHash = '46256e1e9f868bce7e89cef99004c1600e17da2e'
targetHash = '052a3c16072efa89c25f7ab9417794876fd2c131'
file = "C:\\Users\\nikla\\MEGA\\Dokumente\\Applied IT-Security Ma\\Modul 05 - " \
       "Netzsicherheit\\Exercises\\03_Passwords-and-PKI\\common-passwords.txt "

# Open file
print("Opening file: ", file)

with open(file, 'r') as f:
    for line in f.readlines():
        # Convert word from dictionary to hash:
        hashedWord = hashlib.sha1(line.rstrip().encode('utf-8')).hexdigest()
        print(f"Trying word: {line} ({hashedWord})")

        # Break if the hashed word equals the hash
        if hashedWord == targetHash:
            print(f"Word for hash was found: {line} with hash ({hashedWord})")
            break

f.close()