
import unittest
from unittest.mock import patch, Mock

from src import monitor


class TestSystemMonitor(unittest.TestCase):

    @patch("src.monitor.logging")
    @patch("src.monitor.print")
    @patch("src.monitor.psutil.cpu_percent", return_value=45.0)
    def test_check_cpu_usage_normal(
        self, mock_cpu, mock_print, mock_logging
    ):
        monitor.check_cpu_usage()

        mock_print.assert_called_with("CPU usage: 45.0%")
        mock_logging.info.assert_called_with("CPU usage: 45.0%")
        mock_logging.warning.assert_not_called()

    @patch("src.monitor.logging")
    @patch("src.monitor.print")
    @patch(
        "src.monitor.psutil.virtual_memory",
        return_value=Mock(percent=50.0),
    )
    def test_check_memory_usage_normal(
        self, mock_memory, mock_print, mock_logging
    ):
        monitor.check_memory_usage()

        mock_print.assert_called_with("Memory usage: 50.0%")
        mock_logging.info.assert_called_with("Memory usage: 50.0%")
        mock_logging.warning.assert_not_called()

    @patch("src.monitor.logging")
    @patch("src.monitor.print")
    @patch("src.monitor.shutil.disk_usage", return_value=(1000, 500, 500))
    def test_check_disk_usage_normal(
        self, mock_disk, mock_print, mock_logging
    ):
        monitor.check_disk_usage()

        mock_print.assert_called_with("Disk usage: 50.0%")
        mock_logging.info.assert_called_with("Disk usage: 50.0%")
        mock_logging.warning.assert_not_called()


if __name__ == "__main__":
    unittest.main()
