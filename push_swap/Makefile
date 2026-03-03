NAME = push_swap.a
SRCS = push_swap.c \
		stack/stack_init.c
OBJ = $(SRCS:.c=.o)

CC = cc 
CFLAGS = -Wall -Wextra -Werror -I.
$(NAME): $(OBJ)
	ar rcs $(NAME) $(OBJ)

all: $(NAME)

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
