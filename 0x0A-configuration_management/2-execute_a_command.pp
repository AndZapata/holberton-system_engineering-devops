# Coment: The current task terminate the script killmenow
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}
