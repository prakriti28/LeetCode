# Queue & Stack

* restrict the processing order

Goals:

* Understand the principle of the processing orders of FIFO and LIFO;
* Implement these two data structures;
* Be familiar with the built-in queue and stack structure;
* Solve basic queue-related problems, especially BFS;
* Solve basic stack-related problems problems;
* Understand how system stack helps you when you solve problems using DFS and other recursion algorithms;

## Queue: First-in-first-out Data Structure

Goals:

* Understand the definition of FIFO and queue;
* Be able to implement a queue by yourself;
* Be familiar with the built-in queue structure;
* Use queue to solve simple problems.

### First-in-first-out Data Structure

### Queue - Implementation

should support two operations: `enqueue` and `dequeue`

```cpp
#include <vector>

using namespace std;

class MyQueue {
    private:
        // store elements
        vector<int> data;
        // a pointer to indicate the start position
        int p_start;
    public:
        MyQueue() {p_start = 0;}
        /** Insert an element into the queue. Return true if the operation is successful. */
        bool enQueue(int x) {
            data.push_back(x);
            return true;
        }
        /** Delete an element from the queue. Return true if the operation is successful. */
        bool deQueue() {
            if (isEmpty()) {
                return false;
            }
            p_start++;
            return true;
        };
        /** Get the front item from the queue. */
        int Front() {
            return data[p_start];
        };
        /** Checks whether the queue is empty or not. */
        bool isEmpty()  {
            return p_start >= data.size();
        }
};
```

## Circular Queue

> Links searched when designing circular queue
>
> * [CppTest](https://cpptest.sourceforge.io/tutorial.html)
> * [cppreference.com - std::vector](https://en.cppreference.com/w/cpp/container/vector)
> * [How to set initial size of std::vector?](https://stackoverflow.com/questions/11457571/how-to-set-initial-size-of-stdvector)

## Queue & BFS

One common application of Breadth-first Search (BFS) is to find the shortest path from the root node to the target node.

using BFS:

* do traversal
* find the shortest path

Typically, it happens in a tree or a graph, or more abstract scenarios.

* nodes: actual node or status
* edges: actual edge or transition

### Template I

```java
/**
 * Return the length of the shortest path between root and target node.
 */
int BFS(Node root, Node target) {
    Queue<Node> queue;  // store all nodes which are waiting to be processed
    int step = 0;       // number of steps neeeded from root to current node
    // initialize
    add root to queue;
    // BFS
    while (queue is not empty) {
        step = step + 1;
        // iterate the nodes which are already in the queue
        int size = queue.size();
        for (int i = 0; i < size; ++i) {
            Node cur = the first node in queue;
            return step if cur is target;
            for (Node next : the neighbors of cur) {
                add next to queue;
            }
            remove the first node from queue;
        }
    }
    return -1;          // there is no path from root to target
}
```

### Template II - never visit a node twice

e.g. in graph with cycle => cause infinite loop

Add a "hast set" to solve this problem. (`Set<Node> visited;`)

```java
/**
 * Return the length of the shortest path between root and target node.
 */
int BFS(Node root, Node target) {
    Queue<Node> queue;  // store all nodes which are waiting to be processed
    Set<Node> visited;  // store all the nodes that we've visited
    int step = 0;       // number of steps neeeded from root to current node
    // initialize
    add root to queue;
    add root to visited;
    // BFS
    while (queue is not empty) {
        step = step + 1;
        // iterate the nodes which are already in the queue
        int size = queue.size();
        for (int i = 0; i < size; ++i) {
            Node cur = the first node in queue;
            return step if cur is target;
            for (Node next : the neighbors of cur) {
                if (next is not in used) {
                    add next to queue;
                    add next to visited;
                }
                remove the first node from queue;
            }
        }
    }
    return -1;          // there is no path from root to target
}
```

> There are some cases where one does not need keep the visited hash set:
>
> * You are absolutely sure there is no cycle, for example, in tree traversal;
> * You do want to add the node to the queue multiple times.

## Stack: Last-in-first-out Data Structure

Goals:

1. Understand the `definition` of LIFO and Stack;
2. Be able to `implement` a stack using dynamic array;
3. Be familiar with the `built-in stack structure`;
4. Be able to use a stack to solve problems.

### Last-in-first-out Data Structure

should support two operations: `push` and `pop`

```cpp
#include <iostream>

class MyStack {
    private:
        vector<int> data;               // store elements
    public:
        /** Insert an element into the stack. */
        void push(int x) {
            data.push_back(x);
        }
        /** Checks whether the queue is empty or not. */
        bool isEmpty() {
            return data.empty();
        }
        /** Get the top item from the queue. */
        int top() {
            return data.back();
        }
        /** Delete an element from the queue. Return true if the operation is successful. */
        bool pop() {
            if (isEmpty()) {
                return false;
            }
            data.pop_back();
            return true;
        }
};

int main() {
    MyStack s;
    s.push(1);
    s.push(2);
    s.push(3);
    for (int i = 0; i < 4; ++i) {
        if (!s.isEmpty()) {
            cout << s.top() << endl;
        }
        cout << (s.pop() ? "true" : "false") << endl;
    }
}
```

### DFS - Template I - Recursion

There are two ways to implement DFS. The first one is to do recursion which you might already be familiar with. Here we provide a template as reference:

```java
/*
 * Return true if there is a path from cur to target.
 */
boolean DFS(Node cur, Node target, Set<Node> visited) {
    return true if cur is target;
    for (next : each neighbor of cur) {
        if (next is not in visited) {
            add next to visted;
            return true if DFS(next, target, visited) == true;
        }
    }
    return false;
}
```

It seems like we don't have to use any stacks when we implement DFS recursively. But actually, we are using the implicit stack provided by the system, also known as the [Call Stack](https://en.wikipedia.org/wiki/Call_stack).

### DFS - Template II

The advantage of the recursion solution is that it is easier to implement. However, there is a huge disadvantage: if the depth of recursion is too high, you will suffer from `stack overflow`. In that case, you might want to use BFS instead or implement DFS using an explicit stack.

Here we provide a template using an explicit stack:

```java
/*
 * Return true if there is a path from cur to target.
 */
boolean DFS(int root, int target) {
    Set<Node> visited;
    Stack<Node> stack;
    add root to stack;
    while (s is not empty) {
        Node cur = the top element in stack;
        remove the cur from the stack;
        return true if cur is target;
        for (Node next : the neighbors of cur) {
            if (next is not in visited) {
                add next to visited;
                add next to stack;
            }
        }
    }
    return false;
}
```

The logic is exactly the same with the recursion solution. But we use `while` loop and `stack` to simulate the `system call stack` during recursion. Running through several examples manually will definitely help you understand it better.
