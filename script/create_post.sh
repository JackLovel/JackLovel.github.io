#!/usr/bin/bash

#################
# 创建 jekyll 文章
#################

time=`date +%F`
#post_directory='~/codePro/JackLovel.github.io/_posts/'
join='-'

function cm() {
    read -p '文章名：' postname
    filename=${time}${join}${postname}.md
    #cd $post_directory
    touch $filename

    echo "文章创建成功!"
}

cm