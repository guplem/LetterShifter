import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def shift_letter(letter, shift):
    if letter.isalpha():
        return chr((ord(letter) - ord('a') + shift) % 26 + ord('a')) if letter.islower() else chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
    return letter

def shift_word(word, shift):
    return ''.join(shift_letter(letter, shift) for letter in word)

def main():
    with open('diccionario.txt', 'r', encoding='utf-8') as file:
        original_words = set(remove_accents(word.lower()) for word in file.read().splitlines())

    filename = f'outputs/{len(original_words)}_original.txt'
    with open(filename, 'w', encoding='utf-8') as file:
        for word in original_words:
            file.write(word + '\n')

    for shift in range(0, 28):
        shifted_words = set(shift_word(word, shift) for word in original_words)

        filename = f'outputs/{len(shifted_words)}_shifted_words_{shift}.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            for word in shifted_words:
                file.write(word + '\n')

        common_words = shifted_words.intersection(original_words)

        filename = f'outputs/{len(common_words)}_common_words_{shift}.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            for word in common_words:
                file.write(word + '\n')

if __name__ == "__main__":
    main()
