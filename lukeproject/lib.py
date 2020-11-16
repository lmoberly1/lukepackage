# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for lukeproject Project
"""

from os.path import split
import pandas as pd
import datetime
import random

pd.set_option('display.width', 200)


def clean_data(data):
    """ clean data
    """
    # Remove columns starts with vote
    cols = [x for x in data.columns if x.find('vote') >= 0]
    data.drop(cols, axis=1, inplace=True)
    # Remove special characteres from columns
    data.loc[:, 'civility'] = data['civility'].replace('\\.', '', regex=True)
    # Calculate Age from day of birth
    actual_year = datetime.datetime.now().year
    data.loc[:, 'Year_Month'] = pd.to_datetime(data.birthdate)
    data.loc[:, 'Age'] = actual_year - data['Year_Month'].dt.year
    # Uppercase variable to avoid duplicates
    data.loc[:, 'city'] = data['city'].str.upper()
    # Take 2 first digits, 2700 -> 02700 so first two are region
    data.loc[:, 'postal_code'] = data.postal_code.str.zfill(5).str[0:2]
    # Remove columns with more than 50% of nans
    cnans = data.shape[0] / 2
    data = data.dropna(thresh=cnans, axis=1)
    # Remove rows with more than 50% of nans
    rnans = data.shape[1] / 2
    data = data.dropna(thresh=rnans, axis=0)
    # Discretize based on quantiles
    data.loc[:, 'duration'] = pd.qcut(data['surveyduration'], 10)
    # Discretize based on values
    data.loc[:, 'Age'] = pd.cut(data['Age'], 10)
    # Rename columns
    data.rename(columns={'q1': 'Frequency'}, inplace=True)
    # Transform type of columns
    data.loc[:, 'Frequency'] = data['Frequency'].astype(int)
    # Rename values in rows
    drows = {1: 'Manytimes', 2: 'Onetimebyday', 3: '5/6timesforweek',
             4: '4timesforweek', 5: '1/3timesforweek', 6: '1timeformonth',
             7: '1/trimestre', 8: 'Less', 9: 'Never'}
    data.loc[:, 'Frequency'] = data['Frequency'].map(drows)
    return data

def try_me():
    # import random module

    # Print multiline instruction
    # performstring concatenation of string
    print("Winning Rules of the Rock paper scissor game as follows: \n"
                                    +"Rock vs paper->paper wins \n"
                                    + "Rock vs scissor->Rock wins \n"
                                    +"paper vs scissor->scissor wins \n")

    while True:
        print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")

        # take the input from user
        choice = int(input("User turn: "))

        # OR is the short-circuit operator
        # if any one of the condition is true
        # then it return True value

        # looping until user enter invalid input
        while choice > 3 or choice < 1:
            choice = int(input("enter valid input: "))


        # initialize value of choice_name variable
        # corresponding to the choice value
        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'paper'
        else:
            choice_name = 'scissor'

        # print user choice
        print("user choice is: " + choice_name)
        print("\nNow its computer turn.......")

        # Computer chooses randomly any number
        # among 1 , 2 and 3. Using randint method
        # of random module
        comp_choice = random.randint(1, 3)

        # looping until comp_choice value
        # is equal to the choice value
        while comp_choice == choice:
            comp_choice = random.randint(1, 3)

        # initialize value of comp_choice_name
        # variable corresponding to the choice value
        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'paper'
        else:
            comp_choice_name = 'scissor'

        print("Computer choice is: " + comp_choice_name)

        print(choice_name + " V/s " + comp_choice_name)

        # condition for winning
        if((choice == 1 and comp_choice == 2) or
          (choice == 2 and comp_choice ==1 )):
            print("paper wins => ", end = "")
            result = "paper"

        elif((choice == 1 and comp_choice == 3) or
            (choice == 3 and comp_choice == 1)):
            print("Rock wins =>", end = "")
            result = "Rock"
        else:
            print("scissor wins =>", end = "")
            result = "scissor"

        # Printing either user or computer wins
        if result == choice_name:
            print("<== User wins ==>")
        else:
            print("<== Computer wins ==>")

        print("Do you want to play again? (Y/N)")
        ans = input()


        # if user input n or N then condition is True
        if ans == 'n' or ans == 'N':
            break

    # after coming out of the while loop
    # we print thanks for playing
    print("\nThanks for playing")


if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    import lukeproject
    folder_source, _ = split(lukeproject.__file__)
    df = pd.read_csv('{}/data/data.csv.gz'.format(folder_source))
    clean_data = clean_data(df)
    print(' dataframe cleaned')
