def sign(name, d, n):
    signedName = 1
    d = '{0:b}'.format(d)
    for i in range(len(d)):
        signedName = (signedName * signedName) % n
        if d[i] == '1':
            signedName = (signedName * name) % n
    return signedName


if __name__ == '__main__':
    D = int(input("Enter Private key"))
    N = int(input("Enter Modulo N"))
    name = 'hemant'
    name1 = name[0:3].encode('ascii')
    name2 = name[3:6].encode('ascii')
    name1 = name1.hex()
    name2 = name2.hex()
    name1 = int(name1, 16)
    name2 = int(name2, 16)
    print('The signature chunks', name1, name2)
    signature1 = sign(name1, D, N)
    signature2 = sign(name2, D, N)
    print('The signature is', signature1, signature2)
