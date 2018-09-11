#include<iostream>
#include<vector>
using namespace std;

class Array{
public:
        int remove_duplicates(vector<int> & nums){
            // nums: sorted array
            if(nums.empty()) {
                return 0;
            }
            int index = 0;
            for(int i = 1; i < nums.size(); i ++ ){
                if(nums[index]!=nums[i]){
                    nums[++index] = nums[i];
                }
            }
            return index + 1;
        }

        int remove_duplicates_2(vector<int> & nums){
            // nums: sorted array
            if(nums.empty()){ return 0;}
            int index = 0;
            int count = 0;
            for(int i = 1; i<nums.size();++i){
                if(nums.at(index)!=nums.at(i)||count>1){
                    index+=count;
                    nums.at(index) = nums.at(i);
                    count=1;
                }
                else{
                    count++;
                }
            return index+1;
            }
        }

        // search in rotated sorted array
        int search_rotated(const vector<int> &nums, int target){
            cout<<"__search_start____"<<target<<endl;
            if(nums.empty()) return -1;
            int start = 0;
            int end = nums.size()-1;
            int mid = (start + end)/2;
            while(start<end){
                // 5 6 7 8 1 2 3 4
                if(nums[start]>target){

                }

            }


        }

};


int main(){
    int a[] = {4,5,6,7,1,2,3};
    // int: 4 bit
    int a_len = sizeof(a)/4;
    int vec_len, vec_size;
    cout<<a[0]<<endl;
    vector<int> vec;
    for(int i=0;i<a_len;++i){
        vec.push_back(a[i]);
        cout<<vec.at(i)<<endl;
    }

    vec_len = sizeof(vec)/4;
    vec_size = vec.size();

    cout<<"_____vec_____len:"<<vec_len<<endl;
    cout<<"_____vec_____size:"<<vec_size<<endl;
    cout<<"_____a_______len:"<<a_len<<endl;
    cout<<"3/2:"<<3/2<<endl;

    Array arr;
    int result;


    result = arr.search_rotated(vec,3);
    cout<<"______result______"<<result<<endl;



}





class Solution{
    public:
        ListNode* BinaryTreeToLinkList(TreeNode *root){
            ListNode* head=NULL;
            ListNode* tmp = head;
            InOrder(root);
            tmp->next=NULL;
            return head
        }

        void InOrder(TreeNode* root){
            if(TreeNode->left) InOrder(TreeNode->left);
            //
            if(root.val){
                ListNode* node = new ListNode(root.val);
                tmp->next = node;
                tmp=tmp->next;
            }
            if(TreeNode->right) InOrder(TreeNode->right);

        }

}























































