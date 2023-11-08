# KD Tree Nearest Neighbor Search
# tree highet H -> visit 2H nodes  
# https://www.youtube.com/watch?v=Glp7THUpGow

def nearestNeighbor(Node root, Point target, int depth):

    if root == None: return None
    if target[depth % K] < root.point[depth % K]:
        nextBranch = root.left
        otherBranch = root.right
    else:
        nextBranch = root.right
        otherBranch = root.left 

    Node temp = nearestNeighbor(nextBranch, target, depth + 1)
    Node best = closest(temp, root, target)

    long radiusSquared = distSquared(target, best.point) # calculate r
    long dist = target[depth % K] - root.point[depth % K] # calculate r'

    if radiusSquared >= dist * dist:
        # traverse the other side
        temp = nearestNeighbor(otherBranch, target, depth + 1)
        best = closest(temp, best, target)
    
    return best
