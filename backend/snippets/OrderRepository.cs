public class OrderRepository
{
    public Order GetById(int id)
    {
        // Simulate DB fetch
        return new Order { Id = id, Date = DateTime.Now };
    }
}