# Coment: The current task terminate the script killmenow
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/',
}
