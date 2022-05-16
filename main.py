from Stack import Stack

if __name__ == '__main__':
    m_stack = Stack()
    print(m_stack.isEmpty())
    m_stack.push(4)
    m_stack.push(7)
    m_stack.push(8)
    print(m_stack.isEmpty())

    print(m_stack.size())
    print(m_stack.pop())
    print(m_stack.pop())
    print(m_stack.pop())
    print(m_stack.pop())

    m_stack.push(123)
    m_stack.push(4)
    m_stack.push(7)
    m_stack.push(8)

    print(m_stack.peek())
