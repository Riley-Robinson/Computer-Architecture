
#Print out all of the strings in the following array in alphabetical order sorted by the middle letter of each string, each on a separate line. If the word has an even number of letters, choose the later letter, i.e. the one closer to the end of the string. (python solution, please)

lst = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

#The expected output is: 'Cha Cha' 'Paso Doble' 'Viennese Waltz' 'Waltz' 'Samba' 'Rumba' 'Tango' 'Foxtrot' 'Jive'

# for ele in sorted(lst):

# ele = "".join(sorted_characters)
#     print(ele)

lst.sort()

print("sorted list is",lst)

print