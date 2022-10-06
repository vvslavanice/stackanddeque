brackets= "{(){[]()}}"
stack = []

open_brackets = ["{", "(", "[", "<"]
closed_brackets = ["}", ")", "]", ">"]


def stack_func(brackets):
    for i in brackets:
        if i in open_brackets:
            stack.append(i)
            continue
        if i in closed_brackets:
            if stack:
                opened = stack.pop()
                if closed_brackets.index(i) == open_brackets.index(opened):
                    continue
            return False
    if stack:
        return False
    return True


if __name__ == '__main__':
    print(stack_func(brackets))