# Конвертация markdown-файлов с помощью pandoc

## markdown -> html5
```
pandoc -t html5 --toc -s ./summary.md -o ./summary.html
```

## markdown -> pdf
```
pandoc --variable mainfont="Roboto" --variable sansfont="Garuda" --variable monofont="Courier New" --variable fontsize=10pt --variable version=2.0 --pdf-engine=xelatex --toc -s ./summary.md -o ./summary.pdf
```
