# Verificacio d'activitats d'aula

Aquest projecte pretén fer un PoC d'utilitzar Ansible per a fer verificacions a sistemes d'estudiants.

REQUISITS PREVIS
----------------
Es requereix un sistema que serà el node de comprovació que es connecta per SSH als equips que es verificaran.
En aquest node, instal.lar Ansible en un entorn Linux (ansible, ansible-core) o bé en un entorn WSL de Windows (mòdul de Linux per a windows) i Python3.
Per verificar que Ansible funciona: ```ansible --version```

Cal que hi hagi connectivitat entre el node de comprovació i les màquines a verificar per SSH, i un usuari i contrasenya amb privilegis.

En el mateix repositori hi ha material de formació d'Ansible, amb playbooks bàsics per a aprendre a utilitzar-lo.
Ansible requereix d'un fitxer inventory.ini que és el que conté l'inventari dels equips a comprovar. 

APLICACIONS DE SUPORT
---------------------
S'han generat dues aplicacions.

Per a obtenir l'inventari, s'ha generat una aplicació en Flask que recull les dades dels sistemes, els estudiants les poden informar.


APLICACIÓ D'INVENTARI
---------------------

Aplicació amb Flask generada per Gemini i customitzada a les necessitats.
Recull les informacions dels estudiants i afegeix les línies al fitxer inventory.ini de l'arrel del projecte.

* Instal·lar el mòdul env de python: ```apt install python3.12-venv```
* Crear un virtual enviroment de python: ```python3 -m venv flask```
* Activar l’entorn virtual de python: ```source flask/bin/activate```
* Instal·lar els requirements: ```pip install -r requirements.txt```
* Executar l’aplicació: ```python3 apps/inventari.py```
* Per sortir de l’entorn: ```deactivate```

Per accedir a l'aplicació: http://x.x.x.x:5000 (on x.x.x.x és la IP del node de comprovació)

APLICACIÓ DE MOSTRAR RESULTATS
------------------------------

Aplicació amb Flask generada per Gemini i customitzada a les necessitats.
A partir dels TXT que generen els playbooks (directori resultats), crea una taula resum.
S'utilitza el mateix entorn virtual creat al punt anterior anomenat flask.

* Executar l’aplicació: ```python3 apps/resultats.py```

Per accedir a l'aplicació: http://x.x.x.x:5001 (on x.x.x.x és la IP del node de comprovació)

PER A EXECUTAR ELS PLAYBOOKS
----------------------------

Hi ha un playbook d'exemple que invoca les diferents tasques. 
Les tasques estan organitzades dins del directori tasks i separades per funcionalitats.
En la documentació de cada tasca s'indica quina variable espera (si és el cas) i quin valor retorna (si és el cas).

Des del directori arrel del projecte es pot provar l'execució del playbook de mostra:

```ansible-playbook playbooks/comprovacions.yml```

Els resultats si ha funcionat es guarden al directori resultats en mode TXT