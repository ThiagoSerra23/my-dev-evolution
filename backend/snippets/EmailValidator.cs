public static class EmailValidator
{
    public static bool IsValid(string email)
    {
        return email.Contains("@") && email.Contains(".");
    }
}