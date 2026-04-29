from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Rota principal — carrega a página HTML
@app.route('/')
def index():
    return render_template('index.html')

# Rota que recebe a expressão e devolve o resultado
@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    expressao = data.get('expressao','')
    
    try:
        
        # Segurança: permite só caracteres matemáticos
        permitidos = set ("0123456789+-*/.()")
        if not all(c in permitidos for c in expressao):
            return jsonify({'erro': 'Expressão inválida'}), 400
        
        resultado = eval(expressao)
        
         # Trata divisão por zero e infinito
        if resultado != resultado or abs(resultado) == float('inf'):
            return jsonify({'erro': 'Resultado inválido'}), 400
        
        # Remove .0 desnecessário (ex: 6.0 → 6)
        if isinstance(resultado,float) and resultado.is_integer():
            resultado = int(resultado)
            
        return jsonify({'resultado': resultado})
    except ZeroDivisionError:
        return jsonify({'erro': 'Divisão por zero'}), 400
    except Exception:
        return jsonify({'erro': 'Expressão inválida'}), 400
    
if __name__ == '__main__':
    app.run(debug=True)        