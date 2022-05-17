from Stack import Stack


def is_balanced(line: str):
    unknown_list = list(line)
    balanced = False
    if len(unknown_list) % 2 == 0:
        m_stack = Stack()
        for symbol in unknown_list:
            if symbol == '(' or symbol == '{' or symbol == '[':
                m_stack.push(symbol)
            elif symbol == ')' or symbol == '}' or symbol == ']':
                if symbol_dict[symbol] == m_stack.pop():
                    balanced = True
                    continue
                else:
                    balanced = False
                    break
    return balanced


if __name__ == '__main__':
    symbol_dict = {')': '(', '}': '{', ']': '['}
    balanced_line = '(((([{}]))))'
    balanced_line2 = '[([])((([[[]]])))]{()}'
    balanced_line3 = '{{[()]}}'
    unbalanced_line = '}{}'
    unbalanced_line2 = '{{[(])]}}'
    unbalanced_line3 = '[[{())}]'

    if is_balanced(unbalanced_line2):
        print('Сбалансированно')
    else:
        print('Несбалансированно')
