invitedGuests = []

invitedGuests.insert(0,"cody")
invitedGuests.insert(1,"logan")
invitedGuests.append("jayden")

print(f"inviting {invitedGuests[0]} to the dinner")
print(f"inviting {invitedGuests[1]} to the dinner")
print(f"inviting {invitedGuests[2]} to the dinner")

print("\nbigger table obtained, larger party size in return. \n")

invitedGuests.insert(0,"nathan m.")
invitedGuests.insert(2,"nathan a.")
invitedGuests.append("lua")

for guest in invitedGuests: #newer way for loops damn im outdated
    print(f"now inviting {guest} to the dinner")

print("\nTable wont arrive in time for dinner unfortunally, can only support 2 people \n")

print(invitedGuests)

for guest in range(2,len(invitedGuests)): #funky
    kickingOut = invitedGuests.pop()
    print(invitedGuests)
    print(f"sorry, {kickingOut} you cant come. theres not enough room as the table got delayed, maybe next time?")

print("\n")

for remainingguests in invitedGuests:
   print(f"{remainingguests} you are still invited.")

invitedGuests.clear()

print(invitedGuests)
