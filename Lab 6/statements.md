# Lab 6

1. Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of alpha-numeric characters.
2. Write a function that receives as a parameter a regex string, a text string and a whole number x, and returns those long-length x substrings that match the regular expression.
3. Write a function that receives as a parameter a string of text characters and a list of regular expressions and returns a list of strings that match on at least one regular expression given as a parameter.
4. Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns those elements that have as attributes all the keys in the dictionary and values the corresponding values. For example, the elements that have the attributes: class = "url" and name = "url", "name": "url-form", " "url-form" and date-id = "item".
5. Write another variant of the function from the previous exercise that returns those elements that have at least one attribute that corresponds to a key-value pair in the dictionary.
6. Write a function that, for a text given as a parameter, censures words that begin and end with voices. Censorship means replacing characters from odd positions with *.
7. Verify using a regular expression whether a string is a valid CNP.  
Write a function that recursively scrolls a directory and displays those files whose name matches a regular expression given as a parameter or contains a string that matches the same expression. Files that satisfy both conditions will be prefixed with ">>"