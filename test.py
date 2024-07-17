from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for demonstration
books = [
    {"id": 1, "title": "Python Programming", "author": "Guido van Rossum"},
    {"id": 2, "title": "JavaScript Basics", "author": "John Doe"}
]

# Route with parameter
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book), 200
    else:
        return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
