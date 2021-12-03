call clean-pyscripts.cmd

setLocal
	set notebooks="Finger Identifier" FingerMovement HandDirection Main "Static Gestures Class" Untitled

	:: build
	for %%F in (%notebooks%) do (
		jupyter nbconvert --to script "%%~F.ipynb"
	)
endLocal