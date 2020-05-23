class RouteTrie:
    def __init__(self):
        self.root = '/'
        self.handler = None
        self.next = {}

    def insert(self, paths, handler):
        current = self.next
        paths = paths.split('/')
        for path in paths:
            current.insert(RouteTrieNode(path))
            current = current.next[path]
        current.handler = handler

    def find(self, paths):
        if paths == '/':
            return self.handler
        paths = paths.split('/')
        for sub_path in paths:
            current = self
            for sub_path in path:
                current = current.next
                current = current[sub_path]
            handler = current.handler

class RouteTrieNode:
    def __init__(self, val=''):
        self.value = val
        self.handler = None
        self.next = {}
    def insert(self, next_path, handler=None):
        self.next[next_path] = self.next.get(next_path, RouteTrieNode(next_path))
        self.next[next_path].handler = handler
class Router:
    def __init__(self, root_handler, not_found_handler):    
        self.root = '/'
        self.handler = root_handler
        self.next = {}
        self.not_found = not_found_handler

    def add_handler(self, path, path_handler):
        if path == self.root:
            self.handler = path_handler
        else:
            path = self.split_path(path)
            current = self.next
            i = 1
            for sub_path in path:
                if not sub_path:
                    continue
                if i:
                    i = 0
                    current[sub_path] = current.get(sub_path, RouteTrieNode(sub_path))
                    current = current[sub_path]
                else:
                    current.insert(sub_path, path_handler)

    def lookup(self, path):
        if path == '/':
            return self.handler
        path = self.split_path(path)
        current = self
        
        for sub_path in path:
            if sub_path:
               
                if sub_path in current.next:
                  
                    current = current.next
                    current = current[sub_path]
                else:
                    return self.not_found

        handler = current.handler
        if handler:
            return handler
        else:
            return 'not found'

    def split_path(self, path):
       
        return path.split('/')

router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  


print(router.lookup("/")) 
print(router.lookup("/home"))
print(router.lookup("/home/about")) 
print(router.lookup("/home/about/"))
print(router.lookup("/home/about/me"))
router.lookup("/home/about")
