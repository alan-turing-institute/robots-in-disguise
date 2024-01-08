pdfs = transformers-rcp-benchmarking.pdf

all: $(pdfs)

$(pdfs): %.pdf: %.tex
	pdflatex $<
	pdflatex $<

clean:
	rm -f *.blg *.log *.pdf *.bbl *.aux *.out *.fls *.nav *.snm *.toc

