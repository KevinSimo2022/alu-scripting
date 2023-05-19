#!/usr/bin/env ruby

regex = /School/i

input_string = ARGV[0]

if match = input_string.match(regex)
  puts match[0]
else
  puts input_string
end
