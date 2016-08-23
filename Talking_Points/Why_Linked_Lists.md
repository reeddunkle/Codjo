Why would I...linked lists?
----

Totally fair question.

Sometimes you need to design something that performs a task really well, really efficiently.

That's what algorithms are all about. We're accustomed to thinking about them as college courses and [1200 page books](https://en.wikipedia.org/wiki/Introduction_to_Algorithms).

That stuff all arose out of the basic importance of being able to efficiently perform tasks.

Consider the stack. You need a structure, a container, that will let you push new items to the top of this structure. You also need to be able to pop the top item from it. And often you need to be able to peek at the top item (without popping it).

We need that functionality and layout, and it makes sense to spend time thinking about how this is set up (what does "top" mean?) and how handle these actions efficiently.

A queue, on the other hand, lets you add new items to the end of the list, remove the oldest items from the beginning, and probably peek at the beginning item without removing it.

Interview Cake has a good explanation. I'm not going to link to the article until after we finish Problem4 because there are code spoilers, but I recommend poking around their site if you get stuck.

>Like linked lists, arrays also store ordered lists of items, so you usually have a choice of which one to use.

>*Advantages of linked lists:*

>Linked lists have **constant-time insertions and deletions** in any position (you just change some pointers). Arrays require _O(n)_ time to do the same thing, because you'd have to "shift" all the subsequent items over 1 index.

>Linked lists can *continue to expand* as long as there is space on the machine. Arrays (in low-level languages) must have their size specified ahead of time. Even in languages with "dynamic arrays" that automatically resize themselves when they run out of space (like Python, Ruby and JavaScript), the operation to resize a dynamic array has a large cost which can make a single insertion unexpectedly expensive.

>*Disadvantages of linked lists:*

>To access or edit an item in a linked list, you **have to take _O(i)_ time to walk from the head of the list to the _i_ th item** (unless of course you already have a pointer directly to that item). Arrays have _constant-time_ lookups and edits to the _i_ th item.


Those are the basics
----

What if you want to implement something like a queue, but instead of removing the oldest item, it removes the item with the lowest or highest "priority"? This is called a *priority queue*. You can insert an object and key (its priority), and remove the object with the minimum key.

In our daily coding, we're accustomed to having most of these sorts of things taken care of for us. We define arrays and we manipulate them.

If you know how to make your own linked list, though, you could find yourself in an exciting position where you're able to actually _engineer_ a data structure that solves a unique problem. Something that does your specific task extremely well.

In a [blog post](http://jvns.ca/blog/2016/08/16/how-do-you-work-on-something-important/), Julia Evans wrote:

> **I’m not in undergrad anymore**
> I loved being a math/CS undergrad. My professors would give me a series of challenging assignments which were hard but always within my abilities. I improved gradually over time! It was so fun! I was awesome at it! But it is over.

> Being employed is more like -- I have a series of tasks which range from totally trivial to I-don’t-even-know-where-to-start and I need to figure out how to interrogate people and build up my skills so that I can do the hard things. And I need to decide what “good enough” means for the things I do decide to do, and nobody will do it for me, not really.

This may be more than you signed up for, but I think _this is why_ linked lists. It's about adding tools to your tool belt, weapons to your arsenal that you can whip out to save the day and impress the boss, and so that you can design the right tool for the job.

You're an architect, an engineer. Someone says, "I need to be able to do this," and you say, "Then you'll need to design it this way."


Hoping to land your first dev job?
----

Your main competition are fresh-out-of-school undergrads with a shiny CS degree. At my first on-site one of my interviewers pointed this out to me. He asked, "why should we hire you instead?"

What does a CS grad have that I don't? Four years of experience with basic data structures and algorithms.

I'm working hard to narrow that gap.
