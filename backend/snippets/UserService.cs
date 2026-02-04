public class UserService
{
    public void Register(User user)
    {
        if (user == null) throw new ArgumentNullException(nameof(user));
        // Logic to register user
    }
}