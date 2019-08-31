# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = handler

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        
        for folder in path:
            if folder not in current_node.children:
                current_node.children[folder] = RouteTrieNode()
            current_node = current_node.children[folder]
            
        current_node.handler = handler

    def find(self, parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        for part in parts:

            if part in current_node.children:
                current_node = current_node.children[part]
            
            else:
                return None

        return current_node.handler 





# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = ''

    def insert(self, path):
        # Insert the node as before
        node = self

        for w in path:
            node = node.children[w]






# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, no_page):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.RouteTrie = RouteTrie(root_handler)
        self.no_page = no_page


    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        
        if len(path) < 1:
            return self.no_page

        path = self.split_path(path)

        self.RouteTrie.insert(path, handler)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        if len(path) == 1 and path[0] == '/':
            return self.RouteTrie.handler

        Trie = self.RouteTrie
        path = self.split_path(path)
        trie_find = Trie.find(path)

        if trie_find == None or trie_find == '':
            return self.no_page

        return trie_find


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        sep = '/'
        list_path = []

        path = path.split(sep)

        for i in range(len(path)):
            if path[i] == '':
                path[i] = sep
        
        return path





# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print("This is the Test")
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one



# create the router and add a route
router1 = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router1.add_handler("/home/extension/folder1/folder2", "Folder2 handler")  # add a route

# some lookups with the expected output
print("This is the Test 1")
print(router1.lookup("/")) # should print 'root handler'
print(router1.lookup("/home")) # should print 'not found handler'
print(router1.lookup("/home/extension/")) # should print 'not found handler'
print(router1.lookup("/home/extension/folder1")) # should print 'not found handler'
print(router1.lookup("/home/extension/folder1/folder2")) # should print 'folder2 handler'


# create the router and add a route
router2 = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router2.add_handler("/", "Empty handler")  # add a route

# some lookups with the expected output
print("This is the Test 2")
print(router2.lookup("//")) # should print 'not found handler'

