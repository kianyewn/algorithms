class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class dLinkedlist:

    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.key_to_node_map = {}

    def addNode(self, key, val):
        # we want to add the most recently used value to the value after 'head'
        node = Node(key, val)
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

        self.key_to_node_map[key] = node
        # print(str(key) + ' added.')

    def removeNode(self, key):

        if key not in self.key_to_node_map:
            return
        else:
            node = self.key_to_node_map[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            del self.key_to_node_map[key]

    def removeTail(self):
        tail_key = self.tail.prev.key
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

        del self.key_to_node_map[tail_key]


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.current_capacity = 0
        self.ll = dLinkedlist()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.ll.key_to_node_map:
            val = self.ll.key_to_node_map[key].val
            # remove the old position of the node in the linkedlist
            self.ll.removeNode(key)
            # add the node to make it most recent in the ll
            self.ll.addNode(key, val)
            # print(key, self.ll.key_to_node_map[key], self.ll.key_to_node_map[key].val)
            return self.ll.key_to_node_map[key].val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.ll.key_to_node_map:
            val = self.ll.key_to_node_map[key].val
            self.ll.removeNode(key)
            self.ll.addNode(key, value)
            return None
        else:
            # Note that this must be more than OR EQUALS.
            # because when we put, we are adding it already
            if self.current_capacity >= self.capacity:
                # evict the least recently used key
                # This is quite close.
                # you can use ordered dictionary, and then use the del to remove key, and then add back the key as well
                # del self.cache[self.most_recent_key]

                # remove the least recently used key
                self.ll.removeTail()
                self.ll.addNode(key, value)
            else:
                self.current_capacity += 1
                self.ll.addNode(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Proof that using del does not work haha....

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}

    def debug(self, call):
        print(call, self.cache)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.debug('get' + str(key))
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = key
            self.debug('get' + str(key))
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.debug('put' + str(value))
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
            return None
        else:
            # Note that this must be more than OR EQUALS.
            # because when we put, we are adding it already
            if len(self.cache) >= self.capacity:
                # evict the least recently used key
                # This is quite close.
                # you can use ordered dictionary, and then use the del to remove key, and then add back the key as well
                # del self.cache[self.most_recent_key]

                # remove the least recently used key
                least_recent = self.cache.keys()[0]
                del self.cache[least_recent]
                self.cache[key] = value
                # self.debug()
            else:
                self.cache[key] = value
