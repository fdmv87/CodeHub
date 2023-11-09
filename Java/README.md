#  Java

There are 4 core concepts in OOP: encapsulation, inheritance, polymorphism, and abstraction.

## Encapsulation

To ensure that implementation details are not visible to users. 
The variables of one class will be hidden from the other classes, accessible only through the methods of the current class. This is called data hiding.

To achieve encapsulation in Java, declare the class' variables as private and provide public setter and getter methods to modify and view the variables' values.

encapsulation provides the following benefits:

- Control of the way data is accessed or modified
- More flexible and easily changed code
- Ability to change one part of the code without affecting other parts

For example:

    class BankAccount {
        private double balance=0;
        public void deposit(double x) {
            if(x > 0) {
            balance += x;
            }
        }
    }


Exercise:

### Task

Complete the setAge method of the Pupil class. If the value of parameter a is over 6, assign it to age attribute and output "Welcome".
Output "Sorry" otherwise.

Sample Input: 7
Sample Output: Welcome
    
    import java.util.Scanner;
    public class Main
    {
        public static void main(String[] args) {
            Scanner read = new Scanner(System.in);
            int a = read.nextInt();
            
            Pupil pupil =  new Pupil();
                pupil.setAge(a);
        }
    }

    class Pupil{
        private int age;
        
        //complete setter method
        public void setAge(int a){
            if(a > 6 )
                System.out.println("Welcome");
            else
                System.out.println("Sorry");
        }
        
        public int getAge(){
            return age;
        }
    }


## Inheritance

is the process that enables one class to acquire the properties (methods and variables) of another. With inheritance, the information is placed in a more manageable, hierarchical order.
The class inheriting the properties of another is the subclass (also called derived class, or child class); the class whose properties are inherited is the superclass (base class, or parent class).
To inherit from a class, use the extends keyword.

This example shows how to have the class Dog (subclass) to inherit from the class Animal (superclass).

    class Dog extends Animal {
        // some code
    }


When one class is inherited from another class, it inherits all of the superclass' non-private variables and methods.

Example:

    class Animal {
    protected int legs;
        public void eat() {
            System.out.println("Animal eats");
        }
    }

    class Dog extends Animal {
        Dog() {
            legs = 4;
        }
    }

As you can see, the Dog class inherits the legs variable from the Animal class.
We can now declare a Dog object and call the eat method of its superclass.

Other Example:

    class Animal {
        public void makeSound() {
            System.out.println("Hi");
        }
    }

    class Dog extends Animal {}

    class Main {
        public static void main(String args[ ]) {
            Dog dog = new Dog();
            dog.makeSound();
        }
    }

    >Hi


Constructors are not member methods, and so are not inherited by subclasses.
However, the constructor of the superclass is called when the subclass is instantiated.

Example:

    class A {
        public A() {
            System.out.println("New A");
        }
    }
    class B extends A {
        public B() {
            System.out.println("New B");
        }
    }
    class Program {
        public static void main(String[ ] args) {
            B obj = new B();
        }
    }

    >New A
    >New B



## Polymorphism

Polymorphism, which refers to the idea of "having many forms", occurs when there is a hierarchy of classes related to each other through inheritance.
A call to a member method will cause a different implementation to be executed, depending on the type of the object invoking the method.
Here is an example: Dog and Cat are classes that inherit from the Animal class. Each class has its own implementation of the makeSound() method.


    class Animal {
        public void makeSound() {
            System.out.println("Grr...");
        }
    }
    class Cat extends Animal {
        public void makeSound() {
            System.out.println("Meow");
        }
    }
    class Dog extends Animal {
        public void makeSound() {
            System.out.println("Woof");
        }
    }
    class Program {
        public static void main(String[ ] args) {
            Animal a = new Dog();
            Animal b = new Cat();

            a.makeSound();
            b.makeSound();
        }
    }

    >Woof
    >Meow

This feature is known as method overriding.


Rules for Method Overriding:

- Should have the same return type and arguments
- The access level cannot be more restrictive than the overridden method's access level (Example: If the superclass method is declared public, the overriding method in the sub class can be neither private nor protected)
- A method declared final or static cannot be overridden
- If a method cannot be inherited, it cannot be overridden
- Constructors cannot be overridden

+ Method Overloading +
When methods have the same name, but different parameters, it is known as method overloading.
This can be very useful when you need the same method functionality for different types of parameters.
The following example illustrates a method that returns the maximum of its two parameters.

    int max(int a, int b) {
        if(a > b) {
            return a;
        }
        else {
            return b;
        }
    }

The method shown above will only work for parameters of type integer.
However, we might want to use it for doubles, as well. For that, you need to overload the max method:

    double max(double a, double b) {
        if(a > b) {
            return a;
        }
        else {
            return b;
        }
    }

Now, our max method will also work with doubles.
An overloaded method must have a different argument list; the parameters should differ in their type, number, or both.

Another name for method overloading is compile-time polymorphism.


## Abstraction

Data abstraction provides the outside world with only essential information, in a process of representing essential features without including implementation details.
A good real-world example is a book. When you hear the term book, you don't know the exact specifics, such as the page count, the color, or the size, but you understand the idea, or abstraction, of a book.
The concept of abstraction is that we focus on essential qualities, rather than the specific characteristics of one particular example.

In Java, abstraction is achieved using abstract classes and interfaces.
An abstract class is defined using the abstract keyword.
- If a class is declared abstract it cannot be instantiated (you cannot create objects of that type).
- To use an abstract class, you have to inherit it from another class.
- Any class that contains an abstract method should be defined as abstract.

An abstract method is a method that is declared without an implementation (without braces, and followed by a semicolon): abstract void walk();

For example, we can define our Animal class as abstract:

    abstract class Animal {
        int legs = 0;
        abstract void makeSound();
    }

The makeSound() method is also abstract, as it has no implementation in the superclass.
We can inherit from the Animal class and define the makeSound() method for the subclass:  

    class Cat extends Animal {
        public void makeSound() {
            System.out.println("Meow");
        }
    }

Every Animal makes a sound, but each has a different way to do it. That's why we define an abstract class Animal, and leave the implementation of how they make sounds to the subclasses.
This is used when there is no meaningful definition for the method in the superclass.

class Main {
    public static void main(String[ ] args) {
        Cat lara = new Cat();
        lara.makeSound();
   }
}

abstract class Animal {
    int legs = 0;
    abstract void makeSound();
}

class Cat extends Animal{
    public void makeSound(){
        System.out.println("Meow");
    }
}

>Meow


## Interfaces

An interface is a completely abstract class that contains only abstract methods.

Some specifications for interfaces:

- Defined using the interface keyword.
- May contain only static final variables.
- Cannot contain a constructor because interfaces cannot be instantiated.
- Interfaces can extend other interfaces.
- A class can implement any number of interfaces.

An example of a simple interface:

    interface Animal {
        public void eat();
        public void makeSound();
    }

Interfaces have the following properties:

- An interface is implicitly abstract. You do not need to use the abstract keyword while declaring an interface.
- Each method in an interface is also implicitly abstract, so the abstract keyword is not needed.
- Methods in an interface are implicitly public.
- In Java, a subclass can inherit from only one superclass.

A class can inherit from just one superclass, but can implement multiple interfaces!

Use the "implements" keyword to use an interface with your class.


interface Animal {
  public void eat();
  public void makeSound();
}

class Cat implements Animal {
  public void makeSound() {
    System.out.println("Meow");
  }
  public void eat() {
    System.out.println("omnomnom");
  }
}


------------------------------------------------------------------------------------------------------------
----------------
- Type Casting -
----------------

Assigning a value of one type to a variable of another type is known as Type Casting.

To cast a value to a specific type, place the type in parentheses and position it in front of the value.

Example:

    int a = (int) 3.14;
    System.out.println(a);

The code above is casting the value 3.14 to an integer, with 3 as the resulting value.

Another example:

    double a = 42.571;
    int b = (int) a;
    System.out.println(b);
    >42

Java supports automatic type casting of integers to floating points, since there is no loss of precision.
On the other hand, type casting is mandatory when assigning floating point values to integer variables.



For classes, there are two types of casting:

+ Upcasting +
You can cast an instance of a subclass to its superclass.

Consider the following example, assuming that Cat is a subclass of Animal. 

    Animal a = new Cat();

Java automatically upcasted the Cat type variable to the Animal type.


+ Downcasting +
Casting an object of a superclass to its subclass is called downcasting.

Example:

    Animal a = new Cat();
    ((Cat)a).makeSound();

This will try to cast the variable a to the Cat type and call its makeSound() method.

Why is upcasting automatic, downcasting manual? Well, upcasting can never fail. But if you have a group of different Animals and want to downcast them all to a Cat, then there's a chance that some of these Animals are actually Dogs, so the process fails.



## Anonymous Classes

Anonymous classes are a way to extend the existing classes on the fly.
For example, consider having a class Machine:

    class Machine {
        public void start() {
            System.out.println("Starting...");
        }
    }

When creating the Machine object, we can change the start method on the fly.

    public static void main(String[ ] args) {
        Machine m = new Machine() {
            @Override public void start() {
                System.out.println("Wooooo");
            }
        };
        m.start();
    }

After the constructor call, we have opened the curly braces and have overridden the start method's implementation on the fly.

The @Override annotation is used to make your code easier to understand, because it makes it more obvious when methods are overridden.
The modification is applicable only to the current object, and not the class itself. So if we create another object of that class, the start method's implementation will be the one defined in the class.

    class Machine {
        public void start() {
            System.out.println("Starting...");
        }
    }  
        public static void main(String[ ] args) {
        Machine m1 = new Machine() {
            @Override 
            public void start() {
                System.out.println("Wooooo");
            }
        };
        m1.start();

        Machine m2 = new Machine();
        m2.start();
    }

    >Wooooo
    >Starting...


## Inner Classes

Java supports nesting classes; a class can be a member of another class.
Creating an inner class is quite simple. Just write a class within a class. Unlike a class, an inner class can be private. Once you declare an inner class private, it cannot be accessed from an object outside the class.

Example:
    class Robot {
        int id;
        Robot(int i) {
            id = i;
            Brain b = new Brain();
            b.think();
        }

        private class Brain {
            public void think() {
                System.out.println(id + " is thinking");
            }
        }
    }

The class Robot has an inner class Brain. The inner class can access all of the member variables and methods of its outer class, but it cannot be accessed from any outside class.


## Comparing Objects

Remember that when you create objects, the variables store references to the objects.
So, when you compare objects using the equality testing operator (==), it actually compares the references and not the object values.


    class Animal {
        String name;
        Animal(String n) {
            name = n;
        }
    }

    class MyClass {
        public static void main(String[ ] args) {
            Animal a1 = new Animal("Robby");
            Animal a2 = new Animal("Robby");
            System.out.println(a1 == a2);
        }
    }
    >False

Despite having two objects with the same name, the equality testing returns false, because we have two different objects (two different references or memory locations).



+ equals()
Each object has a predefined equals() method that is used for semantical equality testing.
But, to make it work for our classes, we need to override it and check the conditions we need.
There is a simple and fast way of generating the equals() method, other than writing it manually.
Just right click in your class, go to Source->Generate hashCode() and equals()...

    class Animal {
    String name;
    Animal(String n) {
        name = n;
    }
    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((name == null) ? 0 : name.hashCode());
        return result;
    }
    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Animal other = (Animal) obj;
        if (name == null) {
            if (other.name != null)
                return false;
            } else if (!name.equals(other.name))
                return false;
            return true;
        }
    }

The automatically generated hashCode() method is used to determine where to store the object internally. Whenever you implement equals, you MUST also implement hashCode.

We can run the test again, using the equals method:

    public static void main(String[ ] args) {
        Animal a1 = new Animal("Robby");
        Animal a2 = new Animal("Robby");
        System.out.println(a1.equals(a2));
    }
    >True

## Enums

An Enum is a special type used to define collections of constants.
Here is a simple Enum example:

    enum Rank {
        SOLDIER,
        SERGEANT,
        CAPTAIN
    }

Note that the values are comma-separated.
You can refer to the constants in the enum above with the dot syntax.

    Rank a = Rank.SOLDIER;

Basically, Enums define variables that represent members of a fixed set.


After declaring an Enum, we can check for the corresponding values with, for example, a switch statement.

    Rank a = Rank.SOLDIER;

    switch(a) {
        case SOLDIER:
            System.out.println("Soldier says hi!");
            break;
        case SERGEANT:
            System.out.println("Sergeant says Hello!");
        break;
        case CAPTAIN:
            System.out.println("Captain says Welcome!");
            break;
    }
    >Soldier says hi!

You should always use Enums when a variable (especially a method parameter) can only take one out of a small set of possible values.
If you use Enums instead of integers (or String codes), you increase compile-time checking and avoid errors from passing in invalid constants, and you document which values are legal to use.

Some sample Enum uses include month names, days of the week, deck of cards, etc.


## Java API

The Java API is a collection of classes and interfaces that have been written for you to use.
The Java API Documentation with all of the available APIs can be located on the Oracle website at 
http://docs.oracle.com/javase/7/docs/api/

Once you locate the package you want to use, you need to import it into your code.
The package can be imported using the import keyword.

For example:

    import java.awt.*;

The awt package contains all of the classes for creating user interfaces and for painting graphics and images.
The wildcard character (*) is used to import all of the classes in the package.


## Exceptions, Lists, Threads & Files

### Exception Handling

An exception is a problem that occurs during program execution. Exceptions cause abnormal termination of the program.
Exception handling is a powerful mechanism that handles runtime errors to maintain normal application flow.
An exception can occur for many different reasons. Some examples:
    - A user has entered invalid data.
    - A file that needs to be opened cannot be found.
    - A network connection has been lost in the middle of communications.
    - Insufficient memory and other issues related to physical resources.

As you can see, exceptions are caused by user error, programmer error, or physical resource issues. However, a well-written program should handle all possible exceptions.

    try {
        //some code
    } catch (Exception e) {
        //some code to handle errors
    }

Example:
    public class MyClass {
        public static void main(String[ ] args) {
            try {
                int a[ ] = new int[2];
                System.out.println(a[5]);
            } catch (Exception e) {
                System.out.println("An error occurred");
            }
        }
    }

Without the try/catch block this code should crash the program, as a[5] does not exist.
Notice the (Exception e) statement in the catch block - it is used to catch all possible Exceptions.


### Multiple Exceptions

+ thow

The throw keyword allows you to manually generate exceptions from your methods. Some of the numerous available exception types include the IndexOutOfBoundsException, IllegalArgumentException, ArithmeticException, and so on.

For example, we can throw an ArithmeticException in our method when the parameter is 0.

    int div(int a, int b) throws ArithmeticException {
        if(b == 0) {
            throw new ArithmeticException("Division by Zero");
        } else {
            return a / b;
        }
    }

The throws statement in the method definition defines the type of Exception(s) the method can throw.
Next, the throw keyword throws the corresponding exception, along with a custom message.
If we call the div method with the second parameter equal to 0, it will throw an ArithmeticException with the message "Division by Zero".

Multiple exceptions can be defined in the throws statement using a comma-separated list.


+ Exception Handling

A single try block can contain multiple catch blocks that handle different exceptions separately.
Example:

    try {
        //some code
    } catch (ExceptionType1 e1) {
        //Catch block
    } catch (ExceptionType2 e2) {
        //Catch block
    } catch (ExceptionType3 e3) {
        //Catch block
    }

All catch blocks should be ordered from most specific to most general.
Following the specific exceptions, you can use the Exception type to handle all other exceptions as the last catch.


### Threads

Java is a multi-threaded programming language. This means that our program can make optimal use of available resources by running two or more components concurrently, with each component handling a different task.
You can subdivide specific operations within a single application into individual threads that all run in parallel.


There are two ways to create a thread.
1. Extend the Thread class
Inherit from the Thread class, override its run() method, and write the functionality of the thread in the run() method.
Then you create a new object of your class and call it's start() method to run the thread.

Example:
    class Loader extends Thread {
        public void run() {
            System.out.println("Hello");
        }
    }

    class MyClass {
        public static void main(String[ ] args) {
            Loader obj = new Loader();
            obj.start();
        }
    }

As you can see, our Loader class extends the Thread class and overrides its run() method.
When we create the obj object and call its start() method, the run() method statements execute on a different thread.

Every Java thread is prioritized to help the operating system determine the order in which to schedule threads. The priorities range from 1 to 10, with each thread defaulting to priority 5. You can set the thread priority with the setPriority() method.


+ Runnable
The other way of creating Threads is implementing the Runnable interface.
Implement the run() method. Then, create a new Thread object, pass the Runnable class to its constructor, and start the Thread by calling the start() method.

Example:

    class Loader implements Runnable {
        public void run() {
            System.out.println("Hello");
        }
    }

    class MyClass {
        public static void main(String[ ] args) {
            Thread t = new Thread(new Loader());
            t.start();
        }
    }

The Thread.sleep() method pauses a Thread for a specified period of time. For example, calling Thread.sleep(1000); pauses the thread for one second. Keep in mind that Thread.sleep() throws an InterruptedException, so be sure to surround it with a try/catch block.

It may seem that implementing the Runnable interface is a bit more complex than extending from the Thread class. However, implementing the Runnable interface is the preferred way to start a Thread, because it enables you to extend from another class, as well.


### Runtime vs. Checked Exceptions

+ Types of Exceptions

There are two exception types, checked and unchecked (also called runtime). The main difference is that checked exceptions are checked when compiled, while unchecked exceptions are checked at runtime.

As mentioned in our previous lesson, Thread.sleep() throws an InterruptedException. This is an example of a checked exception. Your code will not compile until you've handled the exception.


    public class MyClass {
        public static void main(String[ ] args) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                //some code
            }
        }
    }


We have seen examples of unchecked exceptions, which are checked at runtime, in previous lessons.
Example (when attempting to divide by 0):


    public class MyClass {
        public static void main(String[ ] args) {
            int value = 7;
            value = value / 0;
        }
    }
    /*
    Exception in thread "main" java.lang.ArithmeticException: / by zero at MyClass.main(MyClass.java:4)
    */



## ArrayList

The Java API provides special classes to store and manipulate groups of objects.
One such class is the ArrayList. Standard Java arrays are of a fixed length, which means that after they are created, they cannot expand or shrink.
On the other hand, ArrayLists are created with an initial size, but when this size is exceeded, the collection is automatically enlarged.
When objects are removed, the ArrayList may shrink in size. Note that the ArrayList class is in the java.util package, so it's necessary to import it before using it.
Create an ArrayList as you would any object.

    import java.util.ArrayList;
    //...
    ArrayList colors = new ArrayList();

You can optionally specify a capacity and type of objects the ArrayList will hold:

    ArrayList<String> colors = new ArrayList<String>(10);

The code above defines an ArrayList of Strings with 10 as its initial size.

ArrayLists store objects. Thus, the type specified must be a class type. You cannot pass, for example, int as the objects' type. Instead, use the special class types that correspond to the desired value type, such as Integer for int, Double for double, and so on.



The ArrayList class provides a number of useful methods for manipulating its objects.
The add() method adds new objects to the ArrayList. Conversely, the remove() method removes objects from the ArrayList.
Example:

    import java.util.ArrayList;

    public class MyClass {
        public static void main(String[ ] args) {
            ArrayList<String> colors = new ArrayList<String>();
            colors.add("Red");
            colors.add("Blue");
            colors.add("Green");
            colors.add("Orange");
            colors.remove("Green");

            System.out.println(colors);
        }
    }

Other useful methods include the following:
- contains(): Returns true if the list contains the specified element
- get(int index): Returns the element at the specified position in the list
- size(): Returns the number of elements in the list
- clear(): Removes all of the elements from the list

Note: As with arrays, the indexing starts with 0.


## LinkedLists

The LinkedList is very similar in syntax to the ArrayList.
You can easily change an ArrayList to a LinkedList by changing the object type.

    import java.util.LinkedList;

    public class MyClass {
        public static void main(String[ ] args) {
            LinkedList<String> c = new LinkedList<String>();
            c.add("Red");
            c.add("Blue");
            c.add("Green");
            c.add("Orange");
            c.remove("Green");
            System.out.println(c);
        }
    }

You cannot specify an initial capacity for the LinkedList.


+ LinkedList vs. ArrayList
The most notable difference between the LinkedList and the ArrayList is in the way they store objects.
The ArrayList is better for storing and accessing data, as it is very similar to a normal array.
The LinkedList is better for manipulating data, such as making numerous inserts and deletes.

In addition to storing the object, the LinkedList stores the memory address (or link) of the element that follows it. It's called a LinkedList because each element contains a link to the neighboring element.

You can use the enhanced for loop to iterate over its elements.

    LinkedList<String> c = new LinkedList<String>();
    c.add("Red");
    c.add("Blue");
    c.add("Green");
    c.add("Orange");
    c.remove("Green");

    for(String s: c) {
        System.out.println(s);
    }

Summary:

- Use an ArrayList when you need rapid access to your data.
- Use a LinkedList when you need to make a large number of inserts and/or deletes.


## HashMap

Arrays and Lists store elements as ordered collections, with each element given an integer index.
HashMap is used for storing data collections as key and value pairs. One object is used as a key (index) to another object (the value). 
The put, remove, and get methods are used to add, delete, and access values in the HashMap.

Example:

    import java.util.HashMap;
    public class MyClass {
        public static void main(String[ ] args) {
            HashMap<String, Integer> points = new HashMap<String, Integer>();
            points.put("Amy", 154);
            points.put("Dave", 42);
            points.put("Rob", 733);
            System.out.println(points.get("Dave")); 
        }
    }

We have created a HashMap with Strings as its keys and Integers as its values.

Use the get method and the corresponding key to access the HashMap elements.

A HashMap cannot contain duplicate keys. Adding a new item with a key that already exists overwrites the old element.
The HashMap class provides containsKey and containsValue methods that determine the presence of a specified key or value.
If you try to get a value that is not present in your map, it returns the value of null.

null is a special type that represents the absence of a value.


## Set

A Set is a collection that cannot contain duplicate elements. It models the mathematical set abstraction.
One of the implementations of the Set is the HashSet class.

Example:
    import java.util.HashSet;

    public class MyClass {
        public static void main(String[ ] args) {
            HashSet<String> set = new HashSet<String>();
            set.add("A");
            set.add("B");
            set.add("C");
            System.out.println(set);
        }
    }

You can use the size() method to get the number of elements in the HashSet.


+ LinkedHashSet
The HashSet class does not automatically retain the order of the elements as they're added. To order the elements, use a LinkedHashSet, which maintains a linked list of the set's elements in the order in which they were inserted.

What is hashing?
A hash table stores information through a mechanism called hashing, in which a key's informational content is used to determine a unique value called a hash code.
So, basically, each element in the HashSet is associated with its unique hash code.

You've learned about the various collection types that are available in Java, including Lists, Maps, and Sets. The choice of which one to use is specific to the data you need to store and manipulate.

### Sorting Lists

For the manipulation of data in different collection types, the Java API provides a Collections class, which is included in the java.util package.
One of the most popular Collections class methods is sort(), which sorts the elements of your collection type. The methods in the Collections class are static, so you don't need a Collections object to call them.

Example:

    public class MyClass {
        public static void main(String[ ] args) {
            ArrayList<String> animals = new ArrayList<String>();
            animals.add("tiger");
            animals.add("cat");
            animals.add("snake");
            animals.add("dog");
            
            Collections.sort(animals);
            
            System.out.println(animals);
        }
    }
    >[cat, dog, snake, tiger]

As you can see, the elements have been sorted alphabetically.

Other useful methods in the Collections class:
 - max(Collection c): Returns the maximum element in c as determined by natural ordering.
 - min(Collection c): Returns the minimum element in c as determined by natural ordering.
 - reverse(List list): Reverses the sequence in list.
 - shuffle(List list): Shuffles (i.e., randomizes) the elements in list.


### Iterators

An Iterator is an object that enables to cycle through a collection, obtain or remove elements. 
Before you can access a collection through an iterator, you must obtain one. Each of the collection classes provides an iterator() method that returns an iterator to the start of the collection. By using this iterator object, you can access each element in the collection, one element at a time.

The Iterator class provides the following methods:
 - hasNext(): Returns true if there is at least one more element; otherwise, it returns false.
 - next(): Returns the next object and advances the iterator.
 - remove(): Removes the last object that was returned by next from the collection.

The Iterator class must be imported from the java.util package.

Example:

    import java.util.Iterator;
    import java.util.LinkedList;

    public class MyClass {
        public static void main(String[ ] args) {
            LinkedList<String> animals = new LinkedList<String>();
            animals.add("fox");
            animals.add("cat");
            animals.add("dog");
            animals.add("rabbit");

            Iterator<String> it = animals.iterator();
            String value = it.next();
            System.out.println(value);
        }
    }

it.next() returns the first element in the list and then moves the iterator on to the next element.
Each time you call it.next(), the iterator moves to the next element of the list

Typically, iterators are used in loops. At each iteration of the loop, you can access the corresponding list element.
Example:

    import java.util.Iterator;
    import java.util.LinkedList;

    public class MyClass {
        public static void main(String[ ] args) {
            LinkedList<String> animals = new LinkedList<String>();
            animals.add("fox");
            animals.add("cat");
            animals.add("dog");
            animals.add("rabbit");
            
            Iterator<String> it = animals.iterator();
            while(it.hasNext()) {
                String value = it.next();
                System.out.println(value);   
            }
        }
    }
    
    >fox
    >cat
    >dog
    >rabbit

Here, the while loop determines whether the iterator has additional elements, prints the value of the element, and advances the iterator to the next.


## Working with Files

The java.io package includes a File class that allows you to work with files.
To start, create a File object and specify the path of the file in the constructor.

    import java.io.File;
    //...
    File file = new File("C:\\data\\input-file.txt");

With the exists() method, you can determine whether a file exists.

    import java.io.File;

    public class MyClass {
        public static void main(String[ ] args) {
            File x = new File("C:\\sololearn\\test.txt");
            if(x.exists()) {
                System.out.println(x.getName() +  "exists!");
            }
            else { 
                System.out.println("The file does not exist");
            }
        }
    }

The code above prints a message stating whether or not the file exists at the specified path.

The getName() method returns the name of the file.
Note that we used double backslashes in the path, as one backslash should be escaped in the path String.


## Reading a File

Files are useful for storing and retrieving data, and there are a number of ways to read from a file.
One of the simplest ways is to use the Scanner class from the java.util package.
The constructor of the Scanner class can take a File object as input.
To read the contents of a text file at the path "C:\\sololearn\\test.txt", we would need to create a File object with the corresponding path and pass it to the Scanner object.

    try {
        File x = new File("C:\\sololearn\\test.txt");
        Scanner sc = new Scanner(x);      
    }
        catch (FileNotFoundException e) {
    }

The Scanner class inherits from the Iterator, so it behaves like one.
We can use the Scanner object's next() method to read the file's contents.

    try {
        File x = new File("C:\\sololearn\\test.txt");
        Scanner sc = new Scanner(x);
        while(sc.hasNext()) {
            System.out.println(sc.next());
        }
        sc.close();
        } catch (FileNotFoundException e) {
            System.out.println("Error");
    }

The file's contents are output word by word, because the next() method returns each word separately.

It is always good practice to close a file when finished working with it. One way to do this is to use the Scanner's close() method.


Example of reading console input

    import java.util.Scanner;

    public class ConsoleInputExample {
        public static void main(String[] args) {
            // Create a Scanner object to read input from the console
            Scanner scanner = new Scanner(System.in);

            // Prompt the user for input
            System.out.print("Enter your name: ");

            // Read a line of text from the console
            String name = scanner.nextLine();

            // Prompt the user for a number
            System.out.print("Enter your age: ");

            // Read an integer from the console
            int age = scanner.nextInt();

            // Display the user's information
            System.out.println("Name: " + name);
            System.out.println("Age: " + age);

            // Close the Scanner when done
            scanner.close();
        }
    }


## Creating Files

Formatter, another useful class in the java.util package, is used to create content and write it to files.

Example:

    import java.util.Formatter;

    public class MyClass {
        public static void main(String[ ] args) {
        try {
            Formatter f = new Formatter("C:\\sololearn\\test.txt");
        } catch (Exception e) {
            System.out.println("Error");
        }
        }
    }

Once the file is created, you can write content to it using the same Formatter object's format() method.

Example:

    import java.util.Formatter;

    public class MyClass {
        public static void main(String[ ] args) {
            try {
                Formatter f = new Formatter("C:\\sololearn\\test.txt");
                f.format("%s %s %s", "1","John", "Smith \r\n");
                f.format("%s %s %s", "2","Amy", "Brown");
                f.close();    
            } catch (Exception e) {
                System.out.println("Error");
            }
        }
    }

The format() method formats its parameters according to its first parameter.

%s mean a string and get's replaced by the first parameter after the format. The second %s get's replaced by the next one, and so on. So, the format %s %s %s denotes three strings that are separated with spaces.

Note: \r\n is the newline symbol in Windows.

The code above creates a file with the following content:

    1 John Smith
    2 Amy Brown

Don't forget to close the file once you're finished writing to it!
