#Implement Playfair Cipher
def generate_table(key):
    # Create a 5x5 grid of letters
    table = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append('')
        table.append(row)

    # Fill in the grid with the key and the alphabet
    key = key.upper()
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    index = 0
    for char in key + alphabet:
        if char not in [row[j] for row in table for j in range(5)]:
            table[index // 5][index % 5] = char
            index += 1

    return table

def prepare_input(plaintext):
    # Convert the plaintext to uppercase and remove spaces
    plaintext = plaintext.upper().replace(' ', '')

    # Replace J with I
    plaintext = plaintext.replace('J', 'I')

    # Split the plaintext into pairs of letters
    pairs = []
    i = 0
    while i < len(plaintext):
        if i + 1 < len(plaintext):
            pairs.append(plaintext[i:i+2])
            i += 2
        else:
            pairs.append(plaintext[i] + 'X')
            i += 1

    return pairs

def encrypt(plaintext, key):
    table = generate_table(key)
    pairs = prepare_input(plaintext)
    ciphertext = ''

    for pair in pairs:
        # Find the coordinates of the two letters in the pair
        for i in range(5):
            for j in range(5):
                if table[i][j] == pair[0]:
                    row1 = i
                    col1 = j
                if table[i][j] == pair[1]:
                    row2 = i
                    col2 = j

        # Apply the encryption rules
        if row1 == row2:
            ciphertext += table[row1][(col1 + 1) % 5] + table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += table[(row1 + 1) % 5][col1] + table[(row2 + 1) % 5][col2]
        else:
            ciphertext += table[row1][col2] + table[row2][col1]

    return ciphertext

# Example usage
plaintext = "hello"
key = "god"
ciphertext = encrypt(plaintext, key)
print(ciphertext)