def makeAnagram(a, b):
    # Write your code here
    chars = {}
    # Build up character frequency map
    for char_a in a:
        if char_a in chars:
            chars[char_a] += 1
        else:
            chars[char_a] = 1
    # Subtract frequency map for b; chars with equal frequency will end up being 0
    for char_b in b:
        if char_b in chars:
            chars[char_b] -= 1
        else:
            chars[char_b] = -1

    return sum(abs(count) for char, count in chars.items())



print(makeAnagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke"))  # Should be 30
