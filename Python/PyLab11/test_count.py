import pytest
#Part 1 
def count(sequence, item):
	sum = 0
	for n in sequence:
		if n == item:
			sum += 1
	return sum albumsList = ["David Bowie", "Space Oddity", "Hunky Dory", "The Man Who Sold The World", "The Rise and Fall of Ziggy Stardust and the Spiders from Mars", "Aladdin Sane", "Diamond Dogs", "Young Americans", "Station to Station", "Low", "Heroes", "Lodger"]yearsList = [1964, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979] # = 23678albumsAndYearsList = [1964,"David Bowie",1969,"Space Oddity"]def test_countStringList():	assert count(albumsList,"Young Americans")== 1def test_countNumsList():	assert count(yearsList,1972)== 1def test_countStringsAndNumsList():	assert count(albumsAndYearsList,1969)== 1	assert count(albumsAndYearsList,"David Bowie")== 1