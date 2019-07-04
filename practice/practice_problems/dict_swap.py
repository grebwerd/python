# function to be tested
def dict_swap(d1):
    # Given an input dictionary, return a dictionary with the keys and values swapped.
    d2 = {}
    for key in d1.keys():
        d2[d1[key]] = key
    return d2


# Test data and expected responses
# TODO: Add more test data elements

#Drew Goldberg: Add unhashable types as values which should break the dict_swap function 
test_data = [
    {'a': 1, 'b': 2, 'c': 3}, 
    {'',''}, 
    {'emptyListKey', []},
    {'listKey', [1,2,3]}, 
    {'emptySetKey', set()},
    {'setKey', set(1)},
    {"emptyDictKey", dict()},
    {"dictKey", dict({"a":1})},
    {None, None},
    {}
]

response = [
    {1: 'a', 2: 'b', 3: 'c'},
    {'',''},
    TypeError,
    TypeError,
    TypeError,
    TypeError,
    TypeError,
    TypeError,
    {None, None},
    {},
]


def main():
    # Call the dict_swap function with each of the test data elements and check the response
    print("test")
    for i, test_dict in enumerate(test_data):
        print('running test', i)
        new_dict = dict_swap(test_dict)
        assert response[i] == new_dict
        print('passed test', i)


if __name__ == '__main__':
    main()