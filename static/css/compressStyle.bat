@echo off

set scss=.\style.min.css

if exist %scss% (
    del %scss%
)

@echo on
stylus .\style.styl -c -o %scss%