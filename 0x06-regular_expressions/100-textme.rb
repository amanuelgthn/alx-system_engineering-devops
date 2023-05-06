#!/usr/bin/env ruby
#The regular expression must be only matching: capital letters
scrap = ARGV[0].scan(/(?<=from:|to:|flags:)(.*?)(?=\s|$)/)
fields = [(scrap[0]%?),(scrap[1]%?),(scrap[2]%?)]
puts fields.join(',')
