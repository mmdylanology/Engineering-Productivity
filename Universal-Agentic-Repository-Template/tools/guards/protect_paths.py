import sys, os, fnmatch, yaml

def check_file(path):
    if not os.path.exists("governance/protected_paths.yaml"):
        return True
    rules = yaml.safe_load(open("governance/protected_paths.yaml"))
    for rule in rules.get("immutable", []):
        if fnmatch.fnmatch(path, rule["glob"]):
            print(f"BLOCKED: {rule['reason']}\nRemedy: {rule['remedy']}", file=sys.stderr)
            return False
    return True

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        if not check_file(arg):
            sys.exit(2)
    sys.exit(0)
