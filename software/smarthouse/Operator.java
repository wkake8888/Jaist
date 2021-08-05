import java.util.Scanner;
import java.util.ArrayList;

 public class Operator {
    // Room room;
    // Integer targetDeviceNumber;
    static public ArrayList<Room> roomList = new ArrayList<Room>();

    public static void main(String args[]){
        // Initilize room and devices
        Room room = new Room();
        roomList.add(room);
        room.makeDevices();

        // Show registered room
        System.out.println("[System] Avairable room IDs are below\nID: 0\n");

        // Receive operation from User
        Scanner scan = new Scanner(System.in);
        System.out.println("[System] Choose the number from below.\n1. show\n2. control\n3. optim\n");
        Integer order = Integer.parseInt(scan.next());

        // Show
        if (order.equals(1)) {
            System.out.println("\n[System] Input room ID.");
            Integer roomId = Integer.parseInt(scan.next());
            show(roomId);
        }
        // Control
        else if (order.equals(2)) {
            System.out.println("\n[System] Input room ID.");
            Integer roomId = Integer.parseInt(scan.next());
            control(roomId);
        }
        // Optimize
        else if (order.equals(3)) {
            System.out.println("\n[System] Input room ID.");
            Integer roomId = Integer.parseInt(scan.next());
            optimize(roomId);
        }
        else {
            System.out.println("\n##### Error ####\nYour input was wrong.");
        }
        scan.close();
    }

    public static void show(Integer roomId) {
        Room room = roomList.get(roomId);
        room.curtain.getStatus();
        room.light.getStatus();
        room.meter.getStatus();
        room.window.getStatus();
    }

    public static void control(Integer roomId) {
        Scanner scan = new Scanner(System.in);

        Room targetRoom = roomList.get(roomId);
        System.out.println("\n[System] Select number of target devices from below.\n1. Meter\n2. Light\n3. Curtain\n4. Window\n");
        Integer targetDeviceNumber = Integer.parseInt(scan.next());

        // Meter is selected
        // getBrightness() method is nor for User, so it's not in the options.
        if (targetDeviceNumber.equals(1)) {
            System.out.println("\n[System] Select number of function ID from below.\n1. getStatus()");
            Integer funcId = Integer.parseInt(scan.next());
            if (funcId.equals(1)) {
                targetRoom.meter.getStatus();
            }
        }
        // Light is selected
        else if (targetDeviceNumber.equals(2)) {
            System.out.println("\n[System] Select number of function ID from below.\n1. getStatus()\n2. powerOn()\n3. powerOff()\n4. changeBrightness()");
            Integer funcId = Integer.parseInt(scan.next());
            if (funcId.equals(1)) {
                targetRoom.light.getStatus();
            }
            else if (funcId.equals(2)) {
                targetRoom.light.powerOn();
            }
            else if (funcId.equals(3)) {
                targetRoom.light.powerOff();
            }
            else if (funcId.equals(4)) {
                System.out.println("\n[System] Select brightness from 0 to 9");
                Integer targetBrightness = Integer.parseInt(scan.next());
                targetRoom.light.changeBrightness(targetBrightness);
                targetRoom.light.getStatus();
            }

        }
        // Curtain is selected
        else if (targetDeviceNumber.equals(3)) {
            System.out.println("\n[System] Select number of function ID from below.\n1. getStatus()\n2. close()\n3. open()\n");
            Integer funcId = Integer.parseInt(scan.next());
            if (funcId.equals(1)) {
                targetRoom.curtain.getStatus();
            }
            else if (funcId.equals(2)) {
                targetRoom.curtain.close();
            }
            else if (funcId.equals(3)) {
                targetRoom.curtain.open();
            }
        }
        else if (targetDeviceNumber.equals(4)) {
            System.out.println("\n[System] Select number of function ID from below.\n1. getStatus()\n2. close()\n3. open()\n");
            Integer funcId = Integer.parseInt(scan.next());
            if (funcId.equals(1)) {
                targetRoom.window.getStatus();
            }
            else if (funcId.equals(2)) {
                targetRoom.window.close();
            }
            else if (funcId.equals(3)) {
                targetRoom.window.open();
            }
        }
        scan.close();
    }

    public static void optimize(Integer roomId) {
        Room room = roomList.get(roomId);
        Room.RoomLightOptimizer lightOpt = room.new RoomLightOptimizer();
        Integer brightness = lightOpt.getMeterInfo();
        lightOpt.lightOptimize(brightness);
        lightOpt.getStatus();
    }
}
