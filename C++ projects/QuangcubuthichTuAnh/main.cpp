#include <iostream>
using namespace std;

int main(){
    int x,y,n,m,hc; /* hc means hit counts */
    cin >> x >> y >> n >> m;
    hc=0;
    // x 136 y 2 n 3 m 450 => 
    // x 138 n 2 4 hits,x 140 142 
    for (int i=n;i > 0;i--){
        for (int j=m;j>0;j-=x){     /* j-= => j=j-x */
            hc++;
            if(j<0){
                x+=y;
            }
        } 
    }
    cout << hc  << endl;



    return 0;    
}