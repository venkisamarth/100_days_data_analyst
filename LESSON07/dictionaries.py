# Dictionaries
band={
    "vocals":"plant",
    "guitar":"page"
    }
band2=dict(vocals='plant',guitar='Page')
print(band)
print(band2)

print(type(band))
print(type(band2))
print(len(band))
print(len(band2))

# Acces items in dictionares

print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all the keys from dictinaries

print(band.values())

# list of key/ value pairs as tuples

print(band.items())

# verify a key exists 

print("guitar" in band)
print("traingle " in band)

# change values in dictioares 
band["vocales "]="coverdale"

band.update({"bass":"jpj"})

# Remove items

print(band.pop("bass"))
print(band)

band ['drums']="Bonham"
print(band)

print(band.popitem())

print(band.popitem())
print(band)

# delete and clear 

band['drums']="Bonham"



print(band)

band2.clear()

print(band2)


# copy dictionaries 
band2=band # creates a refrence 
print("Bad copy!")
print(band2)
print(band)
band2["drums"]="Dave"
print(band)

band2 =band.copy()
band2["drums"]="Dave"
print(band)

print(band)
print(band2)

print("Good copy!")
# or use the dict() constructor fucntion

band3 =dict(band)
print(dict)

# nested dictionary
member1={
    "name":"plant",
    "instrumet":"guitar"

}
member2={
    "name":"page",
    "instrument":"guitar"

}

band={"member1":member1,
     "member2":member2
     }
print(band)

print(band["member1"]["name"])
# sets 

nums ={1,2,3,3,4,4}
print(nums)

nums2=set((1,2,2,3,4))
print(nums)

print(type(nums))
print(len(nums))

# No Duplicates Allowed 

nums={1,2,3,4,5}
print(nums)

# True is a dupe of 1 , flase is a duoe of a Zero 

nums={1,True,2,False,3,4,0}
print(nums)

# check if a value  is in set 
print(2 in nums )

# but you cannot refer to an elelemnt in the  set 
# with and in the   an index  position or a kye 

nums.add(8)
print(nums)

morenums={5,6,7}

nums.update(morenums)
print(nums)
# you can use with lists ,tuples and dictioaries too . 



# Merge to sets to creatte a new sets 

one ={1,2,3}
two ={5,6,7}

my_newset=one.union(two)
print(my_newset)

# merger tow sets to create a new set 
one ={1,2,3,4}
two ={5,6,7}

# merger keep onwly the duplicates
one.intersection_update(two)
print(one)

# one ={1,2,3,4}
one={1,2,3,4
}

two ={2,3,4,4}
print(one.intersection(two))

print(one.symmetric_difference_update(two))


