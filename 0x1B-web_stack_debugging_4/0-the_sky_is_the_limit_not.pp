# change limits to open file
exec { 'replace the limit':
  command => "sed -i 's/15/4096/g' /etc/default/nginx",
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}
-> exec { 'restarting':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}
