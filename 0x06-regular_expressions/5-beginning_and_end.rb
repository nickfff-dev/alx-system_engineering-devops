#!/usr/bin/env ruby

txt = ARGV[0]

txt.scan(/h[A-Za-z0-9]n/) do |match|
  print match
end
puts
