letters = ['a','b','c']
nums = [1,2,3]

for letter,num in zip(letters,nums):
    print("{}: {}".format(letter,num))

'''
a: 1
b: 2
c: 3
'''

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters,nums = zip(*some_list)
print(letters)
print(nums)
