import winsound, sys, wave
# MAJOR
# Scale Degrees {1, 2, 3, 4, 5, 6, 7} Midi Note Numbers {0, 2, 4, 5, 7, 9, 11}
major = [0, 2, 4, 5, 7, 9, 11]
soundDir = "C:/Codedump/birdsong/sounds/"
clipDict = { \
			40: "40-G.wav", \
			41: "birds011.wav", \
			42: "43-G.wav", \
			43: "birds011.wav", \
			44: "44-G.wav", \
			45: "45-G.wav", \
			46: "birds011.wav", \
			47: "47-G.wav", \
			47: "birds011.wav", \
			49: "49-G.wav", \
			50: "50-G.wav", \
			51: "birds011.wav", \
			52: "52-G.wav", \
			53: "birds011.wav", \
			54: "54-G.wav", \
			55: "55-G.wav", \
			56: "birds011.wav", \
			57: "57-G.wav", \
			58: "birds011.wav", \
			59: "59-G.wav", \
			60: "birds011.wav", \
			61: "birds011.wav", \
			}
print(clipDict[42])
winsound.PlaySound('/sounds/%s.wav' % clipDict[42], winsound.SND_FILENAME)
print(clipDict[52])
winsound.PlaySound('/sounds/%s.wav' % clipDict[52], winsound.SND_FILENAME)
print(clipDict[59])
winsound.PlaySound('/sounds/%s.wav' % clipDict[59], winsound.SND_FILENAME)

