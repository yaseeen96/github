import os

fd = os.open("secret.txt", os.O_RDONLY)

secret = os.read(fd, 100)
print(secret)
