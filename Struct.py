# String Changes

def StringChanges(s):
    result = []
    i = 0
    while i < len(s):
        if s[i] == 'M':
            if len(result) > 0:  # Ensure there is a previous character to duplicate
                result.append(result[-1])  # Duplicate the previous character
            i += 1  # Move past 'M'
        elif s[i] == 'N':
            i += 2  # Skip the next character
        else:
            result.append(s[i])  # Append the current character
            i += 1  # Move to the next character

    return ''.join(result)
print(StringChanges("MrtyNNgMM"))
print(StringChanges("oMoMkkNrrN"))
print(StringChanges("abcNdgM"))
