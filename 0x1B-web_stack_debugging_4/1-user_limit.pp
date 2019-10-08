# Changes too many files error
exec { 'replace hard limit':
  command => "sed -i 's/holberton hard nofile 5/holberton hard nofile 4096/' /etc/security/limits.conf",
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}
-> exec { 'replace soft limit':
  command => "sed -i 's/holberton soft nofile 4/holberton soft nofile 1024/' /etc/security/limits.conf",
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}
-> exec { 'restarting':
  command => 'sudo sysctl -p',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}
