# Comment: Current task puppet install, file and rewrite 301 and restart server
exec { 'update server':
  command => '/usr/bin/apt-get update',
}
-> package { 'nginx':
  ensure => present,
}
-> file { '/etc/nginx/sites-available/default':
  ensure => present,
}
-> file_line { 'rewrite a line':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "   location / {
        add_header X-Served-By ${hostname};",
  match  => '^\tlocation / {',
}
-> exec { 'initialize server':
  command => '/usr/sbin/service nginx restart',
}
