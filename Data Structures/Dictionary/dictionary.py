# Dictionary have same declaratiion types as set 
# but it different because it has key, values pair 
# for ach key there is value

""" Dictionaries are 
1. Mutable  : but  we cannot chnage key but can change value
              key are unique but values may be common

2. It follows insertion order

3. It is completely heterogenous key and values can be anything 
"""
# d={1:"Hello",2:84}
# print(type(d))
# print(d)

d={10:100,20:200,30:300,40:400}

#print(d[20]) # We can print/access using the key of value

# We can CRUD operation but not on keys

#d[10] = 1000 # Now its updates in dictionary
#print(d[10])  # It will give 1000 instead of 100

# Update is use to add new key-value
#d.update({50:500})
#print(d)

""" Alternate way"""

# d[50] = 500 # if not find any then create on its own

# for delete item 
# del d[40]
# d.__delitem__(30) 
# print(d)