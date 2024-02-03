#script to edit user file limits
exec { 'set_global_nofile_soft_limit':
  command  => 'echo "holberton soft nofile 65535" >> /etc/security/limits.conf',
  provider => shell
}

exec { 'set_global_nofile_hard_limit':
  command  => 'echo "holberton hard nofile 65535" >> /etc/security/limits.conf',
  provider => shell
}
