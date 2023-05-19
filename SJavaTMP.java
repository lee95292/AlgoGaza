

import java.util.*;
import java.util.stream.Collectors;
import java.io.*;

public class SJavaTMP {
    private static final long MODULAR_UNIT = 62;
    private static final char[] BASE62_SHUFFLE_UNIT = "m9baosDF3VwpzMAPvNfjSHYuyGZBQl0x1U2ERdc5KT7I68WX4rkhqtJCOngLie".toCharArray();
    
    public static void main(String[] args) throws IOException {

        int LINK_SIZE=7;
        Long linkId=1000000000L;
        char[] shortenLink = new char[LINK_SIZE];
        for(int index = 0; index < LINK_SIZE; index++){
            shortenLink[index] = BASE62_SHUFFLE_UNIT[(int) (linkId%MODULAR_UNIT)];
            linkId /= MODULAR_UNIT;
        }
        System.out.println(String.valueOf(shortenLink));
        for(Character c: BASE62_SHUFFLE_UNIT){
            System.out.print(c);
        }
    }
}

