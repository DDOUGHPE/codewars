
sentence = 'we fly'
vowel = ['a','e','i','o','u']
vow_count = 0
for letter in vowel:
    if letter in sentence:
        vow_count += 1
   
print(str(vow_count))

