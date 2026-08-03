class Solution {
public:
    bool checkInclusion(string s1, string s2) {

        vector<int> f1(26,0),f2(26,0);
        if(s1.size()>s2.size())return false;
        for(char c:s1) f1[c-'a']++;
        int k=s1.size();
        int l=0,r=k;
        for(int i=0;i<k;i++){
            f2[s2[i]-'a']++;
        }
        if(f1==f2)return true;
        while(r<s2.size()){
            f2[s2[l++]-'a']--;
            f2[s2[r++]-'a']++;
            if(f1==f2)return true;
        }
        return false;
    }
}; 