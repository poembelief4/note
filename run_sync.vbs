Option Explicit

Dim shell, fileSystem, scriptDirectory, batchPath, exitCode
Set shell = CreateObject("WScript.Shell")
Set fileSystem = CreateObject("Scripting.FileSystemObject")

scriptDirectory = fileSystem.GetParentFolderName(WScript.ScriptFullName)
batchPath = fileSystem.BuildPath(scriptDirectory, "sync_once.bat")
shell.CurrentDirectory = scriptDirectory

exitCode = shell.Run(Chr(34) & batchPath & Chr(34), 0, True)
WScript.Quit exitCode
