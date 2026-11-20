class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        l = 0
        r = len(mat[0])-1

        total = 0
        for row in mat:
            if l == r:
                total += row[l]
            else:
                total += row[l]+row[r]
            l+=1
            r-=1

        return total