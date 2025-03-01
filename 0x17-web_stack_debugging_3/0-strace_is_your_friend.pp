# A puppet script that fixes a wordpress internal server error
exec { 'fixinternalservererror':
  command => "/bin/sed -i 's/class-wp-locale.phpp/class-wp-locale.php/1' /var/www/html/wp-settings.php"
}
