folder_list_dir = os.getenv("HOME") + "/aiffel/friends_list/"
folder_list = os.listdir(folder_list_dir)
print(folder_list)
print(len(folder_list))

x_data, y_data = [], []
print(x_data, y_data)

for i in range(len(folder_list)):
    image_path = folder_list_dir + folder_list[i]
    # 각 사람들 폴더를 돌며 트레인셋 모음 생성
    x_data.append(load_data(image_path)[0])
    print(np.array(x_data).shape)
    y_data.append(load_data(image_path)[1])
    print(np.array(y_data).shape)
    #print(image_path)
    #print(load_data(image_path)[0].shape)
    #print(x_data)
    #(x_data, y_data) = load_data(image_dir_path[0])