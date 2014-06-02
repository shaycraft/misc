public class FizzBuzz 
{
	public static void main(String[] args)
	{
		int[] nums = new int[100]; //initialise the array of ints
		for (int i = 0; i < nums.length; i++) //populate
		{
			nums[i] = i+1;
		}
		String buzz = "buzz", fizz = "fizz"; //initialise the string variables
		for (int i = 0; i < nums.length; i++) //iterate for the size of the array
		{
			if (nums[i] % 15 == 0) //check if number in position i is divisable by 15, if so ddont check other 2 conditions - we dont want a double print
			{
				System.out.println(buzz +fizz + (i+1));
			}
			else //if above is not executed then check the other 2 conditions
			{
				if (nums[i] % 3 == 0 )
				{		
				System.out.println(buzz + (i+1));
				}
			}
			if(nums[i] % 5== 0)
			{
				System.out.println(fizz +(i+1));
			}
		}
	}
}
