name="kanimusi"
namelist = [*name]
result = ""
for c in [hex(ord(n)) for n in namelist]:
    result += chr(int(c,16))
print(result)
