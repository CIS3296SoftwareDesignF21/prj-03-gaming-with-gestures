Gestures.UML: Gestures.UML.pdf Gestures.UML.png

Gestures.UML.pdf: Gestures.UML.dot
	dot -Tpdf $^ -o$@

Gestures.UML.png: Gestures.UML.dot
	dot -Tpng $^ -o$@
