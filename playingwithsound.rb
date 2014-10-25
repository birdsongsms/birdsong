#!/bin/env ruby
# encoding: utf-8
require 'win32/sound'
include Win32
asciiChars = []
inputString = "thisisastringthatiwanttomakelonger to test mor!!£$%215235352412P{}@P_+-=-';/;["

soundDir = "sounds/"
h = { 
	0 => "birds0.wav", 
	1 => "birds1.wav",
	2 => "birds2.wav",
	3 => "birds3.wav", 
	4 => "birds4.wav"
}

puts h.fetch(1)
inputChars = inputString.split(//)
inputChars.each do |char|
	asciiChars.push(char.ord)
end

asciiChars.each do |ascii|
	sound= soundDir+h.fetch(ascii%5)
	Sound.play(sound,Sound::ASYNC)
	puts sound

end

#Sound.play("sounds/birds011")

