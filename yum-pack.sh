#!/bin/bash
ansible -m yum_repository -a 'name=EX407 file=repository1 description="Ex407-Description" baseurl=http://content.example.com/rhel8.0/x86_64/dvd/BaseOS/ gpgcheck=yes gpgkey=http://content.example.com/rhel8.0/x86_64/dvd/RPM-GPG-KEY-redhat-release enabled=true state=absent' all
ansible -m yum_repository -a 'name=EXX407 file=repository2 description="Exx407 Description" baseurl=http://content.example.com/rhel8.0/x86_64/dvd/AppStream/ gpgcheck=yes gpgkey=http://content.example.com/rhel8.0/x86_64/dvd/RPM-GPG-KEY-redhat-release enabled=true state=absent' all

