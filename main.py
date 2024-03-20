from flask import Flask, render_template, request

app = Flask(__name__)

PRODUCTS = [
    {
        'name':
        'iPhone 10',
        'price':
        '$500',
        'desc':
        'The iPhone 10 is a sleek and powerful smartphone that combines cutting-edge technology with elegant design. With its vibrant display, intuitive interface, and impressive camera capabilities, it’s a device that caters to both productivity and entertainment needs. Whether you’re capturing stunning photos, browsing the web, or staying connected with loved ones, the iPhone 10 delivers a seamless experience. Available in various colors and sizes, it’s a versatile companion for modern life.',
        'image':
        'https://images.unsplash.com/photo-1609654984575-f64878202abf?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    },
    {
        'name':
        'iPhone 11',
        'price':
        '$600',
        'desc':
        'The iPhone 11 is a sleek and powerful smartphone that combines cutting-edge technology with elegant design. With its vibrant display, intuitive interface, and impressive camera capabilities, it’s a device that caters to both productivity and entertainment needs. Whether you’re capturing stunning photos, browsing the web, or staying connected with loved ones, the iPhone 11 delivers a seamless experience. Available in various colors and sizes, it’s a versatile companion for modern life.',
        'image':
        'https://images.unsplash.com/photo-1616348436168-de43ad0db179?q=80&w=1981&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    },
    {
        'name':
        'iPhone 12',
        'price':
        '$700',
        'desc':
        'The iPhone 12 is a sleek and powerful smartphone that combines cutting-edge technology with elegant design. With its vibrant display, intuitive interface, and impressive camera capabilities, it’s a device that caters to both productivity and entertainment needs. Whether you’re capturing stunning photos, browsing the web, or staying connected with loved ones, the iPhone 12 delivers a seamless experience. Available in various colors and sizes, it’s a versatile companion for modern life.',
        'image':
        'https://images.unsplash.com/photo-1607936854279-55e8a4c64888?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    },
    {
        'name':
        'iPhone 13',
        'price':
        '$800',
        'desc':
        'The iPhone 13 is a sleek and powerful smartphone that combines cutting-edge technology with elegant design. With its vibrant display, intuitive interface, and impressive camera capabilities, it’s a device that caters to both productivity and entertainment needs. Whether you’re capturing stunning photos, browsing the web, or staying connected with loved ones, the iPhone 13 delivers a seamless experience. Available in various colors and sizes, it’s a versatile companion for modern life.',
        'image':
        'https://images.unsplash.com/photo-1632661674596-df8be070a5c5?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    },
    {
        'name':
        'iPhone 14',
        'price':
        '$900',
        'desc':
        'The iPhone 14 is a sleek and powerful smartphone that combines cutting-edge technology with elegant design. With its vibrant display, intuitive interface, and impressive camera capabilities, it’s a device that caters to both productivity and entertainment needs. Whether you’re capturing stunning photos, browsing the web, or staying connected with loved ones, the iPhone 14 delivers a seamless experience. Available in various colors and sizes, it’s a versatile companion for modern life.',
        'image':
        'https://images.unsplash.com/photo-1678685888221-cda773a3dcdb?q=80&w=1769&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    },
]

ORDERS = []

@app.route("/")
def homepage():
  return render_template("homepage.html")

@app.route("/browse-products")
def browse_products():
  return render_template("browse-products.html", products=PRODUCTS)

@app.route("/browse-products/product-page", methods=['POST'])
def product_page():
  DATA = request.form.to_dict()
  
  return render_template("product-page.html", product=DATA)

@app.route("/browse-products/product-page/receipt", methods=['POST'])
def receipt():
  DATA = request.form.to_dict()

  ORDERS.append(DATA)

  return render_template("receipt.html", order=DATA)

@app.route("/orders")
def orders():
  return ORDERS

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)


