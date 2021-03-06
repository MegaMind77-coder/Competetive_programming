# Write your code here
class Node :
    def __init__(self,key) :
        self.key = key 
        self.left = None 
        self.right = None 


def insert(node,key) :
    if node is None :
        return Node(key)
    
    if key < node.key :
        node.left = insert(node.left,key)
    else :
        node.right = insert(node.right,key) 
    return node 


def inorder(root) :
    if root :
        inorder(root.left)
        print(root.key,end = " ")
        inorder(root.right)

def search(root,key) :
    if root is None :
        return 0
    if root.key == key :
        return 1
    if root.key < key :
        return search(root.right,key)
    
    return search(root.left,key)
    
        
if __name__ == "__main__" :
    test = int(input())
    while test > 0 :
        n,m = map(int,input().split())
        l = list(map(int,input().split()))
        root = None 
        for i in range(n) :
            root = insert(root,l[i])
        for i in range(n,n+m) :
            boole = search(root,l[i])
            if boole == 1 :
                print("YES")
            else :
                print("NO")
                root = insert(root,l[i])
        #inorder(root)
        test -= 1
