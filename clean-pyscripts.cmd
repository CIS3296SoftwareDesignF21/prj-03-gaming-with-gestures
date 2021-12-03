setLocal
	set notebooks="Finger Identifier" FingerMovement HandDirection Main "Static Gestures Class" Untitled

	:: clean
	for %%F in (%notebooks%) do (
		del "%%~F.py"
	)
endLocal