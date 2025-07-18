from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file(filepath):
    with open(filepath, "r") as file:
        return json.load(file)

def read_csv_file(filepath):
    products = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)
    return products

def read_sqlite_file(filepath):
    try:
        conn = sqlite3.connect(filepath)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        # Transforme chaque ligne SQL en dictionnaire
        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        return products
    except Exception:
        return None


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)  # transforme le JSON en dictionnaire Python

        # Récupère la liste des items
        items_list = data.get('items', [])  # si 'items' n'existe pas dcp retourne liste vide !

    except Exception as erreur:
        print(f"Erreur lors de la lecture du fichier JSON : {erreur}")
        items_list = []

    # Passation de la liste au template
    return render_template('items.html', items=items_list)


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ["json", "csv", "sql"]:
        return render_template("product_display.html", error="Wrong source")

    products_list = []         # contiendra tous les produits vide pour l'instant!!

    try:
        if source == "json":
            products_list = read_json_file("products.json")
        elif source == "csv":
            products_list = read_csv_file("products.csv")
    except Exception:
        return render_template("product_display.html", error="Error reading file")

    if product_id:
        try:
            # Convertit le paramètre id dc la string en int
            product_id = int(product_id)

            # Cherche le produit avec cet id dans la liste
            matching_products = [p for p in products_list if int(p["id"]) == product_id]
            if not matching_products:
                return render_template("product_display.html", error="Product not found")
            products_list = matching_products  # On garde uniquement le produit filtré
        except ValueError:
            return render_template("product_display.html", error="Invalid id format")

    return render_template('product_display.html',
                           products=products_list)

if __name__ == '__main__':
	app.run(debug=True, port=5000)
