class CsvReader:
    def __init__(self, filename):
        self.filename = filename
        self.col_names = []
        self.rows = []

    def read_data(self):
        with open(self.filename, "r") as f:
            raw_lines = f.readlines() #read lines개행문자를 기준으로 리스트를 작성한다,

            #raw_lines = ["name, age, position"]

        col_count = -1
        row_strings = []
        for raw_line in raw_lines:
            if col_count < 0:
                col_count = len(raw_line.split(","))
                #col_count ==3 ==len(다음줄의 데이터의 갯수 가 이전 데이터의 갯수와 같은가)
            elif col_count != len(raw_line.split(",")):
                raise ValueError("Not valid CSV")
            
            row_strings.append(raw_line.replace("\n", ""))

        self.col_names = row_strings[0].split(",")
        for row_string in row_strings[1:]:
            self.rows.append(row_string.split(","))

    def as_dict_list(self):
        result_list = []
        for row in self.rows:
            result_dict = {}
            for idx, col in enumerate(self.col_names):
                result_dict[col] = row[idx]
            
            result_list.append(result_dict)

        return result_list

    def as_tuple(self):

        tuple_list = []
        for row in self.rows:
            





if __name__ == "__main__": #엔트리 포인트 메인 플로우의 시작점을 정의한다.
    csv_reader = CsvReader("test_csv.csv")
    csv_reader.read_data()
    result_list = csv_reader.as_dict_list()
    for result in result_list:
        print(result)

    re