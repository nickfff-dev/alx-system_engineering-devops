#!/usr/bin/env ruby

txt = ARGV[0]

txt.scan(/School/) do |match|
  print "#{match}"
end
puts
