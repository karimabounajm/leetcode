def getMostVisited(n, sprints) :
    vertices = [0]* (n+2)
    for i, val in enumerate (sprints[1:]) :
        left = min(sprints[i], val)
        right = max(sprints[i], val)
        vertices[left] += 1
        vertices[right+1] -= 1
    ans = current_max = -1
    s = 0
    for i in range (1, len(vertices)):
        vertices[i] += s
        s = vertices[i]
        if s > current_max:
            current_max = s
            ans = i
    return ans