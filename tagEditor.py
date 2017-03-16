import glob
import songdetails

song = glob.glob('*.mp3')

number = len(song)

for i in range(number):
	print song[i]
	name = songdetails.scan(song[i])
	print name.title
	print name.artist
	print name.duration
	print "\n"
	name.artist = u'Ed Sheeran'
	name.save()

