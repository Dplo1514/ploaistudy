word = 'zxcvbnm'
for letter in word:
    if letter == 'y':
        print("Eek! An 'x'!")
        break
    print(letter)
else:
    print("No 'y' in there.")