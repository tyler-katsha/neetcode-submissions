class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        mapping = {'2':'abc',
                   '3':'def',
                   '4':'ghi',
                   '5':'jkl',
                   '6':'mno',
                   '7':'pqrs',
                   '8':'tuv',
                   '9':'wxyz'
        }
        
        res = []

        def backtracking(index,path):
            if index == len(digits):
                res.append("".join(path))
                return
            for c in mapping[digits[index]]:
                path.append(c)
                backtracking(index+1,path)
                path.pop()
        
        backtracking(0,[])
        return res


