import re


def read_file_to_string(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            file_lines = file.readlines()
            file_content = ''.join(file_lines)

        return file_content
    except OSError:
        print("ERROR! No such file or directory!")


def save_string_to_file(file_path: str, file_lines: str) -> None:
    try:
        with open(file_path, 'w', encoding="utf-8") as file:
            file.writelines(file_lines)
    except TypeError:
        print("ERROR! Unable to save empty string!")


def add_hyperlinks_to_string(file_lines: str, file_format: str, user_format: str) -> str:

    # === Add hyperlinks to domain names ===
    domain_pattern = r'\s\w+\.[a-zа-я]{2,6}'
    domains = re.findall(domain_pattern, file_lines)

    domains = list(set(domains))  # remove duplicates
    domains = list(filter(lambda x: x[0] != "@", domains))

    for domain in domains:
        domain_link = f"{domain[0]}https://{domain[1:]}"

        if file_format == ".txt":
            file_lines = file_lines.replace(domain, domain_link)
        elif file_format == ".md":
            file_lines = file_lines.replace(domain, f"[{domain}]({domain_link[1:]})")
        elif file_format == ".html":
            file_lines = file_lines.replace(domain, f'<a href="{domain_link[1:]}">{domain}</a>')

    # === Add hyperlinks to @users ===
    user_pattern = re.compile(r'\s@[\w\d_]+')
    users = re.findall(user_pattern, file_lines)
    users = list(set(users))  # remove duplicates

    for user in users:
        if user_format == 'tg':
            file_lines = file_lines.replace(user, f"{user[0]}https://t.me/{user[2:]}")
        elif user_format == 'vk':
            file_lines = file_lines.replace(user, f"{user[0]}https://vk.com/{user[2:]}")

    # === Add hyperlinks to emails ===
    email_pattern = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
    emails = re.findall(email_pattern, file_lines)
    emails = list(set(emails))  # remove duplicates

    for email in emails:
        email_link = f"https://{email}"

        if file_format == ".txt":
            file_lines = file_lines.replace(email, email_link)
        elif file_format == ".html":
            file_lines = file_lines.replace(email, f'<a href="mailto:{email_link}">{email}</a>')


    # Заменяем все последовательности пробелов на один пробел:
    file_lines = re.sub(r'\s{2,}', '\n', file_lines)
    return file_lines


