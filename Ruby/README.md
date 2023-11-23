#  Ruby


## Overview

Ruby is a powerful, flexible programming language you can use in web/Internet development, to process text, to create games, and as part of the popular Ruby on Rails web framework. Ruby is:

- High-level, meaning reading and writing Ruby is really easy—it looks a lot like regular English!
- Interpreted, meaning you don’t need a compiler to write and run Ruby. You can write it here at Codecademy or even on your own computer (many are shipped with the Ruby interpreter built in—we’ll get to the interpreter later in this lesson).
- Object-oriented, meaning it allows users to manipulate data structures called objects in order to build and execute programs. We’ll learn more about objects later, but for now, all you need to know is everything in Ruby is an object.
- Easy to use. Ruby was designed by Yukihiro Matsumoto (often just called “Matz”) in 1995. Matz set out to design a language that emphasized human needs over those of the computer, which is why Ruby is so easy to pick up.


## Data Types: Numbers, Strings, Booleans

#### Strings

Strings in Ruby are a sequence of characters enclosed by single quotation marks (‘’) or double quotation marks (“”).

    my_string = "Ruby"

#### Numeric

    # Integer value
    x = 1

    # Float value
    y = 1.2

#### Boolean
    true 
    false

#### Arithmetic operations

    Addition (+)
    Subtraction (-)
    Multiplication (*)
    Division (/)
    Exponentiation (**)
    Modulo (%)


## 'puts' and 'print'

- print: command just takes whatever you give it and prints it to the screen. 
- puts: (for “put string”) adds a new (blank) line after the thing you want it to print.
#####

    puts "What's up?"
    print "Oxnard Montalvo"

    print "print\n"
    puts "amazing"


## Everything in Ruby is an Object


Because everything in Ruby is an object, everything in Ruby has certain built-in abilities called methods. 

For instance, strings have built-in methods that can tell you the length of the string, reverse the string, and more.


### Methods

    puts "I love espresso".length
    # ==> 15

    puts "Eric".reverse
    # ==> cirE

    puts "eric".upcase   
    # ==> ERIC

    puts "eric".downcase
    # ==> eric


## Comments

Single line comments start with a #.
Multi line comments start with =begin and end with =end.


    # I'm a full line comment!
    "Eric".length # I'm a comment, too!

    =begin
    I'm a comment!
    I don't need any # symbols.
    =end


## Naming Conventions

By convention, these variables should start with a lowercase letter and words should be separated by underscores. Ruby won’t stop you from starting your local variables with other symbols, such as capital letters, $s, or @s, but by convention these mean different things, so it’s best to avoid confusion by doing what the Ruby community does.

    counter
    masterful_method


## String interpolation

String interpolation is used to insert the result of Ruby code into a string.

    age = 30

    print "Hi, my name is Cody, and I am #{age} years old"
    # "Hi, my name is Cody, and I am 30 years old"

## Method Chaining

    name = "Unicorn"
    puts name.downcase.reverse.upcase

## Getting Input

    print "What's your first name?"
    first_name = gets.chomp
    puts "My first name is #{first_name}!"


- **gets**: Ruby method that gets input from the user. When getting input, Ruby automatically adds a blank line (or newline) after each bit of input;
- **chomp**: removes that extra line. (Your program will work fine without chomp, but you’ll get extra blank lines everywhere.)


## if Statement

    number = 10
    if number == 10
        puts "Your condition was true!"
    end

### else statement

    if number > 50 
        print "number is greater than 50"
    else
        print "number is not greater than 50"	
    end 


### elsif Statements

    print "enter a number: "
    num = gets.chomp
    num =  num.to_i;

    if num == 5
        print "number is 5"
    elsif num == 10
        print "number is 10"
    elsif num == 11
        print "number is 11"
    else
        print "number is something other than 5, 10, or 11"
    end


## not Operator

The ! (not) operator in Ruby flips a boolean value. If a value is true then applying ! to the value changes it to false and vice versa.

    data = true;
    puts !data;
    # Output: false


## Unless statement

An unless statement in Ruby is used to evaluate an expression. If the expression evaluates to false, then the code following unless is executed.

    #This construct requires a "number" variable to be less than 10 in order to execute:
    print "Enter a number"
    number = gets.to_i
    unless number >= 10
        puts "number is less than 10."
    end

## Comparison operators

- \>   greater than; 
- \<   less than; 
- \>=  greater than or equal to; 
- \<=  less than or equal to; 
- \==  equal to
#####

    a = 1;
    b = 2;
    c = 2;

    puts a > b;
    puts a < b;
    puts b >= c;
    puts a <= c;
    puts b == c;

    # Output: 
    # false
    # true
    # true
    # true
    # true


## Or operator

    grade1 = 50
    grade2 = 30
    grade3 = 80

    if grade1 > grade2 || grade1 > grade3
        puts "Grade 1 is not the lowest score!"
    end

## And operator

    if score1 > score2 && score1 > score3
        print "Score 1 is the greatest in value."
    else
        print "Score 1 is not the greatest in value."
    end


## Assignment Operators


    a = 1;
    a += 3;
    puts a; # Output: 4

    b = 4;
    b -= 2;
    puts b; # Output: 2

    num = 12;
    num *= 2;
    puts num; # Output: 24

    num /= 4;
    puts num; # Output: 6


## each Method


To iterate over an array in Ruby, use the .each method. It is preferred over a for loop as it is guaranteed to iterate through each element of an array.

    data = [3, 6, 9, 12]

    data.each do |num|
        puts "The number is: #{num}"
    end

    # Output:
    # The number is: 3
    # The number is: 6
    # The number is: 9
    # The number is: 12


## “next” Keyword


The next keyword is used within a loop to pass over certain elements and skip to the following iteration. It is useful for omitting elements that you do not wish to have iterated. next is followed by an if statement which defines which elements are to be skipped.


    for i in 1..10
        next if i % 2 == 0
        puts i
    end

    # In this example, the next 
    # keyword along with a shorthand 
    # if statement is used to skip 
    # over the even numbers in the sequence.
    
    # Output:
    # 1
    # 3 
    # 5
    # 7
    # 9


## while Loop


    i = 1
    while i <= 3 do
        puts "Message number #{i}"
        i = i + 1
    end

    # Output:
    # Message number 1
    # Message number 2
    # Message number 3


## times Method

    5.times { puts "Codecademy" }

    # Output: 
    # Codecademy
    # Codecademy
    # Codecademy
    # Codecademy
    # Codecademy


## Range

The range can be divided into an inclusive range where the last integer in the sequence is included and an exclusive range where the last integer is excluded.

    # Inclusive
    (3..5).each do |i|
        puts i
    end
    # Output:
    # 3
    # 4
    # 5

    # Exclusive
    (3...5).each do |i|
        puts i
    end
    # Output
    # 3
    # 4


## loop

A loop method can be used to run a block of code repeatedly in Ruby. Either use curly braces ({}) or the do/end keyword combination to wrap the block of code that will be looped.

    num = 1
    loop do
        puts "We are in the loop!"
        num += 1
        break if num > 3
    end

    puts "We have exited the loop!"

    # Output
    # We are in the loop!
    # We are in the loop!
    # We are in the loop!
    # We have exited the loop!


## until Loop

Putting a block of code inside an until loop in Ruby will cause the code to run as long as its condition remains false. It’s only when the condition becomes true that the loop stops.
If the block of code doesn’t allow for a way for the condition to be changed to true then the loop will continue forever and it will cause an error.

    i = 1

    until i == 4 do
        puts "Message number #{i}"
        i = i + 1
    end

    # Output
    # Message number 1
    # Message number 2
    # Message number 3


## for Loop

    for i in 1..3 do
        puts "Message number #{i}"
    end

    # Output
    # Message number 1
    # Message number 2
    # Message number 3


## Hash


hash is a collection of key-value pairs.

    profile = {
        "name" => "Magnus",
        "profession" => "chess player",
        "ranking" => 1,
        "grandmaster?" => true
    }

    # "name", "profession", "ranking", and "grandmaster?" are the keys. "Magnus", "chess player", 1 and true are the values.

    puts profile["name"] # => Magnus


## Array

array is an ordered collection of Ruby objects separated by commas and enclosed in []. An array can contain the same or different types of Ruby objects, such as Integers, Strings, Floats, etc. An array can also be empty.

    numbers = [1, 2, 3, 4, 5]
    #An array of Integers

    words = ["See", "Spot", "run"]
    #An array of Strings

    mixed = ["hello", 5, true, 3.0]
    #An array with a String, Integer, Boolean, and Float

    empty = []
    #An empty array

## Hash New

hash can be created through literal notation (because we are literally assigning what key=>value pairs we want in the hash) or by assigning a variable equal to Hash.new which generates a new, empty hash.


    #Creating a hash through literal notation:
    lunch = {
        "protein" => "chicken",
        "greens" => "lettuce",
        "organic?" => true
    }

    #Creating a hash through Hash.new
    lunch = Hash.new
    puts lunch # => {}



## Hash Bracket Notation Adding Pairs

a new key-value pair can be added to a hash using bracket notation. The new key is bracketed after the name of the hash and then the value is assigned after the equals sign.

    #Bracket notation applies to any hash, regardless of how it was initialized
    teammates = Hash.new
    teammates["forward"] = "Messi"

    salary = {
        "starting" => 40000
    }
    salary["mid-level"] = 60000


## Multidimensional Arrays

    multi_array = [[0,1,2,3],[4.5, true, "hi"]]

#### Accessing the array at index 1

    puts multi_array[1] # => [4.5, true, "hi"]

#### Accessing the element at index 0 within the array at index 1

    puts multi_array[1][0] # => 4.5


## Array Index

    example = ["Car", "Boar", 45, 9.9, true]

    #For an array named "example", you can retrieve an item of a particular index by referencing its index.

    puts example[2] # => 45
    puts example[0] # => Car


## Method .Each

**.each** method is used to iterate over arrays and hashes. This allows each element in an array and each key-value pair in a hash to be iterated.

    #In this example, the each method iterates over every color in the colors array and prints it to the console.

    colors = ["red", "blue", "green", "yellow"]

    colors.each { |color| puts color }
    #Output
    #red
    #blue
    #green
    #yellow

    #When iterating over hashes, two placeholder variables are needed to represent each key/value pair.

    polygons = {
        "pentagon" => 5,
        "hexagon" => 6,
        "nonagon" => 9
    }

    polygons.each do |shape, sides|
        puts "A #{shape} has #{sides} sides."
    end
    #Output
    #A pentagon has 5 sides.
    #A hexagon has 6 sides.
    #A nonagon has 9 sides.


## Hash Bracket Notation Value

the values in a hash can be accessed using bracket notation. After the hash name, type the key in square brackets in order to access the value.

    my_love = {
        "dog" => "Keanu",
        "breed" => "Shiba Inu",
        "age_in_years" => 1,
    }

    puts my_love["breed"] # => Shiba Inu


## Combined Comparison Operator


the combined comparison operator, **<=>**, also known as the spaceship operator is used to compare two objects. It returns 0 if the first operand equals the second, 1 if the first operand is greater than the second, and -1 if the first operand is less than the second.

    puts "Keanu" <=> "Adrianna" # The first letters of each word are compared in ASCII order and since "K" comes after "A", 1 is printed.

    puts 1 <=> 2 # -1

    puts 3 <=> 3 # 0

    #<=> can also be used inside of a block and to sort values in descending order:
    my_array = [3, 0, 8, 7, 1, 6, 5, 9, 4]
    my_array.sort! { |first_num, second_num| second_num <=> first_num }
    #Attaching an ! to the end of .sort or any other Ruby method modifies the original array.

    print my_array
    #Output => [9, 8, 7, 6, 5, 4, 3, 1, 0]


## Method


    def greeting
        puts "Hello world!"
    end

    #In this example, the first line or header contains the keyword "def" and the method name. puts "Hello world!" is within the body of the method, which describes the certain task that the method carries out. It is also indented two spaces by convention. Following the body, the method ends with the end keyword.


## Method Splat

a splat (*) operator is used to indicate that a parameter can have an unknown number of arguments.

    #The * preceding the parameter "clubs" allows for multiple arguments to be passed into the method when you actually call it.

    def extra_curriculars(*clubs)
        clubs.each { |club| puts "After school, I'm involved with #{club}" }
    end

    extra_curriculars("chess club", "gymnastics", "anime club", "library services")

    #Output
    #After school, I'm involved with chess club
    #After school, I'm involved with gymnastics
    #After school, I'm involved with anime club
    #After school, I'm involved with library services


## Block Parameter

a method can take a block as a parameter.
Passing a block to a method is a great way of abstracting certain tasks from the method and defining those tasks when we call the method.


    # The block, {|i| puts i}, is passed the current array item each time it is evaluated. This block prints the item. 
    [1, 2, 3, 4, 5].each { |i| puts i }


## Return


    def generous_tip(bill)
        return bill * (0.25)
    end

    generous_tip(100) # 25

    #In this example, the generous_tip method is returning the product of bill and 0.25. In order to see that value, a "puts" or "print" can be added before the method call.


## Sort Method

the **.sort** array method is used to sort items in an array in ascending order (least to greatest).

    my_array = [3, 4, 8, 7, 1, 6, 5, 9, 2]
    my_array.sort!
    #Attaching an ! to the end of .sort or any other Ruby method modifies the original array.
    print my_array
    # => [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #If you didn't use !, print my_array returns the original array.


## Method Parameters & Arguments

    def square(num) # num is the parameter
        puts num ** 2
    end

    square(5) #5 is the argument
    #Output => 25


## Block

a block is a section of code defined within the keywords **do** and **end** or with curly braces **{ }**. This is usually preceded by an integer followed by .times to indicate how many times the code is to be executed.

    2.times do
        puts "I'm a code block!"
    end  

    #Output
    #I'm a code block!
    #I'm a code block!

    3.times { puts "So am I!" }

    #Output
    #"So am I!"
    #"So am I!"
    #"So am I!"


## Symbols

symbols are immutable names primarily used as hash keys or for referencing method names.

    my_bologna = {
        :first_name => "Oscar",
        :second_name => "Meyer",
        :slices => 12
    }

    puts my_bologna[:second_name] # => Meyer

    #Symbols must be valid Ruby variable names and always start with a colon (:).



## Hashes, Symbols, & Values

In Ruby hashes, key symbols and their values can be defined in either of two ways, using a => or : to separate symbol keys from values.


    my_progress = {
        :program => "Codecademy",
        :language => "Ruby",
        :enthusiastic? => true 
    }
    #Key symbols and their values can be defined with a =>, also known as a hash rocket.

    my_progress = {
        program: "Codecademy",
        language: "Ruby",
        enthusiastic?: true 
    }
    #Key symbols and their values can also be defined with the colon (:) at the end of the symbol followed by its value.



## .select Method

In Ruby, the .select method can be used to grab specific values from a hash that meet a certain criteria.

    olympic_trials = {
        Sally: 9.58,
        John: 9.69,
        Bob: 14.91
    }

    olympic_trials.select { |name, time| time <  10.05 }

    #The example above returns {:Sally=>9.58, :John=>9.69} since Sally and John are the only keys whose values meet the time < 10.05 criteria.


## .each_key & .each_value

    eren_jaeger = {
        age: 15,
        enemy: "titans",
        branch: "Survey Corps"
    }

    eren_jaeger.each_key { |key| puts key }
    #Output:
    #age
    #enemy
    #branch

    eren_jaeger.each_value { |value| puts value }
    #Output:
    #15
    #titans
    #Survey Corps


## Case Statement

    tv_show = "Bob's Burgers"

    case tv_show
        when "Archer"
            puts "I don't like the voice of Archer."
        when "Bob's Burgers"
            puts "I love the voice of Bob Belcher."
        else
            puts "I don't know who voices this cartoon."
    end

    # => I love the voice of Bob Belcher.


## .respond_to?

takes a symbol representing a method name and returns true if that method can be called on the object and false otherwise.

    puts "A".respond_to?(:push)
    # => false
    # Here, the following Ruby code will return false since .push can’t be called on a String object.

    puts "A".respond_to?(:next)
    # => true
    # Here, however, the following Ruby code will return true since .next can be called on a String object. Calling .next on the letter “A” would return the letter “”.


## Short-Circuit Evaluation

When Ruby evaluates expressions containing boolean operators, it uses short-circuit evaluation. With ||, if the expression on the left evaluates to true, it will return true. Otherwise, it will check if the expression on the right evaluates to true. If so, the expression returns true; otherwise, it will return false.

With &&, both the expression on the left and the expression on the right have to evaluate to true in order to return true. If either expression is false, it will return false

    a = true
    b = false
    c = true

    puts a || b
    #Output => true
    puts b || a
    #Output => true
    puts a && c
    #Output => true 
    puts a && b
    #Output => false


## Ternary Operator

    tacos_eaten = 12

    puts tacos_eaten >= 5 ? "Sir, you've had enough!" : "Keep eating tacos!"

    # => Sir, you've had enough!


## .upto and .downto Methods
are used to iterate over a specific range of values.

    "B".upto("F") { |letter| print letter, " " }
    # => B C D E F

    5.downto(0) { |num| print num, " " }
    # => 5 4 3 2 1 0

    #In both examples, Ruby iterates over specified ranges using the initial value, a .downto or .upto method, and a final value. Each element is passed into the block following the .upto or .downto method.


## Conditional Assignment Operator
a conditional assignment operator (||=) assigns a real value to a variable only when its current value is false or nil. Otherwise, Ruby keeps its original value.

    boyfriend = nil

    boyfriend ||= "Jimmy Jr."

    boyfriend ||= "Josh"

    puts boyfriend
    # => "Jimmy Jr."

    # In this example, since the original value of boyfriend is set to nil which is nothing, Ruby assigns it a value of "Jimmy Jr." on the following line. Once boyfriend holds this real value, another reassignment is overlooked by Ruby and the previous value holds.


## .push Method Alternative (Concatenation)
an alternative to the .push method is the concatenation operator << which can be used to add an element to the end of an array or a string.

    array = [1, 2, 3]
    array << 4
    print array
    #Output => [1, 2, 3, 4]

    puts "Hello," << " welcome to Codecademy."
    #Output => Hello, welcome to Codecademy.


## “if” Statement Short Expression
the if statement can be expressed in a single line in the case of a short expression. This single line would consist of an expression followed by the if keyword and finally an expression that evaluates to either true or false.

    num = 6

    if num % 2 == 0
        puts "This number is even!"
    end

    #Refactored, this can be stated in a single line as demonstrated below:
    puts "This number is even!" if num % 2 == 0


## Implicit Return
the return keyword in a method can be omitted making it an implicit return, in which Ruby automatically returns the result of the last evaluated expression.

    def product(x,y)
        x * y
    end

    product(5, 4)
    # => 20
    #In this example, Ruby evaluates the product method and returns 20 even though the return keyword was omitted.


## .call Method
a proc and a lambda can be called directly using the .call method.

    proc_test = Proc.new { puts "I am the proc method!" }
    lambda_test = lambda { puts "I am the lambda method!"}

    proc_test.call # => I am the proc method!
    lambda_test.call # => I am the lambda method!

    #The following code would result in "I am the proc method!" and "I am the lambda method!" printed to the console respectively, once the proc, proc_test, and the lambda, lambda_test, are called.

## lambda
a lambda is an object similar to a proc. Unlike a proc, a lambda requires a specific number of arguments passed to it, and it returns to its calling method rather than returning immediately.

    def proc_demo_method
        proc_demo = Proc.new { return "Only I print!" }
        proc_demo.call
        "But what about me?" # Never reached
    end

    puts proc_demo_method 
    # Output 
    # Only I print!

    # (Notice that the proc breaks out of the method when it returns the value.)

    def lambda_demo_method
        lambda_demo = lambda { return "Will I print?" }
        lambda_demo.call
        "Sorry - it's me that's printed."
    end

    puts lambda_demo_method
    # Output
    # Sorry - it's me that's printed.

    # (Notice that the lambda returns back to the method in order to complete it.)


## .collect Method
the .collect array method takes a block and applies the expression in the block to every element of an array.

    first_arr = [3, 4, 5]
    second_arr = first_arr.collect { |num| num * 5 }

    print second_arr #Output => [15, 20, 25]

    # In this example, the .collect method is used to multiply each number within first_arr by 5. The outcome is then saved inside of the second_arr variable and printed to the console. The original first_arr is left unchanged.


## yield Keyword
the yield keyword is used to transfer control from a method to a block and then back to the method once executed.

    def yield_test
        puts "I'm inside the method."
        yield
        puts "I'm also inside the method."
    end

    yield_test { puts ">>> I'm butting into the method!" }
    #Output
    # I'm inside the method.
    # >>> I'm butting into the method.
    # I'm also inside the method.


## proc
a proc is an instance of the Proc class and is similar to a block. As opposed to a block, a proc is a Ruby object which can be stored in a variable and therefore reused many times throughout a program.

    square = Proc.new { |x| x ** 2 }
    # A proc is defined by calling Proc.new followed by a block.

    [2, 4, 6].collect!(&square)
    # When passing a proc to a method, an & is used to convert the proc into a block.

    puts [2, 4, 6].collect!(&square)
    # => [4, 16, 36]

## Class
is used to organize and model objects with similar attributes and methods.

    class NewClass
        # code for this class 
    end

    # A basic class definition consists of the class keyword, the name of the class in CamelCase (with the first letter capitalized) format, and an end keyword.


## Class Variables
A class variable should be declared with two @ symbols preceding it.

    class Child
        @@children = 0
        def initialize(name, birth_year)
            @name = name
            @birth_year = birth_year
            @@children +=1
        end

        def self.children_added
            return @@children
        end

    end

    naomi = Child.new("Naomi", 2006)
    bertha = Child.new("Bertha", 2008)

    puts Child.children_added # => 2


## .new Method

    class Fighter
        def initialize(name, style, division, age)
            @name = name
            @style = style
            @division = division
            @age = age
        end
    end

    conor = Fighter.new("Conor", "mixed martial arts", "Welterweight", 31)

## Instance Variable
the @ symbol is used to signify an instance variable. Instance variables hold a value specific to each instance of that class, not to all members of the class itself.

    class Student
        def initialize(name, grade)
            @name = name
            @grade = grade
        end
    end

    # In this example, name and grade are the instance variables.


## Initialize Method
an initialize method is used to generate new instances of the class. It is usually the first method of a class.

    class Person
        def initialize
            # this code runs when a new instance is created
        end
    end

    #Every time Person.new is called, the initialize method of the Person class is called.

## super Keyword
super keyword is used to directly access the attributes or methods of a superclass. This means a class with super will inherit the attributes or methods of a superclass.

    class Trip
        def initialize(duration, price)
            @duration = duration
            @price = price
        end
    end


    class Cruise < Trip
        def initialize(duration, price)
            super
        end
    end

    spain_backpacking = Trip.new(14, 800.00)
    carnival = Cruise.new(7, 2400.00)

    #In this example, the Cruise class inherits from the Trip class and all of its attributes, including duration and price, are carried over with the super keyword.


## attr_reader and attr_writer Methods
In Ruby, attr_reader and attr_writer are methods used to read and write variables, respectively.

    class Student
        attr_reader :name
        attr_writer :name
        def initialize(name)
            @name = name
        end
    end
    #In this example, Ruby is able to both read and write the @name instance variable since it was passed to attr_reader and attr_writer as a symbol.

    top_student = Student.new("Jyothi")
    puts top_student.name # => Jyothi
    #In classes with attr_reader, instance variables can be accessed using . notation

    puts top_student.name # => Jyothi
    top_student.name = "Anika"
    puts top_student.name # => Anika
    #In classes with attr_writer, instance variables can be reassigned using . notation


## attr_accessor Method
attr_accessor, used to make a variable both readable and writeable, is a shortcut to attr_reader and attr_writer

    class CollegeStudent
        attr_reader :dorm
        attr_accessor :major

        def initialize(dorm, major)
            @dorm = dorm
            @major = major
        end
    end

    #In this example, Ruby is able to only read the @dorm instance variable but both read and write the @major instance variable since it was passed to the attr_accessor method.


## namespace
the term namespace refers to a module the contains a group of related objects. An example of a Ruby namespace is the Math module.

    #To retrieve a constant from the Math module, the scope resolution operator (::), should be used.

    puts Math::PI
    # => 3.141592653589793

    #In this example, Ruby is targetting the PI constant from the Math module using the scope resolution operator, (::), and printing its value to the console.


## require Keyword
the require keyword is used to fetch a certain module which isn’t yet presented in the interpreter. It is best practice to place this at the beginning of your code.

    require 'date'

    puts Date.today
    # => 2023-11-23


## Module
a module contains a set of methods, constants, or classes which can be accessed with the . operator similarly to classes. Unlike classes, it is impossible to create instances of a Ruby module.

    #A Ruby module can be created using the module keyword followed by the module name written in CapitalizedCamelCase format finalized with an end.

    module MyPizza
        FAVE_TOPPING = "Buffalo Chicken"
    end
    #In this example, myPizza is a module that holds a constant, FAVE_TOPPING, set equal to the string, Buffalo Chicken.


***

# Code samples

    =begin
        Code Sample
    =end

    print "What's your first name? "
    first_name = gets.chomp
    first_name.capitalize!

    print "What's your last name? "
    last_name = gets.chomp
    last_name.capitalize!

    print "What city are you from? "
    city = gets.chomp
    city.capitalize!

    print "What state or province are you from? "
    state = gets.chomp
    state.upcase!

    puts "Your name is #{first_name} #{last_name} and you're from #{city}, #{state}!"

***

## References

[https://www.codecademy.com/]](https://www.codecademy.com/learn/learn-ruby/modules/learn-ruby-introduction-to-ruby-u/cheatsheet)