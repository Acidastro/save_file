import pandas as pd
import io

def adjust_column_widths(data: dict) -> io.BytesIO:
        """
        Выравнивание колонок в excel
        """
        buffer = io.BytesIO()
        df = pd.DataFrame(data)
        max_lengths = df.map(lambda x: len(str(x))).max()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
            worksheet = writer.sheets['Sheet1']
            for i, max_length in enumerate(max_lengths):
                worksheet.set_column(i, i, max_length + 2)
        return buffer
