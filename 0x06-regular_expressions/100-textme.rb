#!/usr/bin/env ruby
if ARGV.length == 1
  from, to, flag = ARGV[0].match(/^.*\[from:(.*?)\].*\[to:(.*?)\].*\[flags:(.*?)\].*$/i).captures
  puts "#{from},#{to},#{flag}"
  exit
end
