public class P0027 {
    public int removeElement(int[] nums, int val) {
        int idx = 0;
        for (int num: nums) {
            if (num != val) nums[idx++] = num;
        }
        return idx;
    }

    public static void main(String[] args) {
        int[] test_nums1 = {3,2,2,3};
        int test_target1 = 3;
        int expected_len1 = 2;
        int[] expected_nums1 = {2, 2};
        int[] test_nums2 = {0,1,2,2,3,0,4,2};
        int test_target2 = 2;
        int expected_len2 = 5;
        int[] expected_nums2 = {0,1,3,0,4};
        System.out.println(test(test_nums1, test_target1, expected_len1, expected_nums1));
        System.out.println(test(test_nums2, test_target2, expected_len2, expected_nums2));
    }

    private static boolean test(
        int[] nums, 
        int target, 
        int expected_len, 
        int[] expected_nums
    ) {
        P0027 sol = new P0027();
        int result_len = sol.removeElement(nums, target);
        if (result_len != expected_len) return false;
        for (int i = 0; i < result_len; i++) {
            if (nums[i] != expected_nums[i]) return false;
        }
        return true;
    }
}
