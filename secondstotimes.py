inseconds = 1
output = []
stroutput = ""

#calculating years
years = inseconds // 31536000
inseconds = inseconds % 31536000
if years == 1: output.append("1 year")
elif years > 1: output.append(str(years) + " years")

#calculating days
days = inseconds // 86400
inseconds = inseconds % 86400
if days == 1: output.append("1 day")
elif days > 1: output.append(str(days) + " days")

#calculating hours
hours = inseconds // 3600
inseconds = inseconds % 3600
if hours == 1: output.append("1 hour")
elif hours > 1: output.append(str(hours) + " hours")

#calculating minutes
minutes = inseconds // 60
if minutes == 1: output.append("1 minute")
elif minutes > 1: output.append(str(minutes) + " minutes")

#calculating seconds
inseconds = inseconds % 60
if inseconds == 1: output.append("1 second")
elif inseconds > 1: output.append(str(inseconds) + " seconds")

if len(output) > 1:
    indx = 0
    while indx < len(output):
        if indx == len(output) - 1:
            stroutput = "%s and %s " % (stroutput[:-2], output[indx])
        else:
            stroutput += output[indx] + ", "
        indx+=1
elif len(output) == 1:
    stroutput += output[0]
else:
    stroutput = "now"

print(stroutput)

