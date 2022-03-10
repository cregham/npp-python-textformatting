#####
## Draw a dashed line
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

# Add single dashed row
editor.newLine();
editor.homeDisplay();
editor.addText(dash*width);
editor.newLine();

# Refresh selected line positions after insert
currentLinePos = editor.getCurrentPos();
currentLine = editor.lineFromPosition(currentLinePos);

# Place caret above newely added line
editor.gotoLine(currentLine-2);

## Finished.
# End the undo action, so Ctrl-Z will undo the above two actions
editor.endUndoAction()

# Turn the undo recorder back on.
editor.setUndoCollection(1)