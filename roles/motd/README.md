motd
=========
This Role will be used to configure motd on hosts where the /etc/motd will contain the hostname the date time 
Requirements
Role Variables
--------------
The system owner is a variable that should be defined inside your playbook it is defined in the /defaults/main.yml

----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: motd, system_owner: user@example.com }

