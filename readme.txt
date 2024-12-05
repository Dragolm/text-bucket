This project is aimed at making a program that can read an entire file and replace/change it without effecting certain states of such occurance.

example usecase: "your my son" said your mother --> "your my son" said my mother.
Here the 'your' inside the quotes needed to be the same to conserve the meaning while changing the line to first person.

implemented features:
 - get your ass to work
 - be able to replace multiple words quickly
 - avoid replacing occurences that meet certain conditions

current worked on objectives/features:
 - a simple ui to input the replacable words
 - delete words/strings that meet certain conditions

bugs:
 - wont work if the condition for noreplacment is a single word or alone. eg " won't but "hi will
 - wont work if the condition for noreplacment is inbetween a word
