************
*  Python  *
************


Prof. Charles Severance
https://www.py4e.com/lessons



note: https://jupyter.org/
    Jupiter Notebook to create nice python exercises, examples, dashboards, formulas, etc

Any other editor to code in python



- Imports

    Standard Import:
    import module_name

    Import with an Alias:
    import module_name as alias

    Specific Imports:
    from module_name import function_name

        This form of import allows you to directly import a specific function, class, or variable from the module. With this approach, you don't need to use the module's name as a prefix; you can use the imported name directly.

    Import All Names from a Module:
    from module_name import *

        This imports all the names (functions, classes, variables) from the module into your code's namespace. This is generally discouraged because it can lead to naming conflicts and make your code less clear.



- Math Operations

    print(1+2) = 3
    print(2-1) = 1
    print(1*2) = 2
    print(8/2) = 4.0

    import math
    pi = 3.14
    round(pi)           #3
    math.ceil(pi)       #4
    math.floor(pi)      #3
    abs(pi)             #3.14
    pow(pi, 2)          #9.8596
    math.sqrt(pi)       #1.772004514666935

    x = 1
    y = 2
    z = 3

    max(x, y, z)        #3
    min(x, y, z)        #1


- Numerical Data Types

    Integer: ..., -2, -1, 1, 2, 3, ...

    Float: -1.5, -3.14, 3.14, 55.5


- String Data Type

    print("this is a string")
    print('this is also a string')


- Concatenation

    print("a"+"b")

    - Multiple Outputs
    print("balance", 5000)  #by default, the values will be separeted by spaces

    print("Iron", "Man", sep = "-")
    #Iron-Man


- Comments
    # this is a Comments

- Docstrings (documentation strings)
    #Docstrings are retained throughout the runtime of the program (at run time)
    def my_function():
    """
    description:
     some description of the fucntion goes here
    """


- Labeling, Storing and Handling Data with Variables

    x = 42          #Integer
    y = "Hello"     #String
    z = 3.14        #Float

notes: 
    Python is case-sensitive.
    can't start with number or use special characters like %


- Working with Input
    input() function returns a string.

    age = int(input())          #convert input string to integer
    height = float(input())     #convert input string to float

    a = str(32)                 #convert to string


- Multiple Inputs
    name = input()
    age = input()

- In-Place Operators (+, -, *, /, %, **, //)
    x = 2
    x += 3
    x *= 4

Concatenation:
    x = "test"
    x += 1          #test1


- Booleans

    True/False

    compare using ==, !=, <, >, <=, >=

    print("a" == "b")           #False

    print( int(True) )          #1
    print( int(False) )          #0


- if/else statements
    #Python uses identation to delimit blocks of code

    if condition:
        statements
    elif:
        statements
    else:
        statements

    one statement if:
    print('A' if 5>4 else 'B')

- While loop
    #normally used when don't know how many iterations
    i = 1
    while i <= 5:
        print(i)
        i += 1


- Break and continue
    break:  end loop prematurely
    continue: jumps back to the top of the loop. Stops current iteration and continues with the next one.


- For Loop
    #used to iterate over a given sequence
    words = ['hello', 'world', '!']
    for word in words:
        print(word)
    #hello
    #world
    #!

    #iterate over strings
    str = 'testing for loops'
    count = 0
    for i in str:
        if i == 'o':
            count+=1
            
    print(count)   #3

    for i in range(5):
        print(i)            #print 0 to 4 in different lines


- List Slices
    x = [0,1,2,3,4,5,6]
    print(x[2:6])       #[2, 3, 4, 5]
    print(x[:7])        #[0, 1, 2, 3, 4, 5, 6]
    print(x[0:])        #[0, 1, 2, 3, 4, 5, 6]
    print(x[::2])       #[0, 2, 4, 6]
    
    print(x[7:5:-1])    #[6]
    print(x[::-1])      #[6, 5, 4, 3, 2, 1, 0]  #revert


- List Functions
    list = [1,2,3]
    len(list)           #3
    list.append(4)      #[1, 2, 3, 4]
    list.insert(0, 8)   #[8, 1, 2, 3, 4]
    list.index(8)       #0
    min(list)           #1
    max(list)           #8
    list.count(4)       #1
    list.remove(4)      #[8, 1, 2, 3]
    list.reverse()      #[3, 2, 1, 8]
    list.pop()          #removes the last value from the list
    list_b = list.copy()         #copies a list to other variable

- String Functions
    format()
    #example:
    nums = [4,5,6]
    msg = 'numbers: {0}, {1}, {2}'.format(nums[0], nums[1], nums[2])    #numbers: 4, 5, 6

    str = 'for sale: {a}{b}'.format(a = 'T', b='1')     #for sale: T1

    join()
    #example:
    msg = ', '.join(['a','b','c'])          #a, b, c

    split()
    #example:
    str = 'some text goes here'
    x = str.split(' ')                      #['some', 'text', 'goes', 'here']

    replace()
    #example:
    str = 'Hello there'
    str.replace('there', 'world')           #Hello there

    str.lower()
    str.upper()
    len(str)
    str.capitalize()
    str.isdigit()
    str.isalpha()
    str.count('o')
    str.replace('e', 'a')
    str*3


- Custom Functions
    def my_function():
        <code goes here>
    
    #example:
    def sum(x, y):
        return x+y

    sum(1,2)            #3


- dir gives available funtions/methods
    dir()

    example: dir('test')

    l = list()
    print(dir(l))


- Remove Whitespaces
    var = ' test '

    var.lstrip() : removes left whitespace
    var.rstrip() : removes right whitespace
    var.strip()  : removes both  whitespace

    var.startwith('te')  #True



- Open files
    f = open("D:\\myfiles\welcome.txt", "r")
    print(f.read())



Return the 5 first characters of the file:
    print(f.read(5))


Read one line of the file:
    print(f.readline())


Read two lines of the file:
    print(f.readline())
    print(f.readline())


Loop through the file line by line:
    for x in f:
        print(x)

Read all lines without looping:
    f.readlines()

Close the file when you are finish with it:
    f.close()


- Write to an Existing File
    "a" - Append - will append to the end of the file
    "w" - Write - will overwrite any existing content


    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()                                       #we always have to close it in order to save into the file. Otherwise it will be only in the buffer


    #we can do this way, and it will auto close the file when finish to write:
    with open('file.txt', 'a') as f:
        f.write('your test here\n')

    f.write('more text')    #this will get an error, because the file is already closed


- Create a New File
    "x" - Create - will create a file, returns an error if the file exist
    "a" - Append - will create a file if the specified file does not exist
    "w" - Write - will create a file if the specified file does not exist

Create a file called "myfile.txt":
    f = open("myfile.txt", "x")

Create a new file if it does not exist:
    f = open("myfile.txt", "w")

- Delete File
    Remove the file "demofile.txt":

    import os
    os.remove("demofile.txt")

Check if file exists, then delete it:

    import os
    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
        print("The file does not exist")


Delete Folder:
    import os
    os.rmdir("myfolder")


- Collection (List Constants & Dictionary)

Lists

    lst = list()            #or lst = ()
    lst.append(21)
    lst.append(32)
    print(lst)          #[21, 32]

    friends = [ 'Joseph', 'Glenn', 'Sally' ]
    x = [ 1, 24, 43 ]
    y = [ 'red', 98.3, [2, 5] ]

iterate Lists:
    friends = [ 'Joseph', 'Glenn', 'Sally' ]
    for friend in friends:
        print('Friend:', friend)
    print('Done!')

#always start in position 0
    print(friends[0])   #Joseph

Lists are Mutable:
    lotto = [2, 14, 23, 21, 65]
    lotto[2] =  28
    print(lotto)    #[2, 14, 28, 21, 65]

Size of a List:
    print(len(friends))  #3

Check if the item occurs in the list
    words = ['spam', 'egg', 'sausage']
    print('egg' in words)           #True
    
Check if the item is not in the list
    words = ['spam', 'egg', 'sausage']
    if not 'orange' in words:
        print('True')

    #or
    print('orange' not in words)


    order matters:
    [1,2] == [2,1]      #false


- Range function:
 returns a list of numbers that range from zero to one less than the parameter

    print(range(4))     #[0, 1, 2, 3]

    l = list(range(5, 20))      #[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    #step - 3rd argument
    print(list(range(5, 20, 2)))        #[5, 7, 9, 11, 13, 15, 17, 19]

    #backward
    print(list(range(7, 3, -1)))        #[7, 6, 5, 4]


    friends = [ 'Joseph', 'Glenn', 'Sally' ]
    print(len(friends))   #3
    print(range(len(friends)))   #[0, 1, 2]

Range in a For loop:

    friends = [ 'Joseph', 'Glenn', 'Sally' ]
    for friend in friends:
         print('Friend name: ', friend)


    for i in range(len(friends)):
        friend = friends[i]
        print('Friend name: ', friend)


- Dictionary
    #Dictionaries are like lists except that they use keys instead of numbers to look u values
    #database-like operations
    #most powerfull data Collection
    same as:
        #Associative Arrays - Perl/PHP
        #Properties or Map or HashMap - Java
        #Property Bag: C# and .Net

    dict = {"Fri": 20, "Thu": 6, "Sat": 1}
    dict["Thu"] = 13
    dict["Sat"] = 2
    dict["Sun"] = 9

    print(dict)     #{'Fri': 20, 'Thu': 13, 'Sat': 2, 'Sun': 9}


    d = dict()          # or d = {}
    d['age'] = 21
    d['name'] = 'John'

    print(d)            #{'age': 21, 'name': 'John'}


- Dictionary Functions
    get()

    #if the value doesn't exist return 0
    counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
    print(counts.get('kris', 0))                                        #0


- Iterate Dictionaries
    d = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
    for key in d:
        print(key, d[key], sep=', ')

    #chuck, 1
    #annie, 42
    #jan, 100


- Two Iteration Variables

    d = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
    for key,val in d.items():
        print(key, val, sep=', ')

    #chuck, 1
    #annie, 42
    #jan, 100


- Tuples
    Another type kind of sequences like lists
    They have elements which are indexed starting at 0
    Tuples are immutable
    Cannot use: append, sort, reverse

    t = tuple()
    dir(t)              #count, index

    x = (1, 2, 3, 4, 5)
    print(x[1])             #2

    simpler and more efficient in terms of memory use and performance than lists
    used for temporary variables  

    (x, y) = ('4', 'fred')
    print(y)            #fred

    parenthesis are optional
    x, y = '4', 'fred'
    print(y)            #fred


    d = {'quincy': 1, 'beau': 5, 'kris': 9}
    t = d.items()
    print(t)                    #dict_items([('quincy', 1), ('beau', 5), ('kris', 9)])

    #sort by key
    print(sorted(t))            #[('beau', 5), ('kris', 9), ('quincy', 1)]

    #sort by value
    d = {'quincy': 1, 'beau': 5, 'kris': 9}
    tmp = list()

    #switch key, value order
    for k, v in d.items():
        tmp.append( (v, k) )
        
    print(tmp)                  #[(1, 'quincy'), (5, 'beau'), (9, 'kris')]

    tmp = sorted(tmp, reverse=True)
    print(tmp)                  #[(9, 'kris'), (5, 'beau'), (1, 'quincy')]


    #shorter version (Lambdas)
    d = {'quincy': 1, 'beau': 5, 'kris': 9}
    print( sorted ( [ (v, k) for k, v in d.items() ] ) )            #[(1, 'quincy'), (5, 'beau'), (9, 'kris')]


    order matters:
    (1,2) == (2,1)      #False


- Sets
    similar to Dictionaries and Lists 
    duplicate values will automatically get removed from the set
    faster to check whether an item is part of a set using the in operator

    num_set = {1, 2, 3, 4, 5}
    print(3 in num_set) #True

    num_set.add(6)          #{1, 2, 3, 4, 5, 6}
    num_set.remove(1)       #{2, 3, 4, 5, 6}

    | union
    & intersection
    - difference
    ^ symmetric difference

    first = {1, 2, 3, 4, 5}
    second = {2, 3, 5, 8, 9}
    print(first | second)           #{1, 2, 3, 4, 5, 8, 9}
    print(first & second)           #{2, 3, 5}
    print(first - second)           #{1, 4}
    print(first ^ second)           #{1, 4, 8, 9}

    order doesn't matter
    {1,2,3} == {3,2,1}            #True
    {1,2,3} == {3,2,1,1,1,1}      #True


- List Comprehensions
    myList = [1,2,3,4,5]
    [2*item for item in myList]
    #[2, 4, 6, 8, 10]

- List Comprehensions with filters
    evens=[i*2 for i in range(10) if i*2 % 2 == 0]
    print(evens)
    #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


- Collections Summary
    Use Dictionaries when:
        - you need a logical association between key:value pair.
        - you need fast lookup for your data, based on a custom key.
        - your data is constantly modified.

    Lists:
        - collection of data that does not need random access.
        - suitable for storing a collection of data that can be modified and access by index.

    Set:
        - uniqueness for the elements

    Tuples:
        - when your data cannot change


- Lambdas (aka anonymous function)
    lambda (args : expression) (value)

    (lambda x : x*5) (7)        #35



- Regular Expressions
    ^           matches the beginning of a line
    $           matches the end of a line
    .           matches any character
    \s          matches whitespace
    \S          matches any non-whitespace character
    *           repeats a character zero or more times
    *?          repeats a character zero or more times (non-greedy)
    +           repeats a character zero or more times
    +?          repeats a character zero or more times (non-greedy)
    [aeiou]     matches a single character in the list set
    [^XYZ]      matches a single character NOT in the list set
    [a-z0-9]    the set of characteres can include a range
    [0-9]+      one or more digits
    (           indicates where string extraction is to start
    )           indicates where string extraction is to end
    [^ ]        not blank


    #first import the library
    import re

    re.search()             #Returns True or False. Similar to find() method for strings

    re.findall()            #extract portions of a string that match your regular expression, similar to a combination of find() and slicing: var[5:10]


    #example:
    import re
    str = 'john.smith@ab.cd.com'

    print(str.find('@'))
    print(re.search('@', str))


    #example2:
    import re
    str = 'From: John Smith, To: Manuel'

    print(str.startswith('From:'))
    print(re.search('^From:', str))


    import re
    str = 'title-title_goes_here: description_goes_here'
    print(re.search('^t.*:', str))              #<re.Match object; span=(0, 22), match='title-title_goes_here:'>
    print(re.search('^t\S+', str))              #<re.Match object; span=(0, 22), match='title-title_goes_here:'>



    - Non-Greedy matching
    return all in the string that matches the regex

    #example1:
    import re
    str =  'From: Using the : and continues'

    print(re.findall('^F.+:', str))         #['From: Using the :']          (Greedy)        return the longest match
    print(re.findall('^F.+?:', str))        #['From:']                      (Non-Greedy)    return the first macth

    #example2:
    import re
    s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
    lst = re.findall('\\S+@\\S+', s)
    print(lst)                                      #['csev@umich.edu', 'cwen@iupui.edu']



- Networking: Sockets
    -HTTP request 

    import socket

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()        #Unicode to UTF-8
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')         #UTF-8 to Unicode
    mysock.close()


    #see Networking: Using urllib in Python to do the same in less code

- Encoding
    ASCII American Standard Code for Information Interchange

    ord() function tells us the numeric value of a simple ASCII character

    print(ord('H'))     #72
    print(ord('\n'))    #10

    when strings were simple, it is represented by 1 byte per character (8 bits)
    in today modern world there are millions of characters

    UTF-16 - Fixed legnth - Two bytes
    UTF-32 - Fixed legnth - Four bytes
    UTF-8 - 1-4 bytes   - dynamic length - recomended practice for encoding data to be exchanged between systems

    in Python 3 all strings internally are Unicode
    when "talking" to network or databases we have to encode and decode data (usually to UTF-8)


- Networking: Using urllib in Python
    
    import urllib.request, urllib.parse, urllib.error

    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    for line in fhand:
        print(line.decode().strip())


    - reading web pages
    import urllib.request, urllib.parse, urllib.error
    fhand = urllib.request.urlopen('http://data.pr4e.org/page1.htm')
    for line in fhand:
        print(line.decode().strip())



- Networking: Web Scraping with Python
    "spidering the web" or "web crawling"
    pull data
    monitoring
    make a database for search engine

    Make it more simple using the library BeautifulSoup

    install it 

        import urllib.request, urllib.parse, urllib.error
        from bs4 import BeautifulSoup

        #Ignore SSL certification errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        url = input('Enter URL: ')
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

        #Retrieve all of the anchor tags
        tags = soup('a')
        for tag in  tags:
            print(tag.get('href', None))


- Web Services: XML Schema

    import xml.etree.ElementTree as ET

    data = '''<person>
        <name>Chuck</name>
        <phone type="intl">
            +1 734 303 4456
        </phone>
        <email hide="yes"/>
    </person>'''

    tree = ET.fromstring(data)
    print('Name', tree.find('name').text)
    print('Attr:', tree.find('email').get('hide'))
    print('Phone', tree.find('phone').text.strip())


- Web Services: JSON (JavaScript Object Notation)
    import json
    data = '''
    [
        { "id" : "001",
        "x" : "2",
        "name" : "Quincy"
        } ,
        { "id" : "009",
        "x" : "7",
        "name" : "Mrugesh"
        }
    ]
    '''
    info = json.loads(data)
    print(info[1]['name'])




    import json
    data = '''{
        "name" : "Chuck",
        "phone" : {
            "type" : "intl",
            "number" : "+1 745 123 4343"
        },
        "email" : {
            "hide" : "yes"
        }
    }'''

    info = json.loads(data)

    print('Name', info["name"])
    print('Hide:', info["email"]["hide"])




    import json
    data = '''
    [
        { "id" : "001",
        "x" : "2",
        "name" : "Quincy"
        } ,
        { "id" : "009",
        "x" : "7",
        "name" : "Mrugesh"
        }
    ]
    '''
    info = json.loads(data)
    print('User count:', len(info)) #[1, 2]
    for i in info:
            print('Name:', i['name'])
            print('Id:', i['id'])
            print('Attribute:', i['x'])



- Web Services: APIs
   - Web Services: API Rate Limiting and Security


- Python Objects
    - And Object is a bit of self-contained Code and Data
    - A key aspect of the Object approach is to break the problem into smaller understandable parts
    - Objects have boundaries that allows us to ignore un-needed detail
    - We have been using objects all along: String Objects, Integer Ibjects, Dictionary Objects, List Objects

    - Definitions
        - Class - a template -Dog
        - Method or Message - a defined capability of a class - bark()
        - Field or Attribute - a bit of data in a class - length
        - Object or Instance - a particular instance of a class - Noah

    class PartyAnimal:
        x = 0

        def party(self):
            self.x = self.x + 1
            print("So far", self.x)

    an = PartyAnimal()

    an.party()
    an.party()
    an.party()

    #So far 1
    #So far 2
    #So far 3

- Object lifecycle
    - Objects are created, used and discarded
    - Special methods called: 
        - constructor: set up some instance variables to have the proper initial values when the object is created
            class Person:
                #constructor
                def __init__(self, name, age):
                    self.name = name
                    self.age = age

            # Creating an instance of the Person class
            person1 = Person("Alice", 30)

            # Accessing the attributes
            print("Name:", person1.name)
            print("Age:", person1.age)
        
        - destructor:
            def __del__(self):
                print('I am destructed', self.x)
    

    class PartyAnimal:
        x = 0

        def __init__(self):
            print('I am constructed')

        def party(self) :
            self.x = self.x + 1
            print('So far',self.x)

        def __del__(self):
            print('I am destructed', self.x)

    an = PartyAnimal()  #contructor: x=0
    an.party()          #x=0+1=1
    an.party()          #x=1+1=2
    an = 42             #destructor: x=2
    print('an contains',an) #x=42


- Inheritance
    - reuse an existing class and inherit all the capabilities of an existing class and then add extra features
    - another form of store and reuse
    - write once - reuse many times
    - new class (child) has all the capabilities of the old class (parent) - and then some more
    - Also known as Subclass
    - Parent Class is the Superclass

    class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    class Cat(Animal):
        def purr(self):
            print("Purr...")
            
    class Dog(Animal):
        def bark(self):
            print("Woof!")
            
    noah = Dog("Noah", "brown")
    lara = Cat("Lara", "grey")

    noah.bark()
    lara.purr()



    - function super()
    #inheritance-related function that refers to the parent class.

    class A:
        def spam(self):
            print(1)
            
    class B(A):
        def spam(self):  #override
            print(2)
            super().spam()
    
    B().spam()

    #2
    #1


    example with list() class to avoid duplicated values:
    #myList = list()                #list is a class and we can extend it

    class UniqueList(list):
        def append(self, value)
            if value in self:
                return
            super().append(value)

    uniqueList = UniqueList()

    uniqueList.append(1)
    uniqueList.append(1)
    uniqueList.append(1)
    uniqueList.append(2)

    print(uniqueList)                   #[1,2]



    other example to force to call __init__ of parent class first


    class UniqueList(list):
        
        def __init__(self):             #this overwrites the constructor ( __init__ ) parent class
            super().__init__()          #this ensures parent __init__ is called first

        def append(self, value)
            if value in self:
                return
            super().append(value)


- Relational Databases and SQLite



--------------------------------------------------------

*args and **kwargs


    def myFun(*args, **kwargs):
        print(args)
        print(kwargs)
        
    myFun(1,2,3, param1='test')


    (1, 2, 3)
    {'param1': 'test'}


--------------------------------------------------------

-locals()

    def myFun(*args, **kwargs):
        print(args)                 #(1, 2, 3)
        print(kwargs)               #{'param1': 'test'}
        print(locals())             #{'args': (1, 2, 3), 'kwargs': {'param1': 'test'}}
        
    myFun(1,2,3, param1='test')



- globals()
    print(globals())


    msg = "global variable"

    def myFun(a, b):
        print(msg)      #global variable
        
    myFun(1,2) 


--------------------------------------------------------

- Try / Except
    def causeError():
        try:
            return 1/0
        except Exception as e:
            return print(f'Error occurred: {e}')

    causeError()


- Finally
    import time

    def causeError():
        start_time = time.time()
        try:
            return 1/0
        except Exception as e:
            return print(f'Error occurred: {e}')
        finally:
            print('This is always executed')
            time.sleep(1000)
            print(f'Function took {time.time() -start_time} seconds to execute')

    causeError()


- Catching Exceptions by Type

    def causeError():
        try:
            return 1 + 'a'
        except TypeError:
            print('There was a type error!')
        except ZeroDivisionError:
            print('There was a zero division error!')
        except Exception:
            print('Error occurred')

    causeError()


- Custom decorators

    def handleException(func):
        def wrapper():
            try:
                func()
            except TypeError:
                print('There was a type error!')
            except ZeroDivisionError:
                print('There was a zero division error!')
            except Exception:
                print('Error occurred')
        return wrapper

    @handleException
    def causeError():
        return 1/0

    causeError()


- Rising Exceptions
    
    @handleException
    def raiseError(n):
        if n == 0:
            rase Exception()

        print(n)

    raiseError()


- Custom Exceptions

    class CustomException(Exception):
        pass

    def causeError():
        raise CustomException('custom error')

    causeError()

    

    #example for HTTP:

    class HttpException(Exception):
        statusCode = None
        message = None

        def __init__(self):
            super().__init__(f'Status code: {self.statusCode} and message is: {self.message}')

    class NotFound(HttpException):
        statusCode = 404
        message = 'Page not found'

    class ServerError(HttpException):
        statusCode = 500
        message = 'Server is down'

    def raiseServerError():
        raise ServerError()

    raiseServerError()

    #ERROR!
    #Traceback (most recent call last):
    #  File "<string>", line 19, in <module>
    #  File "<string>", line 17, in raiseServerError
    #ServerError: Status code: 500 and message is: Server is down


--------------------------------------------------------

- Threads
    import threading
    import time

    def longSquare(num, results):
        time.sleep(1)
        results[num] = num**2

    results = {}
    t1 = threading.Thread(target=longSquare, args=(1,results))        
    t2 = threading.Thread(target=longSquare, args=(2,results))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(results)


#improving this
    
    import threading
    import time

    def longSquare(num, results)
        time.sleep(1)
        results[num] = num**2

    results = {}
    threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range(0,2)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print(results)


--------------------------------------------------------

- Multiprocessing

    >pip install multiprocess

    from multiprocessing import Process
    import time

    def longSquare(num, results):
        time.sleep(1)
        results[num] = num**2
        print("Finishing")

    results = {}
    processes = [Process(target=longSquare, args=(n,results)) for n in range(0,2)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    print(results)          # will not print results, unless the print is moved to the function itself. Normally we save data into files

--------------------------------------------------------

- CSV

 - Reading
    import csv

    with open('file.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)                                #skips header - actually skips a row
        for row in reader:
            print(row)


    #other way to do the same:
    with open('file.csv', 'r') as f:
    reader = list(csv.reader(f, delimiter=';'))     #convert to list
    for row in reader[1:]:                          #will skip 1st row (header)
        print(row)


    #convert to dictionary
    with open('file.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:                     
        print(row)

    #{'column1': value, 'column2': value, 'column3': value, 'column4': value, ...}

 - Filtering Data
    
    with open('file.csv', 'r') as f:
        reader = list(csv.DictReader(f, delimiter=';'))

    #create a list of postal codes with prime numbers only - it seems to be a prime postal code in us...
    primes = []
    for number in range(2, 99999):
        for factor in range(2, int(number**0.5)):
            if number % factor == 0:
                break
        else:
            primes.append(number)

    
    data = [row for row in data if int(row['postal code']) in primes and row['state code'] == 'MA']   #in primes and Massachutts



 - Writing

    with open('new_file.csv', 'r') as f:
        writer = csv.write(f)                       #default comma will be used
        for row in data:
            writer.writerow([row['place name'], row['county']])


--------------------------------------------------------

- JSON

 - Loading JSON

    import json
    from json import JSONDecodeError 

    jsonString = '{"a": "apple", "b": "bear", "c": "cat"}'          #this is a string, not json. commun mistake
    try:
        json.loads(jsonString)
    except JSONDecodeError:
        print('Could not parse JSON!')

 - Dumps JSON

    pythonDict = {"a": "apple", "b": "bear", "c": "cat"}
    json.dumps(pythonDict)


 - Custom JSON Decoders
    
    import json
    from json import JSONDecodeError, JSONEncoder

    class Animal:
        def __init__(self, name):
            self.name = name

    class AnimalEncoder:
        def default(self, o):
            if type(o) == Animal:
                return o.name
            return super().default(o)

    pythonDict = {"a": Animal('dog'), "b": Animal('bear'), "c": Animal('cat')}
    json.dumps(pythonDict, cls=AnimalEncoder)

--------------------------------------------------------

- command-line arguments
    python example.py --help

    python example.py -i            #for input values or file


example:

    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('--output')
    args = parser.parse_args()
    print(args.output)

#running
>python example.py --output somefile.txt


    #make arguments required:
    parser.add_argument('--output', required=True)

    #add help text to user:
    parser.add_argument('--output', '-o', required=True, help='The description file for the output parameter')

>python example.py -h

    #add more parameters
    parser.add_argument('--text', '-t', required=True, help='The text file to write to the file')


--------------------------------------------------------
- Functional Programming

-

- Recursion

    functions calling themselves


    def fib(x):
        if x == 0 or x == 1:
            return 1
        else:
            return fib(x-1) + fib(x-2)
            
    print(fib(4))


- The '__main__'

def some_function():
    print("This function can be reused in other scripts.")

if __name__ == '__main__':
    print("This code will only run when the script is the main program.")
    some_function()

    In this example, some_function can be imported and used in other scripts, 
    but the print statement and the function call will only occur when this script is run directly, 
    not when it's imported as a module.


- Placeholders

def hello(name="John"):
    print("Hello %s" % name)

def hello(name="John"):
    print("Hello {}".format(name))

def hello(name="John"):
    print(f"Hello {name}")

--------------------------------------------------------


::::::::::EXERCISES::::::::::

def pay(hours, rate):
    if h > 40:
        print("Overtime")
        pay = ( h * r ) + ( (h - 40)  * (r * 0.5) )
    else:
        pay = h * r
    return pay

try:
    h = float(input("Enter your hours: "))
    r = float(input("Enter your rate: "))
except:
    print("Error! Please enter a numeric value.")
    quit()
    
res = pay(h, r)
print("Pay:", res )


--------------------------------------------------------


def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'pt':
        return 'Olá'
    else:
        return 'Hello'
        

lang = input("Enter your language (es, pt, en): ")
name = input("Enter your name: ")
print(greet(lang), name + "!")


--------------------------------------------------------

#find smallest number

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15, 1]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)

print("Smallest:", smallest)


--------------------------------------------------------

#for a given set of numbers, calculate the sum of the numbers entered, the count of the numbers and the average

num = 0
tot = 0.0

while True :
    sval = input('Enter a number: ') #string value
    if sval == 'done' :
        break
    try :
        fval = float(sval) #float value
    except :
        print('Invalid input')
        continue
    
    num += 1
    tot += fval


print(tot, num, tot/num)



--------------------------------------------------------


use find and string slicing to extract the portion of the string after the colon and use float function to convert.

str='X-DSPAM-Confidence: 0.8475 '

colon_pos=str.find(':')
print(colon_pos)

#get string between : and end of string
portion_str=str[colon_pos+1:len(str)]
#print(len(str))
print(portion_str)

#remove both whitespaces:
str_number=portion_str.strip()

#convert to float
float_number=float(str_number)

print(float_number)


--------------------------------------------------------

Get hostname

data = 'From stephen.marquez@uct.ac.za Sat Jan  5 09:14:16 2001'
begin=data.find('@')+1
end=data.find(' ', begin, len(data))

hostname=data[begin:end]
print(hostname)


--------------------------------------------------------

write a program to read through a file and print the contents of the file (line by line) all in upper case.


file_name = input("Enter a file name: ")

try
    f = open(file_name, r)
except
    print("File doens't exist!")
    quit()

for line in f:
    print(line.rstrip().upper())

f.close()


--------------------------------------------------------

when encounter a new name, add a new entry to dictionary. If this is the second or later time we have seen the name, ass one to the count in the dictionary under that name.

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#{'csev': 2, 'cwen': 2, 'zqian': 1}


#or using get() function

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
   counts[name] = counts.get(name, 0) + 1
print(counts)

#{'csev': 2, 'cwen': 2, 'zqian': 1}



--------------------------------------------------------

Count the letter occurs more frequently

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"

d = dict()

words = text.split()

#print(words)

for word in words:
    d[word] = d.get(word, 0) + 1
#print(d)

max_word=None
max_count=0
for key,val in d.items():
    if val > max_count:
        max_count = val
        max_word = key
print(max_word, max_count, sep=', ')  


--------------------------------------------------------

REGEX - get the hostname from a string:

import re
email = 'From email address: f.d.m.vieira@gmail.com with Subject xyz'
host = re.findall('^From .*@([^ ]*)', email)
print(host)


--------------------------------------------------------

Networking - count words of a web page

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = disct()
for line in fhand:
    words = line.decode().strip()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print (counts)


--------------------------------------------------------

class Student:
    def __init__(self, name):
        self.name = name
    
    def sayHi(self):
        print("Hi from", self.name)
        
s1 = Student("Amy")
s1.sayHi()


--------------------------------------------------------
Using decorators

class Person:
    def __init__(self, name):
        self._name = name  # Note the underscore to indicate it's a private attribute

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string")

person = Person("Alice")
print(person.name)  # Access the 'name' attribute using a property
person.name = "Bob"  # Set the 'name' attribute using a property



other decorator:

    @staticmethod

--------------------------------------------------------

animalList = [('a', 'aardvark'),('b', 'bear'),('c','cat')]
animals = {i[0]: i[1] for i in animalList}
print(animals)
#{'a': 'aardvark', 'b': 'bear', 'c': 'cat'}

or 

animals = {key: value for key, value in animalList}
print(animals)
#{'a': 'aardvark', 'b': 'bear', 'c': 'cat'}



print(
    [{'letter': key, 'name': value} for key, value in animals.items()]
    )

#[{'letter': 'a', 'name': 'aardvark'}, {'letter': 'b', 'name': 'bear'}, {'letter': 'c', 'name': 'cat'}]


--------------------------------------------------------

from datetime import datetime

datetime.now()

datetime.now().second + 2


--------------------------------------------------------

myList = [5, 6, 4, 3, 1]
sorted(myList)                  #[1, 3, 4, 5, 6]



myList = [{'num':5}, {'num':6}, {'num':4}, {'num':3}, {'num':1}]
sorted(myList, key=lambda x: x['num'])                      #[{'num': 1}, {'num': 3}, {'num': 4}, {'num': 5}, {'num': 6}]



--------------------------------------------------------

#get current time

from datetime import datetime

def getCurrentTime():
    return datetime.now().strftime('%m-%d-%Y %H:%M:%S')
    
print(getCurrentTime())


--------------------------------------------------------

#send and receive messages


from datetime import datetime

def getCurrentTime():
    return datetime.now().strftime('%m-%d-%Y %H:%M:%S')
    
class Messenger:
    def __init__(self, listeners=[]):
        self.listeners = listeners
        
    def send(self, message):
        for listener in self.listeners:
            listener.receive(message)
    
    def receive(self, message):
        pass
    
class SaveMessages(Messenger):
    def __init__(self, listeners=[]):
        super().__init__(listeners)
        self.messages = []          #clean messages
        
    def receive(self, message):
        self.messages.append({'message': message, 'time': getCurrentTime()})
    
    def printMessages(self):
        for m in self.messages:
            print(f'Message: "{m["message"]}" Time: {m["time"]}')
        self.messages = []           #clean messages
    
listener = SaveMessages()

sender = Messenger([listener])

sender.send('Loggin attempt 1')
sender.send('Loggin attempt 2')

listener.printMessages()


--------------------------------------------------------

#open files and save with a different delimiter (pipe |)
#[('A', 1), ('B', 80), ('C', 10)]
# becomes A|1-B|80-C|10

with open(filename) as f:
    data = f.read()

data = [f'{char}'|{count} for char, count in data]

with open(newFilename, 'w') as f:
    f.write('-'.join(data))



--------------------------------------------------------
#write to a file from command line input:


from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--output', '-o', required=True, help='The description file for the output parameter')
parser.add_argument('--text', '-t', required=True, help='The text file to write to the file')

args = parser.parse_args()

with open(args.output, 'w') as f:
    f.write(args.text + '\n')

print(f'Wrote "{args.text}" to file "{args.output}"')


--------------------------------------------------------
#iterate and replace in same line:
 
#counter from 3 to 1
import time

for x in [3,2,1]:
    print(x, end = '', flush=True)
    time.sleep(1)
    print('\r', end = '', flush=True)




--------------------------------------------------------
Sample creating graph and sql data 

import pandas as pd
import ploty.graph_objects as go
from sqlalchemy import *

conn = create_engine(connection_url)
num_days = input("How many days?")
symbol = input("Symbol?")

data = pd.read_sql("""
SELECT TIME_BUCKET(%s) AS day,
    symbol,
    MIN(price) AS low,
    MAX(price) AS high,
    FIRST(price) AS open,
    LAST(price) AS close
FROM tick
WHERE symbol = %s
GROUP BY 2, 1
ORDER BY 2, 1;
""", conn, params = (str(num_days), symbol.upper()))

fig = go.Figure(data = [go.Candlestick(
    x = data["day"],
    open = data["open"],
    high = data["high"],
    low = data["low"],
    close = data["close"],
    name = symbol,
)])

fig.update_xaxes(type = "category")
fig.update_layout(xaxis_rangeslider_visible = False)
fig.show()


--------------------------------------------------------
