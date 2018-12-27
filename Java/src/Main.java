public class Main {
    public static void main(String[] args) {
        ContactsManager myContactsManager = new ContactsManager();
        Contact adam = new Contact();
        adam.name = "Adam Moses";
        adam.phoneNumber = "3106584359";
        myContactsManager.addContact(adam);

        Contact cole = new Contact();
        cole.name = "Cole Bransford";
        cole.phoneNumber = "3106584358";
        myContactsManager.addContact(cole);

        Contact max = new Contact();
        max.name = "Max Urbany";
        max.phoneNumber = "3106584357";
        myContactsManager.addContact(max);

        Contact ret = myContactsManager.searchContact("Cole Bransford");
        System.out.println(ret.phoneNumber);
    }
}
