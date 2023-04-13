from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key(passphrase="user")
filename = input("Enter filename to store private key:")
file_out = open(filename, "wb")
file_out.write(private_key)
file_out.close()

print(private_key)

public_key = key.publickey().export_key()
filename2 = input("Enter filename to store public key:")
file_out = open(filename2, "wb")
file_out.write(public_key)
file_out.close()
print(public_key)
