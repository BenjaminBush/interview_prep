class Contact{
    String name;
    String email;
    String phoneNumber;
}

public class ContactsManager {

    Contact[] myFriends;
    int friendCount;

    public ContactsManager() {
        this.friendCount = 0;
        this.myFriends = new Contact[500];
    }

    void addContact(Contact contact) {
        this.myFriends[this.friendCount] = contact;
        this.friendCount++;
    }

    Contact searchContact(String searchName) {
        for (int i = 0; i < this.friendCount; i++) {
            if (this.myFriends[i].name.equals(searchName)) {
                return this.myFriends[i];
            }
        }
        return null;
    }
}
