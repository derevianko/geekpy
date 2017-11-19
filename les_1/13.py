# 13. Write a script to get the maximum and minimum value in a dictionary.

x_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(x_dict.keys(), key=(lambda k: x_dict[k]))
key_min = min(x_dict.keys(), key=(lambda k: x_dict[k]))

print('Max: ',x_dict[key_max])
print('Min: ',x_dict[key_min])

# !!!
