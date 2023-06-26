#configuration using a puppet file
exec { 'configure-ssh-client':
  command => 'echo "Host *\n  IdentityFile ~/.ssh/school\n  PassWordAuthentication no" >> ~/.ssh/config',
  path => '/usr/bin:/bin',
}
