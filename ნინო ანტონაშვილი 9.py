
import requests

url = "https://fakestoreapi.com/products"
response = requests.get(url)

# Check the status of the request
if response.status_code == 200:
    # json გადაგვყავს სიაში
    products = response.json()

    # ა)
    prices = [product['price'] for product in products]
    highest_price = max(prices)
    lowest_price = min(prices)
    average_price = sum(prices) / len(prices)

    print(f"Highest Price: ${highest_price}")
    print(f"Lowest Price: ${lowest_price}")
    print(f"Average Price: ${average_price:.2f}")

    # b)
    categories = sorted(set(product['category'] for product in products))
    print("\nCategories:", categories)

    # c)
    product_list = [{'title': product['title'], 'id': product['id']} for product in products]
    product_list_sorted = sorted(product_list, key=lambda x: x['title'])
    print("\nSorted Product List by Title:")
    for item in product_list_sorted:
        print(f"{item['title']} - ID: {item['id']}")

    # d)
    rating_list = sorted(products, key=lambda x: x['rating'])
    print("\nSorted Rating List:")
    for product in rating_list:
        print(f"{product['title']} - Rating: {product['rating']}")

else:
    print(f"Error...... Status code: {response.status_code}")
