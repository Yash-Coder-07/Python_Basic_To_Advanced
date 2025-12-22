""" 
Map takes 2 arguments map(function/lambda function,iterable)
it use to apply function on each item of iterables
no need of lambda always we can pass normal def function
"""
# a=[1,2,3,4,5]
# doubled = map(lambda x: x**2,a)
# print(doubled)  # It gives you the location of object doubled
# print(list(doubled)) # need to convert object in list 



### Filter 
""" 
Filter takes 2 arguments filter(function/lambda function,iterable)
it use to apply function on each item of iterables to filter out
no need of lambda always we can pass normal def function
"""

def even(x):
    if x%2==0:
        return True
    else:
        return False
    
a=[1,2,3,4,5,6,7,8,9]
# result = filter(lambda x :True if x%2==0 else False, a)
result = filter(even,a)
print(list(result))