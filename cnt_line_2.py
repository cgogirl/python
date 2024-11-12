import re

test_text = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

def extract_number():
    f = open("text1.txt", "r")
    text = f.read()
    lines = text.split('\n')
    # lines = test_text.split('\n')
    accumulated = 0
    str_to_num = {'one': '1', 'two': '2', 'three': '3', 'four': 4, 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
                
    for line in lines:
        x = re.findall(r'\d+|(?:' + '|'.join(str_to_num.keys()) + r')', line)
        print('x ', x)
        for k in str_to_num.keys():
            for i, n in enumerate(x):
                if k == n:
                    x[i] = str(str_to_num[k])
        y = []
        for i in x:
            y += i
        for index, i in enumerate(y):
            y[index] = int(i)

        res = int(str(f"{y[0]}{y[-1]}"))
        print('res ', res)
        accumulated += res
    print (f"accumulated {accumulated}")

def main():
    extract_number()

if __name__ == "__main__":
    main()