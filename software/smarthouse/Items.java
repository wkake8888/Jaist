public class Items {
    class Door {
        // 0 = ロック、1＝アンロック
        private String key = "locked";

        public void getStatus() {
            System.out.println("key: " + key);
        }
        public void lock() {
            key = "locked";
        }
        public void unlock() {
            key = "unlocked";
        }
     }


    }
