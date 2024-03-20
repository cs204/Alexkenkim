def main():
    string = input()
    string = convert(string)

def convert(nstring):
    nstring= nstring.replace(":)", "🙂").replace(":(", "🙁")
    print(nstring)
    return nstring

main()
