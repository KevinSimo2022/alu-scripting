#!/usr/bin/env ruby

regex = /School/
string = ARGV[0]

if string =~ regex
  puts "School"
else
  puts ""
end
