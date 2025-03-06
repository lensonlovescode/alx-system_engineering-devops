# A puppet script that debugs a web server doing terribly under pressure
exec { 'replaceulimit':
  command => 'sed -i "s/15/1048576/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}
exec { 'restartnginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
