# iterative solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q = [""]

        def is_valid(seq):
            level = 0
            while seq:
                head = seq[0]
                if head == '(':
                    level += 1
                elif head == ')':
                    if level == 0:
                        # There is no more ( to match
                        return False
                    level -= 1
                seq = seq[1:]
            return level == 0

        while q:
            if len(q[0]) >= n * 2:
                # Every item in the queue must be at least 2n in length
                break
            q_head = q.pop(0)
            for char in ['(', ')']:
                new_head = q_head + char
                q.append(new_head)

        return [x for x in q if is_valid(x)]
