# Define job data with job titles and their required skills
jobs = {
    "Software Engineer": ["Python", "Django", "SQL","Databases"],
    "Data Scientist": ["Python", "Machine Learning", "Statistics"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React"],
    "Cloud Engineer": ["AWS", "Terraform", "Linux", "Azure"]
}

def recommend_jobs(user_skills, job_data):
    recommendations = []
    lacking_skills = {}

    for job, required_skills in job_data.items():
        # Convert lists to sets for easier comparison
        skill_set = set(user_skills)
        required_set = set(required_skills)
        
        # Calculate match percentage
        match_percentage = len(skill_set & required_set) / len(required_set) * 100

        # If match percentage is above a threshold, consider it a recommendation
        if match_percentage > 50:  # Adjust this threshold as needed
            recommendations.append(job)
            missing = required_set - skill_set
            if missing:
                lacking_skills[job] = list(missing)

    return recommendations, lacking_skills

def main():
    # Get user input
    user_input = input("Enter your skills separated by commas: ")
    user_skills = [skill.strip() for skill in user_input.split(',')]

    # Recommend jobs and find lacking skills
    recommendations, lacking_skills = recommend_jobs(user_skills, jobs)
    
    # Output results
    print("\nRecommended Jobs:")
    if recommendations:
        for job in recommendations:
            print(f"- {job}")
    else:
        print("No jobs found that match your skills.")

    print("\nLacking Skills for Recommended Jobs:")
    if lacking_skills:
        for job, skills in lacking_skills.items():
            print(f"{job}: Missing skills - {', '.join(skills)}")
    else:
        print("No additional skills required for the recommended jobs.")

if __name__ == "__main__":
    main()
