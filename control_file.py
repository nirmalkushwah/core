


def controls_Func(controlsData):
    if controlsData["type"] == "light":
        print("light id= " + controlsData["id"]+ " value  = " + controlsData["set"])
    if controlsData["type"] == "curtain":
        print("curtain id= " + controlsData["id"] + " value = " + controlsData["set"])
    if controlsData["type"] == "AC":
        print("AC id = " + controlsData["id"] + " value = " + controlsData["set"])
