# A puppet script that fixes a bug for a wordpress web server returning an internal web server error

exec { 'fixinternalservererror':
  command => sed -i 's/class-wp-locale.phpp/class-wp-locale.php/1' /var/www/html/wp-settings.php
}
