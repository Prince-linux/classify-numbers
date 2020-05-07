# This program asks the user to enter a cutoff point, numbers and then 
# arrange the numbers in two groups: numbers that are lesser than or equal to the 
# the cutoff point and numbers that are greater than the cutoff point.
#
# The progam prints out the number of items in each list as well as 
# the average of the values in each list.


# returns an int or float type.

def read_nums(prompt):
    """
     Asks the user to enter a number
     @param prompt str the prompt to show the user    
     @return type value that user entered (int, float)
    
    """
    while True:
        nums = input("{}".format(prompt))
        try:
            number = int(nums)
            return type(number)
        except ValueError:
            try:
                number = float(nums)
                return type(number)
            except ValueError:
                print("Please enter a valid number(integer or a decimal number)")

# returns a boolean 
def read_boolean(prompt):

    """
    Asks the user to enter a boolean value (yes/no).
    @param prompt str the prompt to show the user
    @return bool the value that user entered (True for yes, False for no)
    
    """

    while True:
        ans = input("{} ".format(prompt)).strip().lower()
        if ans in ('yes', 'y'):
            return True
        elif ans in ('no', 'n'):
            return False
        else:
            print("Sorry, I do not understand. Please answer 'yes' or 'no'")



# returns two different lists(higher_numbers, lower_numbers)

def arrange_nums(nums, cutoff):
    """
    Arranges numbers into two different list comparing them to the cutoff number
    @param nums the list of number
    @param cutoff the cutoff number
    @return list greater than cutoff and list smaller than cutoff
    """
    big_nums = []
    small_nums = []
    for i in nums:
        if i > cutoff:
            i = big_nums.append(i)
        else:
            i = small_nums.append(i)
    return (big_nums, small_nums)

    
    
        
    


# unit testing
if __name__ == '__main__':
    #TEMP: testing arrange_nums fucntion
    c = arrange_nums([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
    print("Function returned: {}".format(c))
    # END TEMP

    #TEMP: testing read_nums function
    #a = read_num("Please enter a number: ")
    #print("Function returned: {}".format(a))
    # END TEMP

    #TEMP: testing read_boolean function
    #b = read_boolean("Are you sure?")
    #print("Function returned: {}".format(b))
    # END TEMP

    # TODO: main program goes here
    pass





