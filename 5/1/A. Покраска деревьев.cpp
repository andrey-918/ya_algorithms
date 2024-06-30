#include <iostream>
using namespace std;

int answerFunc(int P, int V, int Q, int M) {
    int answer = 0;
    int left1 = P - V;
    int left2 = Q - M;
    int right1 = P + V;
    int right2 = Q + M;
    answer = max(right1, right2) - min(left1, left2) + 1;
    if( min(right1, right2) < max(left1, left2) ) {
        answer -= max(left1, left2) - min(right1, right2) - 1;
    }
    return answer;
}

int main(){

    int P = 0, V = 0, M  = 0, Q = 0;
    cin >> P >> V;
    cin >> Q >> M;
    cout << answerFunc(P, V, Q, M);
    return 0;
}
