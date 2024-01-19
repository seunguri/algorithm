#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

vector<int> solution(vector<vector<int>> edges) {
    vector<int> answer(4, 0); // 생성한 정점, 도넛, 막대, 8자
    map<int, pair<int, int>> edgeCount;
    int maxNode = 0;

    for(int i=0; i<edges.size(); i++) {
        int from = edges[i][0], to = edges[i][1];
        edgeCount[from].first++;
        edgeCount[to].second++;
        maxNode = max(maxNode, max(from, to));
    }

    for(int i = 1; i <= maxNode; i++) {
        if(edgeCount[i].first >= 2 && edgeCount[i].second == 0){
            answer[0] = i;
        }
        else if(edgeCount[i].first == 0){
            answer[2]++;
        }
        else if(edgeCount[i].first >= 2 && edgeCount[i].second >= 2){
            answer[3]++;
        }
    }

    answer[1] = edgeCount[answer[0]].first - (answer[2]+answer[3]);

    return answer;
}