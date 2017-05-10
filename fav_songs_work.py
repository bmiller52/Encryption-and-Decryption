#!/usr/bin/python
from simplecrypt import encrypt, decrypt
from os.path import exists

filename = 'encrypted.txt'

def main():
	if exists(filename):
		print("reading...")
		print(' ')
        data = read_encrypted(filename).split(' ')
        for items in data:
        	print('- ' + "%s" % items)

def read_encrypted(filename, string=True):
	with open(filename, 'rb') as input:
		ciphertext = input.read()
		plaintext = decrypt(input, ciphertext)
		if string:
			return plaintext.decode('utf8')
		else:
			return plaintext

def write_encrypted(filename):
    with open(filename, 'w+b') as output:
        ciphertext = encrypt(output, ' '.join(songs))
        output.write(ciphertext)

songs = []

print(' ')
print('Here\'s the last saved data')

main()

print (' ')
print ('Type in your favorite songs.')
print ('When finished type done.')

while True:

	asker = raw_input('> ').lower()

	if asker == 'done':
		break

	songs.append(asker)

	continue

print(' ')
print('Here\'s your song list:')

for song in songs:
	print('- ' + song)

write_encrypted(filename)
