from knowledge_base_qa.orm.share_market_overall.tb_sh_market_overall_crawled import ShMarketOverallCrawled

smoc = ShMarketOverallCrawled()



import os

import xlrd

from knowledge_base_qa import config


excel_info_url = 'http://fec.mofcom.gov.cn/article/fwydyl/tjsj/'

excel_path = os.path.join(config.PACKAGE_PATH, 'data/excel/one_belt_one_road')
excel_name = 'one_belt_one_road.xlsx'
excel_file = os.path.join(excel_path,excel_name)


def extract_excel():
    """

    Returns: 将EXCEL中的数据作为二维数组返回

    """
    records = []
    data = xlrd.open_workbook(excel_file)
    table_1 = data.sheet_by_name('Sheet1')
    # 行数
    nrows_1 = table_1.nrows
    # 列数
    ncols_1 = table_1.ncols
    # 取某行的值
    row = table_1.row_values(0)
    # 取某列的值
    col = table_1.col_values(0)

    for i in range(nrows_1):
        records.append(table_1.row_values(i))
    # for j in range(ncols_1):
    #     print(table_1.col_values(j))

    print(records[0])
    return records


if __name__ == '__main__':
    extract_excel()
