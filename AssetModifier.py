import maya.cmds as mc

def ChangePivotPosition(*args):
    # Get Selections
    sl = mc.ls(sl = True)
    
    for i in range(len(sl)):
        try:
            #Cycle through each mesh to get its properties 
            mc.select(sl[i])
            
            #Check the type selection(Needs to be object)
            mc.selectMode( object = True)
            
            #Delete History
            mc.delete(ch = True)
            
            #Get Bounds
            xmin,ymin,zmin,xmax,ymax,zmax = mc.exactWorldBoundingBox(calculateExactly = True)
        
            #Get Centre of the asset
            x = (xmin+xmax)/2
            y = (ymin+ymax)/2
            z = (zmin+zmax)/2
            
            #Get Desired pivot target location mode
            radioSel = mc.radioCollection("Pivot_Location", query = True, select = True)
            position = mc.radioButton(radioSel, query = True, label = True)
               
            #move pivot to Desired location
            if(position == "Bottom-Centre"):
                mc.move(x, ymin, z, sl[i]+".scalePivot", sl[i]+".rotatePivot", absolute = True)
                
            elif(position == "Left-Bottom-Front"):
                mc.move(xmin, ymin, zmax, sl[i]+".scalePivot", sl[i]+".rotatePivot", absolute = True)
                
            elif(position == "Top-Centre"):
                mc.move(x, ymax, z, sl[i]+".scalePivot", sl[i]+".rotatePivot", absolute = True)
                
            elif(position == "Left-Top-Front"):
                mc.move(xmin, ymax, zmax, sl[i]+".scalePivot", sl[i]+".rotatePivot", absolute = True)
                
            elif(position == "Left-Bottom-Back"):
                mc.move(xmin, ymin, zmin, sl[i]+".scalePivot", sl[i]+".rotatePivot", absolute = True)
                
            elif(position == "Left-Top-Back"):
                mc.move(xmin, ymax, zmin, sl[i]+".scalePivot", sl[i]+".rotatePivot", absolute = True)
                
            elif(position == "Centre"):
                mc.xform(sl[i], cp=1)
                
        except:
            mc.headsUpMessage("Some component are not in object mode")

def SetToOrigin(*args):
    
    sl = mc.ls(sl = True)
    
    for i in range(len(sl)):
        mc.select(sl[i])
        
        mc.delete(ch = True)
    
        #Move the mesh to Origin
        mc.move(0,0,0 , rpr = True)

def Freeze(*args):
    
    sl = mc.ls(sl = True)
    
    for i in range(len(sl)):
        mc.select(sl[i])
        
        mc.delete(ch = True)
    
        #Freeze Transformation
        mc.FreezeTransformations()
        
def History(*args):
    # Get Selections
    sl = mc.ls(sl = True)
    
    for i in range(len(sl)):

        mc.select(sl[i])
        
        mc.delete(ch = True)
    

#Define GUI for Asset Modifier/Evalator
def CreateWindow():
	name = "Asset Modifier/Evaluator"
	#if (mc.window(name, exists= True)):
	#	mc.deleteUI(name, window = True)
	mc.window(name)
	mc.showWindow()
	column = mc.columnLayout(adjustableColumn = True)
	mc.setParent(column)
	mc.textField(text = "Y-Top and Z-Front (Maya to Unreal preference)", editable = False, height = 30)
	mc.radioCollection("Pivot_Location")
	mc.radioButton(label = "Bottom-Centre")
	mc.radioButton(label = "Left-Bottom-Front")
	mc.radioButton(label = "Top-Centre")
	mc.radioButton(label = "Left-Top-Front")
	mc.radioButton(label = "Left-Bottom-Back")
	mc.radioButton(label = "Left-Top-Back")
	mc.radioButton(label = "Centre")
	btnPivot = mc.button(label = "Change Pivot to", command = ChangePivotPosition)
	mc.text("----------------------------") 
	btnPivot = mc.button(label = "Move Mesh to Origin", command = SetToOrigin)
	mc.text("----------------------------")
	btnPivot = mc.button(label = "Freeze Transformation", command = Freeze)
	mc.text("----------------------------")
	btnPivot = mc.button(label = "Delete History", command = History)

#Create Window
CreateWindow()