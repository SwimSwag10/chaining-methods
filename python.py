class User:
  def __init__(self, name, money):
      self.name = name
      self.money = money

  def make_withdraw(self, withdraw=0):
    self.money -= withdraw
    # instead of returning self.money we can just return self and it does the same thing.
    return self

  def make_deposit(self, amount=0):
    self.money += amount
    return self

  def display_user_balance(self):
    return self.make_deposit() + self.make_withdraw()
  
  def transfer_money(self, other_user, amount):
    self.money += amount
    other_user.money -= amount

guido = User("Guido van Rossum", 1000)
# this is what was changed in withdraw/deposit
guido.make_deposit(10).make_deposit(10).make_deposit(50).make_withdraw(100)
monty = User("Monty Python", 10000)
monty.make_withdraw(100)
adrien = User("Adrien", 100)
adrien.make_withdraw(800)
nibbles = User("Mr. Nibbles", 50)
nibbles.make_withdraw(1000)
print(f"User: {guido.name}, Balance: {guido.money}")
print(f"User: {monty.name}, Balance: {monty.money}")
print(f"User: {adrien.name}, Balance: {adrien.money}")
print(f"User: {nibbles.name}, Balance: {nibbles.money}")

print("transfering money...")
guido.transfer_money(monty, 100) # monty is the one that is transfering 100$ to the other person specified when printing.
print(f"User: {guido.name}, Balance: {guido.money}")
print(f"User: {monty.name}, Balance: {monty.money}")

# instead of:
# guido.make_deposit(100)
# guido.make_deposit(200)
# guido.make_deposit(300)
# guido.make_withdrawal(50)
# guido.display_user_balance()

# chaining the method calls:
# guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()
