# Lesson 7: Exploring FHIRPath in Practice

**Author**: Patrick W. Jamieson, M.D.  
**Contributors**: Russ Leftwich, M.D.  
**Organization**: InterSystems – Creative Data Technology

---

## 🔍 Overview

This lesson introduces **FHIRPath**, a powerful, domain-specific expression language designed for navigating, filtering, and transforming FHIR data. You will gain hands-on experience constructing and evaluating FHIRPath expressions, understanding common usage patterns, and applying FHIRPath to real-world interoperability use cases.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand the purpose and core features of FHIRPath.
- Write FHIRPath expressions for data extraction and validation.
- Navigate FHIR resource structures using path traversal syntax.
- Apply FHIRPath to support clinical rules and invariants.
- Identify and correct common errors in FHIRPath usage.

---

## 🛠️ Contents

This repository includes:

- `FHIRPath.pptx` – Companion slide deck with theoretical and practical background.
- `Fhirpath1.ipynb` – Primary Jupyter notebook for interactive FHIRPath examples.
- `FHIRPath2.ipynb` – Supplemental notebook for deeper experimentation.
- `basepath.py` – Support module for shared functions and FHIR resource loading.
- `FHIRPath.jpg` – Cover image for presentations or documentation branding.

---

## 📦 Getting Started

### 🔗 Clone the Repository

```bash
git clone https://github.com/pjamiesointersystems/fhirlesson7.git
cd fhirlesson7


Prerequisites
Python 3.8+

JupyterLab or Jupyter Notebook

fhir.resources Python package

Install the required package:

pip install fhir.resources

How to Use
Open Fhirpath1.ipynb in Jupyter.

Clear all outputs to start fresh: Click Kernel → Restart & Clear Output.

Run cells step-by-step to explore:

Simple expressions like Patient.name.given

Logical expressions such as Patient.birthDate.exists()

Filtering via Patient.gender = 'female'

Deep navigation like MedicationRequest.dosageInstruction.doseQuantity

Optionally explore FHIRPath2.ipynb for extended examples.

💡 Key Concepts Covered
Graph-traversal and fluent syntax

Collection-centric logic: everything is a list

Use of exists(), where(), first(), count(), and comparison operators

Evaluation of requirement constraints/invariants using logical expressions

Common pitfalls: null handling, type mismatches, multi-value comparisons


Example Use Cases
Expression	Purpose
Patient.name.given	Extract a patient's given name
Patient.birthDate.exists()	Ensure a birthDate is present
Patient.gender = 'female'	Filter female patient records
MedicationRequest.dosageInstruction.doseQuantity	Retrieve medication dosage info
Observation.component.valueQuantity.value > 70	Validate numeric observations

🚫 Common Mistakes
Comparing collections directly to scalars

Forgetting .first() or .where(...) when filtering

Confusing optional fields (null) with empty collections

Incorrect use of choice-type fields like deceased[x]

📚 Reference Links
🔗 FHIRPath Specification

📘 FHIR Documentation

🛠 FHIR Validator

🧠 Attribution
This educational resource is part of an ongoing curriculum by InterSystems to teach modern FHIR-based data science and application development using open tools.