// C++ Syntax

// This is a single-line comment in C++

/*
This is a multi-line comment
in C++
*/

// Including a library
#include <iostream>

// Declaring a variable
int my_variable = 10;

// Printing the value of a variable
std::cout << my_variable << std::endl;

// Basic arithmetic operations
int addition = 2 + 2;
int subtraction = 5 - 3;
int multiplication = 4 * 6;
int division = 10 / 2;
int modulo = 10 % 3; // remainder of 10 divided by 3

// Conditional statements
if (my_variable > 5) {
std::cout << "my_variable is greater than 5" << std::endl;
} else if (my_variable == 5) {
std::cout << "my_variable is equal to 5" << std::endl;
} else {
std::cout << "my_variable is less than 5" << std::endl;
}

// Looping through an array
int my_array[5] = {1, 2, 3, 4, 5};
for (int i = 0; i < 5; i++) {
std::cout << my_array[i] << std::endl;
}

// Defining a function
int my_function(int argument1, int argument2) {
int result = argument1 + argument2;
return result;
}

// Calling a function
int function_result = my_function(3, 5);
std::cout << function_result << std::endl;

// Creating a class
class MyClass {
public:
MyClass(int attribute1, std::string attribute2) {
this->attribute1 = attribute1;
this->attribute2 = attribute2;
}

void my_method() {
std::cout << "Hello, world!" << std::endl;
}

private:
int attribute1;
std::string attribute2;
};

// Creating an instance of a class
MyClass my_instance(10, "value2");

// Calling a class method
my_instance.my_method();