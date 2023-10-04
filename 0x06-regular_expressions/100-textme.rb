#!/usr/bin/env ruby

# Get the log line from the command line argument
log_line = ARGV[0]

# Use regular expressions to extract the sender, receiver, and flags
sender = log_line[/\[from:(.+?)\]/, 1]
receiver = log_line[/\[to:(.+?)\]/, 1]
flags = log_line[/\[flags:(.+?)\]/, 1]

# Output the extracted information
puts "#{sender},#{receiver},#{flags}"
