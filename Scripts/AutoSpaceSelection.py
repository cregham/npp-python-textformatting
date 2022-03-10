#####
## Auto space spacingTokened lines
#####
# Set Undo Action
#Usage: Replace spacing token with what you want to auto space.
#       Highlight rows or none to do entire file. 
#       Run script and all content will be spaced by the token based on the longest string in the selection/file

editor.beginUndoAction();

spacingToken='-'
joinSpace=' ' + spacingToken + ' '
width = 0;
selectedLines = editor.getUserLineSelection();

#nppTabWidth = Notepad++ Preferences Tab Width    
nppTabWidth = 4; 

# Calculate longest string in the file
def GetStringLengthBeforespacingToken(contents, lineNumber, totalLines):
    global width, spacingToken, selectedLines, nppTabWidth;   
    if spacingToken in contents:
        leftContent = contents.split(spacingToken, 1)[0].expandtabs(nppTabWidth).rstrip();
        index = len(leftContent) + 2;
        if lineNumber >= selectedLines[0] and lineNumber <= selectedLines[1] and width < index:            
            width = index;
  
# Split the string, set the new whitespace width based on longest line and join together by the split character
def SetWhiteSpace(contents, lineNumber, totalLines):
    global width, spacingToken, selectedLines, nppTabWidth;
    index = contents.find(spacingToken);
    if lineNumber >= selectedLines[0] and lineNumber <= selectedLines[1] and index > 0:       
        splitArray = contents.split(spacingToken, 1);
        #Left of spacingToken: strip whitespace to the right and expand tabs as len(tab) = 1 instead of 4;
        splitArray[0] = splitArray[0].expandtabs(nppTabWidth).rstrip();
        #The trailing space is the result of GetStringLengthBeforespacingToken() subtract the length of the text on this line
        trailingWhitespace = ' '*(width - len(splitArray[0].replace(' ', '.')) - 1);
        splitArray[0] = splitArray[0] + trailingWhitespace;
        #For everything after the first spacingToken strip the white space;
        for i in range(1, len(splitArray)):
            splitArray[i] = splitArray[i].strip();
        editor.replaceLine(lineNumber, joinSpace.join(splitArray));    

editor.forEachLine(GetStringLengthBeforespacingToken);
editor.forEachLine(SetWhiteSpace);
## Finished.
# End the undo action, ctrl - z will revert script
editor.endUndoAction();

# Turn the undo recorder back on.
editor.setUndoCollection(1);