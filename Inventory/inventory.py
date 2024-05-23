import random

class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class InventoryNode:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None
        self.height = 1

class Inventory:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node is None:
            return 0 
        else: 
            return node.height

    def get_balance(self, node):
        if node is None:
            return 0 
        else: 
            return self.get_height(node.left) - self.get_height(node.right)

    #Create a new node with the given product
    def new_node(self, product):
        return InventoryNode(product)

    #Right rotate subtree
    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        #Perform rotation
        x.right = y
        y.left = T2

        #Update heights
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        #Return new root
        return x

    #Left rotate subtree
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        #Perform rotation
        y.left = x
        x.right = T2

        #Update heights
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        #Return new root
        return y

    #Insert a product in the AVL tree
    def insert_product(self, node, product):
        if node is None:
            return self.new_node(product)

        #Insert the product
        if product.id < node.product.id:
            node.left = self.insert_product(node.left, product)
        elif product.id > node.product.id:
            node.right = self.insert_product(node.right, product)
        else:
            return node  #Duplicate IDs not allowed

        #Update height of this node
        node.height = 1 + max(self.get_height(node.left), \
                              self.get_height(node.right))

        #Get balance factor
        balance = self.get_balance(node)

        #Left Left Case
        if balance > 1 and product.id < node.left.product.id:
            return self.rotate_right(node)

        #Right Right Case
        if balance < -1 and product.id > node.right.product.id:
            return self.rotate_left(node)

        #Left Right Case
        if balance > 1 and product.id > node.left.product.id:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        #Right Left Case
        if balance < -1 and product.id < node.right.product.id:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def traverse_tree(self, node):
        if node is not None:
            self.traverse_tree(node.left)
            print(f"ID: {node.product.id}, Name: {node.product.name}, "
                  "Price: {node.product.price}, "
                  "Quantity: {node.product.quantity}")
            self.traverse_tree(node.right)

    def search_product(self, node, id):
        if node is None or node.product.id == id:
            if node is None:
                print("Product not found.")
            else:
                print(f"Found product: ID: {node.product.id}, "
                      "Name: {node.product.name}, "
                      "Price: {node.product.price}, "
                      "Quantity: {node.product.quantity}")
            return node

        print(f"Visited product ID: {node.product.id}")

        if id < node.product.id:
            return self.search_product(node.left, id)
        else:
            return self.search_product(node.right, id)

    def insert_product_public(self, product):
        self.root = self.insert_product(self.root, product)

    def traverse_tree_public(self):
        self.traverse_tree(self.root)

    def search_product_public(self, id):
        return self.search_product(self.root, id)

if __name__ == "__main__":
    inv = Inventory()
    products = []

    #Initialize products with random values
    for i in range(100):
        products.append(Product(id=i + 1, \
                                name=f"Product {i + 1}", \
                                price=random.uniform(0, 100), \
                                quantity=random.randint(1, 100)))

    #Shuffle products list
    random.shuffle(products)

    #Insert products into the inventory
    for product in products:
        inv.insert_product_public(product)

    #Display all products in the inventory
    print("Inventory:")
    inv.traverse_tree_public()

    #Search for a specific product
    product_id_to_search = 35
    found_product = inv.search_product_public(product_id_to_search)
    if found_product is not None:
        print(f"Product found: ID: {found_product.product.id}, "
              "Name: {found_product.product.name}, "
              "Price: {found_product.product.price}, "
              "Quantity: {found_product.product.quantity}")
    else:
        print(f"Product with ID {product_id_to_search} not found.")
