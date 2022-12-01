class NameTooShortError(Exception):
    """Name is less than five valid characters."""


class MustContainAtSymbolError(Exception):
    """Email address missing '@' symbol."""


class InvalidDomainError(Exception):
    """Domain name is not among the specified names."""


line = input()

while line != "End":
    if "@" not in line:
        raise MustContainAtSymbolError("Email must contain @")
    full_email_address = line.split("@")
    name = full_email_address[0]
    domain_list = full_email_address[1]

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    valid_domains = [
        '.com',
        '.bg',
        '.org',
        '.net'
    ]
    if not domain_list.endswith(tuple(valid_domains)):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    line = input()