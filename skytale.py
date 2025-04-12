def skytale_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    while len(plaintext) % key != 0:
        plaintext += '_'
    spalten = len(plaintext) // key
    ciphertext = ''
    for i in range(spalten):
        for j in range(key):
            ciphertext += plaintext[j * spalten + i]
    return ciphertext

def skytale_decrypt(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "").upper()
    spalten = len(ciphertext) // key
    plaintext = [''] * len(ciphertext)
    index = 0
    for i in range(spalten):
        for j in range(key):
            plaintext[j * spalten + i] = ciphertext[index]
            index += 1
    return ''.join(plaintext).rstrip('_')

def main():
    print("Skytale-Chiffre")
    print("------------------")
    print("1. Verschlüsseln")
    print("2. Entschlüsseln")
    print("3. Beenden")
    while True:
        wahl = input("Bitte Option wählen (1, 2 oder 3): ")
        if wahl == '1':
            plaintext = input("Gib den Klartext ein: ")
            key = int(input("Gib die Stabdicke (Key) ein: "))
            encrypted = skytale_encrypt(plaintext, key)
            print(f"Verschlüsselter Text: {encrypted}")
        elif wahl == '2':
            ciphertext = input("Gib den Geheimtext ein: ")
            key = int(input("Gib die Stabdicke (Key) ein: "))
            decrypted = skytale_decrypt(ciphertext, key)
            print(f"Entschlüsselter Text: {decrypted}")
        elif wahl == '3':
            break
        else:
            print("Ungültige Auswahl. Bitte 1, 2 oder 3 eingeben.")

if __name__ == "__main__":
    main()
