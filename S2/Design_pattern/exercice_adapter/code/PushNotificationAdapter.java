public class PushNotificationAdapter extends AbstractNotification {
    private PushNotification pushNotification;

    public PushNotificationAdapter(String message) {
        super(message);
        pushNotification = new PushNotification();
    }

    @Override
    public void sendNotification() {
        pushNotification.pushMessage(message);
    }
}