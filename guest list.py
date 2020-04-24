guest_list = ["Nariman", "Kara", "Dima"]
print("Один гость не может прийти это " + guest_list[1])

guest_list[1] = "Dimas"
print("Приглашение на обед " + guest_list[0])
print("Приглашение на обед " + guest_list[1])
print("Приглашение на обед " + guest_list[2])

print("Приглашение на обед в место Kapa " + guest_list[1] )
guest_list.insert(0, "lflflefl")
guest_list.insert(3, "eeorpefpekc")
guest_list.append("ekekdlklsklkxk")
print(len(guest_list))
print(guest_list)
print(guest_list)
print(guest_list)
print("места хватит только для двух гостей")
popped_list = guest_list.pop(0)
print("сожалеете об отмене приглашения " + popped_list)
popped_list = guest_list.pop(4)
print("сожалеете об отмене приглашения " + popped_list)
popped_list = guest_list.pop(2)
print("сожалеете об отмене приглашения " + popped_list)
popped_list = guest_list.pop(1)
print("сожалеете об отмене приглашения " + popped_list)
print("подтверждать, что более раннее приглашение остается в силе " + guest_list[0])
print("подтверждать, что более раннее приглашение остается в силе " + guest_list[1])
print(guest_list)
del guest_list[1]
del guest_list[0]
print(guest_list)
print(len(guest_list))




