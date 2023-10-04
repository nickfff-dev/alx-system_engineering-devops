#!/usr/bin/env ruby

txt = ARGV[0]

txt.scan(/h[b]?tn/) do |match|
  print match
end
puts
