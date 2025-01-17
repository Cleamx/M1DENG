from faker import Faker
import pymongo
from datetime import datetime, timedelta
import random
from bson import ObjectId

# Configuration
fake = Faker('fr_FR')
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ent_database"]

def generate_students(num_students=100):
    students = []
    specialties = ["Informatique", "Mathématiques", "Physique", "Chimie", "Biologie"]
    promotions = ["2024", "2025", "2026"]
    
    for _ in range(num_students):
        student = {
            "_id": ObjectId(),
            "studentId": f"ST{fake.unique.random_number(digits=6)}",
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "email": fake.email(),
            "promotion": random.choice(promotions),
            "specialty": random.choice(specialties),
            "createdAt": fake.date_time_this_year()
        }
        students.append(student)
    
    db.students.insert_many(students)
    return [s["studentId"] for s in students]

def generate_courses(num_courses=20):
    courses = []
    professors = [fake.name() for _ in range(10)]
    course_titles = [
        "Introduction à la programmation",
        "Algèbre linéaire",
        "Physique quantique",
        "Chimie organique",
        "Biologie cellulaire",
        "Analyse numérique",
        "Statistiques",
        "Intelligence artificielle",
        "Réseaux",
        "Base de données"
    ]
    
    for i in range(num_courses):
        resources = []
        for _ in range(random.randint(5, 15)):
            resource_type = random.choice(["document", "video", "quiz", "interactive"])
            resource = {
                "resourceId": f"RES{fake.unique.random_number(digits=6)}",
                "type": resource_type,
                "title": f"{course_titles[i % len(course_titles)]} - {resource_type.capitalize()}",
                "uploadDate": fake.date_time_this_year(),
                "description": fake.text(max_nb_chars=200)
            }
            resources.append(resource)
        
        course = {
            "_id": ObjectId(),
            "courseId": f"CRS{fake.unique.random_number(digits=6)}",
            "title": course_titles[i % len(course_titles)],
            "professor": random.choice(professors),
            "semester": random.choice(["S1", "S2"]),
            "credits": random.randint(1, 30),
            "resources": resources
        }
        courses.append(course)
    
    db.courses.insert_many(courses)
    return [(c["courseId"], c["resources"]) for c in courses]

def generate_interactions(student_ids, course_resources, num_days=30):
    interactions = []
    start_date = datetime.now() - timedelta(days=num_days)
    
    for student_id in student_ids:
        for day in range(num_days):
            current_date = start_date + timedelta(days=day)
            num_interactions = random.randint(3, 10)
            
            for _ in range(num_interactions):
                course_id, resources = random.choice(course_resources)
                resource = random.choice(resources)
                interaction_type = random.choice([
                    "download", "view", "quiz_submission", 
                    "forum_post", "resource_access"
                ])
                
                completion_rate = random.randint(0, 100)
                status = "completed" if completion_rate == 100 else random.choice([
                    "started", "interrupted", "failed"
                ])
                
                interaction = {
                    "_id": ObjectId(),
                    "studentId": student_id,
                    "courseId": course_id,
                    "type": interaction_type,
                    "resourceId": resource["resourceId"],
                    "timestamp": fake.date_time_between(
                        start_date=current_date,
                        end_date=current_date + timedelta(hours=8)
                    ),
                    "duration": random.randint(300, 7200),  # 5min to 2h
                    "status": status,
                    "completionRate": completion_rate,
                    "metadata": {
                        "difficulty": random.choice(["easy", "medium", "hard"]),
                        "feedback": fake.text(max_nb_chars=100),
                        "attempts": random.randint(1, 5)
                    }
                }
                
                if interaction_type == "quiz_submission":
                    interaction["metadata"]["quizScore"] = random.randint(0, 100)
                elif interaction_type == "forum_post":
                    interaction["metadata"]["forumPostId"] = str(ObjectId())
                
                interactions.append(interaction)
    
    db.interactions.insert_many(interactions)

def generate_sessions(student_ids, course_ids, num_days=30):
    sessions = []
    start_date = datetime.now() - timedelta(days=num_days)
    
    for student_id in student_ids:
        for day in range(num_days):
            current_date = start_date + timedelta(days=day)
            num_sessions = random.randint(1, 4)
            
            for _ in range(num_sessions):
                session_start = fake.date_time_between(
                    start_date=current_date,
                    end_date=current_date + timedelta(hours=12)
                )
                duration = random.randint(1800, 14400)  # 30min to 4h
                session_end = session_start + timedelta(seconds=duration)
                
                activities = []
                remaining_time = duration
                
                while remaining_time > 300:  # S'assurer qu'il reste au moins 5 minutes
                    # Calculer la durée maximale possible pour cette activité
                    max_duration = min(3600, remaining_time - 300)  # Garder au moins 5 minutes pour les activités suivantes
                    min_duration = min(300, max_duration)  # Prendre le minimum entre 300 et max_duration
                    
                    if max_duration <= min_duration:
                        activity_duration = remaining_time  # Utiliser le temps restant
                    else:
                        activity_duration = random.randint(min_duration, max_duration)
                    
                    activity = {
                        "type": random.choice([
                            "course_view", "resource_access", 
                            "assignment_work", "quiz_attempt"
                        ]),
                        "courseId": random.choice(course_ids),
                        "timestamp": session_start + timedelta(seconds=duration - remaining_time),
                        "duration": activity_duration,
                        "status": random.choice([
                            "in_progress", "completed", "paused"
                        ]),
                        "progress": random.randint(0, 100)
                    }
                    activities.append(activity)
                    remaining_time -= activity_duration
                
                session = {
                    "_id": ObjectId(),
                    "studentId": student_id,
                    "startTime": session_start,
                    "endTime": session_end,
                    "duration": duration,
                    "sessionType": random.choice([
                        "course", "td", "tp", "exam", "personal_work"
                    ]),
                    "deviceInfo": {
                        "browser": random.choice([
                            "Chrome", "Firefox", "Safari", "Edge"
                        ]),
                        "os": random.choice([
                            "Windows", "MacOS", "Linux", "iOS", "Android"
                        ]),
                        "device": random.choice([
                            "Desktop", "Laptop", "Tablet", "Mobile"
                        ])
                    },
                    "activities": activities
                }
                sessions.append(session)
    
    db.sessions.insert_many(sessions)
    
    

def generate_assignments(course_ids, student_ids, num_assignments=50):
    assignments = []
    
    for _ in range(num_assignments):
        # Utiliser future_datetime au lieu de future_date
        due_date = fake.date_time_between(start_date='+1d', end_date='+30d')
        submissions = []
        num_submissions = random.randint(len(student_ids)//2, len(student_ids))
        
        for student_id in random.sample(student_ids, num_submissions):
            submission_date = fake.date_time_between(
                start_date='-30d',
                end_date=due_date
            )
            
            revision_history = []
            version = random.randint(1, 3)
            for v in range(version):
                revision = {
                    "version": v + 1,
                    "date": fake.date_time_between(
                        start_date='-30d',
                        end_date=submission_date
                    ),
                    "changes": fake.text(max_nb_chars=100)
                }
                revision_history.append(revision)
            
            submission = {
                "studentId": student_id,
                "submissionDate": submission_date,
                "version": version,
                "status": random.choice([
                    "draft", "submitted", "graded", "returned"
                ]),
                "grade": random.randint(0, 20),
                "teacherComments": fake.text(max_nb_chars=200),
                "revisionHistory": revision_history
            }
            submissions.append(submission)
        
        assignment = {
            "_id": ObjectId(),
            "courseId": random.choice(course_ids),
            "title": f"Devoir {fake.word()} - {fake.word()}",
            "dueDate": due_date,
            "description": fake.text(max_nb_chars=500),
            "maxGrade": 20,
            "submissions": submissions
        }
        assignments.append(assignment)
    
    db.assignments.insert_many(assignments)
    
    
def generate_calendar_events(student_ids, course_ids, num_events=200):
    events = []
    
    for _ in range(num_events):
        student_id = random.choice(student_ids)
        event_type = random.choice(["course", "personal", "group_work"])
        start_date = fake.date_time_between(start_date="-30d", end_date="+60d")
        
        event = {
            "_id": ObjectId(),
            "studentId": student_id,
            "title": fake.sentence(nb_words=4),
            "type": event_type,
            "startDate": start_date,
            "endDate": start_date + timedelta(hours=random.randint(1, 4)),
            "location": fake.building_number() + " " + fake.street_name(),
            "participants": random.sample(student_ids, random.randint(1, 5)) if event_type == "group_work" else [],
            "courseId": random.choice(course_ids) if event_type != "personal" else None,
            "metadata": {
                "recurring": random.choice([True, False]),
                "recurrencePattern": random.choice(["daily", "weekly", "monthly"]) if random.choice([True, False]) else None,
                "reminder": random.choice([True, False])
            }
        }
        events.append(event)
    
    db.calendar_events.insert_many(events)

def generate_workgroups(course_ids, student_ids, num_groups=30):
    workgroups = []
    
    for _ in range(num_groups):
        course_id = random.choice(course_ids)
        members = random.sample(student_ids, random.randint(3, 6))
        
        meetings = []
        num_meetings = random.randint(2, 8)
        meeting_date = datetime.now() - timedelta(days=30)
        
        for _ in range(num_meetings):
            meeting_date += timedelta(days=random.randint(3, 7))
            meeting = {
                "date": meeting_date,
                "duration": random.randint(30, 180),  # 30min to 3h
                "attendees": random.sample(members, random.randint(max(1, len(members)-1), len(members))),
                "summary": fake.text(max_nb_chars=200)
            }
            meetings.append(meeting)
        
        workgroup = {
            "_id": ObjectId(),
            "courseId": course_id,
            "name": f"Groupe {fake.word().capitalize()}",
            "members": members,
            "createdAt": fake.date_time_this_month(),
            "meetings": meetings
        }
        workgroups.append(workgroup)
    
    db.workgroups.insert_many(workgroups)

def generate_messages(student_ids, course_ids, num_messages=300):
    messages = []
    teacher_ids = [f"PROF{i:03d}" for i in range(10)]  # Création d'IDs de professeurs
    
    for _ in range(num_messages):
        message_type = random.choice(["student_teacher", "student_student"])
        
        if message_type == "student_teacher":
            sender_id = random.choice(student_ids)
            receiver_id = random.choice(teacher_ids)
        else:
            sender_id = random.choice(student_ids)
            receiver_id = random.choice([s for s in student_ids if s != sender_id])
        
        has_attachment = random.choice([True, False])
        attachments = []
        if has_attachment:
            num_attachments = random.randint(1, 3)
            for _ in range(num_attachments):
                attachment = {
                    "type": random.choice(["pdf", "doc", "image", "zip"]),
                    "url": f"https://storage.ent.edu/files/{fake.uuid4()}",
                    "name": fake.file_name()
                }
                attachments.append(attachment)
        
        message = {
            "_id": ObjectId(),
            "senderId": sender_id,
            "receiverId": receiver_id,
            "type": message_type,
            "content": fake.text(max_nb_chars=500),
            "timestamp": fake.date_time_this_month(),
            "courseId": random.choice(course_ids) if random.choice([True, False]) else None,
            "status": random.choice(["sent", "delivered", "read"]),
            "attachments": attachments
        }
        messages.append(message)
    
    db.messages.insert_many(messages)

def generate_learning_progress(student_ids, course_ids):
    progress_records = []
    
    for student_id in student_ids:
        for course_id in course_ids:
            modules = [f"MODULE{i:03d}" for i in range(random.randint(3, 8))]
            
            for module_id in modules:
                completed_items = []
                num_items = random.randint(5, 15)
                num_completed = random.randint(0, num_items)
                for i in range(num_completed):
                    completed_items.append(f"ITEM{i:03d}")
                
                achievements = []
                if random.choice([True, False]):
                    num_achievements = random.randint(1, 3)
                    for _ in range(num_achievements):
                        achievement = {
                            "type": random.choice(["completion", "excellence", "participation"]),
                            "earnedAt": fake.date_time_this_month(),
                            "description": fake.sentence()
                        }
                        achievements.append(achievement)
                
                progress = {
                    "_id": ObjectId(),
                    "studentId": student_id,
                    "courseId": course_id,
                    "moduleId": module_id,
                    "progress": (len(completed_items) / num_items) * 100,
                    "completedItems": completed_items,
                    "lastAccess": fake.date_time_this_month(),
                    "achievements": achievements
                }
                progress_records.append(progress)
    
    db.learning_progress.insert_many(progress_records)

def generate_tutoring_sessions(student_ids, course_ids, num_sessions=100):
    sessions = []
    tutor_ids = [f"TUT{i:03d}" for i in range(5)]  # Création d'IDs de tuteurs
    
    for _ in range(num_sessions):
        is_group = random.choice([True, False])
        students = random.sample(student_ids, random.randint(1, 5) if is_group else 1)
        
        start_time = fake.date_time_between(start_date="-30d", end_date="+30d")
        duration = random.randint(30, 120)  # 30min to 2h
        
        has_resources = random.choice([True, False])
        resources = []
        if has_resources:
            num_resources = random.randint(1, 4)
            for _ in range(num_resources):
                resource = {
                    "type": random.choice(["document", "exercise", "video", "link"]),
                    "url": f"https://storage.ent.edu/tutoring/{fake.uuid4()}",
                    "sharedAt": start_time - timedelta(days=random.randint(1, 5))
                }
                resources.append(resource)
        
        session = {
            "_id": ObjectId(),
            "tutorId": random.choice(tutor_ids),
            "students": students,
            "courseId": random.choice(course_ids),
            "startTime": start_time,
            "endTime": start_time + timedelta(minutes=duration),
            "type": "group" if is_group else "individual",
            "status": random.choice(["scheduled", "completed", "cancelled"]),
            "notes": fake.text(max_nb_chars=300) if random.choice([True, False]) else "",
            "resources": resources
        }
        sessions.append(session)
    
    db.tutoring_sessions.insert_many(sessions)

def main():
    # Nettoyage des collections existantes
    for collection in db.list_collection_names():
        db[collection].drop()
    
    print("Génération des étudiants...")
    student_ids = generate_students(100)
    
    print("Génération des cours...")
    course_data = generate_courses(20)
    course_ids = [cd[0] for cd in course_data]
    
    print("Génération des interactions...")
    generate_interactions(student_ids, course_data)
    
    print("Génération des sessions...")
    generate_sessions(student_ids, course_ids)
    
    print("Génération des devoirs...")
    generate_assignments(course_ids, student_ids)
    
    print("Génération des événements du calendrier...")
    generate_calendar_events(student_ids, course_ids)
    
    print("Génération des groupes de travail...")
    generate_workgroups(course_ids, student_ids)
    
    print("Génération des messages...")
    generate_messages(student_ids, course_ids)
    
    print("Génération des progrès d'apprentissage...")
    generate_learning_progress(student_ids, course_ids)
    
    print("Génération des sessions de tutorat...")
    generate_tutoring_sessions(student_ids, course_ids)
    
    print("Génération terminée!")

if __name__ == "__main__":
    main()