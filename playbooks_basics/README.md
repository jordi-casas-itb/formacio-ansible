#Instal·lar la llibreria per a la gestió de passwords (error - : Unable to encrypt nor hash, passlib must be installed. No module named 'passlib'. Unable to encrypt nor hash, passlib must be installed. No module named 'passlib')
```bash
sudo apt install python3-passlib
```

#Crear el vault
El fitxer es crea a group_vars/all amb la següent comanda:
```bash
ansible-vault create vault.yml
```

I en aquest moment demana una password per protegir-lo.

#Editar el contingut del vault
```bash
ansible-vault edit vault.yml
```

#Executar el playbook cridant el VAULT:
```bash 
ansible-playbook -i inventory.ini crear_usuari.yml --become --ask-vault-pass
```
