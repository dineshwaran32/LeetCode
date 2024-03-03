class Solution {
    public int romanToInt(String s) {
        Map<Character,Integer> r =new HashMap<>();
        r.put('I', 1);
        r.put('V', 5);
        r.put('X', 10);
        r.put('L', 50);
        r.put('C', 100);
        r.put('D', 500);
        r.put('M', 1000);
        int sum=0;
        for(int i=0;i<s.length();i++){
            if(i+1<s.length()&& r.get(s.charAt(i))<r.get(s.charAt(i+1))){
                sum-=r.get(s.charAt(i));
            }else{
                sum+=r.get(s.charAt(i));
            }
        }
        return sum;
    }
}