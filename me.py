from random import choice


def main():
    head()


def head():
    while True:
        flip = choice(["head", "tail"])
        if flip == "head":
            print(flip)
            return
        else:
            print("try again")
        break


main()
