
# here we create a class called car
# create attributes for it
# those attributes can then be used in a function
# that will be methods inherent to the class

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# we can no create objects of class car and invoke methods by...
my_car = Car(make="Acura", model="TSX", year=2004)
my_car.display_info()






# when want to creat a new class that has the same classes attributes
# as car we can avoid a little typing when we use super ()
# we still need to intialize, and I think we want to name
# the attributes we want to take from Car I think other wise it takes
# all attributes...note display_info() is re written to include battery

class Car2(Car):
    def __init__(self,make,model,year,battery):
        super().__init__(make, model, year)
        self.battery = battery

    def display_info(self):
        return f"{self.year} {self.make} {self.model} {self.battery}"


mel_car = Car2("Tesla","Y", 20015, "electric")
mel_car.display_info()


class MaxNumberFinder:

    def __init__(self, nums):
        self.nums = nums

        # your code here

    def find_max_number(self):
        if self.nums == []:
            return(None)
        else:
            return (max(self.nums))


finder = MaxNumberFinder(nums=[1,3,4,2])
finder.find_max_number()


# Create a class called Stack that implements a stack data structure.
# The stack should support the following operations:
# push(item): Pushes an item onto the top of the stack
# pop(): Removes and returns the item at the top of the stack.
# peek(): Returns the item at the top of the stack without removing it.
# is_empty(): Returns True if the stack is empty and False otherwise.
# size(): Returns the number of items in the stack.
# NOTICE HOW WE CAN REFER TO OTHER FUNCTIONS INSIDE THE CLASS
# SUCH AS is.empty2


class Stack:
    def __init__(self):
        self.item = []

    def push(self, item2):
        return( self.item .insert( len(self.item), item2))


    def pop(self):
        return(self.item.pop(self.item[1]))


    def peek(self):
        return (self.item[len(self.item) -1])

    def is_empty(self):
        if self.item == []:
            return(True)
        else:
            return(False)

    def size(self):
        if self.item == []:
            return(0)
        else:
            return(len(self.item)-1)

    def is_empty2(self):
        if self.is_empty() == True:
            print( "Spelled T-R-U-E")

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Should print 3
print(stack.peek())  # Should print 2
print(stack.is_empty())  # Should print False
print(stack.size())  # Should print 2


# Create a class called Queue that implements a queue data structure.
# The queue should support the following operations:
# enqueue(item): Adds an item to the back of the queue.
# dequeue(): Removes and returns the item from the front of the queue.
# peek(): Returns the item at the front of the queue without removing it.
# is_empty(): Returns True if the queue is empty and False otherwise.
# size(): Returns the number of items in the queue.

class Queue:
    def __init__(self):
        # Initialize an empty queue
        self.item = []

    def enqueue(self, item2):
        # Add the item to the back of the queue
        if self.item == []:
            return (self.item.append(item2))
        else:
            return (self.item.insert(len(self.item), item2))




    def dequeue(self):
        # Remove and return the item from the front of the queue
        if self.item == []:
            return None
        else:
            return self.item.pop(0)


    def peek(self):
        # Return the item at the front of the queue without removing it
        if self.item == []:
            return None
        return self.item[0]



    def is_empty(self):
        # Return True if the queue is empty, False otherwise
        if self.item == []:
            return True
        else:
            return False


    def size(self):
        # Return the number of items in the queue
        return len(self.item)



my_queue = Queue()
my_queue.enqueue(6)
my_queue.enqueue(3)
my_queue.peek()
my_queue.is_empty()

my_queue.size()

my_list = [1,2,3,4,5,6]

my_list.pop(0)


# Write a function that finds the first closest number in a list
# In: ([2, 4, 8, 10], 6)
# Out: 4

def find_closest_number(numbers, target):
    x = []
    stack = []
    if numbers == []:
            #x.append(target)
            return None
    if len(numbers) == 1:
        return abs(numbers[0] - target)
    else:
        for i in range(0,len(numbers)):
            x.append(abs(numbers[i] - target))
    return x.pop(min(x))

# Create a function called longest_consecutive_subsequence
# that takes a list of integers as input and returns the
# length of the longest consecutive subsequence of integers
# in the list. A consecutive subsequence is a sequence of integers
# where each integer appears exactly once and they are in consecutive order.
# Your function should use only built-in Python tools
x = []
def longest_consecutive_subsequence(nums):
    x = []
    #nums = sorted(nums)
    if nums == []:
        print("The list is empty")
    if len(nums) >= 1:
        i = 0
        #end = len(nums)
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                x.append(nums[i])
                print(x)
                i += 1
            #if i > 0 and i == len(nums):
             #   break
            else:
                i += 1
                print(x)

    return(x)

longest_consecutive_subsequence([10,25,1,2,3,5,6])
longest_consecutive_subsequence([])
### My While loop isn't printing or appending
## and I don't know why ??????????????????



