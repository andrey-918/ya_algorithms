#include <iostream>
using namespace std;

int ans( int k ) {
    int answer = k / 4;
    if( k - answer * 4 >= 2 ) {
        return answer + 2;
    }
    return answer + (k - answer * 4);

}


int main() {

    int n = 0;
    cin >> n;
    long int answer = 0;
    for( int i = 0; i < n; ++i ) {
        int k = 0;
        cin >> k;
        answer += ans(k);
    }

    cout << answer;
}
