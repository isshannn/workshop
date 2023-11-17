def bubble_sort(argument):
    """This program performs a bubble sort on the provided list of integers
    """
    print(argument)
    minimum = argument[0]
    for x in range(len(argument)-1):
       if(minimum >= argument[x]):
            minimum = argument[x]
            if(minimum > argument[x+1]):
                swap = swap_variables(argument[x],argument[x+1])
                argument[x] = swap[0]
                argument[x+1] = swap[1]
                print(argument)
    print(minimum)
    return None

def swap_variables(var1,var2):
   swapped = [var2,var1]
   return swapped