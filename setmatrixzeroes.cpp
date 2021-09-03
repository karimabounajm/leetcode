

#include <vector>
#include <iostream>
#include <cstring>

using namespace std;

class Solution {
public:
    void setZeroes(vector< vector<int> >& matrix) {
        int rem_col = 0, rem_row = 0, length = matrix[0].size(), height = matrix.size();
        for(int i = 0; i < height; i++) {
            for(int j = 0; j < length; j++) {
                cout << matrix[i][j] << ' ';
            } cout << endl;
        }
        // checking if first row should be zeroed in the end
        for(int i = 0; i < length; i++) {
            if(matrix[0][i] == 0) {
                rem_row = 1;
                break;
            }
        }
        
        // checking if first column should be zeroed in the end
        for(int i = 0; i < height; i++) {
            if(matrix[i][0] == 0) {
                rem_col = 1;
                break;
            }
        }
        // checking every value to see if it's zero, and zeroing 
        // corresponding column and row indicator
        for(int i = 1; i < height; i++) {
            for(int j = 1; j < length; j++) {
                if(matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        // zeroing out columns and rows based on first passover
        for(int i = 1; i < length; i++) {
            if(matrix[0][i] == 0) {
                for(int j = 0; j < height; j++) {
                    matrix[j][i] = 0;
                }
            }
        }
        // checking if first column should be zeroed in the end
        for(int i = 1; i < height; i++) {
            if(matrix[i][0] == 0) {
                memset(&(matrix[i][0]), 0, length * sizeof(int));
            }
        }
        if(rem_col == 1) {
            for(int i = 0; i < height; i++) {
                matrix[i][0] = 0;
            }
        }
        if(rem_row == 1) {
            for(int i = 0; i < length; i++) {
                matrix[0][i] = 0;
            }
        }
        cout << endl;
        for(int i = 0; i < height; i++) {
            for(int j = 0; j < length; j++) {
                cout << matrix[i][j] << ' ';
            } cout << endl;
        }
    }
};
		
int main() {
    Solution s;
    vector<vector<int> > vec{ { 0, 2, 3 },
                              { 4, 5, 6 },
                              { 7, 0, 9 }, 
                              { 1, 9, 8} };
    vector<vector<int> > vik{ { 1, 0, 3 } };
    s.setZeroes(vik);

}