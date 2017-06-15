all:
	mkdir -p text
	xelatex gtools-icon.tex
	rm -f gtools-icon.aux
	rm -f gtools-icon.log
	rm -f gtools-icon.fls
	rm -f gtools-icon.log
	convert -density 600 gtools-icon.pdf\[0\] gtools-icon-text.svg
	convert gtools-icon-text.svg gtools-icon-text.png
	convert gtools-icon-text.png -fuzz 0% -transparent white gtools-icon-text.png
