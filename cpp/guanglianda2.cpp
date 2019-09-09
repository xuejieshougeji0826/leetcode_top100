//
// Created by gzc on 2019-08-26.
//

void DFS(vector<vector<char>> &board,int row, int col,int rows,int cols){
    if ( row<0 || row>rows-1 || col < 0 || col>cols-1 )
        return;
    if( board[row][col] == 'O' )
    {
        board[row][col] = '#';
        if ( row > 0 )
            DFS(board,row-1,col,rows,cols);
        if ( col > 0 )
            DFS(board,row,col-1,rows,cols);
        if ( row < rows-1 )
            DFS(board,row+1,col,rows,cols);
        if ( col < cols-1 )
            DFS(board,row,col+1,rows,cols);
    }
}

void solve(vector<vector<char>> &board) {
    if( board.empty() || board[0].empty() )
        return;
    int rows = board.size();
    int cols = board[0].size();

    for(int i=0; i<rows; ++i){
        if( board[i][0] == 'O' ){
            DFS(board,i,0,rows,cols);
        }
        if( board[i][cols-1] == 'O' ){
            DFS(board,i,cols-1,rows,cols);
        }
    }

    for(int j=0; j<cols; ++j){
        if( board[0][j] == 'O'){
            DFS(board,0,j,rows,cols);
        }
        if( board[rows-1][j] == 'O'){
            DFS(board,rows-1,j,rows,cols);
        }
    }

    for(int i=0; i<rows; ++i){
        for(int j=0; j<cols; ++j){
            if( board[i][j] == 'O'){
                board[i][j] = 'X';
            }
            if( board[i][j] == '#'){
                board[i][j] = 'O';
            }
        }
    }
}