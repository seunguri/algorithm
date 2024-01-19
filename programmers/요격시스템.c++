#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(vector<int> A, vector<int> B){
    if(A[1] == B[1]) return A[0] < B[0];
    return A[1] < B[1];
}

int solution(vector<vector<int>> targets) {
    int answer = 1;
    
    sort(targets.begin(), targets.end(), cmp);
    
    int end = targets[0][1];
    
    for(int i = 1; i < targets.size(); i++){
        if(end <= targets[i][0]){            
            end=targets[i][1];
            answer++;
        }
    }
    return answer;
}