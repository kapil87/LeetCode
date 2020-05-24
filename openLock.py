class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        queue = deque(['0000'])
        level = 0
        
        while queue:
            queue_size = len(queue)
            
            while queue_size > 0:
                lock_position = queue.popleft()
                if lock_position in deadends:
                    queue_size -= 1
                    continue
                
                if lock_position == target:
                    return level
                
                for i in range(4):
                    fwd_char = '0' if lock_position[i] == '9' else str(int(lock_position[i]) + 1)
                    bkward_char = '9' if lock_position[i] == '0' else str(int(lock_position[i]) - 1)
                    
                    forward_move_lock_position = lock_position[:i] + fwd_char + lock_position[i+1:]
                    backward_move_lock_position = lock_position[:i] + bkward_char + lock_position[i+1:]
                    
                    if forward_move_lock_position not in visited and forward_move_lock_position not in deadends:
                        queue.append(forward_move_lock_position)
                        visited.add(forward_move_lock_position)
                    
                    if backward_move_lock_position not in visited and backward_move_lock_position not in deadends:
                        queue.append(backward_move_lock_position)
                        visited.add(backward_move_lock_position)
                
                queue_size -= 1
            
            level += 1
        
        return -1
                    
