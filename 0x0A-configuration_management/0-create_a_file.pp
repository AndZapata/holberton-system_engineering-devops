# coment: The current task creates a File in the /tmp path
file { '/tmp/holberton':
  mode    =>  '0744',
  owner   =>  'www-data',
  group   =>  'www-data',
  content =>  'I love Puppet',
}
