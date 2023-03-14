/*Em Python essa solução seria demasiadamente simples, então decidi escolher a linguagem JAVA nesse caso
 * def reverseString(string):
 *     return string[::-1]
 */


package JobRotation;

class reverseString {
    public static String reverse(String string) {

        if(string.length() == 0) {
            return string;
        }

        String new_string = "";
        char letter;

        for(int i = 0; i < string.length(); i++) {
            letter = string.charAt(i);
            new_string = letter + new_string;
        }

        return new_string;
    }
    public static void main(String[] args) {
        String string = "Erik Samuel Medeiros";

        System.out.println(reverse(string));
    }
}