board = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]   # => False

valid = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def main():
    print(valid_solution())


def valid_solution():
    if check_rows() and check_columns() and check_squares():
        return True
    else: 
        return False
    

def check_rows():
    for row in board:
        if sorted(row) != valid:
            return False
    return True


def check_columns():
    for column in zip(*board):
        if sorted(column) != valid:
            return False
    return True


def check_squares():
    summs = []
    for x in [0, 3, 6]:                
        for y in [0, 3, 6]:
            #making list of each square's elements
            square = board[x][y:y+3] + board[x+1][y:y+3] + board[x+2][y:y+3]
            #remember sum in square
            summs.append(sum(square))
        if sorted(square) != valid:
            return False                
        square.clear()
        
    #if all summs are the same
    if len(set(summs)) != 1:
        return False
    
    return True


if __name__ == "__main__":
    main()