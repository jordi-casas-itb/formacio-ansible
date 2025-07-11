# Verificacio d'activitats d'aula

S'han generat dues aplicacions:

APLICACIÓ D'INVENTARI
---------------------

Aplicació amb Flask generada per Gemini i customitzada a les necessitats.
Recull les informacions dels estudiants i afegeix les línies al fitxer inventory.ini de l'arrel del projecte.

* Instal·lar el mòdul env de python: apt install python3.12-venv
* Crear un virtual enviroment de python: python3 -m venv flask
* Activar l’entorn virtual de python: source flask/bin/activate
* Instal·lar els requirements: pip install -r requirements.txt
* Executar l’aplicació: python3 apps/inventari.py
* Per sortir de l’entorn: deactivate

TODO:
* Adaptar-la a diferents sistemes clients pels paràmetres d'inventory.ini (actualment només per Alpine)


APLICACIÓ DE MOSTRAR RESULTATS
------------------------------

Aplicació amb Flask generada per Gemini i customitzada a les necessitats.
A partir dels TXT que generen els playbooks, crea una taula resum amb els resultats

* Instal·lar el mòdul env de python: apt install python3.12-venv
* Crear un virtual enviroment de python: python3 -m venv flask
* Activar l’entorn virtual de python: source flask/bin/activate
* Instal·lar els requirements: pip install -r requirements.txt
* Executar l’aplicació: python3 apps/resultats.py
* Per sortir de l’entorn: deactivate


PER A EXECUTAR ELS PLAYBOOKS
----------------------------

Des del directori arrel del projecte:

ansible-playbook playbooks/comprovacions.yml

