# A puppet script that installs version flask v2.1.0 on a node
exec {'pip3 install flask':
  require => Exec['python-installed'],
  command => '/usr/bin/pip3 install flask==2.1.0'
}
exec {'python-installed':
  command => '/usr/bin/which python3'
}
