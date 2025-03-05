from fhirpathpy import evaluate

patient = {
  "resourceType": "Patient",
  "id": "example",
  "name": [
    {
      "use": "official",
      "given": [
        "Peter",
        "James"
      ],
      "family": "Chalmers"
    },
    {
      "use": "usual",
      "given": [
        "Jim"
      ]
    },
    {
      "use": "maiden",
      "given": [
        "Peter",
        "James"
      ],
      "family": "Windsor",
      "period": {
        "end": "2002"
      }
    }
  ]
}

# Evaluating FHIRPath
result = evaluate(patient, "Patient.name.where(use='usual').given.first()", [])
print(result)