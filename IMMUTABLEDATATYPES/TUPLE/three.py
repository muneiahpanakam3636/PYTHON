#  sorting the tuple - using sorted inbuilt function

enames = ('rahul','sonia','muni','priya','raju','raani')
#  index    0       1       2       3       4      5

new_names = sorted(enames)
print(new_names)
print(type(new_names))
#converte to tuple

enames =tuple(new_names)
print(enames)
print(type(enames))


