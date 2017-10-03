# Project [Fission][Fission (Biology)] #

Project Fission is a personal website creation tool. 

## Quickstart Guide ##

*Requires a bash shell with `make` and `clang` to be installed*

In your bash shell (Terminal.app on macOS) enter the following:

`git clone https://github.com/ninjha01/fission`

This will create a local copy of the Project Fission code.

Open and edit the `details.md` file using an editor of your choice. `nano` is suggested for those who aren't familiar with command-line editors.

```
cd fission;
nano details.md;
```

Fill in the form with your own personal details. Here's how that looks on my personal website:

```
{FIRST}-Nishant  
{LAST}-Jha  
{TITLE}-MS in CS Candidate at the University of Virginia  
{BIO}-I am a computer scientist with a solid background in the Physical, Social, and Life Sciences. I enjoy writing about the potential impact of revolutionary technology on society as well as working at the intersection of biological research and computer science.  
{LINKEDIN}-https://www.linkedin.com/in/ninjha01  
{EMAIL}-ninjha01@gmail.com  
```

After filling in `details.md`, run the `init.sh` script.

`bash init.sh;`

Next, replace the blank blank profile picture and resume with your own copies.

```
mv /path/to/profile.jpg myweb/html/images/profile.jpg
mv /path/to/resume.pdf myweb/html/resume.pdf
```

Lastly, navigate to `public_html/content/` and edit your `projects.md` file.

```
cd public_html/content;
nano projects.md;
```

Lastly, replace the project name, website link, project icon, and project description. You can replace the default icon, i.e. `terminal` with any other icon on [fontawesome.io](http://fontawesome.io/icons/) by replacing the icon name. My `projects.md` looks like this:

```
The App for Allergens
https://github.com/ninjha01/Mast
stethoscope
Developed an app that provides up to date information about purified allergens. It also provides users with information about Indoor Biotechnologies products: purified allergens, allergen standards, and assays. The app interfaces with the WHO allergen database.
---
Google Calendar CLI
https://gitlab.com/ninjha01/Project-Saturn
terminal
Created CLI that interacts with Google APIs to replicate the calendar functionality of the now-defunct Google CL application. Once the user is authenticated, it allows them to both view and add items to their agenda and to-do list.
---
Virginia Journal of Bioethics
http://www.vabioethics.com/
balance-scale
Maintained online presence of the Journal. Directed design and edited content of all published pieces. Created new submissions system that significantly decreased time required to publish articles. Automated large percentage of Social Media related tasks.
---
Looper
https://github.com/epigen/looper
circle-o-notch
A project manager written in python; it simplifies submitting pipeline jobs for your samples either on a supercomputing cluster or on your local computer.
``` 

Run the build.sh script, and you're finished!

```
cd ../../;
bash build.sh;
```

Congratulations! You now have your own personal website! Open it up and check it out!

`open myweb/html/index.html`

Thanks to QA testers:

1. Conner Pike
2. Nancy Lee
3. Jesse Persily
4. Samer El-abd

Produced by [Nishant Jha][my website].

[my website]: http://people.virginia.edu/~nj7kv/
[Fission (Biology)]: https://en.wikipedia.org/wiki/Fission_(biology)
