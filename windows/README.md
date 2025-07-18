# ANSIBLE en entorn Windows
ANSIBLE és natiu per sistemes Linux, però es pot utilitzar també a entorns Windows.
Els exemples que proposo son via SSH en entorn Windows. Hi ha l'opció de fer-ho via WinRM que de moment no he aconseguit que funcioni.

NOTA: He detectat més lentitud a l'hora d'executar els playbooks. Cal veure si és una tònica general.

INSTAL·LACIÓ OPENSSH A WINDOWS
------------------------------

Per a què es pugui connectar via SSH cal instal·lar OpenSSH a l'entorn Windows. A continuació s'indica les comandes en Powershell per a fer-ho.

``` 
Get-WindowsCapability -Name OpenSSH.Server* -Online |
    Add-WindowsCapability -Online
Set-Service -Name sshd -StartupType Automatic -Status Running

$firewallParams = @{
    Name        = 'sshd-Server-In-TCP'
    DisplayName = 'Inbound rule for OpenSSH Server (sshd) on TCP port 22'
    Action      = 'Allow'
    Direction   = 'Inbound'
    Enabled     = 'True'  # This is not a boolean but an enum
    Profile     = 'Any'
    Protocol    = 'TCP'
    LocalPort   = 22
}
New-NetFirewallRule @firewallParams

$shellParams = @{
    Path         = 'HKLM:\SOFTWARE\OpenSSH'
    Name         = 'DefaultShell'
    Value        = 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
    PropertyType = 'String'
    Force        = $true
}
New-ItemProperty @shellParams
```

Executar-ho sobre un entorn en Powershell amb permisos d'administració.

MÒDUL WINDOWS ANSIBLE
---------------------

Si dona error, verificar que el moòdul de Windows està instal·lat al node manager:

```ansible-galaxy collection install ansible.windows```

INVENTARI
---------

En el cas de l'inventari, cal canviar lleugerament alguns paràmetres. Substitueixen els paràmetres de Linux: ansible_sudo_pass i ansible_become_method. Són els següents:

```ansible_connection=ssh ansible_shell_type=powershell ansible_shell_executable=powershell.exe```

Si es vol treballar amb CMD enlloc de Powershell canviar pels següents paràmetres:

```ansible_shell_type=cmd ansible_shell_executable=cmd.exe```
