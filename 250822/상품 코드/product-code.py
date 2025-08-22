product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class server:
    def __init__(self, product_name='codetree', product_code=50):
        self.product_name = product_name
        self.product_code = product_code

product_1 = server()
product_2 = server(product_name, product_code)

print(f"product {product_1.product_code} is {product_1.product_name}")
print(f"product {product_2.product_code} is {product_2.product_name}")

