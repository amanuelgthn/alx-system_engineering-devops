#!/usr/bin/env ruby
#The regular expression must be only matching: capital letters
scrap = ARGV[0].scan(/from:(.\w+)|to:(.\w+)|flags:([0-9:-]+)/)
fields = [scrap[0].compact,scrap[1].compact,scrap[3].compact]
puts fields.join(',')
