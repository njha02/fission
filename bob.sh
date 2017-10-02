#!/bin/bash

# Build Home Page

## Build the Top
rm ./myweb/html/index.html;
touch ./myweb/html/index.html;
cat ./public_html/boilerplate/top_home.html > ./myweb/html/index.html

## Build Projects
./public_html/builders/project_builder.out ./public_html/content/projects.md >> ./myweb/html/index.html

## Build the Menu
cd ./myweb/html/;
../../public_html/builders/menu_builder.out ../../public_html/content/projects.md >> ../../myweb/html/index.html;
cd ../../;

## Build the Bottom
cat ./public_html/boilerplate/bottom_home.html >> ./myweb/html/index.html;
