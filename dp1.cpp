#include<bits/stdc++.h>
using namespace std;

// nums: 3 2 1 0 4
// nums: 2 3 1 1 4
// By only recursive method: 75 test cases passed out of 172
// Added one array to store the result of each stage which is visited multiple times - Dynamic Programming

bool solve(vector<int>&nums, int startIndex, vector<int>&dp){

    if(dp[startIndex]==1)
        return true;

    else if(dp[startIndex]==0)
        return false;
    
    int length = nums.size();
    
    if(nums[startIndex]>=(length-startIndex-1)){
        dp[startIndex] = 1;
        return true;
    }

    for(int i=startIndex+1;i<=(startIndex+nums[startIndex]);i++){
        if(solve(nums,i,dp)) {
            dp[startIndex] = 1;
            return true;
        }
    }

    dp[startIndex] = 0;
    return false;
}

bool canJump(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp(n,-1);
    return solve(nums,0,dp);
}

int main(){


    return 0;
}