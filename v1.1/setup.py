import cx_Freeze
import sys

cx_Freeze.setup(
	name="Soy Qbertito v1.0",
	version="1.0",
	options={"build_exe": {"packages": ["pygame"],
						   "include_files":["imagenes",
                                            "pantallas",
                                            "utiles.py"]}
		    },
	executables=[cx_Freeze.Executable("principal.pyw")]
)