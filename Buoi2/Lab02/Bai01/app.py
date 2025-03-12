from flask import Flask, request, json,render_template
from cipher.caesar import CaesarCipher
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")
@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form['inPutPlainText']
    key = int(request.form['inPutKey'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted_text: {encrypted_text}"
@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form['inPutCipherText']
    key = int(request.form['inPutKey'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted_text: {decrypted_text}"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)