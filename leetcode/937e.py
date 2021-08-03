class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        def is_digits(string):
            return all(char in '0123456789' for char in string)

        if not logs:
            return logs
        for log in logs:
            identifier, *words = log.split(' ')
            if all(is_digits(word) for word in words):
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        def sort_letter_logs(log):
            identifier, *words = log.split(' ')
            return tuple(words), identifier

        letter_logs = sorted(letter_logs, key=sort_letter_logs)

        return letter_logs + digit_logs
