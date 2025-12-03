def caesar(text, shift, encrypt=True):
    """Applying a Caesar cipher to the given text."""

    if not isinstance(shift, int):
        raise TypeError("Shift must be an integer.")

    if shift < 1 or shift > 25:
        raise ValueError("Shift must be between 1 and 25.")

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = -shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    return text.translate(translation_table)


def encrypt(text, shift):
    """Encrypt text using the Caesar cipher."""
    return caesar(text, shift)


def decrypt(text, shift):
    """Decrypt text using the Caesar cipher."""
    return caesar(text, shift, encrypt=False)
