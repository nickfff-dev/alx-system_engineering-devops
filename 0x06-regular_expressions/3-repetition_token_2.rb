#!/usr/bin/env ruby

txt = ARGV[0]

txt.scan(/hb[t]{1,}n/) do |match|
  print match
end
puts
