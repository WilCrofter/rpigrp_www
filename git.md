## Git and Github

Electronic collaboration is a critical technology in today's fast-paced, geographically distributed world. Learning how to collaborate electronically allows for a mix of in person and electronic interaction, a mix which has become the most effective way to work and learn today. In this respect, Git and Github are central. Github has been called the Facebook of technology.

### What is git?

Git is a version control system.

1. It applies to any kind of text: computer code, cad files, legal documents, novels.
2. It keeps the entire history of your project secure and at your fingertips.
3. Each person has his or her own copy of the project and its history.
4. Branches and forks allow people to work independently and in parallel.
5. Branches and forks can be merged into "master" versions of the project.

### What is Github?

Watch minutes 1:30 thru 7:30 of [The New Developer](https://www.youtube.com/watch?v=0A-u1tQTBqo)

Watch the 4 minute [What is Github video](https://www.youtube.com/watch?v=w3jLJU7DT5E)

1. Github is the largest, most active, online host of git based projects. Examples include:
	* [Raspberry Pi](https://github.com/raspberrypi)
    * [RepRap, the 3D printer](https://github.com/reprap)
    * [Linux](https://github.com/torvalds/linux)
	* [Arduino](https://github.com/arduino/Arduino)
	* [Python](https://github.com/python)
	* [Flask](https://github.com/pallets/flask)
	* [Bounce](https://github.com/WilCrofter/bounce)
2. Github is free for open source projects like those above.
3. Github supports
    * Issue pages to coordinate plans, answer questions, point out problems.
	* Wiki pages for documentation, how-tos, pictures.
	* Static web pages to support documentation, blogs, demos etc.
4. Tracks contributions, making your contribution history a public credential.
5. Supports contributions to big projects like Flask by
    * cloning (forking) the project respository
	* improving something or adding a feature to your clone
	* issuing a pull request to the original project

### Setting up on your Raspberry Pi

1. Create a new user for yourself on your rPi:
    * `sudo adduser <you>`
2. Log on as `<you>` and create a public/private key pair: 
    * `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`
3. Get a free GitHub account and add your *public* key to it: 
    * Copy and paste the stuff in `.ssh/id_rsa.pub` to your settings page at GitHub.
4. Accept an invitation to collaborate in the "rpigrp_www" project.
5. Clone rpigrp_www to your rPi: 
    * `git clone git@github.com:WilCrofter/rpigrp_www.git`
7. Create a personal branch in your clone of rpigrp and push it to GitHub
    * `git -b checkout <name of your branch>`
	* `git push origin <name of your branch>`

### Try it out

1. Run `git status`.
2. Edit one of the files in your branch, save it, and run `git status` again.
3. Create a new file and run `git status` once more.
4. `git add` the new file and `git commit` the changes.
5. `git push origin <name of your branch>`
6. Open an issue on GitHub.
7. Comment on somebody else's issue on GitHub.
