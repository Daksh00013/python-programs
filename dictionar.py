student={
    "name":"rahul kumar",
    "subject":{
        "physics":78,
        "chem":78,
        "maths":67
    }
}
print(student.items())# give the (key, value ) tuples
print(student.keys())# give the keys of the dictionary
student.update({"name":"daksh"})# can be update beacouse dictionary is mutuable
print(student.get("physics"))# give the value of the specific key  
print(len(list(student.keys())))
print(list(student.values()))
print(student)
print(student["subject"]["physics"])