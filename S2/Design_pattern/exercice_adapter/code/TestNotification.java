public class TestNotification {
    public static void main(String[] args) {
        Notification pushAdapter = new SnapAdapter();
        pushAdapter.sendNotification("Alerte importante !");
    }
}