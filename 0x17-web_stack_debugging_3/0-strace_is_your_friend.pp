# using strace fixing and automatic
exec { 'sed':
  command => 'sed -i "s|.phpp|.php|" /var/www/html/wp-settings.php',
  path    => '/bin/'
}