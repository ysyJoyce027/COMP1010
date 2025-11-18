Board_2D=[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
def board_reset():
    '''
    function does: reset all the squares in the 4*4 chessboard to 0
    '''
    for row in range(0,4):
        for col in range(0,4):
            Board_2D[row][col]=0

def find_next_location(starting_position):
    '''
    input: starting position
    output: (current_row,col): available position is (current_row,col)  
            -1: no available position, a dead end
    function does: search the first available place from specified column to last column in current row from left to right 
    '''
    current_row,current_col=starting_position
    for col in range(current_col,4):
        if Board_2D[current_row][col]==0:
            return (current_row,col)
    return -1 #no available position, dead end

def place_queen(queen_number,starting_position=None):
    '''
    input: queen_number: the number of queen
           starting_position: from this specified place to search
    output: -1: fail to place the queen in this position
            (row,col): place the queen in this position
    function does: find a position to place the queen and update the conflict positions
    '''
    if starting_position == None:
        starting_position=(queen_number-1,0)
    
    position=find_next_location(starting_position)
    if position==-1:
        return -1
    else:
        row,col=position
        Board_2D[row][col]="Q"+str(queen_number)
        set_conflict_locations(queen_number,row,col)
        return (row,col)
    
def set_conflict_locations(queen_number,queen_row,queen_col):
    '''
    input: queen_number: the number of queen
           queen_row: queen located in this row
           queen_col: queen located in this column
    function does: declare the rules that becomes "conflict position", which is horizontally, vertically, and diagonally for any number of places to queen
    '''
    for row in range(0,4):
        if Board_2D[row][queen_col]==0:
            Board_2D[row][queen_col]=queen_number
    for col in range(0,4):
        if Board_2D[queen_row][col]==0:
            Board_2D[queen_row][col]=queen_number
    
    r,c=queen_row-1,queen_col-1
    while r>=0 and c>=0: #the upper left corner of the queen
        if Board_2D[r][c]==0:
            Board_2D[r][c]=queen_number
        r=r-1
        c=c-1
    r,c=queen_row+1,queen_col+1
    while r<4 and c<4: #the lower right corner of the queen
        if Board_2D[r][c]==0:
            Board_2D[r][c]=queen_number
        r=r+1
        c=c+1
    r,c=queen_row-1,queen_col+1
    while r>=0 and c<4:
        if Board_2D[r][c]==0:
            Board_2D[r][c]=queen_number
        r=r-1
        c=c+1
    r,c=queen_row+1,queen_col-1
    while r<4 and c>=0:
        if Board_2D[r][c]==0:
            Board_2D[r][c]=queen_number
        r=r+1
        c=c-1

def dead_end():
    '''
    function does: reset the chessboard after dead end
    '''
    board_reset()

def main():
    '''
    function does: try every possible starting position for Q1 and find the solotions
    '''
    end_times = 1
    print("Initial board setting:")
    for row in range(0,4):
        print(" 0 0 0 0")
    print()

    for Q1_col in range(0,4):
        board_reset()
        if end_times==1:
            end=str("first")
        if end_times==2:
            end=str("second")
        if end_times==3:
            end=str("third")

        Q1_position=place_queen(1,(0,Q1_col))
        if Q1_position==-1:
            end_times=end_times+1
            continue # no available position for Q1, try next column
        print("After placing first Queen:")
        for row in range(0,4):
            line=""
            for col in range(0,4):
                element=Board_2D[row][col]
                line=line+" "+str(element)
            print(line)
        print()

        Q2_position=place_queen(2)
        if Q2_position==-1:
            print("After",end,"dead end")
            for row in range(0,4):
                line=""
                for col in range(0,4):
                    element=Board_2D[row][col]
                    line=line+" "+str(element)
                print(line)
            print()
            end_times=end_times+1
            continue
        print("After placing second Queen:")
        for row in range(0,4):
            line=""
            for col in range(0,4):
                element=Board_2D[row][col]
                line=line+" "+str(element)
            print(line)
        print()

        Q3_position=place_queen(3)
        if Q3_position==-1:
            print("After",end,"dead end")
            for row in range(0,4):
                line=""
                for col in range(0,4):
                    element=Board_2D[row][col]
                    line=line+" "+str(element)
                print(line)
            print()
            end_times=end_times+1
            continue
        print("After placing third Queen:")
        for row in range(0,4):
            line=""
            for col in range(0,4):
                element=Board_2D[row][col]
                line=line+" "+str(element)
            print(line)
        print()

        Q4_position=place_queen(4)
        if Q4_position==-1:
            print("After",end,"dead end")
            for row in range(0,4):
                line=""
                for col in range(0,4):
                    element=Board_2D[row][col]
                    line=line+" "+str(element)
                print(line)
            print()
            end_times=end_times+1
            continue
        print("Final Solution:")
        for row in range(0,4):
            line=""
            for col in range(0,4):
                element=Board_2D[row][col]
                line=line+" "+str(element)
            print(line)
        print()
main()