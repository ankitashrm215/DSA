#function to encode list into string
def encode(strs: list[str]) -> str:
    encodedString = ""

    #for each item in list, add length of item with # at starting
    for s in strs:
        encodedString =  encodedString + str(len(s)) + "#" + s
    return encodedString

#function to decode string into list
def decode(encodedString: str) -> list:
    decodedList = []
    l = len(encodedString)
    i = 0
    while i < l:
        j = i + 1

        #find "#"
        while(j < l and encodedString[j] != "#"):
            j = j + 1
            
        #find length of encoded string form i until "#"
        length = int(encodedString[i:j])   
        i = j + 1        
        decodedString = ""

        #fetch original string starting with the length captured above
        while length > 0:
            decodedString = decodedString + encodedString[i]
            i = i + 1
            length = length - 1
        decodedList.append(decodedString)            
    return decodedList

print("Original list : ", ["neet","code","love","you"])
encodedString = encode(["neet","code","love","you"])
print("Encoded String : ", encodedString)
print("Decoded list : ", decode(encodedString))
