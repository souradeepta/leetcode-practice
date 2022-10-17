package mypackage;

public class Main {
    public static void main(String[] args) {
        longestSubstring s = new longestSubstring();
        int result = s.lengthOfLongestSubstring("ppkew");
        System.out.println(result);

        int result2 = s.lengthOfLongestSubstring("abcabcbb");
        System.out.println(result2);
    }
}
