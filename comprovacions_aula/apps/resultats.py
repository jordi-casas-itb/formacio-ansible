# Jordi Casas - 11/7/2025
# Codi generat per Gemini i adaptat a les necessitats.

# resultats.py
from flask import Flask, render_template
import os
import re

app = Flask(__name__)

# Directori on es troben els fitxers de resultats
RESULTS_DIR = 'resultats'

def parse_result_file(filepath):
    """
    Analitza un fitxer de text de resultats i extreu la IP i l'estat de cada comprovació.
    Retorna un diccionari amb la IP i un llistat de {comprovacio: estat}.
    """
    ip = None
    comprovacions = {}
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Regex per trobar la IP entre parèntesis
        ip_match = re.search(r'\((?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\)', lines[0])
        if ip_match:
            ip = ip_match.group('ip')

        in_checks_section = False
        for line in lines:
            line = line.strip()
            if line.startswith('| Comprovació'):
                in_checks_section = True
                continue
            if in_checks_section and line.startswith('---'):
                continue

            if in_checks_section and line.startswith('|'):
                parts = [p.strip() for p in line.split('|') if p.strip()]
                if len(parts) == 2:
                    comprovacio = parts[0]
                    estat = parts[1]
                    comprovacions[comprovacio] = estat

    except Exception as e:
        app.logger.error(f"Error processant el fitxer {filepath}: {e}")
        return {'ip': 'Error', 'data': {'Error de lectura': 'N/A'}, 'grade': 'N/A'} # Afegim grade per defecte

    return {'ip': ip, 'data': comprovacions}

@app.route('/')
def index():
    """
    Ruta principal que mostra la taula resum dels resultats amb les notes.
    """
    all_results = {} # Diccionari per emmagatzemar els resultats per IP

    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)
        app.logger.warning(f"El directori '{RESULTS_DIR}' no existia i ha estat creat.")
        
    result_files = [f for f in os.listdir(RESULTS_DIR) if f.endswith('.txt')]

    for filename in result_files:
        filepath = os.path.join(RESULTS_DIR, filename)
        parsed_data = parse_result_file(filepath)
        
        if parsed_data['ip']:
            # Calcular la nota (grade)
            num_ok = 0
            num_errors = 0
            
            for comprovacio, estat in parsed_data['data'].items():
                if estat == 'OK':
                    num_ok += 1
                elif estat == 'ERROR':
                    num_errors += 1
                # Ignorem 'N/A' per al càlcul de la nota si no es considera una prova fallida

            total_comprovacions_qualificables = num_ok + num_errors # Considerem OK i ERROR
            
            grade = "N/A"
            if total_comprovacions_qualificables > 0:
                # La nota és el percentatge d'OKs
                grade = (num_ok / total_comprovacions_qualificables) * 100
                grade = f"{grade:.2f}%" # Format a dos decimals
            elif num_ok == 0 and num_errors == 0 and parsed_data['data']:
                # Si hi ha comprovacions però cap és OK/ERROR (només N/A)
                grade = "N/A"
            elif not parsed_data['data']:
                # Si no hi ha dades de comprovació (fitxer buit o mal formatat)
                grade = "No Data"


            all_results[parsed_data['ip']] = {
                'data': parsed_data['data'],
                'grade': grade
            }

    unique_comprovacions = set()
    for ip, server_data in all_results.items():
        unique_comprovacions.update(server_data['data'].keys())
    
    sorted_comprovacions = sorted(list(unique_comprovacions))

    return render_template('resultats.html', 
                           all_results=all_results, 
                           comprovacions=sorted_comprovacions,
                           results_dir=RESULTS_DIR) # Passem la variable per mostrar al missatge d'error


if __name__ == '__main__':
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

    app.run(debug=True, host='0.0.0.0', port=5001)
