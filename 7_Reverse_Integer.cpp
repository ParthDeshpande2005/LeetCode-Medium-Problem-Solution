#include <iostream>
#include <limits.h>
using namespace std;
int reverse(int x)
{
    int sign;
    if (x == INT_MIN) {
        return 0;
    }
    if(x<0)
    {
        sign=-1;
        x=-x;
    }
    else
    {
        sign=1;
    }
    int reverse=0;
    while(x!=0)
        {    
            int a=x%10;
            if (reverse > (INT_MAX - a) / 10)
            {
                return 0;
            }
            reverse=reverse*10+a;
            x /= 10;
        }
    return (reverse*sign);
}
int main()
{
    int a=reverse(-2147483648);
    cout<<a;
    return 0;
}