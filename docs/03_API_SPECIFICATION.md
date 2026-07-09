# HostelHub API Specification

## Base URL

/api/v1

## Authentication

JWT Bearer Token

RESIDENT APIS

GET    /residents
GET    /residents/{resident_id}
POST   /residents
PUT    /residents/{resident_id}
DELETE /residents/{resident_id}

Guardian APIs

GET    /guardians
POST   /guardians
PUT    /guardians/{guardian_id}
DELETE /guardians/{guardian_id}

Document APIs

POST   /documents/upload
GET    /documents/{document_id}
DELETE /documents/{document_id}


Hostel APIs

GET /hostels
POST /hostels

Room APIs

GET /rooms
POST /rooms
PUT /rooms/{room_id}

Bed APIs

GET /beds
POST /beds
PUT /beds/{bed_id}
