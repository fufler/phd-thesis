XELATEX='xelatex'
LLFLAGS=--halt-on-error --shell-escape --file-line-error

TIKZ := $(patsubst %.tex,%.pdf,$(wildcard tikz/*.tex))
DEPS := $(shell grep '\\subfile' *.tex | grep -v '^%'  | cut -f2 -d: | sed 's/.*{\([a-z_-/A-Z0-9]\+\)}.*/\1.tex/g')

GRAYSCALE_IMGS := $(shell grep gray.png *.tex | egrep -v '[ \t]*%' | sed 's/.*{\(png\/[a-z_-+/A-Z0-9]\+-gray.png\)}.*/\1/g')
TRANSPARENT_IMGS := $(shell grep transparent.png *.tex | egrep -v '[ \t]*%' | sed 's/.*{\(png\/[a-z_-+/A-Z0-9]\+-transparent.png\)}.*/\1/g')
TRANSPARENT_IMGS := $(patsubst %.png,%-transparent.png, $(shell find png/spgcm/ png/air-nuke png/air-nuke-engines png/satellite png/markers -type f | grep -v transparent ))
SPGCM_IMGS := $(shell grep all.png *.tex | egrep -v '[ \t]*%' | sed 's/.*{\(png\/[a-z_-+/A-Z0-9]\+-all.png\)}.*/\1/g')

JPG_IMGS := $(patsubst png/%.png, jpg/%.jpg, $(shell find png/armor/50 -name *.png | grep -v transparent))

default: all

all: thesis abstract presentation
thesis: ermakov_phd_thesis.pdf
abstract: ermakov_phd_thesis_abstract.pdf
presentation: ermakov_phd_thesis_presentation.pdf

tikz: $(TIKZ)

grayscale: $(GRAYSCALE_IMGS)
transparent: $(TRANSPARENT_IMGS)
spgcm_imgs: $(SPGCM_IMGS)
jpg: $(JPG_IMGS)

tikz/%.pdf: tikz/%.tex
	$(XELATEX) $(LLFLAGS) --output-directory tikz $<

jpg/%.jpg: png/%.png
	mkdir -p $$(dirname $@ )
	convert $< $@

%-gray.png: %.png
#	convert -colorspace gray -auto-level $< $@
#	convert -colorspace gray -auto-level -auto-gamma $< $@
	convert -colorspace gray -auto-gamma -auto-level $< $@
%-transparent.png: %.png
	convert  -transparent white $< $@

%-all.png: $(shell echo %-{0..9}-transparent.png)
	convert \
		\( $*-0-transparent.png  $*-1-transparent.png +append \) \
		\( $*-2-transparent.png  $*-3-transparent.png +append \) \
		\( $*-4-transparent.png  $*-5-transparent.png +append \) \
		\( $*-6-transparent.png  $*-7-transparent.png +append \) \
		\( $*-8-transparent.png  $*-9-transparent.png +append \) \
		-append $@

beamer-mtheme/%.sty: beamer-mtheme/%.dtx
	make -C beamer-mtheme sty

%.sty: beamer-mtheme/%.sty
	ln -sf $< $@

ermakov_phd_thesis.pdf: $(DEPS) spgcm_imgs thesis.pdf
	mv thesis.pdf $@

ermakov_phd_thesis_abstract.pdf: grayscale abstract.pdf
	mv abstract.pdf $@

ermakov_phd_thesis_presentation.pdf: transparent jpg beamercolorthememetropolis.sty beamerfontthememetropolis.sty beamerthemem.sty presentation.pdf
	mv presentation.pdf $@

%.pdf: %.tex
	$(XELATEX) $(LLFLAGS) $<;
	$(eval AUX := $(patsubst %.tex,%.aux,$<))
	if grep -q bibdata $(AUX); then \
		bibtex  $(AUX); \
	fi
	$(XELATEX) $(LLFLAGS) $<;
	$(XELATEX) $(LLFLAGS) $<;

clean:
	rm -rf jpg
	find .                                        \
		 \(                                       \
			-name '*.log'                      -o \
			-name '*.aux'                      -o \
			-name '*.bbl'                      -o \
			-name '*.blg'                      -o \
			-name '*.toc'                      -o \
			-name '*.out'                      -o \
			-name '*.tdo'                      -o \
			-name '*.eps'                      -o \
			-name '*.nav'                      -o \
			-name '*.snm'                      -o \
			-name '*.sty'                      -o \
			-name '*.pyc'                      -o \
			-name '*.vrb'                      -o \
			-name 'latex.py'                   -o \
			-name 'composite.py'               -o \
			-name 'composite.pyc'              -o \
			-name 'composite.py.err'           -o \
			-name 'thesis.py'                  -o \
			-name 'thesis.pyc'                 -o \
			-name 'thesis.py.err'              -o \
			-name 'obstacle.pyc'               -o \
			-name 'obstacle.py'                -o \
			-name 'obstacle.py.err'            -o \
			-name 'presentation.py'            -o \
			-name 'presentation.pyc'           -o \
			-name 'presentation.py.err'        -o \
			-name 'presentation_moar.py'       -o \
			-name 'presentation_moar.pyc'      -o \
			-name 'presentation_moar.py.err'   -o \
			-name '*pgf-plot*'                 -o \
			-name '*.gnuplot'                  -o \
			-name '*-gnuplottex-*'             -o \
			-name '*.pdf'                      -o \
			-name '*-transparent.png'          -o \
			-name '*-gray.png'                 -o \
			-name '*-all.png'                  -o \
			-name '__pycache__'                   \
		 \)                                       \
		 ! -path './eps/*'                        \
		 ! -path './beamer-mtheme/*'            | \
	xargs -r rm -rf

.PHONY: default clean tikz all thesis abstract grayscale presentation
