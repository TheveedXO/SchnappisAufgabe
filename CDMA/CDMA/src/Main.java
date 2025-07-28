//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class CDMA {
    static class Chip {
        private int[] S = new int[4];

        public Chip(int s1, int s2, int s3, int s4) {
            S[0] = s1;
            S[1] = s2;
            S[2] = s3;
            S[3] = s4;
        }

        public int get(int index) {
            return S[index];
        }
    }

    public static void main(String[] args) {
        var A = new Chip(1,1,1,1);
        var B = new Chip(1,-1,1,-1);
        var C = new Chip(1,1,-1,-1);
        var D = new Chip(1,-1,-1,1);
    }
    static class BitMessage {
        private int[] message = new int[4];
        @Override public String toString() {
            return "(" + message[0] + "," + message[1] + "," + message[2] + "," + message[3] + ")";
        }

        public BitMessage encode(Chip c, boolean bit) {
            int factor = bit ? 1 : -1;

            for (int i = 0; i < 4; i++) {
                message[i] += factor * c.get(i);
            }
        }
    }
}
