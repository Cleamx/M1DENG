public class SnapAdapter extends Notification {
    private Snap snap;

    public SnapAdapter() {
        snap = new Snap();
    }

    @Override
    public void sendNotification(String message) {
        snap.pushMessage(message);
    }
}