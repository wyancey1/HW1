philosophers = ['John Locke', 'David Hume', 'Edmund Burke']

def main():
    outfile = open('philosophers.txt','w')

    for i in philosophers:
        outfile.write(i+'\n')
    
    outfile.close()

main()