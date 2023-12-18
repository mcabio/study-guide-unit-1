"""List Practice
Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.
    
    For example::
    
        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """
    for item in items: #for loop iterates over the list and then prints them individually
        print(item)

    # print("the wrong thing")


def long_words(words):
    """Return words in input list that longer than 4 characters.
    
    For example::
    
        >>> long_words(["hello", "a", "b", "hi", "muffin", "muffin"])
        ['hello', 'muffin', 'muffin']
    
    (If there are duplicates, show both --- notice "muffin" appears
    twice in output)
    
    If no words are longer than 4 characters, return an empty list::
    
        >>> long_words(["all", "are", "tiny"])
        []
    """
    # This uses list comprehension. Basic syntax is: [expression for item in iterable if condition]
    return [word for word in words if len(word) > 4]


def n_long_words(words, n):
    """Return words in list longer than `n` characters.
    
    For example::
    
        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "muffin", "muffin"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'muffin', 'muffin']
        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """

    return [word for word in words if len(word) > n]


def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.
    **DO NOT USE** the built-in function `min()`!
    
    For example::
    
        >>> smallest_int([-5, 2, -5, 7])
        -5
        >>> smallest_int([3, 7, 2, 8, 4])
        2
    
    If the input list is empty, return `None`::
    
        >>> smallest_int([]) is None
        True
    """
    if not numbers: # This applies to the condition that if the input list is empty, it should return None
        return None
    
    smallest = numbers[0] # This turns the 0 index as the smallest number in the list.

    for num in numbers: # This for loop iterates over the list, looking over the rest of the numbers (num)
        if num < smallest: # This if statement says, if the loop comes across a number smaller than the 0 index,
                           # replace the smallest number as that number. This continues until the end of the list.
            smallest = num

    return smallest 


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.
    **DO NOT USE** the built-in function `max()`!
    
    For example::
    
        >>> largest_int([-5, 2, -5, 7])
        7
        >>> largest_int([3, 7, 2, 8, 4])
        8
    
    If the input list is empty, return None::
    
        >>> largest_int([]) is None
        True
    """

    if not numbers:
        return None
    
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.
    
    For example::
    
        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]
   
    If any of the numbers are odd, make sure you don't round off
    the half::
   
        >>> halvesies([1, 5])
        [0.5, 2.5]
    """
    divided_by_two = [] # This list was created for the function to put the output into

    for num in numbers: # This for loop iterates over the numbers
        divided = num / 2 # This creates a variable that represents each number being divided by 2
        divided_by_two.append(divided) # This appends the divided variable into the empty list called 
                                       # divided_by_two
    
    return divided_by_two # The return statement is outside of the for loop because when it is inside, it 
                          # exits the loop within the first iteration.



def word_lengths(words):
    """Return the length of words in the input list.
    
    For example::
    
    >>> word_lengths(["hello", "hey", "hello", "spam"])
    [5, 3, 5, 4]"""

    length_of_words = []

    for word in words:
        length = len(word)
        length_of_words.append(length)

    return length_of_words # I had the brackets surrounding length_of_words but it gave an error because
                           # the brackets created a list within a list.


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.
    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.
    
    For example::
    
        >>> sum_numbers([1, 2, 3, 10])
        16
    
    Any empty list should return the sum of zero::
    
        >>> sum_numbers([])
        0
    """
    add_all = 0
    
    for num in numbers:
        add_all += num # This for loop says that every number that the loop iterates over will be added
                       # to the add_all variable.
    
    return add_all


def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.
    
    For example::
    
        >>> mult_numbers([1, 2, 3])
        6
    
    Obviously, if there is a zero in input, the product is zero::
    
        >>> mult_numbers([10, 20, 0, 50])
        0
    
    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::
    
        >>> mult_numbers([])
        1
    """

    multiply_all = 1 # If the list is empty, the output should always be 1.

    for num in numbers:
        multiply_all *= num

    return multiply_all


def join_strings(words):
    """Return a string of all input strings joined together.
    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.
    
    For example::
    
        >>> join_strings(["spam", "spam", "muffin", "balloonicorn"])
        'spamspammuffinballoonicorn'
    
    For an empty list, you should return an empty string::
    
        >>> join_strings([])
        ''
    """

    joint_words = "" # This creates a variable that represents the string output taken from the input list

    for word in words:
        joint_words += word # This for loop iterates through all the string in the input list and adds each
                            # string to the joint_words variable.
    
    return joint_words
    


def average(numbers):
    """Return the average (mean) of the list of numbers given.
    
    For example::
    
        >>> average([2, 4])
        3.0
    
    This should handle cases where the result isn't an integer::
    
        >>> average([2, 12, 3])
        5.666666666666667
    
    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.
    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """

    if not numbers: # This if statement returns None if there are no numbers in the list
        return None
    
    total_sum = 0 # This creates a variable that the for loop will dump total sum of numbers in.

    for num in numbers: # This for loop says that each number that it iterates over will be
                        # added to the total_sum and continues to add to it 
                        # until for loop reaches end of the list
        total_sum += num

    mean = total_sum / len(numbers) # This creates a variable 'mean' that says the total_sum is then 
                                    # divided by the length of numbers 

    return mean


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".
    
    For example::
     
        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'
    
    If there's only one thing in the list, it should return just that
    thing, of course::
   
        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """

    # joint_words = " "
    # for word in words:
    #     joint_words += " " + word

    # return joint_words

    return ', '.join(words)


def reverse_list(items):
    """Return the input list, reversed.
    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.
    
    For example::
    
        >>> reverse_list([1, 2, 3])
        [3, 2, 1]
        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']
    
    You should do this without changing the original list::
    
        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """
    # reversed_items = [] # Creates a variable that will add the reversed words that the for loop iterates over

    # for i in range(len(items) - 1, -1, -1): #  This is a for loop that iterates 
    #                                         # over the indices generated by the range object. This 
    #                                         # creates a range object that starts from 
    #                                         # len(items) - 1 (the last index of the list) 
    #                                         # and goes down to -1 (exclusive) with a step of -1.
    #                                         # This effectively generates indices in reverse order.
    #     reversed_items.append(items[i]) # For each index i in reverse order, it appends 
    #                                     # the corresponding element from the original items 
    #                                     # list to the reversed_items list.

    # return reversed_items

    return items[::-1]


def reverse_list_in_place(items):
    """Reverse the input list `in place`.
    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.
    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.
    
    For example::
    
        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]
        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """
    

# This calculates the length of the input list and assigns it to the variable length.
    length = len(items)

    # This loop iterates over the first half of the list. 
    for i in range(length // 2): # The range(length // 2) generates indices from 0 to the length of the list 
                                 # divided by 2. It gives the result of the division 
                                 # rounded down to the nearest integer. For example, 
                                 # if length of the list is 11, then length // 2 is 5 (since we don't want a decimal 
                                 # number as an answer). This will output items from indices 0 to 4 (since that is
                                 # length of 5 items).
        
        # Inside the loop, this line swaps elements between the beginning and end of the list. It uses tuple 
        # unpacking to perform the swap without needing a temporary variable. The result is that the list is 
        # reversed in place, and no additional list is created. This is achieved by swapping elements 
        # symmetrically around the midpoint of the list.
        items[i], items[length - 1 - i] = items[length - 1 - i], items[i] 



def duplicates(items):
    """Return list of words from input list which were duplicates.
    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.
   
    For example::
   
        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']
        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]
   
    You should do this without changing the original list::
   
        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']
        >>> orig
        ['apple', 'apple', 'berry']
    """
        # The commented code did not work because it still kept providing duplicates if there are more than 2 of the
    # same item.
    # encountered_items = set()
    # duplicated_items = []

    # for item in items:
    #     if item in encountered_items: 
    #         duplicated_items.append(item)
    #     encountered_items.add(item)

    # return sorted(duplicated_items)

    dupes = [] # This initializes an empty list called dupes that will store the duplicate items.

    items = sorted(items) # This line sorts the input list items in ascending order. 
                          # Sorting the list simplifies the process of finding duplicates 
                          # because identical items will be adjacent to each other.

    # This loop iterates over the sorted list, starting from index 1 (the second element) and going up to 
    # the length of the list. It uses i to represent the current index.
    for i in range(1, len(items)): # The loop starts at index 1 because the loop compares each element (items[i]) 
                                   # with its preceding element (items[i - 1]). By starting at index 1, 
                                   # it ensures that the first element (at index 0) is not compared with 
                                   # any preceding element. If the loop started at index 0, the comparison 
                                   # would be between the first and second elements, and there would 
                                   # be no preceding element for the first element. By starting the 
                                   # loop at index 1, the code ensures that each element is compared 
                                   # with the one immediately before it, and it avoids potential issues related to negative indices. 
        if items[i] == items[i - 1]: # This if statement says, if current item is the same as the item before it, 
            if items[i] not in dupes: # And if current item is not in the dupes list, 
                dupes.append(items[i]) # Add it to the dupes list.

    return dupes

# items = ["This", "This", "is", "is", "a", "a", "list", "list", "with", "with", "no", "no", "duplicates", "duplicates"]
# result = duplicates(items)
# print(result)

def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.
    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.
    **DO NOT** use the `list.index()` method.
    
    For example::
    
        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]
    
    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")
    
    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::
    
        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]
    
    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """

    indices = [] # This initializes an empty list that will store the index number of the letter stated in 
                 # the second parameter, letter.

    # Outer Loop (for word in words:): Iterates over each word in the list of words.
    # found_at = None: Initializes a variable to store the index of the first 
    # occurrence of the letter in the current word. It starts as None to indicate 
    # that the letter has not been found yet. 
    for word in words: 
        found_at = None # This will also be what is returned if the string does not contain the letter

        # Inner Loop (for i in range(len(word)):): Iterates over each character in the current word.
        for i in range(len(word)):
            # Checks if the current character (word[i]) is equal to the target letter. 
            if word[i] == letter:
                # If true, it updates found_at with the current index i 
                # and breaks out of the inner loop.
                found_at = i
                break
        # Appends the result (either the index or None if the letter was not found) to the list of indices.             
        indices.append(found_at)

    return indices


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")