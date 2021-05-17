# Takeaways

1. Method 1
   1. The first method that i did felt like a hard coded approach, where i just included additional code to solve edge cases, and i didnt felt much accomplishment..., but nonetheless i still want to document my thoughts here.
   2. The key thing is to create numRows of strings, where each string keeps track of the characters that are supposed to be in the corresponding columns. For example in ["","",""], the first "" keeps track of the characters that belong in the first row of the zigzagged output.
   3. The first method that i did was to use a variable called "current" to keep track of a window of characters, and if the window is equals to the length of the given numRows, i add each of the elements into their respective strings.
   4. when doing the window approach, then we are not going in the diagonal direction, we can append the entire elements in "current" into their respective elements. However, when we are going in the diagonal direction, adding the elements become more complex because the last character that is added belongs to the first row of the output.
      1. I was confused in the beginning as to how to do this, but i am happy to be able to solve it by drawing out examples
         1. For an array of size 4, the original index is [0,1,2,3], and the reverse is [3,2,1,0]. The pattern here is very simple, in that the sum of  2 elements from each array that are in the same position will always sum to 3.
            1. This is the equation therefore, we just have to use (size_of_array - 1 - reversed_index) to obtain the original array
      2. Another thing to note is that since i am using the idea of windowing, there are overlaps in the first and last characters whenever i am moving in a straight line to the diagonal. "current" is initialized specially because of this as well...
   5. Another thing to notice is that similar to merge_sort, it is possible for "current" to have characters when the main loop is terminated. Therefore, we have to do another loop to add the remaining characters in "current" 
   6. Overall, the code is very messy and complicated and i do not really like it.

2. Method2
   1. This method is so simple that it makes my original attempt very laughable
   2. What this did was just to have a "step" variable so that we are adding to a row index when moving vertically, and  substracting from the row index when moving diagonally.
      1. All these solved the issue of having to use a condition that relies on the size of "current" to be equals to numRows, and simplied the code by multitudes.
   3. One thing to realize is also that there may be times when there will really be a need to hardcode edge cases, as is the case when numRows = 1.