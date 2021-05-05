def hex_cipher_encryptor(message: str) -> str:
    """Encrypts a given message using a Hex Cipher (converts characters to their hexadecimal equivalents).

    Args:
        message (str): Message to be encrypted.

    Returns:
        encrypted_message (str): Encrypted message.
    """
    encrypted_message = "".join([hex(ord(char)) for char in message])

    return encrypted_message


def hex_cipher_decryptor(encrypted_message: str) -> str:
    """Decrypts a message which has been encrypted using a Hex Cipher.

    Args:
        encrypted_message (str): Message to be decrypted.
    
    Returns:
        decrypted_message (str): Decrypted message.
    """
    encrypted_characters = [
        encrypted_message[i : i + 4] for i in range(0, len(encrypted_message), 4)
    ]
    decrypted_message = "".join([chr(int(char, 16)) for char in encrypted_characters])

    return decrypted_message


def atbash_cipher_encryptor_decryptor(message: str) -> str:
    """Encrypts and decrypts a given message using an AtBash Cipher (substitutes a letter of the plaintext 
    alphabet with the corresponding letter of the reversed alphabet).

    a <-> z
    b <-> y
    c <-> x

    Args:
        message (str): Message to be encrypted or decrypted.

    Returns:
        encrypted_decrypted_message (str): Encrypted or decrypted message.
    """
    N = ord("z") + ord("a")
    encrypted_decrypted_message = "".join([chr(N - ord(char)) for char in message])

    return encrypted_decrypted_message


def caesar_cipher_encryptor(key: int, message: str) -> str:
    """Encrypts a given message using a Caesar Cipher (substitutes a letter of the plaintext alphabet with a 
    letter located some fixed number of letters down the alphabet).

    If key = 3:
    a -> d
    b -> e
    z -> c

    Args:
        message (str): Message to be encrypted.
        key (int): Shift.

    Returns:
        encrypted_message (str): Encrypted message.
    """
    encrypted_message = "".join(
        [chr(((ord(char) - ord("a") + key) % 26) + ord("a")) for char in message]
    )

    return encrypted_message


def caesar_cipher_decryptor(key: int, encrypted_message: str) -> str:
    """Decrypts a message which has been encrypted using a Caesar Cipher.

    Args:
        encrypted_message (str): Message to be decrypted.
        key (int): Original shift.

    Returns:
        decrypted_message (str): Decrypted message.
    """
    decrypted_message = "".join(
        [
            chr(((ord(char) - ord("a") - key) % 26) + ord("a"))
            for char in encrypted_message
        ]
    )

    return decrypted_message


def keyword_cipher_encryptor(key: str, message: str) -> str:
    """Encrypts a given message using a Keyword Cipher (replaces a consecutive set of letters in the alphabet 
    (from the beginning) with a chosen keyword with any repeated letters removed. All other characters which 
    do not appear in the keyword are placed directly after the keyword in alphabetical order to form the 
    cipher alphabet.

    Args:
        message (str): Message to be encrypted.
        key (str): Keyword.

    Returns:
        encrypted_message (str): Encrypted message.
    """
    # Remove duplicate characters in key
    key = "".join(dict.fromkeys(key))

    # Create string of all lowercase characters
    chars = "".join([chr(char) for char in range(97, 123)])

    # Create cipher key
    for char in chars:
        if char not in key:
            key += char

    index_values = [chars.index(char) for char in message]
    encrypted_message = "".join(key[index] for index in index_values)

    return encrypted_message


def keyword_cipher_decryptor(key: str, encrypted_message: str) -> str:
    """Decrypts a message which has been encrypted using a Keyword Cipher.

    Args:
        encrypted_message (str): Message to be decrypted.
        key (str): Keyword.
    
    Returns:
        decrypted_message (str): Decrypted message.
    """
    # Remove duplicate characters in key
    key = "".join(dict.fromkeys(key))

    # Create string of lowercase characters
    chars = "".join([chr(char) for char in range(97, 123)])

    # Create cipher key
    for char in chars:
        if char not in key:
            key += char

    index_values = [key.index(char) for char in encrypted_message]
    decrypted_message = "".join(chars[index] for index in index_values)

    return decrypted_message


def vigenere_cipher_encryptor(key: str, message: str) -> str:
    """Encrypts a given message using a Vigenere Cipher (a more complicated cipher involving a keyword, in 
    which the letter subsitution of a plaintext letter is not always the same).

    Args:
        message (str): Message to be encrypted.
        key (str): Keyword.

    Returns:
        encrypted_message (str): Encrypted message.
    """
    key = list(key)
    if len(message) == len(key):
        full_key = key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
        full_key = "".join(key)

    encrypted_message = []
    for char in range(len(message)):
        x = (ord(message[char]) - 2 * ord("a") + ord(full_key[char])) % 26
        x += ord("a")
        encrypted_message.append(chr(x))
    encrypted_message = "".join(encrypted_message)

    return encrypted_message


def vigenere_cipher_decryptor(key: str, encrypted_message: str) -> str:
    """Decrypts a message which has been encrypted using a Vigenere Cipher.

    Args:
        encrypted_message (str): Message to be decrypted.
        key (str):
    
    Returns:
        decrypted_message (str): Decrypted message.
    """
    key = list(key)
    if len(encrypted_message) == len(key):
        full_key = key
    else:
        for i in range(len(encrypted_message) - len(key)):
            key.append(key[i % len(key)])
        full_key = "".join(key)

    decrypted_message = []
    for char in range(len(encrypted_message)):
        x = (ord(encrypted_message[char]) - ord(full_key[char])) % 26
        x += ord("a")
        decrypted_message.append(chr(x))
    decrypted_message = "".join(decrypted_message)

    return decrypted_message
