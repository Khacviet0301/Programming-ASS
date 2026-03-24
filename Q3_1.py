
KNIGHT_MOVES = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]


def knight_related(i, j, rows=None, cols=None):
    
    positions = []
    for di, dj in KNIGHT_MOVES:
        ni, nj = i + di, j + dj
        if rows is not None and cols is not None:
            if 1 <= ni <= rows and 1 <= nj <= cols:
                positions.append((ni, nj))
        else:
            positions.append((ni, nj))
    return positions

def main():

    print("Knight-related positions")


    print("\n- 3.1 knight_related(i, j) -")
    print(f"  knight_related(1, 1) [no bounds]  = {knight_related(1, 1)}")
    print(f"  knight_related(2, 3) [no bounds]  = {knight_related(2, 3)}")
    print(f"  knight_related(1, 1) [8x8 board]  = {knight_related(1, 1, 8, 8)}")
    print(f"  knight_related(4, 4) [8x8 board]  = {knight_related(4, 4, 8, 8)}")

if __name__ == "__main__":
    main()