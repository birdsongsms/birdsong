import winsound, sys, wave
# MAJOR
# Scale Degrees {1, 2, 3, 4, 5, 6, 7} Midi Note Numbers {0, 2, 4, 5, 7, 9, 11}
major = [0, 2, 4, 5, 7, 9, 11]
soundDir = "C:/Codedump/birdsong/sounds/"
clipDict = { \
			40: "183059__quartertone__gtrclass-00f-6s-40-v05.wav", \
			41: ".wav", \
			42: "183042__quartertone__gtrclass-02f-6s-42-v05.wav", \
			43: ".wav", \
			44: "183072__quartertone__gtrclass-04f-6s-44-v05.wav", \
			45: "182966__quartertone__gtrclass-00f-5s-45-v04.wav", \
			46: ".wav", \
			47: "183029__quartertone__gtrclass-02f-5s-47-v05.wav", \
			47: ".wav", \
			49: "183000__quartertone__gtrclass-04f-5s-49-v05.wav", \
			50: "182945__quartertone__gtrclass-00f-4s-50-v01.wav", \
			51: ".wav", \
			52: "183083__quartertone__gtrclass-02f-4s-52-v01.wav", \
			53: ".wav", \
			54: "182979__quartertone__gtrclass-04f-4s-54-v01.wav", \
			55: "182944__quartertone__gtrclass-00f-3s-55-v01.wav", \
			56: ".wav", \
			57: "183087__quartertone__gtrclass-02f-3s-57-v02.wav", \
			58: ".wav", \
			59: "183007__quartertone__gtrclass-00f-2s-59-v01.wav", \
			60: ".wav", \
			61: ".wav", \
			}
print(clipDict[42])
winsound.PlaySound('/sounds/%s.wav' % clipDict[42], winsound.SND_FILENAME)
print(clipDict[52])
winsound.PlaySound('/sounds/%s.wav' % clipDict[52], winsound.SND_FILENAME)
print(clipDict[59])
winsound.PlaySound('/sounds/%s.wav' % clipDict[59], winsound.SND_FILENAME)

