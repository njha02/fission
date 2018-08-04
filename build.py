import os
import pypandoc
import yaml
    
tags = ["{FIRST}", "{LAST}", "{EMAIL}", "{LINKEDIN}", "{TITLE}", "{BIO}"]

def main():
    ## Load and parse config file
    with open('config.yml', 'r') as config_file:
        config_file = yaml.load(config_file)

    #Populate Templates with Personal Data
    files_to_load = ("template/home.html", "template/menu.html")
    home_template, menu_template = load_files(files_to_load)
    personal_details = config_file["Personal"]
    for tag, value in personal_details.items():    
        home_template = home_template.replace(tag, value)

    project_details = config_file["Projects"]
    
    menu_html = build_menu(project_details, menu_template)
    tag = "$MENU$"
    home_template = home_template.replace(tag, menu_html)
    
    build_home(project_details, menu_html, home_template)
    print("Website Built!")

def build_menu(p_details, menu_template):
    entry_template = '<li><a href="$URL$">$TITLE$</a></li>'    
    # Process Projects
    p_entries = []
    for essay in p_details:
        entry = entry_template
        for tag, value in essay.items():
            entry = entry.replace(tag, value)
        p_entries.append(entry)
    p_entries = '\n'.join(p_entries)
    menu = menu_template.replace("$PROJECTS$", p_entries)
    return menu

def build_home(p_details, menu_html, home_template):
    
    entry_template = ( '<article>\n<span class="icon fa-$ICON$"></span>'
                         '<div class="content">'
                         '<h3><a href=$URL$>$TITLE$</a></h3>'
                         '<p>$BLURB$</p></div>\n</article>' )
    
    # Process Projects
    p_entries = []
    for project in p_details:
        entry = entry_template
        for tag, value in project.items():
            entry = entry.replace(tag, value)
        p_entries.append(entry)
    p_entries = '\n'.join(p_entries)
    payload = home_template.replace("$PROJECTS$", p_entries)
    with open('index.html', "w") as page:
        page.write(payload)
                    
def load_files(filenames):
    loaded_files = []
    for filename in filenames:
       with open(filename, "r") as file:
            loaded_files.append(file.read())
    return loaded_files

if __name__=="__main__":
    main()
