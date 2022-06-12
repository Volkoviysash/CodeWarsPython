inseconds = 100
hours = inseconds/3600
minutes = (inseconds%3600)/60
seconds = inseconds%60
print("%02d:%02d:%02d" % (hours, minutes, seconds))