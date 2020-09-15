from firebase import firebase

fire=firebase.FirebaseApplication("https://covidcases-eaad8.firebaseio.com/",None)

data={
    'name':'radhesh',
    'rollno':28
}
result=fire.post('/covidcases-eaad8/studentinfo',data)
print(result)