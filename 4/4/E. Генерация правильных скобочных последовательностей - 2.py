def generate_brackets(n, cur_str='', stack=[]):
    if len(cur_str) == n:
        if not stack:
            print(cur_str)
        return

    if len(stack) < n:
        generate_brackets(n, cur_str + '(', stack + ['('])
    if len(stack) < n:
        generate_brackets(n, cur_str + '[', stack + ['['])
    if stack and stack[-1] == '[':
        new_stack = stack[:-1]
        generate_brackets(n, cur_str + ']', new_stack)
    if stack and stack[-1] == '(':
        new_stack = stack[:-1]
        generate_brackets(n, cur_str + ')', new_stack)





n = int(input())
generate_brackets(n)
