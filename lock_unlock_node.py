# Lock / Unlock selected node
def lockSelectedNode():
    selected = getSelectedNode()
    print('Locking node:' + selected.getName())
    lock = createAttachment("VREDLock")
    selected.addAttachment(lock)

def unlockSelectedNode():
    selected = getSelectedNode()
    print('Unlocking node:' + selected.getName())
    lock = selected.getAttachment("VREDLock")
    selected.subAttachment(lock)

# Press "L" in Viewport to Lock
keyL = vrKey(Key_L)
keyL.connect("lockSelectedNode()")
keyL.setDescription("Lock Selected Node")

# Press "Shift-L" in Viewport to Unlock
keyLs = vrKey(Key_L, ShiftButton)
keyLs.connect("unlockSelectedNode()")
keyLs.setDescription("UnLock Selected Node")
