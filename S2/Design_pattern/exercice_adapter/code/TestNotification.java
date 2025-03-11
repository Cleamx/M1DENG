public class TestNotification {
    public static void main(String[] args) {
        Notification pushAdapter = new PushNotificationAdapter();
        pushAdapter.sendNotification("Alerte importante !");
    }
}