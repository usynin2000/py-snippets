paths = {} # get it by taking openapi.json (/docs) usually helps find it

with open("paths.md", "a", encoding="utf-8") as file:
    file.write("Service-Name paths:")
    for key in paths["paths"]:
        file.write(f"- [ ] {key}\n")


