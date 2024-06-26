from main_functions import add_hyperlinks_to_string
import unittest


class TestHyperlinks(unittest.TestCase):
    def setUp(self) -> None:
        self.fun = add_hyperlinks_to_string

    def test_reg1(self):
        self.assertEqual(
            self.fun(" youtube.com", ".txt", "tg"),
            r" https://youtube.com",
            msg='Error with regular links'
        )

    def test_reg2(self):
        self.assertEqual(
            self.fun(" поддерживаю.рф", ".txt", "tg"),
            r" https://поддерживаю.рф",
            msg='Error with regular links'
        )

    def test_reg3(self):
        self.assertEqual(
            self.fun(" sometest.com/home/start", ".txt", "tg"),
            r" https://sometest.com/home/start",
            msg='Error with regular links'
        )

    def test_user1(self):
        self.assertEqual(
            self.fun(" @user", ".txt", "tg"),
            r" https://t.me/user",
            msg='Error with user'
        )

    def test_user2(self):
        self.assertEqual(
            self.fun(" @me", ".txt", "vk"),
            r" https://vk.com/me",
            msg='Error with user'
        )

    def test_email1(self):
        self.assertEqual(
            self.fun(" me@mail.com", ".txt", "tg"),
            r" https://me@mail.com",
            msg='Error with emails'
        )

    def test_email2(self):
        self.assertEqual(
            self.fun(" me@mail.com", ".md", "tg"),
            r" me@mail.com",
            msg='Error with emails'
        )

    def test_html(self):
        self.assertEqual(
            self.fun("i like youtube.com", ".html", "tg"),
            r'i like<a href="https://youtube.com"> youtube.com</a>',
            msg='Error with html'
        )

    def test_markdown(self):
        self.assertEqual(
            self.fun("i like youtube.com", ".md", "tg"),
            r'i like[ youtube.com](https://youtube.com)',
            msg='Error with markdown'
        )


if __name__ == "__main__":
    unittest.main()
