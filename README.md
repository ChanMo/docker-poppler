# Docker Poppler

A simple http api service for poppler, include `pdftohtml`, `pdftotext`, `pdfinfo`, `pdftoppm`, `pdftocairo`

Need more format converting tools ? 
- [chanmo/pandoc](https://github.com/ChanMo/docker-pandoc)
- [chanmo/unoserver](https://github.com/ChanMo/docker-unoserver)

## Usage

pull the docker image
```
docker pull chanmo/poppler
```

start a http server
```
docker run --rm -p 5000:5000 chanmo/poppler
```

convert a pdf file to the html format
```
http -f POST :5000/pdftohtml file@/path/to/file.pdf -o demo.html
```

convert a pdf file to the text string
```
http -f POST :5000/pdftotext file@/path/to/file.pdf
```

convert a pdf file to multiple images
```
http -f POST :5000/pdftocairo file@/path/to/file.pdf
```

get a pdf file information
```
http -f POST :5000/pdfinfo file@/path/to/file.pdf
```

## TODO

- [ ] add pdfgrep
- [ ] add params
