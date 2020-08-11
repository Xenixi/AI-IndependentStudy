package main;

import java.math.BigInteger;
import java.util.Scanner;
import java.util.Formatter.BigDecimalLayoutForm;
import java.math.BigInteger;

public class FactorialCalculator {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		// loop in case the user doesn't understand what a number is and enters random
		// text, or if they just decide that they want to enter a negative for no
		// reason. This happens sometimes...
		while (true) {
			System.out.println(
					"Factorial calculation with recursion example\nenter a postitve integer to calculate the factorial (limit is 1k): ");

			String input = scan.nextLine();
			try {
				long userValue = Long.parseLong(input);
				if (userValue < 0) {
					throw new Exception("Number must be positive");
				} else if (userValue > 1000) {
					System.err.println("Limit is set to 1000!, please enter a smaller number");
					throw new Exception();

				} else {
					System.out.println("Calculating...");
					long start = System.currentTimeMillis();
					BigInteger result = calculate(BigInteger.valueOf(userValue));
					long end = System.currentTimeMillis();

					System.out.println("Result: " + result + " -- Took " + (end - start) + "ms to complete");
				}
			} catch (Exception e) {
				System.err.println("Please enter a valid positive integer");
			}
		}
	}

	// where everything happens:
	public static BigInteger calculate(BigInteger num) {

		if (num.compareTo(BigInteger.valueOf(0L)) == 1) {
			return num.multiply(calculate(num.subtract(BigInteger.valueOf(1L))));
			/*
			 * Explanation of everything: Let's say you enter 4. 4 > 0 so the above return
			 * statement will be used. Since the factorial of a number is just that number
			 * multiplied by every whole number under it until you reach 1, this works. the
			 * variable num is multiplied by calculate(num-1) the return statement will
			 * return the final answer that was put together from every iteration, since
			 * calculate(num-1) must be called for num * calculate(num - 1) to be
			 * calculated, and no value can be returned until the product of those two
			 * numbers is calculated.
			 * 
			 * calculate(num - 1) simply does the same operation, so with an input of 4 at
			 * the start, we're multiplying 4 * calculate(4-1) or really calculate(3) when
			 * we do calculate(3), it takes 3 and multiplies it by calculate(3-1), or
			 * calculate(2) calculate(2) is completing the operation 2 * calculate(2-1) or
			 * calculate(1), and calculate(1) will perform 1 * calculate(1-1) or
			 * calculate(0) --since if num = 0, 1 is returned, that last iteration which was
			 * 1 * calculate(1-1) will really be 1*1=1 the iteration before that gets the
			 * returned value from the previously mentioned iteration (value is 1) and
			 * performs 2 * calculate(2-1), which we know is equal to 2*1=2 that value (2)
			 * is returned and the iteration before that utilizes it in 3 * calculate(3-1),
			 * which is really just 3*2=6 6 is returned and the iteration before that does 4
			 * * calculate(4-1), which we know is 4*6=24 the original function call was just
			 * calculate(4), and the result (24) is returned. The program then just outputs
			 * the result, and the user gets the result of 4! (24) That's it! If you enter a
			 * larger number, the same thing happens, just more iterations, more returns,
			 * more multiplying numbers (and bigger result -- which is why I used a
			 * BigInteger for insanely big results... try entering something like 600) the
			 * 'L' after the number is just to specify that they're longs
			 * 
			 * 
			 * Note: I changed everything to BigInteger, so instead of using num *
			 * calculate(num-1), it's
			 * num.multiply(calculate(num.subtract(BigInteger.valueOf(1L)))); returning a
			 * value of 1 below now is return BigInteger.valueOf(1L), which is just creating
			 * a BigInteger with a value set to the long: 1L
			 */

		} else {
			// if the number is 0, 1 will be returned since 0! = 1
			return BigInteger.valueOf(1L);
		}
	}
}