letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt(letters):
    plaintext = ''
    for i in range(len(letters)):
        for j in cipher:
            if j in letters:
                n = letters.find(j)
                n = n - i
                if n < 0:
                    n = n + len(letters)
                plaintext += letters[n]

        print('\nKEY {} : Plaintext -  {}'.format(i, plaintext))
        plaintext = ''


if __name__ == "__main__":
    cipher = input("Enter Cipher : ")
    if cipher.islower():
       letters = letters.lower()
    decrypt(letters)
    
