#!/bin/bash

quoteSubst() {
    IFS= read -d '' -r < <(sed -e ':a' -e '$!{N;ba' -e '}' -e 's/[&/\]/\\&/g; s/\n/\\&/g' <<<"$1")
    printf %s "${REPLY%$'\n'}"
}
#Build Home Page

##Build Projects
TAG="{PROJECTS}";
VALUE=$(./public_html/builders/project_builder.out ./public_html/content/projects.md);
sed -e ':a' -e '$!{N;ba' -e '}' -e "s/$TAG/$(quoteSubst "$VALUE")/" ./public_html/boilerplate/home.html > ./myweb/html/index.html;

##Build the Menu
TAG="{MENU}";
VALUE=$(./public_html/builders/menu_builder.out ./public_html/content/projects.md);
sed -e ':a' -e '$!{N;ba' -e '}' -e "s/$TAG/$(quoteSubst "$VALUE")/" ./myweb/html/index.html > temp.html;
mv temp.html ./myweb/html/index.html;
