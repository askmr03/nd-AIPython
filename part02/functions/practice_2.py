numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(lambda num_list: sum(num_list) / len(num_list), numbers))
print(averages)

'''
[57.0, 58.2, 50.6, 27.2]
'''