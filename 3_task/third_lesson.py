import numpy as np

def create_matrix(size):
    matrix = np.eye(size)
    st, m = 1, 0
    matrix[size // 2, size // 2] = size ** 2
    for v in range(size//2):
        for i in range(size-m):
            matrix[v][i+v] = st
            st+=1   
        for i in range(v+1, size-v):
            matrix[i][-v-1] = st
            st+=1
        for i in range(v+1, size-v):
            matrix[-v-1][-i-1] =st
            st+=1
        for i in range(v+1, size-(v+1)):
            matrix[-i-1][v]= st
            st+=1
        m+=2
    return matrix, int(np.sum(np.diagonal(matrix)))

if __name__ == "__main__":
    n = None
    try: 
        n = int(input('Print size of matrix >> '))
    except ValueError:
        print('Wrong input.')
    if n:
        matrix, sum_diagonal = create_matrix(n)
        print(f'Matrix \n{matrix}')
        print(f'Sum = {sum_diagonal}')