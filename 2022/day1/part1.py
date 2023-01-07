def main():
    elf_foods = open('in1.txt', 'r').read().split('\n\n')
    print(max(list(map(lambda elf: sum(map(int, elf.split('\n'))) , elf_foods))))

main()