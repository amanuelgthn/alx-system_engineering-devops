#!/usr/bin/env ruby
#The regular expression must be only matching: capital letters
scrap = ARGV[0].scan(/from:(.\w+)|to:(.\w+)|flags:([0-9:-]+)/)
fields = [scrap[0],scrap[1],scrap[3]]
puts fields.compact.join(',')
