Depth-First Search (DFS)
----

In DFS, you visit a node `a` and then iterate through each of `a`'s neighbors. When visiting a node `b` that is a neighbor of `a`, you visit all of `b`'s neighbors before going on to `a`'s other neighbors. That is, `a` exhaustively searches `b`'s branch before any of its other neighbors.

Forms of tree traversal can be a form of DFS. They key difference is that when implementing DFS for a graph, you've got to check whether a node has been visited. If you don't you'll likely get stuck in an infinite loop.

Here is DFS pseudocode:

```python
def search(root):
    if not root:
        return None

    root.visited = True

    for node in root.adjacent:
        if not node.visited:
            search(node)
```

Note the use of a stack -- the call stack in this case. The main thing that distinguishes DFS from BFS (breadth-first search) is its use of a stack. BFS uses a queue. The rest of the logic flows from this.

The Problem
----

### Connected Cells in a Grid


Consider a matrix with `n` rows and `m` columns, where each cell contains either a `0` or a `1`. Any cell containing a `1` is called a _filled_ cell. Two cells are said to be _connected_ if they are adjacent to each other horizontally, vertically, or diagonally, provided that the location exists in the matrix.

If one or more _filled_ cells are _connected_, they form a _region_. Note that each cell in a region is connected to at least one other cell in the region but is not necessarily directly connected to all of the cells in the region.

**Task**
Given an _n x m_ matrix, find and print the number of cells in the largest _region_ in the matrix. Note that there may be more than one region in the matrix.

**Input Format**
The first line contains an integer, `n`, denoting the number of rows in the matrix.
The second line contains an integer, `m`, denoting the number of columns in the matrix.
Each line `i` of the `n` subsequent lines contains `m` space-separated integers describing the respective values filling each row in the matrix.

**Constraints**
0 < n,m < 10

**Output Format**
Print the number of cells in the largest _region_ in the given matrix.

**Sample Input**

```
4
4
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0
```

**Sample Output**

```
5
```

**Explanation**

The diagram below depicts two regions of the matrix; for each region, the component cells forming the region are marked with an `X`:

```
X X 0 0     1 1 0 0
0 X X 0     0 1 1 0
0 0 X 0     0 0 1 0
1 0 0 0     X 0 0 0
```

The first region has five cells and the second region has one cell. Because we want to print the number of cells in the largest region of the matrix, we print `5`.

Tests
----

This is taken from [this](https://www.hackerrank.com/challenges/connected-cell-in-a-grid) HackerRank problem. I'd like you to use HR's tests.

Because HR's I/O system takes a little getting used to, here it the pattern that I use for almost all of my HR problems:

```python
def my_function(x):
    return answer

if __name__ == '__main__':
    first_num = int(input())

    for _ in range(first_num):
        n = int(input())
        answer = my_function(n)
        print(answer)
```

The key points are:

- Each `input()` call reads one line of the input
- `input` reads in a string, so you need to convert it to an `int`
- You `print` the answer

Let me know if you have questions about this. I don't want HR's interface to slow you down learning about more interesting things like DFS.

Best of luck! Let me know if you have questions.

Also! We've got a new mentor on board, [Adrien Lamarque](https://github.com/lamarqua)! Other than being a really fine fellow in general, he also has expertise in a handful of languages beyond Python: C, C++, Rust as well as a few other functional languages (Haskell, Racket and some others). So, if you'd like to do this week's problem in a different language, send @adrien.lamarque a message on Slack and chat with him.
