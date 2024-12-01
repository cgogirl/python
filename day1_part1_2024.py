def parce_input(input: str) -> list[list[str], list[str]]:
    lines = input.split('\n')
    table1 = []
    table2 = []
    for line in lines:
        res = line.split('   ')
        table1.append(int(res[0]))
        table2.append(int(res[1]))
    return [table1, table2]

def find_distance(table1: list[int], table2: list[int]) -> int:
    return abs(min(table1) - min(table2))
        
def pair_up(table1: list[int], table2: list[int]) -> int:
    acc = 0
    while len(table1) > 0:
        acc += find_distance(table1, table2)
        table1.pop(table1.index(min(table1)))
        table2.pop(table2.index(min(table2)))
    return acc

def main():
    f = open("input_day1_2024.txt", "r")
    text = f.read()
    parced = parce_input(text)
    result = pair_up(*parced)
    print(result)

if __name__ == "__main__":
    main()