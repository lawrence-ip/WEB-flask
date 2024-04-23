use('employeraccDB');


db.getCollection('employers').insertMany([
    {'acc_key':'0000001', 'name':'John Doe', 'email':'www.example@example.com'},
]);

const 