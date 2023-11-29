#!/usr/bin/env ruby
puts ARGV[0].scan(/(\w+),(\+?\d{11})(-1:0:-1:0:-1)/).join
