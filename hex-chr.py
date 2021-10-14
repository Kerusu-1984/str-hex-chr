name="kanimusi"
namelist = [*name]
hexlist = [hex(ord(c)) for c in namelist]
result = ""
for c in hexlist:
    result += chr(int(c,16))
print(result)
