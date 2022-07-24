import string
shift = input('Please enter a shift number:')
shift_num = int(shift)
new_word =''
word= input('Please enter a word:')
for i in word:
    if i in string.ascii_lowercase:
        length_shift = ord(i)+shift_num
        if length_shift > 122:
            length_shift -= len(string.ascii_lowercase)
            new_word += chr(length_shift)
        else:
            x = chr(ord(i)+shift_num)
            new_word +=x
    elif i in string.ascii_uppercase:
        length_shift = ord(i)+shift_num
        if length_shift > 90:
            length_shift -= len(string.ascii_lowercase)
            new_word += chr(length_shift)
        else:
            x = chr(ord(i)+shift_num)
            new_word +=x
    if i in string.punctuation or i == ' ' or i in string.digits:
        x= i;
        new_word +=x
print(new_word)
