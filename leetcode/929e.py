class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        answer = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            if '+' in local:
                local = local[:local.index('+')]
            canonical = local + '@' + domain
            answer.add(canonical)
        return len(answer)
