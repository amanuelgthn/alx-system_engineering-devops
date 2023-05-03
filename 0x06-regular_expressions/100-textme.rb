#!/usr/bin/env ruby
#The regular expression must be only matching: capital letters
fields = ARGV[0].scan(/(?<=from:|to:|flags:)(.*?)(?=\s|$)/)
puts fields.compact.join(',')
