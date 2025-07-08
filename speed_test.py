import time
import urllib.request


def test(file_size_mb):
    if file_size_mb == 1:
        url = "http://speedtest.rastrnet.ru/1MB.zip"
    elif file_size_mb == 10:
        url = "http://speedtest.rastrnet.ru/10MB.zip"
    elif file_size_mb == 100:
        url = "http://speedtest.rastrnet.ru/100MB.zip"
    else:
        print("Invalid file size")
        return

    start = time.time()
    with urllib.request.urlopen(url) as response:
        while response.read(8192):
            pass
    end = time.time()

    duration = end - start
    speed_mbps = (file_size_mb * 8) / duration

    print(f"Download {file_size_mb}MB in {duration:.2f}s ({speed_mbps:.2f}Mbps)")


if __name__ == "__main__":
    print("HTTP download speed test")

    test(1)
    test(1)
    test(10)
    test(100)
