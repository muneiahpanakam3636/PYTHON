# find the even and odd numbers

numbers = [4,42,93,41,15,6,17,81,9,110]


even_numbers=0
odd_numbers =0

for number in numbers:
    if number %2 == 0:
        even_numbers= even_numbers+1
    else:
       odd_numbers = odd_numbers+1

print("No of even numbers:",even_numbers)
print("ODD:",odd_numbers)

