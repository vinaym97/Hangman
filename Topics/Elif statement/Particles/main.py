spin = input()
charge = input()
if charge == "-1/3" and spin == "1/2":
    print("Strange Quark")
if charge == "2/3" and spin == "1/2":
    print("Charm Quark")
elif charge == "-1" and spin == "1/2":
    print("Electron Lepton")
elif charge == "0" and spin == "1/2":
    print("Neutrino Lepton")
elif charge == "0" and spin == "1":
    print("Photon Boson")
