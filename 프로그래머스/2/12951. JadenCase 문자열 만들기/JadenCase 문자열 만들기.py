def solution(s):
    result = ''
    prev_word = ''
    
    for now in s:
        if now == ' ':
            if prev_word != '':
                prev_word_change = prev_word[0].upper() + prev_word[1:].lower()
                result += prev_word_change
                prev_word = ''
            result += now
        else:
            prev_word += now

    if prev_word != '':
        prev_word_change = prev_word[0].upper() + prev_word[1:].lower()
        result += prev_word_change
    
    return result