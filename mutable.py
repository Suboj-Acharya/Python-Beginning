# Immutable And Mutable 
# Immutable data types are those whose values, once stored in memory, cannot be changed or updated. If any modification is attempted, a new object with a new memory address is created instead.

# For example, if an integer "a" is assigned the value 10, a specific memory address is allocated to store that value. The value 10 at this memory address cannot be changed directly due to immutability. When "a" is reassigned to another value (e.g., 20), a new memory address is allocated for the new value, and the reference to the original memory address is removed. If no other references exist to the value 10, Python's automatic garbage collector will eventually reclaim that memory, making it available for reuse.

#if a=10 and b=a then both take refrence from the memory address allocated to 10  and when a is again assigned 20 then the variable a takes refrence from the memory address allocated to 20 but as b is unchanged it still takes refrence from madd=30 .After that when a is assigned 10 then due to optimization for integer and string a again takes refrence from the same memory address

#Mutable data types are thos whose values,once stored in memory can be changed or updated using different methods .

#For example if list1=["Ram","Hari","Krishna"] is a list of topper boys and if a new topper boy arrives in the school then list1.append("Prabin") can be used to update the list without creating a new memory address