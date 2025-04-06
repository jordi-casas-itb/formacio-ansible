#Instal·lar la llibreria per a la gestió de passwords (error - : Unable to encrypt nor hash, passlib must be installed. No module named 'passlib'. Unable to encrypt nor hash, passlib must be installed. No module named 'passlib')
sudo apt install python3-passlib

#Executar el playbook cridant el VAULT: 
ansible-playbook -i inventory.ini crear_usuari.yml --become --ask-vault-pass
