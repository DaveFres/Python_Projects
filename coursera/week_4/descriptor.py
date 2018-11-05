class Value:

    def __init__(self, amount=None):

        self.amount = amount

    def __get__(self, obj, obj_type):

        self.amount = self.amount - obj.commission * self.amount

        return self.amount

    def __set__(self, obj, value):

        self.amount = value


"""
Testing

class Account:

    amount = Value()

    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.5)
new_account.amount = 100

print(new_account.amount) # 50.0
new_account.amount = 50
print(new_account.amount) # 25.0
new_account.amount = 0
print(new_account.amount) # 0.0
"""
