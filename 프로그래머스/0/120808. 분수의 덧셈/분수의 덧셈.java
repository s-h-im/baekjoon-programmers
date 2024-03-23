class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int numer = numer1 * denom2 + numer2 * denom1;
        int denom = denom1 * denom2;
        int gcd = 1; // 최대 공약수
        for(int i = 1; i <= numer && i <= denom; i++){
            if(numer%i == 0 && denom%i == 0){ 
                gcd = i;
            }
        }
        numer = numer/gcd;
        denom = denom/gcd;
        int[] answer = {numer, denom};
        return answer;
    }
}