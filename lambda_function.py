"""
    Lambda functions can seem a bizarre or too-abstract concept. It is related to both "first-class functions" and
    "anonymous functions", which are capabilities of many languages including Python.

"""

## Create a list of tuples and sort it using the index
list_of_tuples = [(1, 'Joe'),
                  (2, 'James'),
                  (5, 'Smith'),
                  (3, 'Alberta'),
                  (4, 'Francine'),
                  (7, 'Charles')]

print (sorted (list_of_tuples))  # this produces the standard sort order


## Create a function to get the names from the tuple using the index.
def get_name_from_tuple(t: tuple) -> str:
    return t[1]


## now use the key argument for sorting the tuples.

print (sorted (list_of_tuples, key=get_name_from_tuple))

## Using lambda function instead of the regular one.

number_names = [[1, 'one', 'eins', 'uno'],
                [2, 'two', 'zwei', 'dos'],
                [3, 'three', 'drei', 'tres'],
                [4, 'four', 'vier', 'quatro'],
                [5, 'five', 'fünf', 'cinco'],
                [6, 'six', 'sechs', 'seis'],
                [7, 'seven', 'sieben', 'siete'],
                [8, 'eight', 'acht', 'ocho'],
                [9, 'nine', 'neun', 'nueve'],
                [10, 'ten', 'zehn', 'diez']]

print (sorted (number_names, key=lambda t: t[1]))

## If we want to sort it using the other columns use a different index.

print (sorted (number_names, key=lambda t: t[3]))
