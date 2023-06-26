#configuration using a puppet file
exec { 'ssh_config':
  path => '/bin',
  command => 'echo "IdentityFile ~/.ssh/school\n  PassWordAuthentication no" >> ~/.ssh/config',
  }
