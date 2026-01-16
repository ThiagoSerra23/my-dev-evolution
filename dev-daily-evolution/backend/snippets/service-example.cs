using System;

namespace Backend.Snippets
{
    public class ServiceExample
    {
        public void ProcessData(string data)
        {
            if (string.IsNullOrEmpty(data))
                throw new ArgumentException("Data cannot be empty", nameof(data));
                
            Console.WriteLine($"Processing: {data}");
        }
    }
}
