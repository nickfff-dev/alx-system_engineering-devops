#!/usr/bin/env ruby

txt = ARGV[0]

txt.scan(/[A-Z]/) do |match|
  print match
end
puts
