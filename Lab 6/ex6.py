# Write a function that, for a text given as a parameter, censures words that
# begin and end with vowels. Censorship means replacing characters from odd
# positions with *.

import re


def censor(text):
    words = re.findall(r"\w+", text)
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    for a in range(0, len(words)):
        if words[a][0] in vowels:
            words[a] = "*" + words[a][1:len(words[a])]

        if words[a][len(words[a]) - 1] in vowels:
            words[a] = words[a][0:len(words[a]) - 1] + '*'

    return words


print(censor("Write a function that, for a text given as a parameter, censures words that begin and end with vowels." +
             "Censorship means replacing characters from odd positions with *."))
