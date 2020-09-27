package chat;

import java.io.IOException;
import java.net.*;
import java.util.HashMap;
import java.util.Properties;

/**
 * Gerencia o protocolo e o processamento das mensagens
 * @author rodrigo
 */
public class ProtocolController {

    private final MulticastSocket multicastSocket;
    private final DatagramSocket udpSocket;
    private final InetAddress group;
    private final Integer mport, uport;
    private final String nick;
    private final HashMap<String, InetAddress> onlineUsers;
    private final UIControl ui;

    public ProtocolController(Properties properties) throws IOException {
        mport = (Integer) properties.get("multicastPort");
        uport = (Integer) properties.get("udpPort");
        group = (InetAddress) properties.get("multicastIP");
        nick = (String) properties.get("nickname");
        ui = (UIControl) properties.get("UI");

        multicastSocket = new MulticastSocket(mport);
        udpSocket = new DatagramSocket(uport);
        
        onlineUsers = new HashMap<>();
        onlineUsers.put("Todos", group);  
    }

    public void send(String targetUser, String msg) throws IOException {
        Message message = new Message((byte) 0x3, this.nick, msg);
        System.out.println(targetUser);
        if (targetUser.toLowerCase().equals("todos")) {
            this.sendMessageGroup(message);
        } else {
            InetAddress inetAddress = onlineUsers.get(targetUser);
            if (inetAddress != null) {
                this.sendMessage(message, inetAddress);
            }
        }
    }

    private void sendMessageGroup(Message msg) throws IOException {
        if (msg != null) {
            byte[] msgBytes = msg.getBytes();
            DatagramPacket packet = new DatagramPacket(msgBytes, msgBytes.length, group, mport);
            multicastSocket.send(packet);
        }
    }

    private void sendMessage(Message msg, InetAddress target) throws IOException {
        if (msg != null) {
            byte[] msgBytes = msg.getBytes();
            DatagramPacket packet = new DatagramPacket(msgBytes, msgBytes.length, target, uport);
            udpSocket.send(packet);
        }
    }

    public void join() throws IOException {
        multicastSocket.joinGroup(group);
        Message message = new Message((byte) 0x1, this.nick, "");
        this.sendMessageGroup(message);
    }

    public void leave() throws IOException {
        Message message = new Message((byte) 0x5, this.nick, "");
        this.sendMessageGroup(message);
        multicastSocket.leaveGroup(group);
    }
    
    public void close() throws IOException {
        if (udpSocket != null) udpSocket.close();
        if (multicastSocket != null) multicastSocket.close();
    }

    public void processPacket(DatagramPacket p) throws IOException {
        if (p != null){
            Message message = new Message(p.getData());
            String source = message.getSource();
            switch (message.getType()){
                case 1:
                    onlineUsers.put(source, p.getAddress());
                    Message msg = new Message((byte) 0x2, this.nick, "");
                    this.sendMessage(msg, p.getAddress());
                    break;
                case 5:
                    onlineUsers.remove(source);
            }
            if (!this.nick.equals(source) || message.getType() == 1){
                ui.update(message);
            }
        }
    }

    public void receiveMulticastPacket() throws IOException {
        DatagramPacket packet = new DatagramPacket(new byte[503],503);
        multicastSocket.receive(packet);
        this.processPacket(packet);
    }

    public void receiveUdpPacket() throws IOException {
        DatagramPacket packet = new DatagramPacket(new byte[503],503);
        udpSocket.receive(packet);
        this.processPacket(packet);
    }
}
