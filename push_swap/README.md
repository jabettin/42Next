*This project has been created as a part of the 42 curriculum by: jabettin*

## Description ##
>push_swap is a sorting algorithm project where the goal is to sort a stack of integers using a limited set of operations, with the lowest possible number of moves. You are given two stacks — **a** and **b** — and a set of operations to manipulate them. Stack a starts with the input integers, stack b starts empty. The program must output the shortest sequence of operations needed to sort stack a in ascending order.

push_swap at its core can be summarized as follows: the program first parses and validates the input, then depending on the size of the input, applies the most appropriate sorting algorithm. For 2 elements it uses a single swap if needed. For 3 elements it uses a hardcoded decision tree covering all 6 possible permutations. For larger inputs it uses **radix sort** — first normalizing the values to ranked indices `0` to `n-1`, then sorting bit by bit from the least significant bit to the most significant, using `pb`, `ra`, and `pa` to separate and reorder elements each pass.

This push_swap does **NOT** include the bonus checker program.

## Instructions ##
>Because push_swap makes use of a Makefile, as required by the subject file. The first step is to write `make` in your terminal.

This will compile the program with the three standard flags: `-Wall -Wextra -Werror` and produce the executable `push_swap`. It can then be run as follows:
```
./push_swap 3 2 1
```
Or with a quoted string of numbers:
```
./push_swap "3 2 1"
```
The program will print the sequence of operations needed to sort the input, one per line.

To verify correctness using the provided checker binary:
```
ARG="4 67 3 87 23"; ./push_swap $ARG | ./checker_OS $ARG
```

To get rid of the `.o` files after having used `make`, you can write: `make clean` — this removes all `.o` files but leaves the **push_swap** binary.

If you also want to remove the binary, use: `make fclean`. **make fclean will also get rid of any `.o` files.**

To recompile from scratch: `make re`.

## Resources ##
For this project I used information from:
- [Radix Sort — Wikipedia](https://en.wikipedia.org/wiki/Radix_sort)
- [push_swap — Medium overview by various 42 students](https://medium.com/search?q=push_swap)
- [Sorting Algorithms — GeeksforGeeks](https://www.geeksforgeeks.org/sorting-algorithms/)

As well as AI (Claude) to help debug parsing issues, explain bitwise operations used in radix sort, trace through algorithm execution step by step, and explain the logic of normalize and radix sort in plain language.

## Code snippet ##

<ins>Makefile</ins>
```make
NAME = push_swap
SRCS = push_swap.c \
		stack/stack_init.c \
		parsing/atoi_strict.c \
		parsing/is_duplicate.c \
		parsing/parse_args.c \
		operations/sa.c \
		operations/pb.c \
		operations/pa.c \
		operations/ra.c \
		operations/rb.c \
		operations/rra.c \
		sorting/normalize.c \
		sorting/sort_three.c \
		sorting/sort_two.c \
		sorting/radix_sort.c
OBJ = $(SRCS:.c=.o)

CC = cc
CFLAGS = -Wall -Wextra -Werror -I.

$(NAME): $(OBJ)
	$(CC) $(CFLAGS) -o $(NAME) $(OBJ)
	chmod +x $(NAME)

all: $(NAME)

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
```

<ins>normalize</ins>
```c
void	normalize(t_node *a)
{
	t_node	*current;
	t_node	*scanner;
	int		rank;

	current = a;
	while (current != NULL)
	{
		rank = 0;
		scanner = a;
		while (scanner != NULL)
		{
			if (current->value > scanner->value)
				rank++;
			scanner = scanner->next;
		}
		current->value = rank;
		current = current->next;
	}
}
```

## Flow of push_swap ##

You call:
`./push_swap 3 1 2`

1. **Parsing**

* `main` receives `argc = 4`, `argv = ["./push_swap", "3", "1", "2"]`
* `parse_args` iterates through argv from index 1
* Each argument is validated with `atoi_strict` (checks it is a valid integer within INT limits)
* Duplicate check is performed with `is_duplicate`
* Each valid value is inserted into stack a via `create_node` and `add_back`
* Stack a after parsing: `3 → 1 → 2`

---

2. **Sorted check**

* `is_sorted` traverses the stack comparing each node to the next
* `3 > 1` → returns `0` (not sorted), execution continues

---

3. **Size check**

* `stack_size` counts the nodes → returns `3`
* Size is `3` → `sort_three` is called

---

4. **sort_three**

* Reads `top = 3`, `mid = 1`, `bot = 2`
* Checks all 6 possible orderings via if/else chain
* Matches `mid < bot && bot < top` (1 < 2 < 3) → calls `ra`

---

5. **ra**

* Saves the first node (3), advances head to node (1)
* Traverses to last node (2), appends node (3) to end
* Stack a becomes: `1 → 2 → 3`
* Writes `"ra\n"` to stdout

---

6. **Cleanup**

* `free_stack(&a)` frees all nodes in stack a
* `free_stack(&b)` — b is NULL, does nothing
* Program returns `0`

**Final output:**
```
ra
```

## Flow of radix sort (for inputs larger than 3) ##

For input `4 3 2 1`:

1. **normalize** — replaces each value with its rank (position in sorted order):
   - `4 → 3`, `3 → 2`, `2 → 1`, `1 → 0`
   - Stack becomes: `3 → 2 → 1 → 0`

2. **radix_sort** — calculates how many bit passes are needed (`tbits`), then for each bit position from LSB to MSB:
   - Iterates through all elements in stack a
   - If the current bit of the top element is `0` → `pb` (push to b)
   - If the current bit is `1` → `ra` (rotate to back of a)
   - After all elements processed → `pa` all elements from b back to a
   - Repeat for next bit

   After all passes, stack a is sorted in ascending order.

## Key concepts of push_swap ##

* **stack a / stack b**: Two linked lists. Stack a holds the input, stack b is used as scratch space during sorting.
* **normalize**: Converts arbitrary integers to contiguous ranks `0` to `n-1` based on relative order — makes radix sort viable regardless of actual input values.
* **radix sort**: Sorts by examining one bit at a time, from least to most significant. Elements with bit `0` go to b, elements with bit `1` rotate in a. After each pass the relative order improves until fully sorted.
* **bit shifting (`>> bit`)**: Moves the target bit down to the rightmost position so it can be read.
* **masking (`& 1`)**: Isolates only the rightmost bit, giving a clean `0` or `1` to branch on.
* **sort_three**: Handles 3-element stacks with a hardcoded decision tree — all 6 permutations are covered explicitly with the minimum number of operations.
* **`is_sorted`**: Early exit — if the input is already sorted, nothing is printed and the program exits immediately.
