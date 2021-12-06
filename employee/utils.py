import csv
import xlwt

from django.http import HttpResponse


def export_csv(emp):
    """ It will return csv data  """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename=employee.csv"
    writer = csv.DictWriter(
        response,
        fieldnames=[
            'Name',
            'Department',
            'Contact'
        ]
    )
    writer.writeheader()
    for data in emp:
        writer.writerow({
            'Name': data.name,
            'Department': data.department,
            'Contact': data.contact
        })
    return response

def export_excel(emp):
    """ It will return excel file  """
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment;filename=employee.xls' 

    work_book = xlwt.Workbook(encoding = 'utf-8')
    work_sheet = work_book.add_sheet('Employees')

    work_sheet.write(0,0, 'Name') 
    work_sheet.write(0,1, 'Department') 
    work_sheet.write(0,2, 'Contact')
    
    row = 1 
    for data in emp:
        work_sheet.write(row,0, data.name)
        work_sheet.write(row,1, data.department)
        work_sheet.write(row,2, data.contact)
        row=row + 1 

    work_book.save(response)
    return response