# *args - словарь,*kwargs - список

def min(*args, **kwargs):
    key = kwargs.get("key", None)

    print(args)
    return None


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    
    maximum = args[0]
    for i in range(len(args)):
        if(args[i]>maximum):
           maximum = args[i]



    return maximum


print(max("hello"))

# assert max(3, 2) == 3, "Simple case max"
# assert min(3, 2) == 2, "Simple case min"
# assert max([1, 2, 0, 3, 4]) == 4, "From a list"
# assert min("hello") == "e", "From string"
# assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
# assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
