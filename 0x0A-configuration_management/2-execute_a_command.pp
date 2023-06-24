# create a manifest file that kills a process named killmenow
# must use the exc Puppet resource
# must use pkill

exec { 'pkill':
    command => 'pkill -f killmenow',
    path    =>  '/usr/bin',
}
