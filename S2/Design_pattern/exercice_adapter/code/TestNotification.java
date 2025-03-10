public class TestNotification {
    public static void main(String[] args) {
        Notification pushAdapter = new PushNotificationAdapter("Alerte importante !");

        pushAdapter.sendNotification();
    }
}