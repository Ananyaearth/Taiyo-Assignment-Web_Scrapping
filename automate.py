import subprocess

def run_scraper():
    result = subprocess.run(["python", "scraper.py"], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Error running scraper.py")
        print(result.stderr)
        return False
    return True

def run_standardizer():
    result = subprocess.run(["python", "standardize.py"], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Error running standardize.py")
        print(result.stderr)
        return False
    return True

def main():
    if run_scraper():
        run_standardizer()

if __name__ == "__main__":
    main()
