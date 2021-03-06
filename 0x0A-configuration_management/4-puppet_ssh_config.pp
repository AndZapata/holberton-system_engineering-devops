# Comment: Current task modify file-config ssh
file { '/etc/ssh/ssh_config':
  ensure => symlink,
  target => '/etc/ssh/ssh_config',
  file_line { 'Turn off passwd auth':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    match  => '^PasswordAuthentication',
  }
  file_line { 'Declare identity file':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/holberton',
    match  => '^IdentityFile',
  }
}
