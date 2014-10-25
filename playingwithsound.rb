#!/bin/env ruby
# encoding: utf-8
require 'win32/sound'
include Win32
asciiChars = []
inputString = "thisisastringthatiwanttomakelonger to test mor!!£$%215235352412P{}@P_+-=-';/;["

h = { 
	0 => "0.wav", 
	1 => "1.wav",
	2 => "2.wav" }

puts h.fetch(1)
inputChars = inputString.split(//)
inputChars.each do |char|
	asciiChars.push(char.ord)
end

asciiChars.each do |ascii|
	puts ascii%12
end

Sound.play("sounds/birds011.wav")
Sound.play("sounds/birds011.wav")

