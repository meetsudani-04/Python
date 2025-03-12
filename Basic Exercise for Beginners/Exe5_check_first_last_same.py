# Exercise 5: Check if the first and last numbers of a list are the same
x = [10, 20, 30, 40, 10]
def same(x):
    first_index = x[0]
    last_index = x[-1]

    if first_index == last_index :
        return True
    else:
        return False 
    
x = [10, 20, 30, 40, 40]
print(same(x))