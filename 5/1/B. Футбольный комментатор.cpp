#include <iostream>
#include <stdlib.h>
using namespace std;

int main(){
    char first_match_first_scores = ' ', first_match_second_scores = ' ';
    char second_match_first_scores = ' ', second_match_second_scores = ' ';
    char rubbish = ' ';
    int home = 0;

    cin >> first_match_first_scores >> rubbish >> first_match_second_scores;
    cin >> second_match_first_scores >> rubbish >> second_match_second_scores;
    cin >> home;

    int first_scores = int(first_match_first_scores) + int(second_match_first_scores) - 96;
    int second_scores = int(second_match_second_scores) + int(first_match_second_scores) - 96;

    int first_out, second_out;
    int answer = 0;
    if( home == 1 ) {
        first_out = second_match_first_scores, second_out = first_match_second_scores;

    }
    else {
        first_out = first_match_first_scores, second_out = second_match_second_scores;
    }

    if( first_scores <= second_scores ) {
        answer += second_scores - first_scores;
        if( home == 1 ) {
            first_out += answer;
        }
        if( first_out <= second_out ){
            ++answer;
        }
    }
    cout << answer;

    return 0;
}
