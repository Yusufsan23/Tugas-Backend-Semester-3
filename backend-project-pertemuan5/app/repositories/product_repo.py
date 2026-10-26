class ProductRepository:
    def __init__(self):
        self.products = [
            {
                "id": 1,
                "name": "Laptop Thinkpad X1",
                "category": "Elektronik",
                "price": 15000000,
                "stock": 5,
            },
            {
                "id": 2,
                "name": "Mechanical Keyboard Corsair",
                "category": "Elektronik",
                "price": 850000,
                "stock": 12,
            },
            {
                "id": 3,
                "name": "Mouse Gaming Logitech G502",
                "category": "Elektronik",
                "price": 750000,
                "stock": 20,
            },
            {
                "id": 4,
                "name": "Monitor LG UltraWide 34",
                "category": "Elektronik",
                "price": 4500000,
                "stock": 7,
            },
            {
                "id": 5,
                "name": "Headset Razer Kraken",
                "category": "Elektronik",
                "price": 1200000,
                "stock": 15,
            },
            {
                "id": 6,
                "name": "Webcam Logitech C920",
                "category": "Elektronik",
                "price": 950000,
                "stock": 10,
            },
            {
                "id": 7,
                "name": "External SSD Samsung T7",
                "category": "Elektronik",
                "price": 2000000,
                "stock": 8,
            },
            {
                "id": 8,
                "name": "Printer Canon PIXMA G3010",
                "category": "Elektronik",
                "price": 2500000,
                "stock": 4,
            },
            {
                "id": 9,
                "name": "Router WiFi TP-Link Archer C6",
                "category": "Elektronik",
                "price": 600000,
                "stock": 18,
            },
            {
                "id": 10,
                "name": "Smartphone Samsung Galaxy A52",
                "category": "Elektronik",
                "price": 4000000,
                "stock": 6,
            },
        ]

    def get_all(self):
        return self.products

    def get_by_id(self, product_id):
        return next((p for p in self.products if p["id"] == product_id), None)

    def add(self, product):
        self.products.append(product)
        return product

    def update(self, product_id, updated_data):
        product = self.get_by_id(product_id)
        if product:
            product.update(updated_data)
            return product
        return None

    def delete(self, product_id):
        self.products = [p for p in self.products if p["id"] != product_id]
        return True