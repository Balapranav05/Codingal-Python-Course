class fruit:
    #Class variable
    taste='sweet'
    def __init__(self, name,color):
       self.name=name
       self.color=color

#Object creation
apple=fruit('Apple', 'Red')
banana=fruit('Banana', 'Yellow')
mango=fruit('Mango', 'Orange')
print(apple.taste)
print(apple.name, apple.color)
print(banana.name, banana.color)
print(mango.name, mango.color)