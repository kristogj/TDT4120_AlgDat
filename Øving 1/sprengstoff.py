from sys import stdin

#TNT
class Record:
    value = None
    next = None

    def __init__(self, value):
        self.value = value
        self.next = None


def search(record):
    #SKRIV DIN KODE HER
    biggest = record.value
    done = False

    while not done:
        if record.next == None:
            done = True
        if record.value > biggest:
            biggest = record.value
        record = record.next

    return biggest


def main():
    # reading from stdin and creating a linked list
    first = None
    last = None
    for line in stdin:
        penultimate = last #nest siste
        last = Record(int(line))
        if first is None:
            first = last
        else:
            penultimate.next = last

    # searching and printing out the result
    print(search(first))


if __name__ == "__main__":
    main()


