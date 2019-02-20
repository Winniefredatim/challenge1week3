def list_sort(numbers):
#form a function that holds a list yet to be sorted.
    even = []
    odd = []
    characters = []
    mydict = dict()
    #I used the inbuilt function isinstance to check if numbers is a subclass of list.
    if not isinstance(numbers, list):
        return 'Invalid Input'

    if not numbers:
        mydict['evens'] = even
        mydict['odds'] = odd
        mydict['chars'] = characters
        return mydict

    for i in numbers:

        if isinstance(i, int):
            #separete the even from odd numbers and characters.
            if i % 2 == 0:
                even.append(i)

            else:
                odd.append(i)

        elif isinstance(i, str):
            characters.append(i)

    mydict['evens'] = sorted(even)
    mydict['odds'] = sorted(odd)
    mydict['chars'] = sorted(characters)
    return mydict


print(list_sort([2, 0, 6, 5, 1, 7, 'z', 'a']))
