# Project [Fission][Fission (Biology)] #

Project Fission is a personal website creation tool. 

## Quickstart Guide ##

In your command prompt (Terminal.app on macOS) enter the following:

`git clone https://github.com/ninjha01/fission`

This will create a local copy of the Project Fission code.

Open and edit the `details.md` file using an editor of your choice. `nano` is suggested for those who aren't familiar with command-line editors.

```
cd fission;
nano details.md;
```

Fill in the form with your own personal details. Here's how that looks on my personal website:

{FIRST}-Nishant  
{LAST}-Jha  
{TITLE}-MS in CS Candidate at the University of Virginia  
{BIO}-I am a computer scientist with a solid background in the Physical, Social, and Life Sciences. I enjoy writing about the potential impact of revolutionary technology on society as well as working at the intersection of biological research and computer science.  
{LINKEDIN}-https://www.linkedin.com/in/ninjha01  
{EMAIL}-ninjha01@gmail.com  

After filling in `details.md`, run the `init.sh` and `build.sh` scripts.

```
bash init.sh;
bash build.sh;
```

Lastly replace the blank blank profile picture and resume with your own copies.

```
mv /path/to/profile.jpg myweb/html/images/profile.jpg
mv /path/to/resume.pdf myweb/html/resume.pdf
```

Congratulations! You now have your own personal website! Open it up and check it out!

`open myweb/html/index.html`

Produced by [Nishant Jha][my website].

[my website]: people.virginia.edu/~nj7kv/
[Fission (Biology)]: https://en.wikipedia.org/wiki/Fission_(biology)
