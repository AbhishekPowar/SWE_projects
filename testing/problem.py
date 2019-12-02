def caesarCipher(s, k):
    alpha=list(map(chr,range(ord('a'),ord('z')+1)))
    s=list(s)
    k=k%26
    #add comment
    for i in range(len(s)):
        if s[i] in alpha:
            val=ord(s[i])+k
            if val>ord('z'):
                val=val-ord('z')+ord('a')-1
            s[i]=chr(val)
    return "".join(s)

print(caesarCipher('www.abc.xy',87))