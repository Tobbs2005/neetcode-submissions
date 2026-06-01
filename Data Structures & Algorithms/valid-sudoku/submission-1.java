class Solution {
    public boolean isValidSudoku(char[][] board) {
        for(int i = 0; i<9; i++){
            HashSet<Character> currRow = new HashSet<>();
            HashSet<Character> currCol = new HashSet<>();
            for(int j = 0; j<9; j++){
                if(currRow.contains(board[i][j]) && (board[i][j] != '.')) {
                    return false;
                }
                if(currCol.contains(board[j][i]) && (board[j][i] != '.')){
                    return false;
                }
                currRow.add(board[i][j]);
                currCol.add(board[j][i]);
            }
        }

        for(int square = 0; square < 9; square++){
            HashSet<Character> seen = new HashSet<>();
            for(int i = 0; i < 3; i++) {
                for(int j = 0; j < 3; j++) {
                    int col = square/3 * 3 + j;
                    int row = (square%3)*3 + i;
                    char curr = board[row][col];
                    if(curr == '.') continue;
                    if(seen.contains(curr)) {
                        return false;
                    }
                    seen.add(curr);
                }
            }
        }
        return true;
    }
}
