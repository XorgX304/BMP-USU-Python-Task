from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import bmp_module


class GUI_Info_FileHeader(QWidget):

    def __init__(self):
        super().__init__()
        layout = QFormLayout(self)

        self.type = QLineEdit(self)
        layout.addRow('Type', self.type)
        self.size = QLineEdit(self)
        layout.addRow('Size', self.size)
        self.reserved1 = QLineEdit(self)
        layout.addRow('Reserved1', self.reserved1)
        self.reserved2 = QLineEdit(self)
        layout.addRow('Reserved2', self.reserved2)
        self.off_bits = QLineEdit(self)
        layout.addRow('OffBits', self.off_bits)

    def set_fields(self, bmp_obj):
        assert type(bmp_obj) == bmp_module.BMPIMAGE

        self.type.setText(hex(bmp_obj.BMFileHeader.Type))
        self.size.setText(str(bmp_obj.BMFileHeader.Size))
        self.reserved1.setText(hex(bmp_obj.BMFileHeader.Reserved1))
        self.reserved2.setText(hex(bmp_obj.BMFileHeader.Reserved2))
        self.off_bits.setText(hex(bmp_obj.BMFileHeader.OffBits))


class GUI_Info_BitMapCoreHeader(QWidget):

    def __init__(self):
        super().__init__()
        layout = QFormLayout(self)

        self.size = QLineEdit(self)
        layout.addRow('Size', self.size)
        self.width = QLineEdit(self)
        layout.addRow('Width', self.width)
        self.height = QLineEdit(self)
        layout.addRow('Height', self.height)
        self.planes = QLineEdit(self)
        layout.addRow('Planes', self.planes)
        self.bit_count = QLineEdit(self)
        layout.addRow('BitCount', self.bit_count)

    def set_fields(self, bmp_obj):
        assert type(bmp_obj) == bmp_module.BMPIMAGE

        self.size.setText(str(bmp_obj.BMInfo.Header.Size))
        self.width.setText(str(bmp_obj.BMInfo.Header.Width))
        self.height.setText(str(bmp_obj.BMInfo.Header.Height))
        self.planes.setText(str(bmp_obj.BMInfo.Header.Planes))
        self.bit_count.setText(str(bmp_obj.BMInfo.Header.BitCount))


class GUI_Info_BitMapInfoHeader(QWidget):

    def __init__(self):
        super().__init__()
        layout = QFormLayout(self)

        self.compression = QLineEdit(self)
        layout.addRow('Compression', self.compression)
        self.size_image = QLineEdit(self)
        layout.addRow('SizeImage', self.size_image)
        self.xpels_per_meter = QLineEdit(self)
        layout.addRow('XPelsPerMeter', self.xpels_per_meter)
        self.ypels_per_meter = QLineEdit(self)
        layout.addRow('YPelsPerMeter', self.ypels_per_meter)
        self.clr_used = QLineEdit(self)
        layout.addRow('ClrUsed', self.clr_used)
        self.clr_important = QLineEdit(self)
        layout.addRow('ClrImportant', self.clr_important)

    def set_fields(self, bmp_obj):
        assert type(bmp_obj) == bmp_module.BMPIMAGE

        self.compression.setText(str(bmp_obj.BMInfo.Header.Compression))
        self.size_image.setText(str(bmp_obj.BMInfo.Header.SizeImage))
        self.xpels_per_meter.setText(str(bmp_obj.BMInfo.Header.XPelsPerMeter))
        self.ypels_per_meter.setText(str(bmp_obj.BMInfo.Header.YPelsPerMeter))
        self.clr_used.setText(str(bmp_obj.BMInfo.Header.ClrUsed))
        self.clr_important.setText(str(bmp_obj.BMInfo.Header.ClrImportant))


class GUI(QWidget):

    def __init__(self):
        super().__init__()

        self.bmp_obj = None

        self.tabs = QTabWidget(self)
        self.tabs.setFixedWidth(350)
        self.tabs.setMinimumHeight(400)

        self.file_header = GUI_Info_FileHeader()
        self.tabs.addTab(self.file_header, "FileHeader")
        self.bit_map_core_header = GUI_Info_BitMapCoreHeader()
        self.tabs.addTab(self.bit_map_core_header, "BitMapCoreHeader")
        self.bit_map_info_header = GUI_Info_BitMapInfoHeader()
        self.tabs.addTab(self.bit_map_info_header, "BitMapInfoHeader")

        self.disable_all_dabs()

    def disable_all_dabs(self):
        for i in range(0, 3):
            self.tabs.setTabEnabled(i, False)

    def set_all_fields(self, bmp_obj):
        self.tabs.setTabEnabled(0, True)
        self.file_header.set_fields(bmp_obj)

        self.tabs.setTabEnabled(1, True)
        self.bit_map_core_header.set_fields(bmp_obj)
        if bmp_obj.BMInfo.Header.Size > 12:
            self.tabs.setTabEnabled(2, True)
            self.bit_map_info_header.set_fields(bmp_obj)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    fin = open('input02.bmp', 'rb')
    bmp = bmp_module.BMPIMAGE(fin)

    info = GUI()
    info.set_all_fields(bmp)
    info.show()

    app.exec()