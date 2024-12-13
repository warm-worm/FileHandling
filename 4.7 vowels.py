##
# Write a program that calculates the number of vowels in the text entered from the 
# keyboard. Use regular expressions.
##
import re

def count_vowels(text):
    all_vowels = r'[aieouAIEOU]'
    vowels = re.findall(all_vowels, text)
    return len(vowels)

text = input('Enter text: ')

vowel_count = count_vowels(text)

print(f'The number of vowels in the text is {vowel_count}.')
