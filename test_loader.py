import unittest
from loader import env_load


class LoaderTest(unittest.TestCase):
    def test_env_load(self):
        env = env_load()
        self.assertTrue(env)
        self.assertTrue(env["USERNAME"] == "testuser")
        self.assertTrue(env["PASSWORD"] == "testpass")


if __name__ == "__main__":
    unittest.main()
