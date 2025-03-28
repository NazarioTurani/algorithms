class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        """Добавить элемент в стек."""
        return self.__items.append(item)

    def pop(self):
        """Взять элемент из стека."""
        return self.__items.pop()

    def peek(self):
        """Посмотреть последний элемент из изъятия."""
        if self.is_empty():
            return None
        else:
            return self.__items[-1]

    def size(self):
        """Вернуть размер стека."""
        return len(self.__items)

    def is_empty(self):
        """Проверить пустой ли список."""
        return len(self.__items) == 0


def isValid(s: str) -> bool:
    "Возвращает валидность скобочной последовательности."
    if not s or s[0] in ']})':
        return False

    data = list(s)
    stack_brackets = Stack()
    for i in data:
        if i in '[{(':
            stack_brackets.push(i)
        elif i == ']':
            if stack_brackets.peek() != '[':
                return False
            else:
                stack_brackets.pop()
        elif i == '}':
            if stack_brackets.peek() != '{':
                return False
            else:
                stack_brackets.pop()
        elif i == ')':
            if stack_brackets.peek() != '(':
                return False
            else:
                stack_brackets.pop()
    return stack_brackets.is_empty()


print(isValid("(("))
