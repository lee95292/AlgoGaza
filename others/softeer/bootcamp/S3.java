package others.softeer.bootcamp;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class S3 {
    public static class Car{
        String name;
        boolean isdeprecated;
        String type;
        int capacity;
        int start,end;
        Car(String name, boolean isdeprecated, String type, int capacity,int start, int end){
            this.name = name;
            this.isdeprecated = isdeprecated;
            this.type = type;
            this.capacity = capacity;
            this.start = start;
            this.end = end;
        }
        @Override
        public String toString(){
            StringBuilder sb = new StringBuilder(name);
            if(isdeprecated) sb.append("*");
            sb.append(String.format("(%s)",type));
            return sb.toString();
        }
    }
    static List<Car> carList;
    public static String solution(String param0, int param1) {
        StringBuilder sb = new StringBuilder();
        int date = Integer.parseInt(param0);
        for(int i=0; i< carList.size(); i++){
            Car car = carList.get(i);
            if(car.start <= date && date <= car.end && param1 <= car.capacity ){
                sb.append(car);
                sb.append(",");
            }
        }
        String result;
        if(sb.toString().length() == 0){
            result ="!";
        }
        else result = sb.toString().substring(0, sb.length()-1);
        return result;
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
        carList = new ArrayList<>();
        carList.add(new Car("Aerotown",false,"Bus",30,199406,202305));
        carList.add(new Car("Cortina",true,"Sedan",5,196801,198004));
        carList.add(new Car("Elantra",true,"Sedan",5,199010,199512));
        carList.add(new Car("Equus",true,"Sedan",5,199904,200912));
        carList.add(new Car("Grandeur",false,"Sedan",5,198607,202305));
        carList.add(new Car("Pony",true,"Sedan",5,197512,198201));
        carList.add(new Car("Porter",true,"Truck",3,197702,200405));
        carList.add(new Car("SantaFe",false,"RV",7,200006,202305));
        carList.add(new Car("Tuscani",true,"Coupe",2,200109,200810));
        carList.add(new Car("Universe",false,"Bus",45,200612,202305));
        String[] param = input.replaceAll(" ", "").split(",");

        System.out.println(solution(param[0], Integer.parseInt(param[1])));
	}
}
