
def decrypt(cipher, d, mod):
    plain = 1
    d = '{0:b}'.format(d)
    for i in range(len(d)):
        plain = (plain * plain) % mod
        if d[i] == '1':
            plain = (plain * cipher) % mod
    return plain


if __name__ == '__main__':
    length = int(input('Enter the number of strings:\n'))
    D = int(input('Enter Private key:\n'))
    N = int(input('Enter Modulo:\n'))
    outputs = []
    for x in range(length):
        message = int(input('Enter encrypted text:'))
        p1 = decrypt(message, D, N)
        p1 = hex(p1)
        p1 = p1[2:]
        p1 = bytearray.fromhex(p1).decode('ascii')
        p1 = format(p1)
        outputs.append(p1)
        outputs1 = ("".join(outputs))
    print('The Decrypted text is', outputs1)
