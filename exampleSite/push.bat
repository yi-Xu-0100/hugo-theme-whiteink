@echo off
set pan=.\public\
set repo=git@hugotheme:yi-Xu-0100/hugo-theme-whiteink.git
set branch=gh-pages
if exist %pan% (
    
    echo "clean public directory"
    rd /S /Q %pan%
    if exist %pan% (
        goto error
    ) else (
        echo "public directory clear"
    )
    echo "Hugo again for new site"
    hugo
) else (
    echo "can not find public directory"
    echo "Hugo again for new site"
    hugo
)
if exist %pan% (
    cd %pan%
    echo "git init and commit"
    git init
    git checkout -b %branch%
    git add --all
    git commit -m "update site at %time%"
    echo "set remote repository and push forcely"
    git remote add origin %repo%
    ssh -T git@github.com
    git push -f origin %branch%:%branch% -v
) else (
    echo "can not find public directory, hugo fail!"
)
cd ..
git remote set-url origin %repo%
goto exit

:error
echo "public directory do not be clear"
goto exit

:exit
pause
