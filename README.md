# Winnow_EXERCISE
RESTful API system for testing food waste


1. Overview
A Python-based FLASK API designed to automate the playback of test videos on a
monitor. This system allows an automated test runner to trigger specific video files via
HTTP requests, ensuring consistent and repeatable testing environments.


2. Key Features
a. RESTFUL API:
I realized two requests: one for playing a video and another to see the status of the
system (idle or playing).

b. State Management:
The system is tracking whether a video is currently playing or not, to prevent
overlapping playbacks. At first, the status is IDLE, but when a video starts playing, the
status will change to PLAYING.

c. Auto-Reset Mechanism
I implemented a threading.Timer to automatically return the system to IDLE status
after a predefined duration. I chose 15 second, because my videos are less then 10
seconds. This ensures the test suit cand proceed without manual intervention.

d. Portability:
I used relative pathing (os.path.join) so the project works immediately on any new
machine.


3. Scalability & Testability
 Scalability:
The video library is decoupled from the code. New test videos can be added by simply
placing the .mp4 files into the Video_Files folder. The API dynamically handles any file
found in that directory. For longer videos, the status_reset may need a little changing. I
implemented this for videos around 8-10 seconds.

 Testability:
The /status endpoint provides real-time feedback (JSON) about the server’s
availability. Error handling (HTTP 404 for missing files and 409 for busy state) allows
the test runner to log and handle failures easy.


4. Howto run:
a. Install dependencies: pip install flask
b. Place videos in the Video_Files folder, or test it with the 2 existing files.
c. Run python code.py
d. Send a POSTrequest http://localhost:5000/play with JSON body:
{“video”:”filename.mp4”}
e. Send a GETrequest to http://localhost/5000/status without a body, to see the
status of the system.


5. Future implementations:
If I would have more time. I would implement the reset_status part a little better, so it
can work for videos of any length
