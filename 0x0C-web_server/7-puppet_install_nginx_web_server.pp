# Comment: Current task puppet install, file and rewrite 301 and restart server
package { 'nginx':
  ensure => present,
}
-> file { 'path to create':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Holberton School'
}
-> file { '/etc/nginx/sites-available/default':
  ensure => present,
}
-> file_line { 'rewrite a line'
  ensure => present,
  path => '/etc/nginx/sites-available/default',
  line => 'server {
	rewrite ^/redirect_me https://https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  match => '^server {',
}
-> exec { 'initialize server'
  command => '/usr/sbin/service nginx restart',
}
