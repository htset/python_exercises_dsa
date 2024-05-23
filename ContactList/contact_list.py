class Contact:
    def __init__(self):
        self.name = None
        self.phone = None
        self.next = None

class ContactList:
    HASH_SIZE = 100

    def __init__(self):
        self.bucket_table = [None] * self.HASH_SIZE

    def hash(self, name):
        hash_value = 5381
        for char in name:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return abs(hash_value) % self.HASH_SIZE

    def contact_add(self, name, phone):
        #get index from contact name
        hash_index = self.hash(name)
        new_contact = Contact()
        new_contact.name = name
        new_contact.phone = phone
        new_contact.next = self.bucket_table[hash_index]
        self.bucket_table[hash_index] = new_contact

    def contact_remove(self, name):
        index = self.hash(name)
        contact = self.bucket_table[index]
        previous = None

        while contact is not None:
            if contact.name == name:
                if previous is None:
                    #Contact to remove is the head of the list
                    self.bucket_table[index] = contact.next
                else:
                    #Contact to remove is not the head of the list
                    previous.next = contact.next
                print(f"Contact '{name}' removed successfully.")
                return
            previous = contact
            contact = contact.next
        print(f"Contact '{name}' not found.")

    def contact_search(self, name):
        hash_index = self.hash(name)
        contact = self.bucket_table[hash_index]
        while contact is not None:
            if contact.name == name:
                print(f"Name: {contact.name}\nPhone Number: {contact.phone}")
                return
            contact = contact.next
        print(f"Contact '{name}' not found.")

if __name__ == "__main__":
    phonebook = ContactList()
    phonebook.contact_add("John", "235454545")
    phonebook.contact_add("Jane", "775755454")
    phonebook.contact_add("George", "4344343477")

    phonebook.contact_search("John")
    phonebook.contact_search("Alex")
    phonebook.contact_search("George")

    phonebook.contact_remove("Jake")
    phonebook.contact_remove("Jane")
    phonebook.contact_search("Jane")
