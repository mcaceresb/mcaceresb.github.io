all:
	xelatex ./icon-testing.tex
	# xx convert -density 600 icon-testing.pdf bigdata-icon.png
	# xx convert -density 600 icon-testing.pdf bigdata-icon.svg
	# xx convert -density 600 bigdata-icon-small.png bigdata-icon-small.svg
	# xx convert -density 600 -resize 250 icon-testing.pdf bigdata-icon.png
	# xx convert -background none bigdata-icon.png bigdata-icon.svg
	# convert icon-testing.pdf -transparent white bigdata-icon.svg
	inkscape icon-testing.pdf --export-type=svg --export-filename=bigdata-icon.svg 
	# --export-area-drawing --export-width=50 --export-height=50
