import re;

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()

# Take a record of the currently selected line
currentLinePos = editor.getCurrentPos();
currentLine = editor.lineFromPosition(currentLinePos);

# Check if the url is internal web or core and replace the text with regex
editor.setSel(editor.positionFromLine(currentLine), editor.getLineEndPosition(currentLine));
lineText = editor.getSelText();
editor.clear();

#Usage: Add a key term to the if else statement. Replace everything before that key word with new url.
if('https://www.google.com/' in lineText.lower()):
       editor.addText(re.sub(r'^.*https://www.google.com/', 'http://localhost:00000/', lineText, flags=re.IGNORECASE));
elif('https://www.bing.com/' in lineText.lower()):      
       editor.addText(re.sub(r'^.*https://www.bing.com/', 'http://localhost:11111', lineText, flags=re.IGNORECASE));

editor.setEmptySelection(currentLinePos);

## Finished.
# End the undo action, so Ctrl-Z will undo the above two actions
editor.endUndoAction()

# Turn the undo recorder back on.
editor.setUndoCollection(1)