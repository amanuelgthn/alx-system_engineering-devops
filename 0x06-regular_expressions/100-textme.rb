#!/usr/bin/env ruby
#The regular expression must be only matching: capital letters
Retrieve = ARGV[0].scan(/from:(.\w+)|to:(.\w+)|flags:([0-9:-]+)/)
puts [Retrieve[0].compact, Retrieve[1].compact, Retrieve[2].compact].join(',')
