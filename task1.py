import threading
import time


def download_file(filename):
    print(f"Start downloading: {filename}")
    time.sleep(2)
    print(f"Finished: {filename}")


files = [
    "document.pdf",
    "photo.png",
    "report.xlsx",
    "music.mp3",
    "video.mp4"
]


# sequential download
print("Sequential download:")
start = time.perf_counter()

for filename in files:
    download_file(filename)

sequential_time = time.perf_counter() - start


# download with threads
print("Download with threads:")
start = time.perf_counter()

threads = []

for filename in files:
    thread = threading.Thread(target=download_file, args=(filename,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

thread_time = time.perf_counter() - start


# comparison
print(f"Sequential: {sequential_time:.2f} sec")
print(f"With threads: {thread_time:.2f} sec")