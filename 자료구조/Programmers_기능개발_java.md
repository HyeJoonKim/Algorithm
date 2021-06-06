```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> ans = new ArrayList<>();
        double day =0.0;
        int d = 0;
        int num = 0;
        
        if (progresses.length == 0){
            return ans;
        }
        
        for (int i=0; i<progresses.length; i++){
            if (progresses[i] + d*speeds[i] >= 100){
                num += 1;
                continue;
            }
            
            if (i!=0)
                ans.add(num);
            num = 0;            
            day = (100-progresses[i]) / (double)speeds[i];            
            d = (int)Math.ceil(day);
            num += 1;
        }
        ans.add(num);
        return ans;
    }
}
```

