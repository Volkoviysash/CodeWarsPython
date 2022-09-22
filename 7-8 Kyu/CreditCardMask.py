#function maskify, which changes all but the last four characters into '#'.

def main():
    cc = input("smth: ")
    print(coding(cc))


def coding(cc):
    stroutpt = ""
    if len(cc) <= 4:
        return(cc)

    for _ in range(len(cc)-4):
        stroutpt += "#"

    stroutpt += cc[len(cc)-4:len(cc)]
    return stroutpt


if __name__ == "__main__":
    main()
