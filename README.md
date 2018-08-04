# Project [Fission][Fission (Biology)] #

Project Fission is a personal website creation tool. 

## Quickstart Guide ##

*Requires `pandoc` and `python` with `pypandoc` and `pyyaml`.

In your bash shell (Terminal.app on macOS) enter the following:

`git clone https://github.com/ninjha01/fission`

This will create a local copy of the Project Fission code.

Open and edit the `config.yml` file using an editor of your choice. `nano` is suggested for those who aren't familiar with command-line editors.

```
cd fission;
nano details.md;
```

Fill in the form with your own personal details. You can replace the default icon, i.e. `pencil` with any other icon on [fontawesome.io](http://fontawesome.io/icons/) by replacing the icon name.

Here's how my personal `yaml.config` looks:

```
Personal:
  $FIRST$: Nishant
  $LAST$: Jha
  $TITLE$: MS in CS Candidate at the University of Virginia
  $BIO$: I am a computer scientist with a solid background in the Physical, Social, and Life Sciences. I enjoy writing about the potential impact of revolutionary technology on society as well as working at the intersection of biological research and computer science.
  $LINKEDIN$: https://www.linkedin.com/in/ninjha01
  $EMAIL$: ninjha01@gmail.com
Projects:
  - $TITLE$: Project Fission
    $URL$: https://github.com/ninjha01/fission
    $ICON$: files-o
    $BLURB$: Project Fission is a website generator! Simply edit two text files and Fission will create a full-fledged website. It generates easy-to-edit html files so you have full control over your newly minted website.
  - $TITLE$: Allergen Guru
    $URL$: https://inbio.com/app
    $ICON$: stethoscope
    $BLURB$: Allergen Guru is an Android and iOS containing structural information on allergens listed on the WHO/IUIS Allergen nomenclature database, along with 3D structures and unique search features, which will make Guru an essential tool for allergen researchers.
```

After filling in `yaml.config`, run the `build.py` script.

`python build.py`

Lastly, replace the blank profile picture and resume with your own copies.

```
mv /path/to/profile.jpg ./images/profile.jpg
mv /path/to/resume.pdf ./resume.pdf
``` 

Congratulations! You now have your own personal website! Open it up and check it out!

`open index.html`

Produced by [Nishant Jha][my website].

[my website]: https://ninjha01.github.io/
