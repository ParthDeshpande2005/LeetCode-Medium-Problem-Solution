class Solution {
public:
    int maxBottlesDrunk(int numBottles, int numExchange) {
        int o=numBottles;
        int a=o;
        while(o>=numExchange)
        {
            int x=1;
            a=a+x;
            o=o-numExchange+1;
            numExchange=numExchange+1;    
        }
        return a;   
    }
};