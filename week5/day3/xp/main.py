# 1
def result():
    '''
    function takes a user input, and because data from input is recieved as string the int() function casts it into an integer, finally the abs() function returns the absolute value of the negative int
    '''
    user_num = int(input('enter negtive number: '))
    print(f'Absolute value of  {user_num}  is: {abs(user_num)}')

result()
print(result.__doc__)

# 2

class Currency:
    def __init__(self, coin, value):
        self.coin = coin
        self.value = value

    def __str__(self):
        return f'{self.value} {self.coin}s'

    def __int__(self):
        return self.value

    def __repr__(self):
        return f'{self.value} {self.coin}s'

    def __my__(self):
        return self.coin
    
    def __add__(self, other_num):
        if isinstance(other_num, Currency):
            if self.coin == other_num.coin:
                 return self.value + int(other_num)
            else:
                raise TypeError('Cannot add between Currency type shekel and dollar')
        else:
            return self.value + int(other_num)


    def __iadd__(self, other):
        self.value += int(other)
        return self
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
print(c1 + c3)


