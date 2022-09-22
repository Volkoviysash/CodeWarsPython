def check():
    password = ""
    for c in password:
        if c.isalpha() or c.isdigit():
            print(True)
    print(False)
    
if __name__ == "__mian__":
    main()
