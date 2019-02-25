# This file will be excersises having to do with Arrays and working with them.

# 3.1 Names

names = ['Ruth', 'Mike', 'Tyler', 'John', 'Steve']

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

# 3.2 Greetings

greeting0 = "Hello " + names[0] + ", how are you?"
greeting1 = "Hello " + names[1] + ", how are you?"
greeting2 = "Hello " + names[2] + ", how are you?"
greeting3 = "Hello " + names[3] + ", how are you?"
greeting4 = "Hello " + names[4] + ", how are you?"

print(greeting0)
print(greeting1)
print(greeting2)
print(greeting3)
print(greeting4)

# 3.3 Your own list

favorites = ["pizza", "Jeep", "Macbook", "Razer"]

facts_0 = "I really love " + favorites[0] + "."
facts_1 = "I love Mini Cooper, but my " + favorites[1] + " is the best."
facts_2 = "I have a conflict on wether I want a " + favorites[2] + " or a " + favorites[3] 

print(facts_0)
print(facts_1)
print(facts_2)

# 3.4 Guest List

guest_list = ["Amigo Fiel", "Atalia", "Mami", "Papi", "Moises", "Jose", "Loli", "Abuelita Mami"]

invite_grandparents = "\nDear " + guest_list[0] + " and " + guest_list[7] + ", I hope you can make it to dinner tonight.."
invite_parents = "\nDear " + guest_list[2] + " and " + guest_list[3] + ", I hope you can make it to dinner tonight?"
invite_inlaws = "\nDear " + guest_list[4] + " and " + guest_list[5] + " and " + guest_list[6] + ", I hope you can make it to dinner tonight?"
invite_wife = "\nDear " + guest_list[1] + ", I hope you can make it to dinner tonight?"

invitations = invite_grandparents + invite_inlaws + invite_parents + invite_wife

print(invitations)
 
# 3.5 Changing Guest List

unfortunate =  guest_list[0] + " is deceased so he cannot make it.."

print(unfortunate)

guest_list.remove("Amigo Fiel")
guest_list.insert( 0, "Vea" )

invite_sibling_grandma = "\nDear " + guest_list[0] + " and " + guest_list[7] + ", I hope you can make it to dinner tonight.."
invite_parents = "\nDear " + guest_list[2] + " and " + guest_list[3] + ", I hope you can make it to dinner tonight?"
invite_inlaws = "\nDear " + guest_list[4] + " and " + guest_list[5] + " and " + guest_list[6] + ", I hope you can make it to dinner tonight?"
invite_wife = "\nDear " + guest_list[1] + ", I hope you can make it to dinner tonight?"

new_invitations = invite_sibling_grandma + invite_inlaws + invite_parents + invite_wife

print(guest_list)
print(new_invitations)

# 3.6 More Guests

guest_list.insert(0, "Tyler Phillips")
guest_list.insert(4, "William Mathews")
guest_list.append("Penelope Von Schweetz")

print(guest_list)

invite_friends = "\nDear " + guest_list[0] + " and " + guest_list[4] + ", I hope you can make it to dinner tonight.."
invite_parents = "\nDear " + guest_list[3] + " and " + guest_list[5] + ", I hope you can make it to dinner tonight?"
invite_inlaws = "\nDear " + guest_list[6] + " and " + guest_list[7] + " and " + guest_list[8] + ", I hope you can make it to dinner tonight?"
invite_wife = "\nDear " + guest_list[2] + ", I hope you can make it to dinner tonight?"
invite_sister_grandma = "\nPlease come " + guest_list[9] + ", Oh and you too " + guest_list[1] + "."

updated_invitation = invite_friends + invite_parents + invite_inlaws + invite_sister_grandma + invite_wife

print(updated_invitation)


# 3.7 Shrinking Guest List 

table_issue = " The table has arrived so I can only have two guests..."

sorry = "\nSorry " + guest_list[0] +  ", due to the unexpected lack of table we will not need you to come to the dinner any more."
sorry1 = "\nSorry " + guest_list[1] + ", due to the unexpected lack of table we will not need you to come to the dinner any more."
sorry2 = "\nSorry " + guest_list[2] + ", due to the unexpected lack of table we will not need you to come to the dinner any more."
sorry3 = "\nSorry " + guest_list[3] +  ", due to the unexpected lack of table we will not need you to come to the dinner any more."
sorry4 = "\nSorry " + guest_list[4] +  ", due to the unexpected lack of table we will not need you to come to the dinner any more."
sorry5 = "\nSorry " + guest_list[5] +  ", due to the unexpected lack of table we will not need you to come to the dinner any more."
sorry6 = "\nSorry " + guest_list[6] +  ", due to the unexpected lack of table we will not need you to come to the dinner any more."
sorry7 = "\nSorry " + guest_list[7] +  ", due to the unexpected lack of table we will not need you to come to the dinner any more."
sorry8 = "\nSorry " + guest_list[8] +  ", due to the unexpected lack of table we will not need you to come to the dinner any more."

excuse = sorry + sorry1 + sorry2 + sorry3 + sorry4 + sorry5 + sorry6 + sorry7 + sorry8

print(excuse)

guest_list.pop(0)
guest_list.pop(1)
guest_list.pop(2)
guest_list.pop(3)
guest_list.pop(4)
guest_list.pop(5)
guest_list.pop(4)
guest_list.pop(3)
guest_list.pop(2)

print(guest_list)

congratulations = "Congrats! " + guest_list[0] + " and " + guest_list[1] + ", youre still invited."

print(congratulations)

guest_list.remove("Vea")
guest_list.remove("Mami")

print(guest_list)

# 3.8 Seeing the World

locations = ["Japan", "China", "Brazil", "Africa", "Euorpe"]

print(locations)

print(sorted(locations))
print(locations)

locations.reverse()
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort()
locations.reverse()
print(locations)

# Dinner Guests

len(guest_list)

# 3.10 Every Function

languages = []

languages.append("C#")
languages.append("Java")
languages.append("Python")
languages.append("Swift")
languages.append("Ruby")

code_Languages = "These are some programming languages: "

print(code_Languages)
print(languages)

statement_1 = " These are some programmming languages: " + "\n\t" + languages[0] + "\n\t" + languages[1] + "\n\t" + languages[2] + "\n\t" + languages[3] + "\n\t" + languages[4] 

print(statement_1)

statement_2 = " I was never interested in ruby.. so my prefered languages are these: "

languages.remove("Ruby")

print(statement_2)
print(languages)

statement_3 = "If I had to pick an order to learn them it would be like this: "

sorted(languages)
languages.reverse()

print(statement_3)
print(languages)

statement_4 = "If I could add one language it would be Cobol"

print(statement_4)

languages.insert(0, 'Cobol')

print(languages)

statement_5 = "But thats too many languages to learn at once... so Ill take out a few"

del languages[1]
del languages[0]
languages.pop(2)

full_statement = statement_5 

print(full_statement)
print(languages)






