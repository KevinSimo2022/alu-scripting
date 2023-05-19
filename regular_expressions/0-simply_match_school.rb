#!/usr/bin/env ruby

regex = /School/

input_string = ARGV[0]

if input_string =~ regex
  puts "School"
else
  puts input_string
end
