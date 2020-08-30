@echo off

set scss=.\custom.min.js

if exist %scss% (
    del %scss%
)

@echo on
uglifyjs .\custom.js -c -o %scss%