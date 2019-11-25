def dict_example():
    my_dict = {'name': 'Jack', 'age': 26}
    # Output: 26, best use get
    print(my_dict.get('age1'))

    # Trying to access keys which doesn't exist throws error
    # my_dict.get('address')
    # my_dict['address']

    my_dict['age'] = 27
    my_dict['address'] = 'Downtown'
    print(my_dict)

    # create a dictionary
    squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    # remove a particular item
    # Output: 16
    print(squares.pop(4))
    # Output: {1: 1, 2: 4, 3: 9, 5: 25}
    print(squares)
    # remove an arbitrary item
    # Output: (1, 1)
    print(squares.popitem())
    # Output: {2: 4, 3: 9, 5: 25}
    print(squares)
    # delete a particular item
    # del squares[5]
    # Output: {2: 4, 3: 9}
    print(squares)
    # remove all items
    squares.clear()
    # Output: {}
    print(squares)
    # delete the dictionary itself
    del squares
    # Throws Error
    # print(squares)


def list_example():
    # my_list = ['p', 'r', 'o', 'b', 'e']
    # # Output: p
    # print(my_list[0])
    odd = [1, 3, 5]
    odd.append(7)
    # Output: [1, 3, 5, 7]
    print(odd)
    odd.extend([9, 11, 13])
    # Output: [1, 3, 5, 7, 9, 11, 13]
    print(odd)

    my_list = ['p','r','o','b','l','e','m']
    # delete one item
    del my_list[2]
    # Output: ['p', 'r', 'b', 'l', 'e', 'm']
    print(my_list)
    # delete multiple items
    del my_list[1:5]
    # Output: ['p', 'm']
    print(my_list)
    # delete entire list
    del my_list
    # Error: List not defined
    if my_list  is None:
        print(my_list)

if __name__ == '__main__':
    c = r"this\n and that"
    print(c)
    # dict_example()
    list_example()
