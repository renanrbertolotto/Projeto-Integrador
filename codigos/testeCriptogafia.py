import numpy as np

def encrypt(text, matrix):
    # Remove os espaços da frase de entrada
    text = text.replace(" ", "")
    
    # Verifica se o comprimento do texto é ímpar
    if len(text) % 2 != 0:
        # Se for ímpar, duplica a última letra
        text += text[-1]
    
    # Transforma o texto em conjunto de duas letras
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    encrypted_text = ""
    
    # Loop pelos pares de letras
    for pair in pairs:
        # Converte as letras em vetores
        vector = np.array([ord(char) - ord('a') + 1 if char != 'z' else 0 for char in pair])
        
        # Multiplica pela matriz
        result_vector = np.dot(matrix, vector)
        
        # Divide por 26 e calcula o resto
        result_vector %= 26
        
        # Converte os números de volta em letras
        encrypted_pair = ''.join([chr(char + ord('a') - 1) if char != 0 else 'z' for char in result_vector])
        
        # Adiciona o par criptografado ao texto criptografado
        encrypted_text += encrypted_pair
    
    return encrypted_text

def decrypt(encrypted_text, matrix):
    decrypted_text = ""

    # Calcula a matriz inversa
    inv_matrix = np.linalg.inv(matrix)

    # Loop pelos pares de letras
    for pair in [encrypted_text[i:i+2] for i in range(0, len(encrypted_text), 2)]:
        # Converte as letras em vetores
        vector = np.array([ord(char) - ord('a') + 1 if char != 'z' else 0 for char in pair])

        # Multiplica pela matriz inversa
        result_vector = np.dot(inv_matrix, vector)

        # Divide por 26 e calcula o resto
        result_vector %= 26

        # Converte os números de volta em letras
        decrypted_pair = ''.join([chr(int(char) + ord('a') - 1) if char != 0 else 'z' for char in result_vector])

        # Adiciona o par descriptografado ao texto descriptografado
        decrypted_text += decrypted_pair

    return decrypted_text




# Texto a ser criptografado
text = "we love math"

# Matriz base
matrix = np.array([[4, 3], [1, 2]])

# Chama a função de criptografia
encrypted_text = encrypt(text, matrix)

# Chama a função de descriptografia
decrypted_text = decrypt(encrypted_text, matrix)

# Imprime os resultados
print("Texto criptografado:", encrypted_text)
print("Texto descriptografado:", decrypted_text)


#cg opyf cozj