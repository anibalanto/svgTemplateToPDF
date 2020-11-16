# svgTemplateToPDF
You can use a svg Template using svglue to generete many documents accross data files in csv documents.
You have two options to generate pdf files, using inkscape bash command
```
python svgTemplate.py example/examp1 inkscape
```
 or using cairosvg library
```
python svgTemplate.py example/examp1 cairosvg
```

If you can only generate svg files (without pdf), you can only don't use te pdf generator option
```
python svgTemplate.py example/examp1
```
