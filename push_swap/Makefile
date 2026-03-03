NAME = push_swap
SRCS = push_swap.c \
		stack/stack_init.c
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
