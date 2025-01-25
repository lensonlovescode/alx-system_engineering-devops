# A puppet script that kills the process killmenow
exec { 'pkill killmenow':
  path    => '/usr/bin/',
  command => 'pkill killmenow',
}
