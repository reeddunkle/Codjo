# Linked Lists

A lot of algorithms expect us to know how to use different data structures, but there's generally less focus on how to actually implement them.

> A linked list is a data structure that represents a sequence of nodes. In a **singly linked list**, each node points to the next node in the linked list. A **doubly linked list** gives each node pointers to both the next node and the previous node. <br/> — Gayle Laakmann McDowell

You can see visualizations of different kinds of linked lists [here](http://visualgo.net/list). (Note: The site seems a bit buggy right now.)

A `list` in Python lets you access an element at a particular index in constant time (`O(1)`). A linked list, however, forces you to start at the first node, called the `head`, and traverse through the list one node at a time until you arrive at the "index" you want.

So if you want to find the Kth element in the list, you'll have to iterate through K elements.

On the other hand, if you set up a doubly linked list, you can add and remove items from the _beginning_ of the list in constant time, where a traditional `list` requires `O(N)`.

Linked lists are used to make stacks, queues and deques.

In this exercise, you're going to implement a singly linked list.

<img src="http://i.imgur.com/tVgxoLN.png" />

The Node
----

Don't let this idea intimidate you. This is just a Python class named `Node`. You could name it anything.

Every time you want to add a new element to your linked list, you're going to create a new instance of this class, and you'll use its attributes to connect it to the next node in line.

You can make this prettier with methods like `__repr__`, but at its simplest, the `Node` class for a singly linked list only needs two attributes:

- `data`, the value stored in the node
- `next_node`, a pointer to the next node (this is what "links" them)

**Note:** There are lots of other names for these attributes. I'm only forcing you to use these names for the tests.

The Linked List
----

This will feel similar to Python's built-in `list`. You'll need to implement the following methods:

- `append`
- `__len__`
- `__getitem__`
- `pop` *
- `__delitem__` *

(*Extra Challenge)

<img src="http://i.imgur.com/tVgxoLN.png" />

When you first make the linked list, let's say you start off with just a node storing 42:

```python
linked_list = LinkedList(42)
```

The head of your linked list is a 42-node, which is how I'm going to describe nodes in the list from here on out.

Next, you run:

```python
linked_list.append(9)
```

### `append`

`append` first creates a 9-node. Then it sets the 9-node's "next_node" to be the previous head (the 42-node), making this 9-node the new head, and leaving the 42-node as the tail.

The tail's `next_node` will always equal `None`. (In other languages you'll see `null`, and on a whiteboard it's sometimes written as `Ø`.)

To traverse the linked list you have to start at the head. Each node points to each `next_node` in turn, until it arrives at `None`.

Next, you `append` a 3-node, and then a 23-node, each one becoming the new head in turn.

This works in constant time `O(1)`.

### `__len__`

You could name this method `size`, or `length`, or `len`. I'm going to have you name it `__len__` to follow Python's built-in methods.

In case you aren't aware, when you call `len([0, 1, 2])`, `len` in turn actually calls `list`'s class method `__len__`:

```
In [1]: [0, 1, 2].__len__()
Out[1]: 3
```

So by naming our method `__len__`, we'll be able to call `len()` on our linked list.

You can implement this two ways. The first way iterates over the list, starting at the head, ending at the tail, counting each node along the way.

I'd like you to implement it this way in order to practice working with your node's methods.

This requires `O(N)` time where _N_ is the length of the list.

The second way is to add some kind of `size` attribute which is updated everytime you `append`, `pop`, or `__del__` a node. It keeps track of the length as you work with the structure, and lets you access its length in constant time.

Do this for practice if you have time.

### `__getitem__`

`__getitem__` takes an "index" number and returns the data stored in the node at that index. Another way to think of this, is that you start at the head and count from 0 as you traverse the linked list. Stop when you reach the number.

Using the example in the photo:

```
linked_list.__getitem__(2)  # => 9
```

You should raise an `IndexError` if the index is out of range of the nodes in the linked list.

This requires you to iterate through the nodes one at a time.

### `pop`

When you call `pop()`, it pops off the head of the list. In the example in the photo, it pops off the 23-node, returns it, and then makes the 3-node the new head, effectively disconnecting the 23-node.

This works in constant time `O(1)`.

### `__delitem__`

`__delitem__` takes an index number and removes that node from the list. It connects the node before it to the node after it, disconnecting it from the list.

You should raise an `IndexError` if the index is out of range.

This requires you to iterate through the nodes one at a time.

Extra Challenges
----

To get `pop` and `__delitem__` working, you should open up the test script. One at a time, comment out the lines that starts with `@unittest.skip` before each test function.

After you comment one out, write code and run the test until you get that one passing. Then comment out the next one.

If you want the practice, create a nice `__repr__` for the list:

```
In [9]: a = LinkedList()

In [10]: a
Out[10]: [*None]

In [11]: a.append(5)

In [12]: a
Out[12]: [*5]

In [13]: a.append(3)

In [14]: a
Out[14]: [*3] --> [5]

In [15]: a.append(10)

In [16]: a
Out[16]: [*10] --> [3] --> [5]
```