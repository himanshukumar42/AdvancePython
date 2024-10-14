from abc import ABC, abstractmethod


class Profile(ABC):
    @abstractmethod
    def get_profile(self):
        pass


class JobSeekerProfile(Profile):
    def get_profile(self):
        print("This is a Job Seeker Profile")


class RecruiterProfile(Profile):
    def get_profile(self):
        print("This is a Recruiter Profile")


class ProfileFactory:
    @staticmethod
    def create_profile(user_type):
        if user_type == "JobSeeker":
            return JobSeekerProfile()
        elif user_type == "Recruiter":
            return RecruiterProfile()
        else:
            raise ValueError(f"Invalid Profile {user_type}")


def main() -> None:
    jobSeeker = ProfileFactory.create_profile("JobSeeker")
    jobSeeker.get_profile()


if __name__ == '__main__':
    main()
