db=connect("bdBateaux");
var skipper1={  
    sknum:'5',
    sknom:'JEAN',
    skport:'AJACCIO',
    salaire:3000};
var skipper2={
    sknum:'6',
    sknom:'PAUL',
    skport:'AJACCIO',
    salaire:2000};
var skipper3={
    sknum:'7',
    sknom:'PIERRE',
    skport:'ANTIBES'};
var skipper4={
    sknum:'8',
    sknom:'MARIE',
    salaire:1500};
db.skippers.insertOne(skipper1);
db.skippers.insertOne(skipper2);
db.skippers.insertOne(skipper3);
db.skippers.insertOne(skipper4);

db.skippers.find();
db.skippers.find({skport:"AJACCIO"}, {sknom:1, sknum:1})

db.skippers.find(
    {$and: 
        [ {salaire: {$lt: 2500}}
        , {skport: "AJACCIO"} ]
        });

db.skippers.find(
    {salaire: {$exists: false}});

db.skippers.updateOne(
    {sknom: "JEAN"},
    {
        $set: {salaire: 4000},
        $unset: {skport: ""}
    }
);

db.skippers.updateOne(
    {salaire: {$exists: false}},
    {$set: {salaire: 2000}}
)

db.skippers.updateMany({},
    { $inc: { salaire: 500 } }
);



