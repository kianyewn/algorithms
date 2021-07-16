# Takeaways

- Attempt 1
  - The first attempt is to go back to using iterative approach.
  - Originally, I had wrongly assumed that i need to use a dummy node and set its .next to the head. 
    - However, this is wrong because we are supposed to **reverse** a linkedlist. since we are supposed to reverse a linkedlist, adding a dummy node is just making life harder for me
  - Without using a dummy node, I just had to use a 'prev' initialized to None to keep track of the previous state of 'current' initialized to head.
  - It is a good refresher that i had to return 'prev' instead of 'current', because my while loop terminates when current is None


- Attempt 2
  - Aside from looking at the iterative approach, i was quite interested in the recursive approach
  - I had some difficulties understanding how it worked, but it worked out.
    - The base case where head.next == None is crucial, as it allowed me to find the last node in the linkedlist. Since we are reversing a linkedlist, the last of of the linkedlist is exactly what i wanted to return (assuming that i had reversed the pointers)
    - To reverse to pointers, I made an errorneous notion that I can assume p.next = head is the same as head.next.next = head (refer to the code explanation). 
    - This refreshed my memory of how the recursion stack worked!