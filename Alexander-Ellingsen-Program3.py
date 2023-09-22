def main(file):
    sectors = list_sectors(file)
    sector = get_user_choice(sectors)
    securities = get_securities_in_sector(file, sector)
    generate_report(securities, sector)

def list_sectors(file):
    print("GICS Sectors in the S&P 500".center(60, '-'))
    sp500 = open(file, 'r', errors ="ignore")
    sp500.readline()
    sectors = []
    num = 1
    for line in sp500:
        listing = line.split(',')
        if listing[2] not in sectors:
            sectors.append(listing[2])
    sp500.close()
    sectors.sort()
    for sector in sectors:
        print(str(num) + '. ' + sector)
        num += 1
    print(''.center(60, '-'))
    return sectors

def get_user_choice(sectors):
    choice = int(input("Enter sector by number: "))
    while choice not in range(1,12):
        choice = int(input("Please enter a valid choice (1-11): "))
    else:
        return(sectors[choice-1])

def get_securities_in_sector(file, sector):
    sp600 = open(file, 'r', errors="ignore")
    securities_list = []
    for line in sp600:
        listz = line.split(',')
        if listz[2] == sector:
            securities_list.append((listz[0], listz[1], listz[3]))
    return(securities_list)

def generate_report(securities, sector):
    number = str(len(securities))
    print((number + " S&P Securities in " + sector).center(60, '-'))
    for i in securities:
        count = securities.index(i) + 1
        print(((str(count) + ".").ljust(4, ' ') + str(securities[securities.index(i)][0])).ljust(8, " ") + "   " + str(securities[securities.index(i)][1]).ljust(40, ".") + str(securities[securities.index(i)][2]) )
    answer = input("Save Report? ")
    if answer[:1].lower() == 'y':
        out_file_name = input("Enter filename: ")
        out_file = open(out_file_name, 'w')
        out_file.write((number + " S&P Securities in " + sector).center(60, '-') + "\n")

        for i in securities:
            count = securities.index(i) + 1
            out_file.write(((str(count) + ".").ljust(4, ' ') + str(securities[securities.index(i)][0])).ljust(8, " ") + "   " + str(securities[securities.index(i)][1]).ljust(40, ".") + str(securities[securities.index(i)][2]) + "\n")
        print("Report saved as " + out_file_name)
        out_file.close()
        
        
        
main("sp500.csv")



