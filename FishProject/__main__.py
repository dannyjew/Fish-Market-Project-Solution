import FishProject.App.PullingFromS3 as pulling
import FishProject.App.DF_Manipulator as manip
import FishProject.App.S3Uploader as s3_loader

import pprint as pp

# Instantiating classes required and retrieving the bucket name from declaration when pulling
pulling_class = pulling.PullingClass()
data_frame_manipulator = manip.DataManipulator()
uploader = s3_loader.S3Uploader()
bucket_name = pulling_class.get_bucket_name

# Pulling and combining the three given fish-based lists, no cleaning done as (at first inspection) data is clean
fish_df1 = pulling_class.pull_data_set(bucket_name, pulling_class.get_fish_string_list[0])
fish_df_mon = pulling_class.pull_data_set(bucket_name, pulling_class.get_fish_string_list[1])
fish_df_tues = pulling_class.pull_data_set(bucket_name, pulling_class.get_fish_string_list[2])

full_fish_df = data_frame_manipulator.appender(fish_df1, fish_df_mon, fish_df_tues)

# Calculating average, and printing it for inspection
avg_fish_info = data_frame_manipulator.avg_finder(full_fish_df)
pp.pprint(avg_fish_info)

# Turning data into a dictionary ready to be uploaded to S3
data_to_upload = data_frame_manipulator.df_to_dict(avg_fish_info)

# Calling uploader function to actually upload data
uploader.upload_file(data_to_upload, "Matt_L", bucket_name, "Data100/fish/Matt_L.json", pulling_class.get_client)
