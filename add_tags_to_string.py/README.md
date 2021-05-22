# Takeaways
- The main idea for this solution is to use an array to keep track of the elements that should be bolded and also not bolded.
  - By doing it this way, we handle the issue of overlaps. For example let s = 'abcdefabc' and words = ['abc','bcd'], the the to_bold array will be ['a'==True,'b'==True,'c'==True,'d'==True,'f'==False, 'a'==True, 'b'==True, 'c'==False ], so we just need to handle two cases when the to_bold array goes from False to True and True to False!
    - Note also that we need to handle the case when the word appeared more than once in the string, like "abc"
      - This is done by looking for the remaining substring after the occurence of one word is found.
      - One mistake that i made originally was that i was using the ORIGINAL string for slicing, when the indexed returned corresponded to the SLICED string.
        - This created an infinite loop as the **indexed returned on the SLICED string made the loop unable to terminate on the ORIGINAL string**
  - However, implementing it can be tricky:
    - Because we need to look at the previous index,  at index 0, (0 - 1 = - 1) does not exist which means that we need to handle the case when the starting element is True separately. For example if 'a'==True, then we need to add a "<b>" to the start of the resulting string.
    - Because we need to look at the next index, at index len(s) -1, ((len(s)-1) + 1 = len(s)) does not exist which means that we need to handle the case when the ending element is True separately. For example if 'c'==True, then we need to add a  "</b>" to the end of the resulting string.