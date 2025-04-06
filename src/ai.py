from flask import Flask, request, jsonify
import google.generativeai as genai

# Configura la clave de API de Google Generative AI
genai.configure(api_key="API_KEY_HERE")

app = Flask(__name__)

# Aceptar tanto GET como POST en la misma ruta '/chat'
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    try:
        if request.method == 'POST':
            # Para el método POST, obtenemos el mensaje del cuerpo JSON
            user_message = request.json.get('message')
            
            # Llamada al modelo de Google Generative AI para generar la respuesta
            response = genai.generate_text(
                model="gemini-1.5-pro",
                prompt=user_message
            )
            return jsonify({"response": response.text})

        elif request.method == 'GET':
            # Si es un GET, simplemente respondemos con un mensaje de bienvenida o algo similar
            return jsonify({"message": "Envía un mensaje POST para interactuar con el bot."})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
