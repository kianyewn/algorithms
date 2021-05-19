# Takeaways

- This is a previously attempted question
  - The key is to realize that the volume of the container is dependent on the height and the base.
    - So we beging with the maximum base, and then move our pointers to accomodate the the largest height
      - When we mean largest height, it also means the minimum of the two heights height[left_pointer] and height[right_pointer] because we cannot "overflow".
      - for example, if the height[left_pointer] is smaller than height[right_pointer], this means that we should increment left_pointer because even if we can find a larger height[right_pointer], min(height[left_pointer], height[right_pointer]) will still be height[left_pointer]
        - if height[left_pointer] is larger than height[right_pointer], we should decrement height[right_pointer]
      - SPECIAL CASE!
        - Note that in the case when height[left_pointer] = height[right_pointer], we can choose to increment left_pointer or decrement right_pointer, because in both cases, the base will decrease by 1, and the minimum(height[left_pointer/new_left_pointer], height[right_pointer/new_right_pointer]) will be found in either direction.
  