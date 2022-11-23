#!/usr/bin/expect

# logging into ssh

set index 1;

spawn bash ssh_command.sh $index
expect { 
    "*?onnection refused" {
        spawn sudo ./ssh.exp $index
    }
}