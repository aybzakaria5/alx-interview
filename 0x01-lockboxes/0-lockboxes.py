#!/urs/bin/python3
"""lockboxes"""


def canUnlockAll(boxes):
    """check if all boxes can be opened"""
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key >= 0 and key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
