# Closest-enemies

Using the PYTHON language, have the function ClosestEnemyII(strArr) read the matrix
of numbers stored in strArr which will be a 2D matrix that contains only the
integers 1, 0, or 2. Then from the position in the matrix where a 1 is, return
the number of spaces either left, right, down, or up you must move to reach an
enemy which is represented by a 2. You are able to wrap around one side of the
matrix to the other as well. For example: if strArr is ["0000", "1000", "0002",
"0002"] then this looks like the following:

0 0 0 0
1 0 0 0
0 0 0 2
0 0 0 2

For this input your program should return 2 because the closest enemy (2) is 2
spaces away from the 1 by moving left to wrap to the other side and then moving
down once. The array will contain any number of 0's and 2's, but only a
single 1. It may not contain any 2's at all as well, where in that case your
program should return a 0.

Sample test cases:

Input:

"000",
"100",
"200"

Output: 1

Input: 

 "0000", 
 "2010",
 "0000", 
 "2002"

Output: 2
*/



# ALGORITM

1. We need to find the position of 1 and store it (pos) (x,y)
2. Find all enemy position and store it (enemies) [(x,y),(x,y),....]
3. If there arent any enemies return 0

--------------------------------------------------------------------------------------------

4. Find the length of columns and rows (cols,rows)
5. find the distance between our position ( 1's position) and all enemies
   (distance) -> [1,2,4,5,7]
6. Iterate over enemies pos => (x, y)
        - calculate the horizontal distance (left-right) (h_min)
            - direct distance => abs(pos[y] - enemy[y])
            - wrapped distance  => cols - direct_distance
            - find the min between direct & wrapped(h_min)
        - calculate the vertical distance (v_min)
             - directr distance => abs(pos[x] - enemy[x])
             - wrapped distance = > cols - direct distance
             - find the min between direct_vertical and wrapped_vertical(v_min)
        total distance between player (1) and current enemy => (h_min,v_min)
        store total distance inside distances variable
7. return min value inside the calculated distances