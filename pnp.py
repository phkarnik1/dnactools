# string to search in file

def main():
    file_name = input("Please enter provisioning-service log file: ")
    lines = []
    try:
        with open(file_name, 'r') as fp:
        # read all lines using readline()
            lines = fp.readlines()
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        # Handle other potential exceptions
        print(f"An error occurred: {e}")

    apclaims = []
    i = 0
    for row in lines:
        # check if string present on a current line
        word = 'Ap Claim'
        #print(row.find(word))
        # find() method returns -1 if the value is not found,
        # if found it returns index of the first occurrence of the substring
        if row.find(word) != -1:
            print (row)
            apclaims.append(row)
        
    apclaimsIDs = []
    for j in range(0,len(apclaims)):
        str = apclaims[j]
        apclaimsval = str.split("Ap Claim")[1]
        apclaimsIDs.append(apclaimsval.split(' | ')[0])
        
    for k in range(0,len(apclaimsIDs)):
        print("searching for provision status of : " + apclaimsIDs[k])
        for row in lines:
            word = "Received ZtdDeviceProvisionedMessage for device " + apclaimsIDs[k]
            if row.find(word) != -1:
                print ("deviceID " + apclaimsIDs[k] + " is provisioned")


if __name__ == "__main__":
    main()
