

class morseCodeDecoder:
    letter_to_morse_code_map = {
        'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.', ':': '---...', ' ': '/'
    }
    

    # function to be tested
    def dict_swap(self, d1):
    # Given an input dictionary, return a dictionary with the keys and values swapped.
        d2 = {}
        for key in d1.keys():
            d2[d1[key]] = key
        return d2

    def decodeMorseMessage(self, secret_message):
        morse_code_letters = secret_message.split()
        decoded_message = ""
        morse_code_to_letter_map = self.dict_swap(self.letter_to_morse_code_map)
        for morse_code_letter in morse_code_letters:
            if morse_code_letter in morse_code_to_letter_map.keys():
                decoded_message += morse_code_to_letter_map.get(morse_code_letter)
        
        return decoded_message


def main():
    secret_message = "-. . - .- .--. .--. / ---... / - .... . / -.. .- - .- / .- ..- - .... --- .-. .. - -.-- / " + \
                 "..-. --- .-. / - .... . / .... -.-- -... .-. .. -.. / -.-. .-.. --- ..- -.."
    
    decoder = morseCodeDecoder()
    decoded_message = decoder.decodeMorseMessage(secret_message)
    print(decoded_message)

if __name__ == "__main__":
    main()


