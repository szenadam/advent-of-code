
namespace AdventOfCodeDay1;

public static class Program
{
    private static void Main(string[] args)
    {
        IOrderedEnumerable<int> elfs = File.ReadAllText("input.txt")
            .Split("\n\n")
            .Select(elf => elf.Split("\n", StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).Sum())
            .OrderByDescending(x => x);
        Console.WriteLine($"Most carry: {elfs.Max()}");
        Console.WriteLine($"Sum of top three carriers: {elfs.Take(3).Sum()}");
    }
}