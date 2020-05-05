# This is program asks the user to enter a cutoff poiny, some values and then 
# arrange the numbers in two groups: numbers that are less than or equal to the 
# the cutoff point and numbers that are greater than the cutoff point.
#
# The progam will print out the number of items in each list as well as 
# the average of the values in the list.


def read_num(prompt):
    pass

# returns a boolean 
## Asks the user to enter a boolean value (yes/no).
    # @param prompt str the prompt to show the user
    # @return bool the value that user entered (True for yes, False for no)
    #
def read_boolean(prompt):
    while True:
        ans = input("{} ".format(prompt)).strip().lower()
        if ans in ('yes', 'y'):
            return True
        elif ans in ('no', 'n'):
            return False
        else:
            print("Sorry, I do not understand. Please answer 'yes' or 'no'")

if __name__ == '__main__':
    #TEMP: testing read_boolean function
    b = read_boolean("Are you sure?")
    print("Function returned: {}".format(b))
    # END TEMP

    # TODO: main program goes here
    pass



# arranges the list 

def arrange_nums(num):
    pass



if __name__ == '__main__':
    pass





