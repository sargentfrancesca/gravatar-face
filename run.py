import csv
import hashlib, urllib, time, re
import os
from hashclass import AvatarHash

def getCSV():
	with open('results.csv', 'rU') as csvfile:
		print "Opening CSV..."
		fileread = csv.reader(csvfile, delimiter=',', quotechar='"')
		allFaces = []

		for i, row in enumerate(fileread):
			print "Reading row: ", i
			if i != 0:
				print "Adding row", i, "to array..."
				allFaces.append({'File' : row[0], 'First_Eye_X' : row[7], 'First_Eye_Y' : row[8], 'FrontalFace_X' : row[10], 'FrontalFace_Y' : row[11], 'FrontalFace_Width' : row[12], 'FrontalFace_Height' : row[13], 'Gender' : row[14], 'Second_Eye_X' : row[15], 'Second_Eye_Y' : row[16] })
		
		return allFaces


def generateGravs(avatar_hash, typeof):
	url = "http://www.gravatar.com/avatar/"+avatar_hash+"?s=300&d="+typeof+"&r=g"
	return url 

def getHashUrl(aobject):
	a = aobject
	avatar_hash = a.avatar_hash

	identicon = generateGravs(avatar_hash, "identicon")
	retro = generateGravs(avatar_hash, "retro")
	monster = generateGravs(avatar_hash, "monsterid")

	ts = int(time.time())

	print "Generated URL for "+ a.username+": ", identicon

	for filename in os.listdir("."):
		if filename.startswith("face"):
			os.rename(filename, 'img/raw/'+a.username+'_face_'+str(ts)+'.png')
		else:
			continue
	
	
	urllib.urlretrieve(identicon, 'img/raw/'+a.username+'_identicon_'+str(ts)+'.png')
	urllib.urlretrieve(retro, 'img/raw/'+a.username+'_retro_'+str(ts)+'.png')
	urllib.urlretrieve(monster, 'img/raw/'+a.username+'_monster_'+str(ts)+'.png')

	return identicon

def createHash():
	print "creating hashes"
	faces = getCSV()

	for face in faces:
		hashjuice = face['Gender'] + str(face['First_Eye_X']) + str(face['First_Eye_Y']) + str(face['FrontalFace_Width']) + str(face['FrontalFace_Height']) + str(face['Second_Eye_X']) + str(face['Second_Eye_Y'])
		print "Concatenation of facial values", hashjuice
		print "Hashing facial values.."
		# avatar_hash = hashlib.md5(hashjuice.encode('utf-8')).hexdigest()

		#Putting string directly into URL
		avatar_hash = hashjuice
		print avatar_hash

		username_input = raw_input("What is your name? : ")
		username = re.sub(r'\W+', '', username_input)

		a = AvatarHash(username, face['File'], face['Gender'], face['First_Eye_X'], face['First_Eye_Y'], face['FrontalFace_X'], face['FrontalFace_Y'], face['FrontalFace_Width'], face['FrontalFace_Height'], face['Second_Eye_X'], face['Second_Eye_Y'], hashjuice, avatar_hash, '')

		a.avatar_url = getHashUrl(a)

createHash()