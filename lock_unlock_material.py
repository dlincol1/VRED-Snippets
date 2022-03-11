mtl = findMaterial('PlasticMaterial')
mtl.fields().addAttachment(createAttachment('VREDLock')) # Lock
mtl.fields().subAttachment(mtl.fields().getAttachment('VREDLock')) # Unlock
