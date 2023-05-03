#!/usr/bin/env ruby
#The regular expression must be only matching: capital letters
scrap = ARGV[0].scan(/(?<=from:|to:|flags:)(.*?)(?=\s|$)/)
fields = [scrap[0].scan(/%?/),scrap[1].scan(/%?/),scrap[2].scan(/%?/)]
puts fields.join(',')
