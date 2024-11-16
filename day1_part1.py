
import re

def extract_number():
    f = open("text1.txt", "r")
    text = f.read()
    lines = text.split('\n')
    accumulated = 0
    for line in lines:
        x = re.findall(r'\d+', line)
        y = []
        for i in x:
            y += i
        for index, i in enumerate(y):
            y[index] = int(i)

        res = int(str(f"{y[0]}{y[-1]}"))
        accumulated += res
    print (f"accumulated {accumulated}")

def main():
    extract_number()

if __name__ == "__main__":
    main()
