# Lab 3
1. Write a function that receives as parameters two lists a and b and returns a set of sets containing: (a intersected with b, a reunited with b, a - b, b - a)

2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters in the character string and the values are the number of occurrences of that character in the given text.  
Example: For string "Ana has apples." given as a parameter the function will return the dictionary: {'A': 1, '': 2, 'n': 1, 'a': 2, 'r': 2, '.': 1}.

3. Compare two dictionaries without using the operator "==" and return a list of differences as follows: (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)

4. The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters. Build and return a string that represents the corresponding XML element. Example: build_xml_element ("a", "Hello there", "href =" http://python.org ", _class =" my-link " //python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

5. The validate_dict function that receives as a parameter a set of tuples that represent validation rules for a dictionary with string keys and values of the string type and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix"). A value is considered valid if it starts with "prefix" "middle" is inside the value (not at the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches all the rules, False otherwise.  
Example: the rules [("key1", "", "inside", ""), "key2", "start", "middle", "winter" "key1": "come inside, it's too cold out", "key3": "this is not valid"} => False because although the rules are respected for "key1" and "key2" "key3" that does not appear in the rules.

6. With the global dictionary:  
{  
	"+": lambda a, b: a + b,  
	"*": lambda a, b: a * b,  
	"/": lambda a, b: a / b,  
	"%": lambda a, b: a % b  
}  
Build a apply_operator function (operator, a, b) that will apply over a and b the rule specified by the global dictionary. Implement it so that if a new operator is added, it is not necessary to change the function.

7. Consider a globally defined dictionary similar to the one above, with the difference that the functions given as values of the dictionary can receive any combination of parameters. Write a function apply_function that receives as a parameter the name of an operation and applies the corresponding function over the arguments received. Implement it so that if a new function is added, it is not necessary to change the function apply_function.  
An example of a global dictionary might be the following:  
{  
    "print_all": lambda *a, **k: print(a, k),  
    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),  
    "print_only_args": lambda *a, **k: print(a),  
    "print_only_kwargs": lambda *a, **k: print(k)  
}  

8. Write a function that receives as a parameter a set and returns a tuple (a, b), representing the number of unique elements in the set, and b representing the number of duplicate elements in the set.

9. Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -.   
Ex: {1,2}, {2, 3} =>
{
	"{1, 2} | {2, 3}": 3,  
	"{1, 2} & {2, 3}": 1,  
	"{1, 2} - {2, 3}": 1,  
	...  
}  


OBS:  
*args and **kwargs allow you to pass a variable number of arguments to a function  
If used without *s you will be working with a list for args and a dict for kwargs.  

The naming is not strict - the * and ** are imperative. For instance we could have used *ar and **kw.  
See the following example:

```Python
def my_function(*args,**kwargs):
    f= lambda *a, **k: print(a, k)
    f(args,kwargs)
    f(*args,**kwargs)
```
    
    

