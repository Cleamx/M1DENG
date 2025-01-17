db.Skippers.aggregate([
    {
        $match: {
            CROISIERES: { $eq: [] }
        }
    },
    {
        $project: {
            _id: 0,
            SKNOM: 1
        }
    }
]);

db.Skippers.aggregate([
    {
        $match: {
            "CROISIERES.BATNUM": "B002"
        }
    },
    {
        $project: {
            _id: 0,
            SKNOM: 1
        }
    }
]);

db.Skippers.aggregate([
    {
        $unwind: "$CROISIERES"
    },
    {
        $match: {
            "CROISIERES.DEPPORT": "AJACCIO"
        }
    },
    {
        $project: {
            _id: 0,
            "CROISIERES.CROISNUM": 1
        }
    }
]);

db.Skippers.aggregate([
    {
        $match: {
            SKNUM: "1"
        }
    },
    {
        $unwind: "$CROISIERES"
    },
    {
        $project: {
            _id: 0,
            "CROISIERES.BATNOM": 1
        }
    }
]);

db.Skippers.aggregate([
    {
        $unwind: "$CROISIERES"
    },
    {
        $group: {
            _id: null,
            batnums: { $addToSet: "$CROISIERES.BATNUM" }
        }
    },
    {
        $project: {
            _id: 0,
            BATNUM: "$batnums"
        }
    }
]);
