# Multithreading Synchronized
package cincaphi;

import java.util.*;


class Task implements Runnable {
    Cincaphi lock;
    int threadno;
    int val;
    List<Integer> threaditem = new ArrayList<>();

    public Task(Cincaphi obj, int threadno) {
        this.lock = obj;
        this.threadno = threadno;
    }

    @Override
    public void run() {
        while(Cincaphi.counter < 99) {
            synchronized (lock) {
                while(!((Cincaphi.status % 3) == threadno)){
                    try {
                        lock.wait();
                    } catch (InterruptedException e) {
                        System.out.println("We have a problem.");
                    }
                }

                val = Cincaphi.counter++;
                System.out.println(val);
                Cincaphi.status++;
                threaditem.add(val);
                lock.notifyAll();
            }
        }
        System.out.println(threaditem);
    }
}

public class Cincaphi{

    public static int status = 0;
    public static int counter = 1;
    
    public static void main(String[] args) {

        Cincaphi lock = new Cincaphi();
        Thread t1 = new Thread(new Task(lock,0));
        Thread t2 = new Thread(new Task(lock,1));
        Thread t3 = new Thread(new Task(lock,2));
        t1.start();
        t2.start();
        t3.start();
    }
}