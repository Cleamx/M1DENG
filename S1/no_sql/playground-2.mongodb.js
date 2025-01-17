db.croisieres.aggregate([
    {
        $match: {
            DEPPORT: "BASTIA"
        }
    },
    {
        $lookup: {
            from: "skippers",
            localField: "SKNUM",
            foreignField: "SKNUM",
            as: "skippers_detail"
        }
    },
    {
        $unwind: "$skippers_detail"
    },
    {
        $group: {
            _id: "$skippers_detail.SKNOM",
            nbr: { $sum: 1 }
        }
    },
    {
        $project: {
            _id: 0,
            SKNOM: "$_id",
            nbr: 1
        }
    }
]);

db.croisieres.aggregate([
    {
        $lookup: {
            from: "skippers",
            localField: "SKNUM",
            foreignField: "SKNUM",
            as: "skippers_detail"
        }
    },
    {
        $unwind: "$skippers_detail"
    },
    {
        $group: {
            _id: "$skippers_detail.SKNOM",
            ports_arrivee: { $addToSet: "$ARRPORT" }
        }
    },
    {
        $project: {
            _id: 0,
            SKNOM: "$_id",
            ports_arrivee: 1
        }
    }
]);

db.croisieres.aggregate([
    {
        $lookup: {
            from: "skippers",
            localField: "SKNUM",
            foreignField: "SKNUM",
            as: "skippers_detail"
        }
    },
    {
        $unwind: "$skippers_detail"
    },
    {
        $group: {
            _id: "$skippers_detail.SKNOM",
            total_jours_en_mer: {
                $sum: {
                    $dateDiff: {
                        startDate: "$DEPDATE",
                        endDate: "$ARRDATE",
                        unit: "day"
                    }
                }
            }
        }
    },
    {
        $project: {
            _id: 0,
            SKNOM: "$_id",
            total_jours_en_mer: 1
        }
    }
]);

db.skippers.aggregate([
    {
        $lookup: {
            from: "croisieres",
            localField: "SKNUM",
            foreignField: "SKNUM",
            as: "croisieres_detail"
        }
    },
    {
        $match: {
            "croisieres_detail": { $eq: [] }
        }
    },
    {
        $project: {
            _id: 0,
            SKNOM: 1
        }
    }
]);

db.croisieres.aggregate([
    {
        $lookup: {
          from: "skippers",
          localField: "SKNUM",
          foreignField: "SKNUM",
          as: "skippers_detail"
        }
    },
    {
        $unwind: "$skippers_detail"
    },
    {
        $match: {
            BATNUM: "B002"
        }
    },
    {
        $project: {
            _id: 0,
          "skippers_detail.SKNOM": 1,
          BATNUM: 1
        }
    }
]);

db.croisieres.aggregate([
    {
        $match: {
            DEPPORT: "AJACCIO"
        }
    },
    {
        $project: {
            _id: 0,
            CROISNUM: 1
        }
    }
]);

db.croisieres.aggregate([
    {
        $lookup: {
            from: "bateaux",
            localField: "BATNUM",
            foreignField: "BATNUM",
            as: "bateaux_detail"
        }
    },
    {
        $unwind: "$bateaux_detail"
    },
    {
        $match: {
            SKNUM: "1"
        }
    },
    {
        $project: {
            _id: 0,
            "bateaux_detail.BATNOM": 1
        }
    }
]);

db.croisieres.find({}, {BATNUM: 1})