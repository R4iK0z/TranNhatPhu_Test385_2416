from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher

app = Flask(__name__)
cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def api_encrypt():
    data = request.get_json()
    message = data.get("message", "")
    key = int(data.get("key", 0))
    
    # Thực hiện thuật toán
    encrypted_message = cipher.encrypt_text(message, key)
    
    # Trả về JSON đúng cấu trúc Client đang đợi
    return jsonify({
        "status": "success",
        "encrypted_message": encrypted_message
    })

@app.route('/api/caesar/decrypt', methods=['POST'])
def api_decrypt():
    data = request.get_json()
    ciphertext = data.get("ciphertext", "")
    key = int(data.get("key", 0))
    
    # Thực hiện thuật toán
    decrypted_message = cipher.decrypt_text(ciphertext, key)
    
    # Trả về JSON đúng cấu trúc Client đang đợi
    return jsonify({
        "status": "success",
        "decrypted_message": decrypted_message
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)