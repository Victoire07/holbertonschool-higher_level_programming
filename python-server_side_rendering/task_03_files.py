from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    products_list = []         # contiendra tous les produits vide pour l'instant!!
    error_message = None       # Si erreur source inconnue ou id introuvable

    if source == "json":
        try:
            with open("products.json") as fichier:
                data = json.load(fichier)
                products_list = data
        except Exception as erreur:
            error_message = f"Erreur lecture JSON : {erreur}"

    elif source == "csv":
        try:
            with open ("products.csv") as fichier:
                reader = csv.DictReader(fichier)
                for row in reader:
                    products_list.append(row)
        except Exception as erreur:
            error_message = f"Erreur de lecture du CSV : {erreur}"

    if product_id:
        try:
            # Convertit le paramètre id dc la string en int
            product_id = int(product_id)

            # Cherche le produit avec cet id dans la liste
            matching_product = None
            for product in products_list:
                if int(product['id']) == product_id:
                    matching_product = product
                    break

            if matching_product:
                products_list = [matching_product]  # Garde que CE produit
            else:
                error_message = "Product not found"

        except ValueError:
            error_message = "Invalid id format"

    return render_template('product_display.html',
                           products=products_list,
                           error=error_message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
