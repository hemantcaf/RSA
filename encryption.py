def encrypt(base, exp, mod):
    # variable to store the returning cipher text
    cipher = 1
    # converting 'e' into binary format
    exp = '{0:b}'.format(exp)
    # square and multiply
    for i in range(len(exp)):
        cipher = (cipher * cipher) % mod
        # For every index that is equal to 1 in the binary string, multiplying the cipher with the message
        if exp[i] == '1':
            cipher = (cipher * base) % mod
    # print('The cipher text is', cipher)
    return cipher


if __name__ == '__main__':
    message = "Chill Man"
    print("The message is", message)
    m1 = message[0:3].encode('ascii')
    m2 = message[3:6].encode('ascii')
    m3 = message[6:9].encode('ascii')
    # print("The 3 byte chunks are", m1, m2, m3)
    m1 = m1.hex()
    m2 = m2.hex()
    m3 = m3.hex()
    # print("Hex Strings are", m1, m2, m3)
    m1 = int(m1, 16)
    m2 = int(m2, 16)
    m3 = int(m3, 16)
    print("The messages in integers is", m1, m2, m3)
    e = int(input("Enter Public key e\n"))
    n = int(input("Enter Modulo N\n"))
    c1 = encrypt(m1, e, n)
    c2 = encrypt(m2, e, n)
    c3 = encrypt(m3, e, n)
    print('The encrypted strings are', c1, c2, c3)
