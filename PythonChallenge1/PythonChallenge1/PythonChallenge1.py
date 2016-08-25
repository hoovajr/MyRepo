coded_string  = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq \
ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr \
gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

intab = ''
outtab = ''

for x in range(97, 123):
	intab += chr(x)

outtab = intab[2:] + intab[0:2]
trantab = str.maketrans(intab, outtab)

print(coded_string.translate(trantab))