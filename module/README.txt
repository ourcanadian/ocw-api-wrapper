PROBLEM AS A WINDOWS USER:

	"make test" Fails. Windows does not have the tool "make".
	
SOLUTION:

	Download MAKE from SourceForge: https://sourceforge.net/projects/gnuwin32/files/make/3.81/make-3.81.exe/download?use_mirror=iweb&download=

	Install it, following the recommendations.

	Go to the install folder: (by default) C:\Program Files(x86)\GnuWin32\bin

	Copy the path name (C:\Program Files(x86)\GnuWin32\bin) or whatever file you installed to.

	In the naviagtion bar, search "Edit the system environment variables" and select the option.

	Under the "Advanced" tab, click on the "Environment Variables..." button.

	Click on the "path" variable under "System variables", and click "Edit...".

	Append a semicolon to the variable value and paste the path name of the new install bin for MAKE.

	Click "OK" and "OK" on the next page to complete.

	Reopen Command Prompt to refresh the environment variables. Then, navigate yourself to "module" directory in "ocw-api-wrapper".

	Edit the "Makefile" with a text editor of your choice. I use Notepad++. On a new line at the top of the page, paste "SHELL=C:/Windows/System32/cmd.exe". This will force MAKE to use the correct shell.

	Now run "make.exe" in Command Prompt in the "module" directory to compile the code using MAKE.


FURTHERMORE:

	If you ever have an error along the lines of "'python3' is not recognized as an internal or external command" change "python3" to "py". So change it in the Makefile if you come across this error. 

