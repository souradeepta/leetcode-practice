package mypackage;

public class longestSubstring {
    public static void main() {
        longestSubstring s = new longestSubstring();
        int result = s.lengthOfLongestSubstring("ppkew");
        System.out.println(result);
    }

    public int lengthOfLongestSubstring(String s) {
        Integer[] log = new Integer[128];

        int left =0;
        int right = 0;

        int result = 0;
        while(right < s.length()){
            char c = s.charAt(right);

            Integer index = log[c];
            if(index != null && index >= left && index < right) left = index + 1;

            result = Math.max(result, right - left + 1);

            log[c] = right;
            right++;
        }
        return result;

    }
}