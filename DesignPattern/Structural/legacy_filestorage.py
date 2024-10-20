from abc import ABC, abstractmethod

import boto3


class FileStorage(ABC):
    @abstractmethod
    def save_file(self, filename: str, content: str):
        pass

    @abstractmethod
    def get_file(self, filename: str):
        pass


class LocalFileStorage(FileStorage):
    def save_file(self, filename: str, content: str):
        with open(filename, 'w') as f:
            f.write(content)
            f.write("\nthis is end")
        print(f"File {filename} saved locally.")

    def get_file(self, filename: str):
        with open(filename, 'r') as f:
            return f.read()


class S3FileStorage:
    def __init__(self):
        self.s3_client = boto3.client('s3')
        self.bucket_name = 'my-startup-bucket'

    def upload_to_s3(self, filename: str, content: str):
        self.s3_client.put_object(
            Bucket=self.bucket_name,
            key=filename,
            Body=content
        )
        print(f"file {filename} uploaded to s3")

    def download_from_s3(self, filename: str):
        response = self.s3_client.get_object(
            Bucket=self.bucket_name,
            key=filename
        )
        return response['Body'].read().decode('utf-8')


class S3FileStorageAdapter(FileStorage):
    def __init__(self, s3_storage: S3FileStorage):
        self.s3_storage = s3_storage

    def save_file(self, filename: str, content: str):
        self.s3_storage.upload_to_s3(filename=filename, content=content)

    def get_file(self, filename: str):
        return self.s3_storage.download_from_s3(filename=filename)


class MyApplication:
    def __init__(self, filename):
        self.filename = filename
        self.file_object = S3FileStorageAdapter(S3FileStorage())

    def save_data(self):
        self.file_object.save_file(filename=self.filename, content="No Content")

    def get_data(self):
        return self.file_object.get_file(filename=self.filename)


def main() -> None:
    my_app = MyApplication("new_output.txt")
    my_app.save_data()
    print(my_app.get_data())


if __name__ == '__main__':
    main()
