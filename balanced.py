from Stack import Stack

if __name__ == '__main__':
    symbol_dict = {')': '(', '}': '{', ']': '['}
    balanced_line = '(((([{}]))))'
    balanced_line2 = '[([])((([[[]]])))]{()}'
    balanced_line3 = '{{[()]}}'
    unbalanced_line = '}{}'
    unbalanced_line2 = '{{[(])]}}'
    unbalanced_line3 = '[[{())}]'

    unknown_list = list(balanced_line2)
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
                    break

    if balanced:
        print('Сбалансированно')
    else:
        print('Несбалансированно')
