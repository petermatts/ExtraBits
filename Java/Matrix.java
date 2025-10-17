/**
 * 
 */
public class Matrix<E> {
    /**
     * m rows (vertical size)
     */
    final int m;

    /**
     * n columns (horizontal size)
     */
    final int n;

    private E[][] matrix;

    /**
     * Constuctor
     * @param m vertical dimension
     * @param n horizontal dimension
     * @param matrix the matrix
     * @throws IllegalArgumentException if matrix dimensions do no match m and n
     */
    public Matrix(int m, int n, E[][] matrix) throws IllegalArgumentException {
        if(matrix.length != m)
            throw new IllegalArgumentException("Invalid m");

        for(int i = 0; i < matrix.length; i++)
            if(matrix[i].length != n)
                throw new IllegalArgumentException("Invalid n");

        this.m = m;
        this.n = n;
        this.matrix = matrix;
    }

    /**
     * Overwrites a value at the given location
     * @param m vertical index
     * @param n horizontal index
     * @param val new value
     */
    public void set(int m, int n, E val) {matrix[m][n] = val;}

    /**
     * Gets the value at the given location
     * @param m
     * @param n
     * @return
     */
    public E get(int m, int n) {return matrix[m][n];}

    public E[][] get() {return matrix;}

    //! get rid of generics and make doubles
    // public Matrix<E> scalarMult(E factor) {
    //     E[][] mat = this.get();
    //     for(int i = 0; i < mat.length; i++)
    //         for(int j = 0; j < mat[i].length; j++)
    //             mat[i][j] = mat[i][j]*factor;
    //     return new Matrix<E>(m, n, mat);
    // }

    @Override
    public boolean equals(Object o) {
        return false;
    }

    @Override
    public String toString() {
        return "";
    }
}