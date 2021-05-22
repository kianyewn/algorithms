#Takeaways
- The solution that i done was similar to those discussed by others.
- The crucial part is to first sort the list of intervals according to the start of the interval, as this means that we can just use a "rolling window" approach, where we always look at two intervals at the same timee, such that if we know that the ending of the prev_interval is greater than the start of the next interval, we know that there is an overlap
- Another thing to note is that if there is an overlap, the ending of the new interval could be from the previous interval, OR the current interval. 
  - For example in [[1,10], [2,5]], the ending of the new merged interval should be 10 and thus from the previous interval, while in other cases, [[1,10],[2,29]], the ending of the new merged interval should be from the next interval.
- After looping, it is also necessary to add back the last result manually, since in the code, we only add the result when we see that there is no overlap with the NEXT interval.
  - Since we are comparing with the next interval, the last interval DOES NOT HAVE A "NEXT INTERVAL", which is why we need to add it into our results manually!