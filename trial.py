fr = open('mdinput.md','r');
lines=[];
for line in fr:
	print(line);
	newline=line.replace('I',"ME");
	lines.append(newline);
	print(newline);
print("done reading");

fw = open('mdinput.md','w');
fw.writelines(lines);
