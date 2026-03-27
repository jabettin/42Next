NAME = push_swap
LIBFT = libft/libft.a
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

all: $(NAME)

$(LIBFT):
	$(MAKE) -C libft

$(NAME): $(LIBFT) $(OBJ)
	$(CC) $(CFLAGS) -o $(NAME) $(OBJ) $(LIBFT)
	chmod +x $(NAME)

clean:
	rm -f $(OBJ)
	$(MAKE) -C libft clean

fclean: clean
	rm -f $(NAME)
	$(MAKE) -C libft fclean

re: fclean all

.PHONY: all clean fclean re
