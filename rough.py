from oops_proj import chatBook
#user1=chatBook()

#
# print(user1._chatBook__name)

#getter and setter methods
#user1.set_name()
#print(user1.get_name())
#


#staticmethod getter and setter
user1=chatBook()
print(user1.id)


#using static mmethod directly from class rather than object
chatBook.set_id(10)
user2=chatBook()
print(user2.id)