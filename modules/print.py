from PySide6.QtWidgets import (
    QMessageBox,
)
from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtGui import QTextDocument, QPageLayout, QPageSize
from PySide6.QtCore import QMarginsF, QSizeF

from modules.sekolah import getIdentitas
from modules.utils import terbilang

def cetakTransaksi(parent, data):
    try:
        # Create printer object with high resolution
        printer = QPrinter(QPrinter.HighResolution)
        printer.setResolution(300)  # Set DPI to 300 for better quality

        # Set paper size to F4/Folio (210 x 330 mm)
        page_size = QSizeF(210, 330)  # F4/Folio size in mm
        custom_page_size = QPageSize(page_size, QPageSize.Unit.Millimeter, "F4/Folio")
        printer.setPageSize(custom_page_size)
        # Set margins: top=1.5cm, right=1.5cm, bottom=1.5cm, left=2cm
        printer.setPageMargins(QMarginsF(20, 15, 15, 15), QPageLayout.Unit.Millimeter)

        # Show print dialog
        dialog = QPrintDialog(printer, parent)
        dialog.setWindowTitle("Cetak Kuitansi")

        if dialog.exec() == QPrintDialog.Accepted:
            # Create HTML content for the receipt
            html_content = generateReceiptHTML(data)

            # Create QTextDocument and set HTML content
            document = QTextDocument()
            document.setHtml(html_content)

            # Print the document
            document.print_(printer)

            QMessageBox.information(parent, "Info", "Kuitansi berhasil dicetak!")

    except Exception as e:
        QMessageBox.critical(parent, "Error", f"Gagal mencetak kuitansi: {str(e)}")

def cetakSemuaTransaksi(parent, data_list):
    """Cetak semua kuitansi dalam satu dokumen, satu kuitansi per halaman"""
    try:
        if not data_list:
            QMessageBox.warning(parent, "Warning", "Tidak ada data transaksi untuk dicetak!")
            return

        # Create printer object with high resolution
        printer = QPrinter(QPrinter.HighResolution)
        printer.setResolution(300)  # Set DPI to 300 for better quality

        # Set paper size to F4/Folio (210 x 330 mm)
        page_size = QSizeF(210, 330)  # F4/Folio size in mm
        custom_page_size = QPageSize(page_size, QPageSize.Unit.Millimeter, "F4/Folio")
        printer.setPageSize(custom_page_size)
        # Set margins: top=1.5cm, right=1.5cm, bottom=1.5cm, left=2cm
        printer.setPageMargins(QMarginsF(20, 15, 15, 15), QPageLayout.Unit.Millimeter)

        # Show print dialog
        dialog = QPrintDialog(printer, parent)
        dialog.setWindowTitle(f"Cetak Semua Kuitansi ({len(data_list)} transaksi)")

        if dialog.exec() == QPrintDialog.Accepted:
            # Create combined HTML content for all receipts
            html_content = generateAllReceiptsHTML(data_list)

            # Create QTextDocument and set HTML content
            document = QTextDocument()
            document.setHtml(html_content)

            # Print the document
            document.print_(printer)

            QMessageBox.information(parent, "Info", f"Berhasil mencetak {len(data_list)} kuitansi!")

    except Exception as e:
        QMessageBox.critical(parent, "Error", f"Gagal mencetak semua kuitansi: {str(e)}")

def generateReceiptHTML(data):
    """Generate HTML content for the receipt"""
    # Get school data
    school_data = getIdentitas()

    # Format tanggal untuk tampilan
    tanggal = data.get('tanggal', '-')
    if tanggal != '-':
        try:
            from datetime import datetime
            date_obj = datetime.strptime(tanggal, "%Y-%m-%d")
            tanggal_formatted = date_obj.strftime("%d %B %Y")
            # Translate month names to Indonesian
            bulan_indo = {
                'January': 'Januari', 'February': 'Februari', 'March': 'Maret',
                'April': 'April', 'May': 'Mei', 'June': 'Juni',
                'July': 'Juli', 'August': 'Agustus', 'September': 'September',
                'October': 'Oktober', 'November': 'November', 'December': 'Desember'
            }
            for eng, indo in bulan_indo.items():
                tanggal_formatted = tanggal_formatted.replace(eng, indo)
        except:
            tanggal_formatted = tanggal
    else:
        tanggal_formatted = tanggal

    # Format nominal untuk terbilang
    nominal_raw = data.get('nominal', data.get('nilai', '0'))  # Fallback to 'nilai' if 'nominal' not found
    if isinstance(nominal_raw, (int, float)):
        nominal_clean = str(int(nominal_raw))
    else:
        nominal_clean = str(nominal_raw).replace('.', '').replace(',', '')


    # Format the receipt HTML
    html = f"""
    <!DOCTYPE html>
    <html lang="id">
    <head>
      <meta charset="UTF-8">
      <title>Kuitansi BOS</title>
      <style>
        body {{
          margin: 0;
          padding: 0;
          font-size: 18px;
          font-family: Arial, sans-serif;
        }}
        .text-center {{
          text-align: center;
        }}
        .info-table td,
        .content-table td {{
          padding: 8px;
        }}
        table.ttd td p {{
          line-height: 1.2;
          margin: 3px 0;
        }}
        .content-table {{
          border: 2px solid #000 !important;
          border-collapse: collapse !important;
        }}
        .content-table td {{
          border: 1px solid #000 !important;
        }}
        .header {{
          border-bottom: 3px double #000 !important;
          padding-bottom: 8px !important;
        }}
      </style>
    </head>
    <body>

      <div class="clearfix">
        <!-- Logo akan ditambahkan jika tersedia -->
      </div>

      <div class="header" style="border-bottom: 4px double black; padding-bottom: 4px;">
        <table style="width:100%;">
          <tbody>
            <tr>
              <td>
              </td>
              <td>
        <div class="text-center" style="font-size: 1.5em;"><strong>PEMERINTAH {school_data.get('kabupaten', 'KABUPATEN').upper() if school_data else 'KABUPATEN'}</strong></div>
        <div class="text-center" style="font-size: 1.5em;"><strong>DINAS PENDIDIKAN</strong></div>
        <div class="text-center" style="font-size: 1.5em;"><strong>KORWIL KECAMATAN {school_data.get('kecamatan', 'KECAMATAN').upper() if school_data else 'KECAMATAN'}</strong></div>
        <div class="text-center" style="font-size: 1.5em;"><strong>{school_data.get('sekolah', 'NAMA SEKOLAH').upper() if school_data else 'NAMA SEKOLAH'}</strong></div>
        <div class="text-center" style="font-size: 1.2em;">NPSN: {school_data.get('npsn', '00000000') if school_data else '00000000'}</div>
        <div class="text-center">{school_data.get('alamat', 'Alamat Sekolah') if school_data else 'Alamat Sekolah'}, {school_data.get('desa', 'Desa') if school_data else 'Desa'}, {school_data.get('kecamatan', 'Kecamatan') if school_data else 'Kecamatan'}, Kode POs {school_data.get('kode_pos', '00000') if school_data else '00000'}</div>
        <div class="text-center">Telp.: {school_data.get('telp', '-') if school_data else '-'}, Email: {school_data.get('email', '-') if school_data else '-'}</div>
              </td>
              <td>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <table class="info-table" style="margin: 20px auto;">
        <tbody>
        <tr>
          <td><strong>Mata Anggaran</strong></td>
          <td>: BOS Reguler 2024</td>
          <td style="padding: 0 40px;"></td>
          <td><strong>No Bukti</strong></td>
          <td>: {data.get('no_bukti', '-')}</td>
        </tr>
        <tr>
          <td><strong>Tahun Anggaran</strong></td>
          <td>: Tahun 2024</td>
          <td></td>
          <td><strong>Tanggal</strong></td>
          <td>: {tanggal_formatted}</td>
        </tr>
        <tr>
          <td><strong>Sumber Dana</strong></td>
          <td>: APBN</td>
        </tr>
        </tbody>
      </table>

      <div class="title" style="text-align: center; font-weight: 800; font-size: 2em; text-decoration: underline; margin-bottom: 40px;">KUITANSI</div>

      <div style="display:flex; justify-content: space-between; width: 80%; margin: 20px auto;">
        <div>
        <strong>Kode Rekening:</strong> {data.get('kode_rekening', '-')}
        </div>
        <div>
          <strong>Kode Kegiatan:</strong> {data.get('kode_kegiatan', '-')}
        </div>
      </div>

      <table class="content-table" style="width: 80%; margin: 20px auto; border-collapse:collapse;" border="1">
        <tr>
          <td width="30%">Sudah diterima dari</td>
          <td>Bendahara BOS Reguler {school_data.get('sekolah', 'Nama Sekolah') if school_data else 'Nama Sekolah'}</td>
        </tr>
        <tr>
          <td>Uang Sebesar</td>
          <td><em>{terbilang(nominal_clean).title()} Rupiah</em></td>
        </tr>
        <tr>
          <td>Untuk Keperluan</td>
          <td>{data.get('uraian', '-')}</td>
        </tr>
      </table>

      <div class="berkas" style=" margin: 10px auto;font-weight: bold;">*) Bukti / Berkas Terlampir</div>

      <div class="terbilang" style="text-align:center; font-weight: 800; font-size: 1.5em; margin: 40px auto;">Rp. {'{:,.0f}'.format(int(nominal_clean)).replace(',', '.')},-</div>

      <table class="ttd" style="width:100%;">
        <tbody>
        <tr>
          <td></td>
          <td></td>
          <td>Malang, {tanggal_formatted}</td>

        </tr>
        <tr>
            <td style="width: 33%; text-align: center;">
              <p>Menyetujui,</p>
              <p>Kepala Sekolah</p>
              <p style="text-decoration: underline; font-weight: bold;margin-top: 3cm;">{school_data.get('ks', 'NAMA KEPALA SEKOLAH').upper() if school_data else 'NAMA KEPALA SEKOLAH'}</p>
              <p>NIP. {school_data.get('nip_ks', '000000000000000000') if school_data else '000000000000000000'}</p>

            </td>
            <td style="width: 33%; text-align: center;">
              <p>Yang mengeluarkan,</p>
              <p>Bendahara</p>
              <p style="text-decoration: underline; font-weight: bold;margin-top: 3cm;">{school_data.get('bendahara', 'NAMA BENDAHARA').upper() if school_data else 'NAMA BENDAHARA'}</p>
              <p>NIP. {school_data.get('nip_bendahara', '000000000000000000') if school_data else '000000000000000000'}</p>
            </td>
            <td style="width: 33%; text-align: center;">
              <p>Yang menerima,</p>
              <p>Pelaksana</p>
              <p style="text-decoration:underline;margin-top: 3cm; font-weight: bold;">...............................</p>
              <p>NIP. </p>
            </td>
        </tr>
        </tbody>
      </table>

    </body>
    </html>
    """
    return html

def generateAllReceiptsHTML(data_list):
    """Generate HTML content for all receipts, one per page"""
    # Get school data
    school_data = getIdentitas()

    # Base CSS styles untuk template baru
    css_styles = """
        body {
          margin: 0;
          padding: 0;
          font-size: 18px;
          font-family: Arial, sans-serif;
        }
        .text-center {
          text-align: center;
        }
        .info-table td,
        .content-table td {
          padding: 8px;
        }
        table.ttd td p {
          line-height: 1.2;
          margin: 3px 0;
        }
        .content-table {
          border: 2px solid #000 !important;
          border-collapse: collapse !important;
        }
        .content-table td {
          border: 1px solid #000 !important;
        }
        .header {
          border-bottom: 3px double #000 !important;
          padding-bottom: 8px !important;
        }
        .page-break {
          page-break-before: always;
        }
    """

    # Start HTML document
    html = f"""
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <title>Kuitansi BOS - Semua Transaksi</title>
        <style>{css_styles}</style>
    </head>
    <body>
    """

    # Generate each receipt
    for index, data in enumerate(data_list):
        # Format tanggal untuk tampilan
        tanggal = data.get('tanggal', '-')
        if tanggal != '-':
            try:
                from datetime import datetime
                date_obj = datetime.strptime(tanggal, "%Y-%m-%d")
                tanggal_formatted = date_obj.strftime("%d %B %Y")
                # Translate month names to Indonesian
                bulan_indo = {
                    'January': 'Januari', 'February': 'Februari', 'March': 'Maret',
                    'April': 'April', 'May': 'Mei', 'June': 'Juni',
                    'July': 'Juli', 'August': 'Agustus', 'September': 'September',
                    'October': 'Oktober', 'November': 'November', 'December': 'Desember'
                }
                for eng, indo in bulan_indo.items():
                    tanggal_formatted = tanggal_formatted.replace(eng, indo)
            except:
                tanggal_formatted = tanggal
        else:
            tanggal_formatted = tanggal

        # Format nominal untuk terbilang
        nominal_raw = data.get('nominal', data.get('nilai', '0'))  # Fallback to 'nilai' if 'nominal' not found
        if isinstance(nominal_raw, (int, float)):
            nominal_clean = str(int(nominal_raw))
        else:
            nominal_clean = str(nominal_raw).replace('.', '').replace(',', '')

        # Add page break before each receipt except the first one
        page_break_class = "page-break" if index > 0 else ""

        receipt_html = f"""
        <div class="{page_break_class}">
          <div class="clearfix">
            <!-- Logo akan ditambahkan jika tersedia -->
          </div>

          <div class="header" style="border-bottom: 4px double black; padding-bottom: 4px;">
            <table style="width:100%;">
              <tbody>
                <tr>
                  <td>
                  </td>
                  <td>
            <div class="text-center" style="font-size: 1.5em;"><strong>PEMERINTAH {school_data.get('kabupaten', 'KABUPATEN').upper() if school_data else 'KABUPATEN'}</strong></div>
            <div class="text-center" style="font-size: 1.5em;"><strong>DINAS PENDIDIKAN</strong></div>
            <div class="text-center" style="font-size: 1.5em;"><strong>KORWIL KECAMATAN {school_data.get('kecamatan', 'KECAMATAN').upper() if school_data else 'KECAMATAN'}</strong></div>
            <div class="text-center" style="font-size: 1.5em;"><strong>{school_data.get('sekolah', 'NAMA SEKOLAH').upper() if school_data else 'NAMA SEKOLAH'}</strong></div>
            <div class="text-center" style="font-size: 1.2em;">NPSN: {school_data.get('npsn', '00000000') if school_data else '00000000'}</div>
            <div class="text-center">{school_data.get('alamat', 'Alamat Sekolah') if school_data else 'Alamat Sekolah'}, {school_data.get('desa', 'Desa') if school_data else 'Desa'}, {school_data.get('kecamatan', 'Kecamatan') if school_data else 'Kecamatan'}, Kode POs {school_data.get('kode_pos', '00000') if school_data else '00000'}</div>
            <div class="text-center">Telp.: {school_data.get('telp', '-') if school_data else '-'}, Email: {school_data.get('email', '-') if school_data else '-'}</div>
                  </td>
                  <td>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <table class="info-table" style="margin: 20px auto;">
            <tbody>
            <tr>
              <td><strong>Mata Anggaran</strong></td>
              <td>: BOS Reguler 2024</td>
              <td style="padding: 0 40px;"></td>
              <td><strong>No Bukti</strong></td>
              <td>: {data.get('no_bukti', '-')}</td>
            </tr>
            <tr>
              <td><strong>Tahun Anggaran</strong></td>
              <td>: Tahun 2024</td>
              <td></td>
              <td><strong>Tanggal</strong></td>
              <td>: {tanggal_formatted}</td>
            </tr>
            <tr>
              <td><strong>Sumber Dana</strong></td>
              <td>: APBN</td>
            </tr>
            </tbody>
          </table>

          <div class="title" style="text-align: center; font-weight: 800; font-size: 2em; text-decoration: underline; margin-bottom: 40px;">KUITANSI</div>

          <div style="display:flex; justify-content: space-between; width: 80%; margin: 20px auto;">
            <div>
            <strong>Kode Rekening:</strong> {data.get('kode_rekening', '-')}
            </div>
            <div>
              <strong>Kode Kegiatan:</strong> {data.get('kode_kegiatan', '-')}
            </div>
          </div>

          <table class="content-table" style="margin: 20px auto; border-collapse:collapse;" border="1">
            <tr>
              <td width="30%">Sudah diterima dari</td>
              <td>Bendahara BOS Reguler {school_data.get('sekolah', 'Nama Sekolah') if school_data else 'Nama Sekolah'}</td>
            </tr>
            <tr>
              <td>Uang Sebesar</td>
              <td><em>{terbilang(nominal_clean).title()} Rupiah</em></td>
            </tr>
            <tr>
              <td>Untuk Keperluan</td>
              <td>{data.get('uraian', '-')}</td>
            </tr>
          </table>

          <div class="berkas" style="margin: 10px auto;font-weight: bold;">*) Bukti / Berkas Terlampir</div>

          <div class="terbilang" style="text-align:center; font-weight: 800; font-size: 1.5em; margin: 40px auto;">Rp. {'{:,.0f}'.format(int(nominal_clean)).replace(',', '.')},-</div>

          <table class="ttd" style="width:100%;">
            <tbody>
            <tr>
              <td></td>
              <td></td>
              <td>Malang, {tanggal_formatted}</td>
            </tr>
            <tr>
                <td style="width: 33%; text-align: center;">
                  <p>Menyetujui,</p>
                  <p>Kepala Sekolah</p>
                  <p style="text-decoration: underline; font-weight: bold;margin-top: 3cm;">{school_data.get('ks', 'NAMA KEPALA SEKOLAH').upper() if school_data else 'NAMA KEPALA SEKOLAH'}</p>
                  <p>NIP. {school_data.get('nip_ks', '000000000000000000') if school_data else '000000000000000000'}</p>
                </td>
                <td style="width: 33%; text-align: center;">
                  <p>Yang mengeluarkan,</p>
                  <p>Bendahara</p>
                  <p style="text-decoration: underline; font-weight: bold;margin-top: 3cm;">{school_data.get('bendahara', 'NAMA BENDAHARA').upper() if school_data else 'NAMA BENDAHARA'}</p>
                  <p>NIP. {school_data.get('nip_bendahara', '000000000000000000') if school_data else '000000000000000000'}</p>
                </td>
                <td style="width: 33%; text-align: center;">
                  <p>Yang menerima,</p>
                  <p>Pelaksana</p>
                  <p style="text-decoration:underline;margin-top: 3cm; font-weight: bold;">...............................</p>
                  <p>NIP. </p>
                </td>
            </tr>
            </tbody>
          </table>
        </div>
        """

        html += receipt_html

    # Close HTML document
    html += """
    </body>
    </html>
    """

    return html
