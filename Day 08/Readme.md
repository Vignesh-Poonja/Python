# Lists & Tuples

List is a collection which is ordered and changeable. Allows duplicate members.

Tuple is a collection which is ordered and unchangeable. Allows duplicate members.


# Use Case

List: Lists are used when you need a collection of elements that can change, such as a dynamic list of items or data that needs to be modified.

Tuple: Tuples are used when you need an ordered collection of elements that should not change, such as representing a point in 2D space (x, y), or when you want to ensure the integrity of the data.


# Memory

List: Lists generally consume more memory than tuples because they need to store additional information to support their mutability.

Tuple: Tuples consume less memory because they are immutable, and the interpreter can optimize memory usage.