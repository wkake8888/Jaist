import java.util.Random;

public class Room {
    public Curtain curtain;
    public Light light;
    public Meter meter;
    public Window window;
    public static void main(String args[]){
    }

    Room(){

    }
    public void makeDevices() {
        Room.Curtain curtain = new Room.Curtain();
        this.curtain = curtain;
        Room.Light light = new Room.Light();
        this.light = light;
        Room.Meter meter = new Room.Meter();
        this.meter = meter;
        Room.Window window = new Room.Window();
        this.window = window;
    }

    static public class Curtain {
        private String status = "close";

        public void getStatus() {
            System.out.println("#### Curtain #####\nstatus: " + this.status + "\n");
        }
        public void close() {
            this.status = "close";
        }
        public void open() {
            this.status = "open";
        }
    }

    static public class Light {
        private String power = "OFF";
        private Integer brightness = 0;

        public void getStatus() {
            System.out.println("#### Light #####\npower: " + this.power + "\n" + "brightness: " + this.brightness + "\n");
        }
        public void powerOn() {
            this.power = "ON";
        }
        public void powerOff() {
            this.power = "OFF";
        }
        public void changeBrightness(Integer n) {
            this.brightness = n;
        }
    }

    static public class Meter {
        private Integer brightness = 0;

        Meter() {
            Random rand = new Random();
            // generate random brightness
            this.brightness = rand.nextInt(10);
        }
        public void getStatus() {
            System.out.println("#### Meter #####\nbrightness: " + this.brightness + "\n");
        }
        public Integer getBrightness() {
            return this.brightness;
        }
        public void selectFunc(Integer funcId) {
            if (funcId.equals(1)) {
                getStatus();
            }
            else if (funcId.equals(2)) {
                getBrightness();
            }
        }
    }

    static public class Window {
        String status = "close";

        public void getStatus() {
            System.out.println("#### Window #####\nstatus: " + this.status + "\n");
        }

        public void open() {
            this.status = "open";
        }

        public void close() {
            this.status = "close";
        }
    }

    // Optimization
    public interface Optimizer {
        Integer getMeterInfo();
        void getStatus();
    }

    class RoomLightOptimizer implements Optimizer {
        // Room room;

        RoomLightOptimizer() {
            // Room roomObj = Operator.roomList.get(roomId);
            // room = roomObj;
        }

        public Integer getMeterInfo() {
            Integer brightness = meter.getBrightness();
            return brightness;
        }
        public void getStatus() {
            light.getStatus();
            meter.getStatus();
            curtain.getStatus();
        }
        public void lightOptimize(Integer brightness) {
            window.close();
            if (brightness >= 8) {
                light.powerOff();
                curtain.open();
            }
            else {
                light.powerOn();
                light.changeBrightness(8);
                curtain.close();
            }
        }
    }
}
