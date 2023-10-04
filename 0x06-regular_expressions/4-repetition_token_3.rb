#!/usr/bin/env ruby

txt = ARGV[0]

txt.scan(/hbt*?n/) do |match|
  print match
end
puts
