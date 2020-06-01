import numpy as np 

def Row_Max( grid, N ):
    #Takes a numpy array and returns the largest product of N consecutive integers in a row
    row_max = 1    
    for row in grid:
        for i in range(len(row) - N) :
            new_prod = 1
            for j in range(N):
                new_prod *= row[i+j]
            if new_prod > row_max:
                row_max = new_prod
    return row_max

def Col_Max( grid, N ):
    #Takes a numpy array and returns the largest product of N consecutive integers in a column
    return Row_Max(grid.T, N)

def Diag_Back_Max(grid, N):
    #Takes a numpy array and returns the largest product of N consecutive integers in a backslash diagonal
    diag_back_max = 1
    grid_size = grid.shape

    for i in range( grid_size[0] - N ):
        for j in range( grid_size[1] - N ):
            new_prod = 1
            for n in range(N):
                new_prod *= grid[i+n, j+n]
            if new_prod > diag_back_max:
                diag_back_max = new_prod
    return diag_back_max

def Diag_Fow_Max(grid, N):
    #Takes a numpy array and returns the largest product of N consecutive integers in a forwardslash diagonal
    diag_for_max = 1
    new_prod = 1
    grid_size = grid.shape

    for i in range(1, grid_size[0] - N ):
        for j in range(N, grid_size[1]):
            new_prod = 1
            for n in range(N):
                new_prod *= grid[i+n, j-n]
            if new_prod > diag_for_max:
                diag_for_max = new_prod
    return diag_for_max
    
def main():
    f = np.loadtxt(fname = "p11_number_grid.txt", dtype = "int")
    
    result = [Row_Max(f, 4), Col_Max(f, 4), Diag_Back_Max(f, 4), Diag_Fow_Max(f, 4)]

    print(result)

main()