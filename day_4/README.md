"""
    Day 4 of 100DaysOfCode with @yu_angela (twitter)
    Today's lectures are mostly about random modules, lists and practical solutions
    You can find this course in
        - https://www.udemy.com/course/100-days-of-code/

    import random 
        - in order to use random module of python one should import random module 
        - list indexing start from zero 
        - list can be accesed using negative indecies
        - using indexing of lists it is easy to alter the lists
        - list.append() function is used to add one more item into list
        - list.exted([ther is added anther list]) and that will be added to the last of 
        like shown above and from there one should use predefined functions inside 
        imported module like random.randint(x, y)
        -> first practice is in random_practice.py file
    
    Tossing a coin
        - tossing a coin is the yet another fun way of using random module
        -> the example is given in toss.py file
    
    Lists
        - using coorelated data in a form that is easily accesible and stored in the form of sequence
        - the example was to have a list of names of states of USA and list of grociries that are mostly related
        -> the example is given in states.py file

    string.split() function 
        - using string.split() function one can create a list of items that is on the string. Basically split function cuts the string as soon as it sees the predefined character and appends to the temporary list and copys to variable that you have created.
        -> Example: list_of_items = "apple, peach, cherry".split(",") ==> list_of_items =["apple", "peach", "cherry"]
    
    Backer Roulette
        - this is the game of bankers. In pubs when someone need to pay the total everyone will put their bussiness cards and waiter is going to choose one business card and the owner of that card is going to pay the total bill.
        - this is yet another interesting challenge for random and string.split() and len() function
        -> the solution is given in banker.py file

        *** random.choice(list) is whole solution for this challenge
    
    nested list
        - lists inside list
        -> nested_list = [[some list here], [some another list here]]
    
    Treasure map coding challenge
        - in this project user must enter the number as coordiantes for putting the treasure
        -> the solution is given in treasure_map.py
    
    The Project of the day
        - Rock, Paper, Scissors game
        - I had 2 solutions in mind so I have programmed them both. first one is rps_long.py file second one is rps_real.py file
        -> the solution is in the rps_real.py file
"""