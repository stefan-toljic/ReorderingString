"""
5. Reordering string

Ask user to enter the sentence with multiple words. If the string contains more than 4 words write it in backwards order. If string contains up to 4 words print out only the last word.

Examples:

Today is a very nice day -> day nice very a is today
I am sick -> sick

Hints: lists, split(), join()
"""

user_input = input("Please enter a multi-word sentence:\n\t")

split_input = user_input.split(" ")

list_size = len(split_input)

def more_than_4(list_size):
    reverse_order = []

    while list_size > 0:
        list_size -= 1
        reverse_order.append(list_size)

    reverse_input = [split_input[i] for i in reverse_order]

    output = " ".join(reverse_input)

    print(f"\n- {output}")

list_size = len(split_input)

if list_size > 4:
    more_than_4(list_size)
else:
    print("\n- {}".format(split_input[list_size - 1]))

# ----------------------------------------------------


