SET WorkingRoot TO $'''C:\\PAD-Labs\\working\\lab02'''
SET CsvCount TO 0
SET TxtCount TO 0
SET IgnoredCount TO 0
IF (Folder.IfFolderExists.DoesNotExist Path: $'''%WorkingRoot%\\archive\\csv''') THEN
    Folder.Create FolderPath: $'''%WorkingRoot%\\archive''' FolderName: $'''csv''' Folder=> NewFolder
END
IF (Folder.IfFolderExists.DoesNotExist Path: $'''%WorkingRoot%\\archive\\txt''') THEN
    Folder.Create FolderPath: $'''%WorkingRoot%\\archive''' FolderName: $'''txt''' Folder=> NewFolder
END
IF (Folder.IfFolderExists.DoesNotExist Path: $'''%WorkingRoot%\\archive\\ignored''') THEN
    Folder.Create FolderPath: $'''%WorkingRoot%\\archive''' FolderName: $'''ignored''' Folder=> NewFolder
END
Folder.GetFiles Folder: $'''%WorkingRoot%\\inbox''' FileFilter: $'''*''' IncludeSubfolders: False FailOnAccessDenied: True SortBy1: Folder.SortBy.NoSort SortDescending1: False SortBy2: Folder.SortBy.NoSort SortDescending2: False SortBy3: Folder.SortBy.NoSort SortDescending3: False Files=> InboxFiles
LOOP FOREACH CurrentFile IN InboxFiles
    File.GetPathPart File: CurrentFile Extension=> FileExtension
    IF FileExtension = $'''.csv''' THEN
        File.Copy Files: CurrentFile Destination: $'''%WorkingRoot%\\archive\\csv''' IfFileExists: File.IfExists.Overwrite CopiedFiles=> CopiedFiles
        Variables.IncreaseVariable Value: CsvCount IncrementValue: 1
    ELSE IF FileExtension = $'''.txt''' THEN
        File.Copy Files: CurrentFile Destination: $'''%WorkingRoot%\\archive\\txt''' IfFileExists: File.IfExists.Overwrite CopiedFiles=> CopiedFiles
        Variables.IncreaseVariable Value: TxtCount IncrementValue: 1
    ELSE
        File.Copy Files: CurrentFile Destination: $'''%WorkingRoot%\\archive\\ignored''' IfFileExists: File.IfExists.Overwrite CopiedFiles=> CopiedFiles
        Variables.IncreaseVariable Value: IgnoredCount IncrementValue: 1
    END
END
SET SummaryText TO $'''CSV=%CsvCount% ; TXT=%TxtCount% ; IGNORED=%IgnoredCount% ;  Done'''
File.WriteText File: $'''%WorkingRoot%\\summary.txt''' TextToWrite: SummaryText AppendNewLine: True IfFileExists: File.IfFileExists.Overwrite Encoding: File.FileEncoding.Unicode
