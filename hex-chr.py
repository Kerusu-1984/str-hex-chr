name="kanimusi"

def str_to_hex(str:str):
    chrlist = [*str]
    return [hex(ord(n)) for n in chrlist]

def hex_to_str(hex:list):
    result = ""
    for c in hex:
        result += chr(int(c,16))
    return result

def No1():
    chrlist = [c.replace("0x","") for c in str_to_hex(name)]
    for i in chrlist:
        print(i,end=" ")

def No2():
    print(hex_to_str(str_to_hex(name)))

No1()
No2()