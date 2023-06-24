# create a manifest file that kills a process named killmenow
# must use the exc Puppet resource
# must use pkill

exec { 'kill-killmenow':
    command => 'pkill -9 killmenow',
}
