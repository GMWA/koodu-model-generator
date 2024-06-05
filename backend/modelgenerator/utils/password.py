
def check_password_policy(password: str) -> bool:
    """Check if password meets the policy:
            - at least 8 characters,
            - 1 uppercase,
            - 1 lowercase,
            - 1 number,
            - 1 special character

        Args:
            password (str): password to check

        Returns:
            bool: True if password meets the policy, False otherwise
    """
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(not char.isalnum() for char in password):
        return False
    return True