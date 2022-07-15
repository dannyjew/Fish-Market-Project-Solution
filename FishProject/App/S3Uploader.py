import json


class S3Uploader:
    # As with DF_Manipulator, this class contains no variables, and only one method (which is static)
    # In this case, there is no need for this to be a class, but it allows for future development if needed
    def __init__(self):
        pass

    # Method to handle the upload, in it's current state, only handles JSONs (hence the default file_type) but
    # allows for growth to include other files (CSVs would be the next step)
    @staticmethod
    def upload_file(file: dict, filename: str, bucket_name: str, full_key: str, s3_client, file_type="json"):
        if file_type == "json":
            full_filename = filename + "." + file_type
            with open(full_filename, 'w') as json_file:
                json.dump(file, json_file)
            s3_client.upload_file(Filename=full_filename,
                                  Bucket=bucket_name,
                                  Key=full_key)
        else:
            print("Would be great fun if this bit was coded...\n"
                  "Real shame, eh?")
