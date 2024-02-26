print("""D2L PDF URL finder
      
Copy the entire HTML Code of the D2L page.
Method 1: (CTRL+U > CTRL+A > CTRL+C) 
    1. Press CTRL+U or right-click > View page source
    2. CTRL+A > CTRL+C
Method 2:
    1. Inspect
    2. Go to the <html> element > right click it > click Edit HTML
    3. CTRL+A > CTRL+C
Afterwards, paste (CTRL+V or SHIFT+CTRL+V) the code to this program.
Then, press Enter. If the URL is not printed, press CTRL+C or CTRL+Z.
As D2L requires authentication, you cannot paste the link.
Paste HTML Code:""")

code = []
try:
    while True:
        userInput = input()
        code.append(userInput)

        # Automatically determine the end of the code
        if userInput.strip().endswith("</html>"):
            raise KeyboardInterrupt()
        
except (KeyboardInterrupt, EOFError):
    pass

# Iterate through each line. If it contains a class for PDFs, then go find the location value
for line in code:
    if "d2l-fileviewer-pdf-pdfjs" in line.lower():
        location = line.split("location=\"", 1)[1].split("\" ", 1)[0] 
        print("\nPDF URL: \nhttps://d2l.cbe.ab.ca" + location + "\n")

input("Press enter to exit...")        