class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int l = 0;
        int r = matrix.length-1;
        int mid = 0;
        while(l<=r){
            mid = (l+r)/2;
            if(target>= matrix[mid][0] && target <=matrix[mid][matrix[0].length-1]){
                break;
            }
            
            if(target>=matrix[mid][0]) {
                l = mid + 1;
            }
            else {
                r = mid - 1;
            }
        }

        l = 0;
        r = matrix[0].length-1;
        int index = mid;
        while(l<=r){
            mid = (l+r)/2;
            System.out.println(l + " " + r);
            if(target == matrix[index][mid]){
                return true;
            }
            if(target > matrix[index][mid]){
                l = mid + 1;
            }
            else {
                r = mid - 1;
            }

        }
        return false;
    }
}
