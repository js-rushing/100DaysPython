using System;

public class Tips
{
    public static void Main()
    {
        double total;
        double people;
        double percentage;
        double tip;
        double perPerson;

        Console.Out.WriteLine("Welcome to the tip calculator.");
        Console.Out.WriteLine("What was the total bill? ");
        total = Convert.ToDouble(Console.ReadLine());
        Console.Out.WriteLine("How many people to split the bill? ");
        people = Convert.ToDouble(Console.ReadLine());
        Console.Out.WriteLine("What percentage tip would you like to give? (10, 12, or 15)? ");
        percentage = Convert.ToDouble(Console.ReadLine());

        tip = total * (percentage / 100);

        perPerson = ((total + tip) / people);

        Console.Out.WriteLine("Each person should pay: {0:c}", perPerson);
    }
}