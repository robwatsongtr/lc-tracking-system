/*  
category table:
 id | category_name 
----+---------------
  1 | Array
  2 | String
  3 | Hash Map
  4 | Intervals

approach table:
 id |   approach_name   
----+-------------------
  1 | Two-Pointer
  2 | Sliding Window
  3 | Frequency Counter
  4 | Hash Map lookup
  5 | Boyer-Moore
  6 | BFS

difficulty table: 
id  | difficulty
----------------------
  1 | Easy
  2 | Medium
  3 | Hard 
*/

-- Add Two Sum problem, 
INSERT INTO problems (leetcode_num, problem_name, problem_desc, approach_id, problem_solution, diff_id) 
VALUES (1, 'Two Sum', 'Find two numbers that add up to a specific target.', 4, 
'Initialize map. In loop (for i, nums in enumerate(nums)) calculate complement: 
let complement = target - currentNum, then check the hashMap for it:  
if( complement in map ) { return [ map[complement], i ] } so you retrun the 
indicies of the number and compelent that add to target. then add to hashmap: 
map[currentNum] = i', 1
);

   -- join two sum to array and hashmap categories, assume id 1 for Two Sum 
INSERT INTO problem_categories (problem_id, category_id) VALUES (1, 1);
INSERT INTO problem_categories (problem_id, category_id) VALUES (1, 3);



-- Add Remove Element problem, 
INSERT INTO problems (leetcode_num, problem_name, problem_desc, approach_id, problem_solution, diff_id)
VALUES (27, 'Remove Element', 'Given an integer array nums and an integer val, remove 
all occurrences of val in nums in-place. The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.', 1, 
'init left pointer to 0. start for loop with right pointer at 0: if right is the 
value, skip it and loop to next element with continue, if its different than value, 
copy right to left. return left.', 1
);
   -- join remove element to array category, assume id 2 for remove element
INSERT INTO problem_categories (problem_id, category_id) VALUES (2, 1);



-- Add Majority Element problem
INSERT INTO problems (leetcode_num, problem_name, problem_desc, approach_id, problem_solution, diff_id)
VALUES (169, 'Majority Element', 'Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume 
that the majority element always exists in the array.', 5, 'Boyer-Moore voting algo: initialize 
variable candidate to None, and count to zero. Iterate through elements, if the count is zero, 
assign curr element to candidate. Then if else: if the element is same as candidate, 
increment count, else decrement count. Return candidate', 1
);
INSERT INTO problem_categories (problem_id, category_id) VALUES (3, 1);


-- Add Summary Ranges problem. Note no approach.  
INSERT INTO problems (leetcode_num, problem_name, problem_desc, approach_id, problem_solution, diff_id)
VALUES (228, 'Summary Ranges', 'You are given a sorted unique integer array nums. A range [a,b] 
is the set of all integers from a to b (inclusive).Return the smallest sorted list of ranges 
that cover all the numbers in the array exactly.', 1, 'Initialize pointer i to mark start of 
next range, j to traverse range, and an array to store ranges. Outer loop is while loop j ptr 
is not end of nums: Inner while: does a consecutive range: while one after j index hasnt 
reached end AND one after j is a consecutive number (+1), increment j.  back to outer while: 
If i == j push in nums[i] only, else push in i->j. then incr j by 1 to start new range 
and i = j to mark new range', 1
);
INSERT INTO problem_categories (problem_id, category_id) VALUES (4, 4);