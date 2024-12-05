words=[];
para=[];
replaceables={"I":"you", "my":"your"};
flag=False;
open("output.txt","w").close();
with open('input.txt','r') as inp, open('output.txt', 'a') as out:
	for line in inp:
		para.append(line.split());
	for words in para:
		for word in words:
			if(word[0]=='"' or flag== True):
				out.write(word+" ");
#				out.write("\n");
				flag=True;
			else:
				if word in replaceables:
					out.write(replaceables.get(word)+" ");
#					out.write("\n");
				else:
					out.write(word+" ");
#					out.write("\n");
			if(word[-1]=='"'):
				flag = False;
		out.write("\n");
#print(words);
