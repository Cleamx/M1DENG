public class PushNotificationAdapter extends Notification {
    private PushNotification pushNotification;

    public PushNotificationAdapter() {
        pushNotification = new PushNotification();
    }

    @Override
    public void sendNotification(String message) {
        pushNotification.pushMessage(message);
    }
}