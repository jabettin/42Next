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
		sorting/radix.c
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
