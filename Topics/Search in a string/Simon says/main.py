def what_to_do(instructions):
    ind = instructions.find("Simon says")
    if instructions.startswith("Simon says"):
        instructions = instructions.replace("Simon says", "").strip()
        return "I " + instructions
    elif instructions.endswith("Simon says"):
        return "I " + instructions[:ind]
    else:
        return "I won't do it!"
