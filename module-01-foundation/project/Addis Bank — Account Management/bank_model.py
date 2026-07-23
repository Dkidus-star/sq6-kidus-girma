from collections import deque
from account import Account

class Branch:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.accounts = []

    def add_branch(self, b): 
        self.children.append(b)

    def add_account(self, a): 
        self.accounts.append(a)

    def total_balance(self):
        total = sum(a.balance for a in self.accounts)
        for c in self.children:
            total += c.total_balance()
        return total

def bfs(transfers, start):
    visited = {start}
    q = deque([start])
    while q:
        cur = q.popleft()
        for n in transfers.get(cur, []):
            if n not in visited:
                visited.add(n)
                q.append(n)
    return visited

if __name__ == "__main__":
    a1 = Account("A", "1001", 1000)
    a2 = Account("B", "1002", 2000)
    a3 = Account("C", "1003", 3000)
    
    head = Branch("Head")
    r = Branch("Region")
    b = Branch("Branch")
    
    head.add_branch(r)
    r.add_branch(b)
    
    head.add_account(a1)
    r.add_account(a2)
    b.add_account(a3)
    
    print("Total:", head.total_balance())
    transfers = {"1001": ["1002"], "1002": ["1003"], "1003": []}
    print(bfs(transfers, "1001"))
