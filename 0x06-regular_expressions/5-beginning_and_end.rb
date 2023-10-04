#!/usr/bin/env ruby

txt = ARGV[0]

txt.scan(/^h.n$/) do |match|
  print match
end
puts
