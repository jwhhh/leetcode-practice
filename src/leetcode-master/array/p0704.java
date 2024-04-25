public class P0704 {
    public int search(int[] nums, int target) {
        int l_idx = 0;
        int r_idx = nums.length;
        while (l_idx < r_idx) {
            int mid_idx = (l_idx + r_idx) / 2;
            int mid_num = nums[mid_idx];
            if (mid_num == target) return mid_idx;
            else if (mid_idx == l_idx) break;
            else if (mid_num < target) l_idx = mid_idx;
            else r_idx = mid_idx;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] test_nums1 = {-1,0,3,5,9,12};
        int test_target1 = 9;
        int test_result1 = 4;
        int[] test_nums2 = {-1,0,3,5,9,12};
        int test_target2 = 2;
        int test_result2 = -1;
        System.out.println(test(test_nums1, test_target1, test_result1));
        System.out.println(test(test_nums2, test_target2, test_result2));
    }

    private static boolean test(int[] nums, int target, int expected) {
        P0704 test_obj = new P0704();
        return test_obj.search(nums, target) == expected;
    }
}
