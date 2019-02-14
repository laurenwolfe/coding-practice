EPI Notes

Analysis tools:
- Concrete examples: manually solve concrete instances of the problem, 
gain insight into general solution.
- Case analysis: partition the into cases and analyze each.

To Do Priorities:
- Trees
- Locks and Synchronization
- Refresh on C/C++ specifics (pointers, etc)
- Graphs 
- Sort

5 Primitive Types
5.1, 5.7

6 Arrays
6.1, 6.6, 6.11, 6.17

7 Strings 
7.1, 7.2, 7.4

8 Linked Lists 
8.1, 8.2, 8.3 

9 Stacks and Queues 
9.1, 9.7

10 Binary Trees 
10.1, 10.4
- Useful for representing hierarchy
- Structure: either empty or made of a root node together with a left and right binary tree.
    - Node struct is generally composed of: 
        - Data element
        - Pointers to its subtrees
        - Pointer to parent node, possibly (null for root)
    - Ancestor-Descendent: A node is an ancestor of node d if it lies on the search path from 
    the root to d. A node is both its own ancestor and descendent.
    - Depth of Node n = # nodes on search path from root to n (exclusive of n).
    - Height of tree = maximum node depth
    - A level of a tree is comprised of all nodes with same depth. 
    - Types:
        - Full binary tree: all but leaf nodes have 2 children.
            - total nodes = n leaf nodes + n-1 interior nodes
        - Perfect binary tree: all leaves at same depth, and every parent has two children.
            - total nodes = 2^(h+1)-1
        - Complete binary tree: at least h-1 levels filled and leaves are as far left as possible
            - for total nodes = n, height = floor(lg n) 
    - Left skewed tree: no node has a right child (and vice versa for right skewed)
- Important computations:
    - Node traversal
        - O(n) time complexity for recursive solution 
        - O(h) space complexity (determined by function call stack); O(1) if child nodes have pointers 
        to parents.
        - preorder (root, left, right)
        - inorder (left, node, right)
        - postorder (left, right, root)
    
     

11 Heaps 
11.1, 11.4

12 Searching 
12.1, 12.4, 12.8

13 Hash Tables 
13.2, 13.6, 13.3

14 Sorting 
14.1, 14.2

15 Binary Search Trees 
15.1, 15.2, 15.3

16 Recursion 
16.1, 16.2

17 Dynamic Programming 
17.1, 17.2

18 Greedy Algorithms and Invariants 
18.4, 18.6

19 Graphs 
19.1, 19.7

20 Parallel Computing 
20.3, 20.6

21 Design Problems 
21.13, 21.15

22 Language Questions

23 Object-Oriented Design 

24 Common Tools 
