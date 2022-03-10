#####
## Draw two dashed lines seperated by empty line and move caret to empty line
#####

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()

dash='-'
width=80

# Take a record of the currently selected line
currentLinePos = editor.getCurrentPos();
currentLine = editor.lineFromPosition(currentLinePos);

# Check if any text exists on the line. If Yes move to the next line before running script
editor.setSel(editor.positionFromLine(currentLine), editor.getLineEndPosition(currentLine));
lineText = editor.getSelText();
editor.setEmptySelection(currentLinePos);
if(len(lineText) > 0):
    editor.newLine();

# Add two dashed rows seperated by a new line
editor.homeDisplay();
editor.addText(dash*width);
editor.newLine();
editor.newLine();
editor.addText(dash*width);

# Refresh selected line positions after insert
currentLinePos = editor.getCurrentPos();
currentLine = editor.lineFromPosition(currentLinePos);

# Place caret in between newely added lines
editor.gotoLine(currentLine-1);

## Finished.
# End the undo action, so Ctrl-Z will undo the above two actions
editor.endUndoAction()

# Turn the undo recorder back on.
editor.setUndoCollection(1)