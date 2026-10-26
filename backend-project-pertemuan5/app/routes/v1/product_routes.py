from flask import Blueprint, request
from app.repositories.product_repo import ProductRepository
from app.utils.response_helper import success_response, fail_response

product_bp_v1 = Blueprint("product_v1", __name__, url_prefix="/api/v1/products")
repo = ProductRepository()

@product_bp_v1.route("", methods=["GET"])
def get_products():
    # Ambil data dari repository
    products = repo.get_all()
    return success_response(
        data={"products": products, "total": len(products)}
    )

@product_bp_v1.route("", methods=["POST"])
def add_product():
    if not request.is_json:
        return fail_response({"content_type": "Harus application/json"})

    body = request.get_json(silent=True)
    if not isinstance(body, dict):
        return fail_response({"body": "Harus berupa objek JSON yang valid"})

    errors = {}
    name = body.get("name")
    category = body.get("category")
    price = body.get("price")
    stock = body.get("stock")

    if not isinstance(name, str) or not name.strip():
        errors["name"] = "Nama produk wajib diisi"
    if not isinstance(category, str) or not category.strip():
        errors["category"] = "Kategori wajib diisi"
    if not isinstance(price, (int, float)) or price < 0:
        errors["price"] = "Harga wajib diisi dan harus berupa angka positif"
    if type(stock) is not int or stock < 0:
        errors["stock"] = "Stok wajib diisi dan harus berupa angka bulat positif"

    if errors:
        return fail_response(errors, 400)

    # Ambil total data saat ini untuk ID baru
    current_products = repo.get_all()
    new_product = {
        "id": len(current_products) + 1,
        "name": name.strip(),
        "category": category.strip(),
        "price": price,
        "stock": stock,
    }

    # Simpan menggunakan repository
    repo.add(new_product)
    
    return success_response(
        data=new_product, message="Produk berhasil ditambahkan", code=201
    )

@product_bp_v1.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    if not request.is_json:
        return fail_response({"content_type": "Harus application/json"})

    body = request.get_json(silent=True)
    if not isinstance(body, dict):
        return fail_response({"body": "Harus berupa objek JSON yang valid"})

    # Cari produk menggunakan repository
    product = repo.get_by_id(product_id)
    if not product:
        return fail_response({"id": "Produk tidak ditemukan"}, 404)

    errors = {}

    if "price" in body:
        price = body.get("price")
        if not isinstance(price, (int, float)) or price < 0:
            errors["price"] = "Harga harus berupa angka positif"
        else:
            product["price"] = price

    if "stock" in body:
        stock = body.get("stock")
        if type(stock) is not int or stock < 0:
            errors["stock"] = "Stok harus berupa angka bulat positif"
        else:
            product["stock"] = stock

    if errors:
        return fail_response(errors, 400)

    # Update menggunakan repository
    repo.update(product_id, product)
    
    return success_response(data=product, message="Data produk berhasil diperbarui")

@product_bp_v1.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    # Cek apakah produk ada menggunakan repository
    product = repo.get_by_id(product_id)
    if not product:
        return fail_response({"id": "Produk tidak ditemukan"}, 404)

    # Hapus menggunakan repository
    repo.delete(product_id)
    return success_response(message="Data produk berhasil dihapus")