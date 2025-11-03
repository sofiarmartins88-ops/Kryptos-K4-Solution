Double Vigenère Cipher Implementation for K4
Author: Sofia do Rosário Martins
Contact: sofia.r.martins.88@gmail.com
"""

def vigenere_encrypt(plaintext, key):
    """
    Standard Vigenère cipher encryption
    """
    ciphertext = []
    key_length = len(key)
    
    for i, char in enumerate(plaintext):
        if char.isalpha():
            p_num = ord(char.upper()) - ord('A')
            k_num = ord(key[i % key_length].upper()) - ord('A')
            c_num = (p_num + k_num) % 26
            ciphertext.append(chr(c_num + ord('A')))
        else:
            ciphertext.append(char)
    
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    """
    Standard Vigenère cipher decryption
    """
    plaintext = []
    key_length = len(key)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            c_num = ord(char.upper()) - ord('A')
            k_num = ord(key[i % key_length].upper()) - ord('A')
            p_num = (c_num - k_num) % 26
            plaintext.append(chr(p_num + ord('A')))
        else:
            plaintext.append(char)
    
    return ''.join(plaintext)

def mirror_transform(text):
    """
    Mirror transformation: reverse text + Atbash substitution
    """
    # Reverse the text
    reversed_text = text[::-1]
    
    # Atbash substitution (A↔Z, B↔Y, ..., M↔N)
    substitutions = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 
                                 'ZYXWVUTSRQPONMLKJIHGFEDCBA')
    
    return reversed_text.translate(substitutions)

def double_vigenere_encrypt(plaintext, key="KRYPTOS"):
    """
    Double Vigenère encryption - Core K4 method
    """
    print(f"🔐 DOUBLE VIGENÈRE ENCRYPTION with key: '{key}'")
    
    # First Vigenère encryption
    stage1 = vigenere_encrypt(plaintext, key)
    print(f"Stage 1 (Vigenère): {stage1[:30]}...")
    
    # Mirror transformation
    stage2 = mirror_transform(stage1)
    print(f"Stage 2 (Mirror): {stage2[:30]}...")
    
    # Second Vigenère encryption
    stage3 = vigenere_encrypt(stage2, key)
    print(f"Stage 3 (Vigenère): {stage3[:30]}...")
    
    return stage3

def double_vigenere_decrypt(ciphertext, key="KRYPTOS"):
    """
    Double Vigenère decryption - Core K4 method
    """
    print(f"🔓 DOUBLE VIGENÈRE DECRYPTION with key: '{key}'")
    
    # First Vigenère decryption
    stage1 = vigenere_decrypt(ciphertext, key)
    print(f"Stage 1 (Vigenère⁻¹): {stage1[:30]}...")
    
    # Mirror transformation
    stage2 = mirror_transform(stage1)
    print(f"Stage 2 (Mirror): {stage2[:30]}...")
    
    # Second Vigenère decryption
    stage3 = vigenere_decrypt(stage2, key)
    print(f"Stage 3 (Vigenère⁻¹): {stage3}")
    
    return stage3

def demonstrate_double_vigenere():
    """
    Demonstrate the complete double Vigenère process
    """
    test_message = "TESTMESSAGE"
    key = "KRYPTOS"
    
    print("🎯 DEMONSTRATING DOUBLE VIGENÈRE CIPHER")
    print("=" * 50)
    
    # Encryption
    ciphertext = double_vigenere_encrypt(test_message, key)
    
    print("\n" + "=" * 50)
    
    # Decryption  
    decrypted = double_vigenere_decrypt(ciphertext, key)
    
    print("\n" + "=" * 50)
    print(f"✅ Original: {test_message}")
    print(f"✅ Decrypted: {decrypted}")
    print(f"✅ Match: {test_message == decrypted}")

if __name__ == "__main__":
    demonstrate_double_vigenere()
