#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Jan. 28, 2022
# This program gives the user for option
# of playing three different games:
# Palindrome Detector, Intgers and Multipliers,
# and Index Size. Lists are used to
# complete tasks.


# determines the index size of each element in list
def index_size(index):
    # declaring empty list
    size = []

    for counter in range(len(index)):
        size.append(len(index[counter]))
    return size


# determines result of a list of integers multipled by x
def int_mult(integer, multiplier):
    # declaring empty list
    new_list = []

    # finding product of each integer element in list
    # and multiplier
    for element in integer:
        result = element * multiplier
        new_list.append(result)
        # copies list back to main
    return new_list


# determines if a string is a palindrome or not
def find_palindrome(string):
    for counter in range(0, int(len(string)/2)):
        if string[counter] != string[len(string)-counter-1]:
            return False
    return True


# collects user input, checks for invalid input,
# and displays results
def main():
    # initializing the counter
    counter = 0

    # empty list for int & multiplier
    int_mult_list = []
    # empty list for index size
    index_size_list = []

    # display opening message to the user
    print("Today you will choose a game to play!")
    print("1: Palindrome Detector")
    print("2: Integers and Multipliers")
    print("3: Index Size")
    print("")

    while True:
        # gets input from the user
        choice = input("Choose which game you would "
                       "like to play (1, 2, or 3): ")

        # block of code for game 1
        if choice == "1":
            # gets input from user
            print("")
            string_user = input("Enter string: ")

            # assigns variable to function call
            palindrome_answer = find_palindrome(string_user)

            # displays results to user
            print("")
            if palindrome_answer:
                print("{} IS a palindrome." .format(string_user))
            else:
                print("{} is NOT a palindrome." .format(string_user))
            break

        # block of code for game 2
        elif choice == "2":
            while True:
                print("")
                # gets input from the user
                user_nums = input("Enter a list of "
                                  "integers (ex. 1, 2, 3, 4): ")
                # process for parsing strings
                list_string_nums = []
                list_string_nums = user_nums.split(",")
                # initializing counter
                counter = 0

                while counter < len(list_string_nums):
                    try:
                        # converts string to int
                        user_nums_int = int(list_string_nums[counter])
                        # adds ints to end of list
                        int_mult_list.append(user_nums_int)
                        # increments counter
                        counter += 1

                    except Exception:
                        print("Only integers are valid!")
                        print("")
                        # gets input from the user
                        user_nums = input("Enter a list "
                                          "of integers (ex. 1, 2, 3, 4): ")
                        list_string_nums = user_nums.split(",")
                        counter = 0

                # checks condition to see if list is full and
                # breaks out of loop
                if counter >= len(list_string_nums):
                    break

            while True:
                # gets input from user
                user_multiplier = input("Enter a multiplier: ")
                try:
                    # converts string to float
                    multiplier_float = float(user_multiplier)

                    # assigns variable to function call
                    result_user = int_mult(int_mult_list, multiplier_float)
                    print("")
                    print("The product of each element with a multiplier is:")
                    print("{}" .format(result_user))

                    break
                except Exception:
                    print("Invalid data!")
                    print("")
            break

        # block of code for game 3
        elif choice == "3":
            print("")
            # parsing strings
            user_string_list = input("Enter a list of "
                                     "strings (ex. hello, "
                                     "123, happy, 34890): ")
            list_string_user = []
            list_string_user = user_string_list.split(", ")

            # adding each string to end of list
            for a_string in list_string_user:
                index_size_list.append(a_string)

            # assigns variable to function call
            index_size_user = index_size(index_size_list)

            # displays results to user
            print("")
            print("The length of each string is: {}" .format(index_size_user))
            break

        # when invalid input is entered
        else:
            print("Invalid selection!")
            print("")


if __name__ == "__main__":
    main()
