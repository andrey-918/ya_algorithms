#include <iostream>
#include <vector>
using namespace std;

pair<int,vector<vector<char>>>  bishop_attacks( int row, int col, vector<vector<char>> board ) {
    int count = 1;

    for (int i = 1; row + i < 8 && col + i < 8; ++i) {
        if (board[row + i][col + i] == '*') {
            ++count;
            board[row + i][col + i] = '-';
        }
        else {
            if (board[row + i][col + i] != '-') {
                break;
            }
        }
    }

    for (int i = 1; row + i < 8 && col - i > -1 ; ++i) {
        if (board[row + i][col - i] == '*') {
            ++count;
            board[row + i][col - i] = '-';
        }
        else {
            if (board[row + i][col - i] != '-') {
                break;
            }
        }
    }

    for (int i = 1; row - i > -1 && col + i < 8; ++i) {
        if (board[row - i][col + i] == '*') {
            ++count;
            board[row - i][col + i] = '-';
        }
        else {
            if (board[row - i][col + i] != '-') {
                break;
            }
        }
    }

    for (int i = 1; row - i > -1 && col - i > -1; ++i) {
        if (board[row - i][col - i] == '*') {
            ++count;
            board[row - i][col - i] = '-';
        }
        else {
            if (board[row - i][col - i] != '-') {
                break;
            }
        }
    }

    return {count, board};
}

pair<int,vector<vector<char>>> rook_attacks( int row, int col, vector<vector<char>> board ) {
    int count = 1;


    for( int i = row - 1; i > -1; --i ) {
        if( board[i][col] == '*' ) {
            ++count;
            board[i][col] = '-';
        } else {
            if( board[i][col] != '-' ) {
                break;
            }

        }
    }

    for( int i = row + 1; i < 8; ++i ) {
        if( board[i][col] == '*' ) {
            ++count;
            board[i][col] = '-';
        } else {
            if( board[i][col] != '-' ) {
                break;
            }

        }
    }

    for( int i = col - 1; i > -1; --i ) {
        if( board[row][i] == '*' ) {
            ++count;
            board[row][i] = '-';
        } else {
            if( board[row][i] != '-' ) {
                break;
            }

        }
    }

    for( int i = col + 1; i < 8; ++i ) {
        if( board[row][i] == '*' ) {
            ++count;
            board[row][i] = '-';
        } else {
            if( board[row][i] != '-' ) {
                break;
            }

        }
    }


    return {count, board};
}

int main() {
    vector<pair<int, int>> bishop_counter;
    vector<pair<int, int>> rook_counter;
    vector<vector<char>> board(8);
    for( int i = 0; i < 8; ++i ) {
        for( int j = 0; j < 8; ++j ) {
            char pos = ' ';
            cin >> pos;
            if( pos == 'B' ) {
                bishop_counter.push_back({i, j});
                board[i].push_back('B');
            }else {
                if (pos == 'R') {
                    rook_counter.push_back({i, j});
                    board[i].push_back('R');
                }
                else {
                    board[i].push_back('*');
                }
            }

        }
    }

    int answer = 0;
    for( pair<int, int> kor : rook_counter ) {
        int row = kor.first, col = kor.second;
        pair<int, vector<vector<char>>> ans = rook_attacks(row, col, board);
        answer += ans.first;
        board = ans.second;
    }

    for( pair<int, int> kor : bishop_counter ) {
        int row = kor.first, col = kor.second;
        pair<int, vector<vector<char>>> ans = bishop_attacks(row, col, board);
        answer += ans.first;
        board = ans.second;
    }

    cout << 64 - answer;

    /*cout << endl;

    for( int row = 0; row < 8; ++row ){
        for( int col = 0; col < 8; ++col ) {
            cout << board[row][col];
        }
        cout << endl;
    }*/
    return 0;
}
