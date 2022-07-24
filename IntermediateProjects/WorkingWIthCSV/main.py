import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

primary_fur_col = data["Primary Fur Color"]
Gray_squirrels = len(data[primary_fur_col=="Gray"])
Black_squirrels = len(data[primary_fur_col=="Black"])
Red_squirrels = len(data[primary_fur_col=="Cinnamon"])

color_count_dict = {
    "primary_fur_col": ["Gray", "Black", "Red"],
    "count": [Gray_squirrels, Black_squirrels, Red_squirrels]
}

new_data_frame = pandas.DataFrame(color_count_dict)
# print(new_data_frame)
new_filtered_csv = new_data_frame.to_csv('filtered_file.csv',index=False)