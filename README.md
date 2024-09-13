# fun-project-fill-null

This is a fun project for performance improvement.

The program is finding the pairs in a list of integers, to make the sum of the pair equals to a target number.

For instance,

my_list = [5, -3, 9, 0, 1, 7, 7, 3, 8, 2, 1, -5, 11, 4, 6, 8, -2]
target = 10

The result would be:

[(4, 6), (7, 3), (8, 2), (9, 1), (2, 8)] 

At first glance, the solution might seem achievable through nested loops, as demonstrated in the find_pairs_slow() method, which has a time complexity of (O(n^2)).

However, the time complexity can be reduced to (O(n)) by using a hash set to track the elements seen, as shown in the find_pairs() method.

Feel free to try the program yourself to observe the performance difference.