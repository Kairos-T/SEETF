def zero_width_to_binary(text):
    binary_text = ""
    for char in text:
        if char == '\u200b':
            binary_text += '1'
        elif char == '\u200c':
            binary_text += '0'
    return binary_text

def binary_to_ascii(binary_text):
    ascii_text = ""
    for i in range(0, len(binary_text), 8):
        chunk = binary_text[i:i+8]
        decimal_value = int(chunk, 2)
        ascii_character = chr(decimal_value)
        ascii_text += ascii_character
    return ascii_text

zero_width_text = "​ ​ ​​  ​ ​​​ ​ ​ ​​​ ​ ​    ​  ​   ​  ​​  ​​​​ ​  ​   ​​  ​ ​​ ​  ​  ​​​  ​  ​​​  ​​​​ ​​ ​   ​​  ​ ​ ​​   ​​  ​​ ​   ​​  ​    ​   ​​ ​​  ​​   ​ ​     ​  ​​ ​​​  ​​  ​​  ​​ ​ ​​  ​  ​​  ​​​​ ​​  ​​​​​​  ​ ​ ​  ​​​  ​  ​​​  ​  ​​​ ​​  ​​ ​ ​  ​​​  ​​   ​​ ​  ​​​ ​​  ​​ ​​​  ​​​​ ​​  ​ ​​​​   ​​ ​  ​​​  ​  ​​ ​​​​  ​​​ ​  ​​​ ​​​  ​   ​​  ​​​​​  ​​​ ​​​  ​​ ​​​  ​  ​​​   ​​ ​​  ​​ ​​  ​​​ ​​​  ​ ​​​​  ​ ​ ​     ​ "
binary_text = zero_width_to_binary(zero_width_text)
decoded_text = binary_to_ascii(binary_text)
print(decoded_text)
