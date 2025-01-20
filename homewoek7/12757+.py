dic = {'negative': -1, 'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100,'thousand': 1000, 'million': 1000000}
def parse_number(words):
    words = words.split()
    negative = -1 if 'negative' in words else 1
    if 'negative' in words:
        words.remove('negative')
    num = 0
    current = 0
    for word in words:
        if word in ['hundred', 'thousand', 'million']:
            if word == 'hundred':
                current *= dic[word]
            else:
                current *= dic[word]
                num += current
                current = 0
        else:
            current += dic[word]
    num += current
    return negative * num
input_str = input().strip()
print(parse_number(input_str))