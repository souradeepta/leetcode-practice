//  Longest Substring Without Repeating Characters
//  Brute force:: Time: O(n^3), Space: O(min(n,n)) We need O(k) space for checking a substring 
//  has no duplicate characters, where k is the size of the Set. The size of the Set is upper bounded 
//  by the size of the string n and the size of the charset/alphabet m
//  
//  Sliding Window Optimzied:: Time:O(n), Space: O(min(n,m)) 
// #include <map>
// #include <string>
// #include <algorithm> // for max
             
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        //check if empty input
        if(s.size() == 0)
            return 0;
        
        map<char, int> usedChar;
        int start = -1;
        int result = 0;
        
        for (int i = 0; i < s.size(); i++) 
        {
            // if character is found in our map, move the start to that character
            if (usedChar.find(s[i]) != usedChar.end()) 
            {
                start = max(start, usedChar[s[i]]);
            }
            usedChar[s[i]] = i;
            result = max(result, i-start);
        }
        
        return result;
    }
};