
import unittest
from unittest.mock import patch

from src.monitor import (
    check_cpu_usage,
    check_memory_usage,
    check_disk_usage,
)


class TestSystemMonitor(unittest.TestCase):

    @patch("src.monitor.psutil.cpu_percent", return_value=25.0)
    def test_cpu_usage_below_threshold(self, mock_cpu):
        with patch("builtins.print") as mock_print:
            check_cpu_usage()

        mock_print.assert_any_call("CPU usage: 25.0%")
        mock_print.assert_not_called = mock_print.assert_not_called

    @patch("src.monitor.psutil.cpu_percent", return_value=95.0)
    def test_cpu_usage_above_threshold(self, mock_cpu):
        with patch("builtins.print") as mock_print:
            check_cpu_usage()

        mock_print.assert_any_call("CPU usage: 95.0%")
        mock_print.assert_any_call("WARNING: High CPU usage!")

    @patch("src.monitor.psutil.virtual_memory")
    def test_memory_usage_below_threshold(self, mock_memory):
        mock_memory.return_value.percent = 40.0

        with patch("builtins.print") as mock_print:
            check_memory_usage()

        mock_print.assert_any_call("Memory usage: 40.0%")
        mock_print.assert_not_called = mock_print.assert_not_called

    @patch("src.monitor.psutil.virtual_memory")
    def test_memory_usage_above_threshold(self, mock_memory):
        mock_memory.return_value.percent = 90.0

        with patch("builtins.print") as mock_print:
            check_memory_usage()

        mock_print.assert_any_call("Memory usage: 90.0%")
        mock_print.assert_any_call("WARNING: High memory usage!")

    @patch("src.monitor.shutil.disk_usage")
    def test_disk_usage_below_threshold(self, mock_disk):
        mock_disk.return_value = (1000, 500, 500)

        with patch("builtins.print") as mock_print:
            check_disk_usage("/")

        mock_print.assert_any_call("Disk usage: 50.0%")
        mock_print.assert_not_called = mock_print.assert_not_called

    @patch("src.monitor.shutil.disk_usage")
    def test_disk_usage_above_threshold(self, mock_disk):
        mock_disk.return_value = (1000, 900, 100)

        with patch("builtins.print") as mock_print:
            check_disk_usage("/")

        mock_print.assert_any_call("Disk usage: 90.0%")
        mock_print.assert_any_call("WARNING: High disk usage!")


if __name__ == "__main__":
    unittest.main()

