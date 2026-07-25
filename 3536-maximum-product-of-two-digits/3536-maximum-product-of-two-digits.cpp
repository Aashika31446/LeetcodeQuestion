class Solution {
public:
    int maxProduct(int n) {
        int list1=0;
        vector<int>val;
        while(n!=0){
            int rem=n%10;
            val.push_back(rem);
            n=n/10;
        }
        for(int i=0;i<val.size();i++){
            for(int j=i+1;j<val.size();j++){
                int prod=val[i]*val[j];
                list1=max(prod,list1);
            }

        }
        return list1;
    }
};