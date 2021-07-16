   def reverseList(self, head):
        # dummy = ListNode(0)
        # dummy.next = head
        # If you use dummy.next = head, then when head.next is set to dummy
        # i.e in the first iteration of while loop, current(head).next = prev(dummy), and then this will cause a cycle.
        prev = None
        current = head
        while current:
            temp_next = current.next
            current.next = prev
            # temp_next.next = current

            prev = current
            current = temp_next
        # you return prev, because now current is set to NONE, and prev keeps track of the previous 1 iteration version of CURRENT
        return prev

    def reverseList(self, head):
        if head.next == None:
            return head
        p = self.reverseList(head.next)
        # this is wrong, because the p that is returned here is the last element
        # initially you were thinking that suppose the linked list is: [1] -> [2] ->[3],
        # then at the top of the recursion stack,
        # self.reverseList(head.next) will return [3] therefore = [3], and head will be [2],
        # therefore we can just use p([3]).next = head([2]) OR head([2]).next([3]).next = head([2])
        # YOU ASSUMED THAT They are essentially the same thing. However, we use head.next.next = head,
        # BECAUSE our p is the last element in the linkedlist, as stated by our base case.
        # After we hit our base case and returned head, our recursion stack continues to be emptied until we come
        # come back to when head = [1], and therefore we needed to set head.next = None by default!
        p.next = head
        head.next = None
        return p
