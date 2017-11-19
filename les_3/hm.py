import random
import timeit

# вывод int random
def int_random():
    int_list = list()
    for x in range(0,100000):
        x = random.randint(0,100)
        int_list.append(int(x))
    # print (int_list)
    int_list.sort()
    print (int_list)
    # print (len(int_list))
int_random()



# вывод float random
def float_random():
    float_list = list()
    for x in range(0,100000):
        x = random.uniform(0,100)
        float_list.append(x)
    # print (float_list)
    float_list.sort()
    print (float_list)
    # print (len(float_list))
float_random()
