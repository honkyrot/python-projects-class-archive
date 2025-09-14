invitedGuests = []

invitedGuests.insert(0,"cody")
invitedGuests.insert(1,"logan")
invitedGuests.append("jayden")

print(f"inviting {invitedGuests[0]} to the dinner")
print(f"inviting {invitedGuests[1]} to the dinner")
print(f"inviting {invitedGuests[2]} to the dinner")

print(f"guest {invitedGuests[2]} could not make it")
invitedGuests.remove(invitedGuests[2])

invitedGuests.append("nathan")

print(f"\ninviting {invitedGuests[0]} to the dinner")
print(f"inviting {invitedGuests[1]} to the dinner")
print(f"inviting {invitedGuests[2]} to the dinner")
