from abc import ABC, abstractmethod
import pandas as pd
from fpdf import FPDF


class ReportFormat(ABC):
    @abstractmethod
    def generate(self, content):
        pass


class PDFFormat(ReportFormat):
    def __init__(self, filename):
        self.filename = filename
        self.pdf = FPDF()

    def generate(self, content):
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(200, 10, txt=content, ln=True, align='C')
        self.pdf.output(self.filename)


class ExcelFormat(ReportFormat):
    def __init__(self, filename):
        self.filename = filename

    def generate(self, content):
        df = pd.DataFrame(content)
        df.to_excel(self.filename, index=False)


class CSVFormat(ReportFormat):
    def __init__(self, filename):
        self.filename = filename

    def generate(self, content):
        df = pd.DataFrame(content)
        df.to_csv(self.filename)


class FormatFactory:
    @staticmethod
    def create_report_format(report_format, filename):
        if report_format == "PDF":
            return PDFFormat(filename)
        elif report_format == "Excel":
            return ExcelFormat(filename)
        elif report_format == "CSV":
            return CSVFormat(filename)
        else:
            return None


class Report(ABC):
    def __init__(self, report_format: ReportFormat):
        self.report_format = report_format

    @abstractmethod
    def generate_report(self, content):
        pass


class SalesReport(Report):
    def generate_report(self, content):
        self.report_format.generate(content)


class InventoryReport(Report):
    def generate_report(self, content):
        self.report_format.generate(content)


class EmployeeReport(Report):
    def generate_report(self, content):
        self.report_format.generate(content)


class ReportFactory:
    @staticmethod
    def create_report(report: str, report_format: ReportFormat):
        if report == "Sales":
            return SalesReport(report_format)
        elif report == "Inventory":
            return InventoryReport(report_format)
        elif report == "Employee":
            return EmployeeReport(report_format)
        else:
            return None


def main() -> None:
    pdf_format = FormatFactory.create_report_format("PDF", "employee.pdf")
    employee_report = ReportFactory.create_report("Employee",  pdf_format)
    employee_report.generate_report("Himanshu Kumar Employee")

    content = {
        "Name": ["John", "Jane", "Alice", "Bob", "Mike"],
        "Age": [25, 30, 21, 20, 26]
    }
    csv_format = FormatFactory.create_report_format("CSV", "employee_data.csv")
    employee_report = ReportFactory.create_report("Employee", csv_format)
    employee_report.generate_report(content)


if __name__ == '__main__':
    main()
