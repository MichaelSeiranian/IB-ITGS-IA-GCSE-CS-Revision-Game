import cx_Freeze

executables = [cx_Freeze.Executable("Game.py")]

cx_Freeze.setup(
	name="Computer Science revision game",
	options={"build_exe": {"packages":["pygame"],"include_files":["R1.png", "R2.png", "R3.png", "R4.png", "L1.png", "L2.png", "L3.png", "L4.png", "U1.png", "U2.png", "U3.png", "U4.png", "D1.png", "D2.png", "D3.png", "D4.png", "bg.jpg", "bg1.jpg"]}},
	executables = executables

	)