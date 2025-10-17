#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cassert>
using namespace std;

class Graph {
    public:
        Graph(int numEdges);
        int V();
        int E();
        bool adjacent(int x, int y);
        vector<int> neighbors(int x);
        void addEdge(int x, int y, int weight = 1);
        void removeEdge(int x, int y);
        int getNodeValue(int x);
        void setNodeValue(int x, int value);
        int getEdgeWeight(int x, int y);
        void setEdgeWeight(int x, int y, int value);
        void printAdjMatrix();
    private:
        vector<vector<int>> graph;
        vector<int> nodeValues;
        int size;
};

Graph::Graph(int numEdges) {
    size = numEdges;
    nodeValues = vector<int>(size);
    graph = vector<vector<int>>(size);
    for (int i = 0; i < size; i++)
        graph[i] = vector<int>(size);    
};

int Graph::V() { return size; };
int Graph::E() {
    int sum = 0;
    for(int i = 0; i < size; i++)
        for(int j = 0; j < size; j++)
            if(graph[i][j] > 0)
                sum += graph[i].size();
    return (sum/2);
};
bool Graph::adjacent(int x, int y) {
    assert(x < size);
    vector<int> adj = neighbors(x);
    return count(adj.begin(), adj.end(), y);
};
vector<int> Graph::neighbors(int x) {
    assert(x < size);
    vector<int> neighborsPaths = graph[x];
    vector<int> neighbors(neighborsPaths.size());
    for(int i = 0; i < neighborsPaths.size(); i++)
        if(neighborsPaths[i] > 0)
            neighbors[i] = neighborsPaths[i];
    return neighbors;
};
void Graph::addEdge(int x, int y, int weight) { setEdgeWeight(x, y, weight); }
void Graph::removeEdge(int x, int y) {
    assert(x < size && y < size);
    graph[x][y] = 0;
    graph[y][x] = 0;
};
int Graph::getNodeValue(int x) { assert(x < size); return nodeValues[x]; };
void Graph::setNodeValue(int x, int value) { assert(x < size); nodeValues[x] = value; };
int Graph::getEdgeWeight(int x, int y) { assert(x < size && y < size); return graph[x][y]; };
void Graph::setEdgeWeight(int x, int y, int weight) {
    assert(x < size && y < size);
    assert(x != y && weight > 0);
    graph[x][y] = weight;
    graph[y][x] = weight;
};
void Graph::printAdjMatrix() {
    cout << "Graph Adjacency Matrix" << endl << "\t";
    for(int i = 0; i < size; i++)
        cout << i << "\t";
    cout << endl;
    for(int i = 0; i < size; i++) {
        cout << i << "\t";
        for(int j = 0; j < size; j++)
            cout << graph[i][j] << "\t";
        cout << endl;
    }
};

class ShortestPath {
    public:
        void vertices();
        vector<int> path(int start, int goal);
        int path_size(int start, int goal);
};

void ShortestPath::vertices() {}; //TODO not sure how/what is being asked for yet
// vector<int> ShortestPath::path(int start, int goal) {};
// int ShortestPath::path_size(int start, int goal) { return path(start, goal).size(); };

int main() {
    Graph g(10);
    g.printAdjMatrix();
    return 0;
}
