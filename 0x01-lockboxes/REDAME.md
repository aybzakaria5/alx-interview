# Must Know

For this project, you will need a solid understanding of several key concepts in order to develop a solution that can efficiently determine if all boxes can be opened. Here’s a list of concepts and resources that will be instrumental in tackling this project:

## Concepts Needed:

- **Lists and List Manipulation:**
    - Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
    - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html) (Python Official Documentation)

- **Graph Theory Basics:**
    - Although not explicitly required, knowledge of graph theory (especially concepts related to traversal algorithms like Depth-First Search or Breadth-First Search) can be very helpful in solving this problem, as the boxes and keys can be thought of as nodes and edges in a graph.
    - [Graph Theory](https://www.khanacademy.org/computing/computer-science/algorithms) (Khan Academy)

- **Algorithmic Complexity:**
    - Understanding the time and space complexity of your solution is important, as it can help in writing more efficient algorithms.
    - [Big O Notation](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/) (GeeksforGeeks)

- **Recursion:**
    - Some solutions might require a recursive approach to traverse through the boxes and keys.
    - [Recursion in Python](https://realpython.com/python-recursion/) (Real Python)

- **Queue and Stack:**
    - Knowing how to use queues and stacks is crucial if implementing a breadth-first search (BFS) or depth-first search (DFS) algorithm to traverse through the keys and boxes.
    - [Python Queue and Stack](https://www.geeksforgeeks.org/queue-in-python/) (GeeksforGeeks)

- **Set Operations:**
    - Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.
    - [Python Sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) (Python Official Documentation)

By reviewing these concepts and utilizing these resources, you will be well-equipped to develop an efficient solution for this project, applying both your algorithmic thinking and Python programming skills.

**Additional Resources:**
    - [Mock technical interview](https://www.youtube.com/watch?feature=shared&v=V8DGdPkBBxg) (YouTube)

## Requirements:
   - **General**

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should be documented
    Your code should use the PEP 8 style (version 1.7.x)
    All your files must be executable
 ## Task1
 You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
        There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
