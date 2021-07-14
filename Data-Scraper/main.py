import secret
from datasetBuilder import twitterDatasetBuilder

def main():
    consumerAPI_Key = secret.consumerAPI_Key
    consumerAPI_Secret = secret.consumerAPI_Secret
    accessToken = secret.accessToken
    accessTokenSecret = secret.accessTokenSecret

    print("Social Media DataSet Building ...")
    keyword = str(input("Enter keywords to search for: "))
    limit = int(input("Enter the DataSet builder limit: "))
    print("Use - to separate the date format. (For Example: 2020-04-15) ")
    begin_date = str(input("Enter the START date to search for in this period: "))
    end_date = str(input("Enter the END date to search for in this period: "))

    # DataSet Builder Init
    twitter_dataset_build = twitterDatasetBuilder(ConsumerAPI_Key=consumerAPI_Key,
                                                ConsumerAPI_Secret=consumerAPI_Secret,
                                                Access_Token=accessToken, Access_Token_Secret=accessTokenSecret)

    # Build a DataSet about this theme for analysis
    twitter_dataset_build.dataset_building(tag=keyword, limit=limit, begin_date=begin_date, end_date=end_date,
                                           lang="en")

if __name__ == "__main__":
    main()


