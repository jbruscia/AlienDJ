from pydub import AudioSegment
secs = 10
miliInterval = 1000 * secs


wholeSong  = AudioSegment.from_wav("yelloSub.wav")
print(len(wholeSong))

i=0 
while True:
	
	startTime = i*miliInterval
	endTime = (i+1)*miliInterval

	if endTime > len(wholeSong):
		print ("safe")
		break
	
	print(startTime)	
	print "/n"
	print (endTime)
	newSnip = wholeSong[startTime:endTime]
	fileName = "out"+ str(i) + ".wav"
	newSnip.export(fileName, format="wav")
	i+=1
