import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        int mode = 0;
        int[] index = new int[1000]; 
        int max = Integer.MIN_VALUE; 
        
        for(int i=0; i<array.length; i++){
           index[array[i]]++;
        }
        
        for(int i=0; i<index.length; i++){
            if( max<index[i] ){ 
                max = index[i]; 
                mode = i ; 
            } else if(max == index[i]) {
                mode = -1;
            }
        }
        
        
        return mode;
    }
}