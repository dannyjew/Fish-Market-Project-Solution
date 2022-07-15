import pandas as pd

import FishProject.config_manager as conf
import FishProject.App.PullingFromS3 as pulling
import FishProject.App.DF_Manipulator as manip

test_puller = pulling.PullingClass()


def test_pull_a_df():
    tested_csv = test_puller.pull_data_set(conf.BUCKETNAME, conf.TARTARE + '.csv')
    assert type(tested_csv) == pd.DataFrame


test_manipulator = manip.DataManipulator()


# From hereon out the tests look messy as they require their own dataframes to test against something known
# definitely not a stress test but that can come when there's more fish
def test_summing_two_dfs():
    test_data1 = [['a', 1], ['b', 2], ['c', 3]]
    test_df1 = pd.DataFrame(test_data1)
    test_df2 = pd.DataFrame([['a', 4], ['b', 5], ['c', 6]])
    new_df = test_manipulator.appender(test_df1, test_df2)
    reference_df = pd.DataFrame([['a', 1], ['b', 2], ['c', 3], ['a', 4], ['b', 5], ['c', 6]],
                                index=[0, 1, 2, 0, 1, 2])
    pd.testing.assert_frame_equal(new_df, reference_df)


def test_avg_finder():
    df = pd.DataFrame([['a', 3.0], ['a', 6.0], ['a', 9.0], ['b', 5.0], ['b', 7.0], ['b', 9.0]], columns=["Species", "Number"])
    new_df = test_manipulator.avg_finder(df)
    new_df = new_df.reset_index(drop=False)     # Adds an index so the average matches the reference
    reference_df = pd.DataFrame([['a', 6.0], ['b', 7.0]], columns=["Species", "Number"])
    print(new_df)
    print(reference_df)
    pd.testing.assert_frame_equal(new_df, reference_df)

def test_df_to_dict():
    df = pd.DataFrame()
    assert type(test_manipulator.df_to_dict(df)) == dict

# I have no clue how to test an upload and google didn't give me much :(
