#!/usr/bin/env ruby

txt = ARGV[0]

txt.scan(/^h\wn$/) do |match|
  print match
end
puts
