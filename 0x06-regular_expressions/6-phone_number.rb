#!/usr/bin/env ruby

txt = ARGV[0]

txt.scan(/^[0-9][0-9]{9}/) do |match|
  print match
end
puts
