//Two Sum
// Brute-force:: Time: O(n^2), Space: O(1)
// One-pass Hash table:: Time O(n), Space: O(n) 
//#include<vector>
//#include<unordered_map>
//using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        // always check for empty input
        if (nums.size() == 0)
            return {};
            
        unordered_map<int, int> index;
        for( int i =0; i<nums.size(); i++)
        {
            if (index.find(target - nums[i]) != index.end())
            {
                return {i , index[target-nums[i]]};
            }
            index[nums[i]] = i;            
        }
        return {};
        
    }
};