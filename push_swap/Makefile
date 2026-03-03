NAME = push_swap.a
SRC = push_swap.c
OBJ = $(SRC:.c=.o)

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
