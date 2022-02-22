
def main():
    amount = int(input("Enter Amount:"))
    notes = [1000, 500, 100, 50, 10, 50, 2, 1]
    notes_count = {}
    for i in notes:
        if amount >= i:
            notes_count.__setitem__(i, 0)
            notes_count[i] = amount//i
            amount -= notes_count[i] * i
            if amount == 0:
                break
    print(notes_count)


if __name__ == "__main__":
    main()


