filename='init.md'
while read p; do
    
    TAG=$(echo $p | cut -f1 -d-);
    VALUE=$(echo $p | cut -f2 -d-);
        
    sed -i -e "s/$TAG/$VALUE/g" public_html/boilerplate/top_home.html;
    sed -i -e "s/$TAG/$VALUE/g" public_html/boilerplate/bottom_home.html;
done < $filename


