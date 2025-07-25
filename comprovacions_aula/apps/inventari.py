# app.py
# Jordi Casas - 10/7/2025
# Codi generat per Gemini i adaptat a les necessitats.

from flask import Flask, request, jsonify, render_template, redirect, url_for
import os

app = Flask(__name__)

# Ruta del fitxer d'inventari d'Ansible
INVENTORY_FILE = 'inventory.ini'

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Gestiona la pàgina principal amb el formulari.
    - GET: Mostra el formulari.
    - POST: Processa les dades del formulari i afegeix el servidor a l'inventari.
    """
    message = None
    error = None

    if request.method == 'POST':
        # Obtenim les dades del formulari
        server = request.form.get('server')
        ip = request.form.get('ip')
        usuari = request.form.get('usuari')
        contrasenya = request.form.get('contrasenya')
        distro_type = request.form.get('distro_type')

        if not all([server, ip, usuari, contrasenya]):
            error = "Falten paràmetres obligatoris: Servidor, IP, Usuari, Contrasenya."
        else:
            # Generar línies diferents en funció de la distribució utilitzada
            # Canvia el mètode per escalar privilegis
            if distro_type == 'Ubuntu':
                inventory_line = f"\n{server} ansible_host={ip} ansible_user={usuari} ansible_password={contrasenya} ansible_sudo_pass={contrasenya} ansible_become_method=sudo\n"
            elif distro_type == 'Alpine':
                inventory_line = f"\n{server} ansible_host={ip} ansible_user={usuari} ansible_password={contrasenya} ansible_doas_pass={contrasenya} ansible_become_method=doas\n"

            try:
                # Afegim la línia al fitxer d'inventari
                with open(INVENTORY_FILE, 'a') as f:
                    f.write(inventory_line)
                message = f"Servidor '{server}' (IP: {ip}) afegit correctament a {INVENTORY_FILE}."
            except IOError as e:
                app.logger.error(f"Error escrivint al fitxer d'inventari: {e}")
                error = f"No s'ha pogut escriure al fitxer d'inventari: {e}"

    return render_template('index.html', message=message, error=error)


# Endpoint opcional per a API si encara el vols mantenir
@app.route('/afegir_servidor_api', methods=['POST'])
def afegir_servidor_api():
    """
    Endpoint API per afegir servidors via JSON (si vols mantenir aquesta funcionalitat).
    """
    if not request.is_json:
        return jsonify({"error": "La petició ha de ser JSON"}), 400

    data = request.get_json()
    server = data.get('server')
    ip = data.get('ip')
    usuari = data.get('usuari')
    contrasenya = data.get('contrasenya')
    distro_type = data.get('distro_type')

    if not all([server, ip, usuari, contrasenya]):
        return jsonify({"error": "Falten paràmetres obligatoris: server, ip, usuari, contrasenya"}), 400

    # Generar línies diferents en funció de la distribució utilitzada
    if distro_type == 'Ubuntu':
        inventory_line = f"\n{server} ansible_host={ip} ansible_user={usuari} ansible_password={contrasenya} ansible_sudo_pass={contrasenya} ansible_become_method=sudo\n"
    elif distro_type == 'Alpine':
        inventory_line = f"\n{server} ansible_host={ip} ansible_user={usuari} ansible_password={contrasenya} ansible_doas_pass={contrasenya} ansible_become_method=doas\n"

    try:
        with open(INVENTORY_FILE, 'a') as f:
            f.write(inventory_line)
        return jsonify({"missatge": f"Servidor '{server}' afegit a {INVENTORY_FILE}"}), 200
    except IOError as e:
        app.logger.error(f"Error escrivint al fitxer d'inventari: {e}")
        return jsonify({"error": f"No s'ha pogut escriure al fitxer d'inventari: {e}"}), 500


if __name__ == '__main__':
    # Crear el fitxer d'inventari si no existeix
    if not os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'w') as f:
            f.write("# Inventari d'Ansible generat per Flask\n")

    app.run(debug=True, host='0.0.0.0', port=5000)
