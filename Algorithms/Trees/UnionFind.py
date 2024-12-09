# Union Find (AKA Disjoint Sets) - a forest of trees. Consider all edges are directed ie [1, 2] means 1 points to 2
# nodes are often created as parents of themselves if they don't have a parent node

class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {} # HEIGHT

        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]] # path compression - optimization to shorten a chain that doesn't change the overall time complexity
            p = self.parent[p]
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False # already part of same set
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True