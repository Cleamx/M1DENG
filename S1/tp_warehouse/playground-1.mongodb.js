/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

const database = 'ent_database';

// Create a new database.
use(database);

// Create a new collection.
db.createCollection('students', 
    {
    validator: {
      $jsonSchema: {
        bsonType: "object",
        required: ["studentId", "firstName", "lastName", "email", "promotion", "specialty"],
        properties: {
          _id: { bsonType: "objectId" },
          studentId: { bsonType: "string" },
          firstName: { bsonType: "string" },
          lastName: { bsonType: "string" },
          email: { bsonType: "string" },
          promotion: { bsonType: "string" },
          specialty: { bsonType: "string" },
          createdAt: { bsonType: "date" }
    }
        }
    }
});


db.createCollection('courses', {
validator: {
    $jsonSchema: {
    bsonType: "object",
    required: ["courseId", "title", "professor", "semester"],
    properties: {
        _id: { bsonType: "objectId" },
        courseId: { bsonType: "string" },
        title: { bsonType: "string" },
        professor: { bsonType: "string" },
        semester: { 
            bsonType: "string",
            enum: ["S1", "S2"]
        },
        credits: { 
            bsonType: "number",
            minimum: 1,
            maximum: 30
        },
        resources: {
        bsonType: "array",
        items: {
            bsonType: "object",
            required: ["resourceId", "type", "title"],
            properties: {
            resourceId: { bsonType: "string" },
            type: { 
                bsonType: "string",
                enum: ["document", "video", "quiz", "interactive"] 
            },
            title: { bsonType: "string" },
            uploadDate: { bsonType: "date" },
            description: { bsonType: "string" }  
            }
        }
        }
    }
    }
}
});


db.createCollection('interactions', {
    validator: {
      $jsonSchema: {
        bsonType: "object",
        required: ["studentId", "courseId", "type", "timestamp"],
        properties: {
          _id: { bsonType: "objectId" },
          studentId: { bsonType: "string" },
          courseId: { bsonType: "string" },
          type: { 
            bsonType: "string",
            enum: ["download", "view", "quiz_submission", "forum_post", "resource_access"]
          },
          resourceId: { bsonType: "string" },
          timestamp: { bsonType: "date" },
          duration: { bsonType: "number" },
          status: {  
            bsonType: "string",
            enum: ["started", "completed", "interrupted", "failed"]
          },
          completionRate: { 
            bsonType: "number",
            minimum: 0,
            maximum: 100
          },
          metadata: {
            bsonType: "object",
            properties: {
              quizScore: { bsonType: "number" },
              documentId: { bsonType: "string" },
              forumPostId: { bsonType: "string" },
              difficulty: { 
                bsonType: "string",
                enum: ["easy", "medium", "hard"]
            },
              feedback: { bsonType: "string" },   
              attempts: { bsonType: "number" }     
            }
          }
        }
      }
    }
  });
  
db.createCollection('sessions', {
validator: {
    $jsonSchema: {
    bsonType: "object",
    required: ["studentId", "startTime", "endTime"],
    properties: {
        _id: { bsonType: "objectId" },
        studentId: { bsonType: "string" },
        startTime: { bsonType: "date" },
        endTime: { bsonType: "date" },
        duration: { bsonType: "number" },
        sessionType: { 
        bsonType: "string",
        enum: ["course", "td", "tp", "exam", "personal_work"]
        },
        deviceInfo: {
            bsonType: "object",
            required: ["browser", "os", "device"],
            properties: {
                browser: { bsonType: "string" },
                os: { bsonType: "string" },
                device: { bsonType: "string" }
            }
        },
        activities: {
        bsonType: "array",
        items: {
            bsonType: "object",
            properties: {
            type: { bsonType: "string" },
            courseId: { bsonType: "string" },
            timestamp: { bsonType: "date" },
            duration: { bsonType: "number" },
            status: {  
                bsonType: "string",
                enum: ["in_progress", "completed", "paused"]
            },
            progress: { 
                bsonType: "number",
                minimum: 0,
                maximum: 100
            }
            }
        }
        }
    }
    }
}
});
  

    
db.createCollection('assignments', {
validator: {
    $jsonSchema: {
    bsonType: "object",
    required: ["courseId", "title", "dueDate"],
    properties: {
        _id: { bsonType: "objectId" },
        courseId: { bsonType: "string" },
        title: { bsonType: "string" },
        dueDate: { bsonType: "date" },
        description: { bsonType: "string" },  
        maxGrade: { 
            bsonType: "number",
            minimum: 0,
            maximum: 20
        },        
        submissions: {
        bsonType: "array",
        items: {
            bsonType: "object",
            properties: {
            studentId: { bsonType: "string" },
            submissionDate: { bsonType: "date" },
            version: { bsonType: "number" },
            status: { 
                bsonType: "string",
                enum: ["draft", "submitted", "graded", "returned"]
            },
            grade: { 
                bsonType: "number",
                minimum: 0,
                maximum: 20
            },
            teacherComments: { bsonType: "string" },  
            revisionHistory: {  
                bsonType: "array",
                items: {
                bsonType: "object",
                properties: {
                    version: { bsonType: "number" },
                    date: { bsonType: "date" },
                    changes: { bsonType: "string" }
                }
                }
            }
            }
        }
        }
    }
    }
}
});

// Collection pour calendar_events
db.createCollection('calendar_events', {
validator: {
    $jsonSchema: {
    bsonType: "object",
    required: ["studentId", "title", "type", "startDate", "endDate"],
    properties: {
        _id: { bsonType: "objectId" },
        studentId: { bsonType: "string" },
        title: { bsonType: "string" },
        type: { 
        bsonType: "string",
        enum: ["course", "personal", "group_work"]
        },
        startDate: { bsonType: "date" },
        endDate: { bsonType: "date" },
        location: { bsonType: "string" },
        participants: {
        bsonType: "array",
        items: { bsonType: "string" }
        },
        courseId: { bsonType: "string" },
        metadata: {
        bsonType: "object",
        properties: {
            recurring: { bsonType: "bool" },
            recurrencePattern: { bsonType: "string" },
            reminder: { bsonType: "bool" }
        }
        }
    }
    }
}
});

// Collection pour workgroups
db.createCollection('workgroups', {
validator: {
    $jsonSchema: {
    bsonType: "object",
    required: ["courseId", "name", "members", "createdAt"],
    properties: {
        _id: { bsonType: "objectId" },
        courseId: { bsonType: "string" },
        name: { bsonType: "string" },
        members: {
        bsonType: "array",
        items: { bsonType: "string" }
        },
        createdAt: { bsonType: "date" },
        meetings: {
        bsonType: "array",
        items: {
            bsonType: "object",
            properties: {
            date: { bsonType: "date" },
            duration: { bsonType: "number" },
            attendees: {
                bsonType: "array",
                items: { bsonType: "string" }
            },
            summary: { bsonType: "string" }
            }
        }
        }
    }
    }
}
});

// Collection pour messages
db.createCollection('messages', {
validator: {
    $jsonSchema: {
    bsonType: "object",
    required: ["senderId", "receiverId", "type", "content", "timestamp", "status"],
    properties: {
        _id: { bsonType: "objectId" },
        senderId: { bsonType: "string" },
        receiverId: { bsonType: "string" },
        type: {
        bsonType: "string",
        enum: ["student_teacher", "student_student"]
        },
        content: { bsonType: "string" },
        timestamp: { bsonType: "date" },
        courseId: { bsonType: "string" },
        status: {
        bsonType: "string",
        enum: ["sent", "delivered", "read"]
        },
        attachments: {
        bsonType: "array",
        items: {
            bsonType: "object",
            properties: {
            type: { bsonType: "string" },
            url: { bsonType: "string" },
            name: { bsonType: "string" }
            }
        }
        }
    }
    }
}
});

// Collection pour learning_progress
db.createCollection('learning_progress', {
validator: {
    $jsonSchema: {
    bsonType: "object",
    required: ["studentId", "courseId", "moduleId", "progress", "lastAccess"],
    properties: {
        _id: { bsonType: "objectId" },
        studentId: { bsonType: "string" },
        courseId: { bsonType: "string" },
        moduleId: { bsonType: "string" },
        progress: {
        bsonType: "number",
        minimum: 0,
        maximum: 100
        },
        completedItems: {
        bsonType: "array",
        items: { bsonType: "string" }
        },
        lastAccess: { bsonType: "date" },
        achievements: {
        bsonType: "array",
        items: {
            bsonType: "object",
            properties: {
            type: { bsonType: "string" },
            earnedAt: { bsonType: "date" },
            description: { bsonType: "string" }
            }
        }
        }
    }
    }
}
});

// Collection pour tutoring_sessions
db.createCollection('tutoring_sessions', 
{
validator: {
    $jsonSchema: {
    bsonType: "object",
    required: ["tutorId", "students", "courseId", "startTime", "endTime", "type", "status"],
    properties: {
        _id: { bsonType: "objectId" },
        tutorId: { bsonType: "string" },
        students: {
        bsonType: "array",
        items: { bsonType: "string" }
        },
        courseId: { bsonType: "string" },
        startTime: { bsonType: "date" },
        endTime: { bsonType: "date" },
        type: {
        bsonType: "string",
        enum: ["individual", "group"]
        },
        status: {
        bsonType: "string",
        enum: ["scheduled", "completed", "cancelled"]
        },
        notes: { bsonType: "string" },
        resources: {
        bsonType: "array",
        items: {
            bsonType: "object",
            properties: {
            type: { bsonType: "string" },
            url: { bsonType: "string" },
            sharedAt: { bsonType: "date" }
            }
        }
        }
    }
    }
}
});



