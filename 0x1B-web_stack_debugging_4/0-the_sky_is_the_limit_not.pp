# A puppet script that debugs a web server doing terribly under pressure
exec { "replaceulimit":
  command => "/bin/sed -i 's/15/1048576/' /etc/default/nginx",
}
