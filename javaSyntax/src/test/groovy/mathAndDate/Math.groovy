package mathAndDate

import java.security.SecureRandom

//import java.util.Random
import java.util.concurrent.ThreadLocalRandom

println "Random Number Generation"
Random random = new Random()

println "This returns a value between 0.0 and 1.0"
double randDouble = random.nextDouble()
println("randDouble:  $randDouble")

println "Same as nextDouble"
float randFloat = random.nextFloat()
println("randFloat:  $randFloat")
println ""

//nextBytes takes a user-supplied byte array,
// and fills it with random bytes. It returns nothing.
byte[] randBytes = new byte[16]
random.nextBytes(randBytes)
println("randBytes: $randBytes")


// Pseudo Random Numbers in Specific Range
// 0 - 999
println "0 - 999: " + random.nextInt(1000)

// number is in the range of 10 to 109
int number = 10 + random.nextInt(100)
println("__range of 10 to 109 >>: " + number)

// nextInt is normally exclusive of the top value,
// so add 1 to make it inclusive
Integer min = 5
Integer max = 7
int randNum1 = ThreadLocalRandom.current().nextInt(min, max + 1)
println "__ThreadLocalRandom >>: " + randNum1
println("")

println "Generating cryptographically secure pseudorandom numbers"
SecureRandom rng = new SecureRandom();
byte[] randomBytes = new byte[64];
rng.nextBytes(randomBytes); // Fills randomBytes with random bytes (duh)
System.out.println("__SecureRandom >>" + Arrays.toString(randomBytes));
println("")


/**
 * returns a array of random numbers with no duplicates
 * @param range the range of possible numbers for ex. if 100 then it can be anywhere from 1-100
 * @param length the length of the array of random numbers
 * @return array of random numbers with no duplicates.
 */
public static int[] getRandomNumbersWithNoDuplicates(int range, int length) {
    if (length < range) {
        // this is where all the random numbers
        int[] randomNumbers = new int[length];

        // loop through all the random numbers to set them
        for (int q = 0; q < randomNumbers.length; q++) {

            // get the remaining possible numbers
            int remainingNumbers = range - q;

            // get a new random number from the remainingNumbers
            int newRandSpot = (int) (Math.random() * remainingNumbers);

            newRandSpot++;

            // loop through all the possible numbers
            for (int t = 1; t < range + 1; t++) {

                // check to see if this number has already been taken
                boolean taken = false;
                for (int number : randomNumbers) {
                    if (t == number) {
                        taken = true;
                        break;
                    }
                }

                // if it hasnt been taken then remove one from the spots
                if (!taken) {
                    newRandSpot--;

                    // if we have gone though all the spots then set the value
                    if (newRandSpot == 0) {
                        randomNumbers[q] = t;
                    }
                }
            }
        }
        return randomNumbers;
    } else {
        // invalid can't have a length larger then the range of possible numbers
    }
    return null;
}