from flask import Flask, render_template
import os

# Inicializa o Flask
app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
    """
    Rota principal que renderiza o template index.html
    Otimizada para Azure App Service
    """
    return render_template('index.html')

# Rota adicional para saúde do serviço (importante para Azure)
@app.route('/health')
def health_check():
    """
    Endpoint de health check para Azure e monitoramento
    """
    return {
        "status": "healthy",
        "service": "Artemis Mission",
        "version": "1.0.0"
    }, 200

# Configurações para produção (Azure)
if __name__ == '__main__':
    # Detecta se está em produção (Azure) ou desenvolvimento local
    port = int(os.environ.get('PORT', 5000))
    
    # Configurações de debug apenas em desenvolvimento
    debug = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    
    app.run(host='0.0.0.0', port=port, debug=debug)