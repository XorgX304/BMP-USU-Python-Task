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


class GUI_Info_BitMapV4Header(QWidget):

    def __init__(self):
        super().__init__()
        layout = QFormLayout(self)

        self.red_mask = QLineEdit(self)
        layout.addRow('RedMask', self.red_mask)
        self.green_mask = QLineEdit(self)
        layout.addRow('GreenMask', self.green_mask)
        self.blue_mask = QLineEdit(self)
        layout.addRow('BlueMask', self.blue_mask)
        self.alpha_mask = QLineEdit(self)
        layout.addRow('AlphaMask', self.alpha_mask)
        self.cs_type = QLineEdit(self)
        layout.addRow('CSType', self.cs_type)
        self.endpoints = QLineEdit(self)
        layout.addRow('Endpoints', self.endpoints)
        self.gamma_red = QLineEdit(self)
        layout.addRow('GammaRed', self.gamma_red)
        self.gamma_green = QLineEdit(self)
        layout.addRow('GammaGreen', self.gamma_green)
        self.gamma_blue = QLineEdit(self)
        layout.addRow('GammaBlue', self.gamma_blue)

    def set_fields(self, bmp_obj):
        assert type(bmp_obj) == bmp_module.BMPIMAGE

        self.red_mask.setText(str(bmp_obj.BMInfo.Header.RedMask))
        self.green_mask.setText(str(bmp_obj.BMInfo.Header.GreenMask))
        self.blue_mask.setText(str(bmp_obj.BMInfo.Header.BlueMask))
        self.alpha_mask.setText(str(bmp_obj.BMInfo.Header.AlphaMask))
        self.cs_type.setText(str(bmp_obj.BMInfo.Header.CSType))
        self.endpoints.setText(str(bmp_obj.BMInfo.Header.Endpoints))
        self.gamma_red.setText(str(bmp_obj.BMInfo.Header.GammaRed))
        self.gamma_green.setText(str(bmp_obj.BMInfo.Header.GammaGreen))
        self.gamma_blue.setText(str(bmp_obj.BMInfo.Header.GammaBlue))


class GUI_Info_BitMapV5Header(QWidget):

    def __init__(self):
        super().__init__()
        layout = QFormLayout(self)

        self.intent = QLineEdit(self)
        layout.addRow('Intent', self.intent)
        self.profile_data = QLineEdit(self)
        layout.addRow('ProfileData', self.profile_data)
        self.profile_size = QLineEdit(self)
        layout.addRow('ProfileSize', self.profile_size)
        self.reserved = QLineEdit(self)
        layout.addRow('Reserved', self.reserved)

    def set_fields(self, bmp_obj):
        assert type(bmp_obj) == bmp_module.BMPIMAGE

        self.intent.setText(str(bmp_obj.BMInfo.Header.Intent))
        self.profile_data.setText(str(bmp_obj.BMInfo.Header.ProfileData))
        self.profile_size.setText(str(bmp_obj.BMInfo.Header.ProfileSize))
        self.reserved.setText(str(bmp_obj.BMInfo.Header.Reserved))


class GUI_ImageView(QWidget):

    def __init__(self):
        super().__init__()
        self.view = QLabel(self)
        self.image = None
        self.setMinimumWidth(350)

    def set_image(self, bmp_obj):
        assert type(bmp_obj) == bmp_module.BMPIMAGE

        height = bmp_obj.BMInfo.Header.Height
        width = bmp_obj.BMInfo.Header.Width
        self.image = QImage(width, height, QImage.Format_RGB32)
        for i in range(height):
            for j in range(width):
                self.image.setPixel(
                    j,
                    i,
                    bmp_module.color_from_tuple(
                        bmp.PixelData[i][j]
                    )
                )
        self.view.setPixmap(QPixmap(self.image))

    def unset_image(self):
        self.image = None
        self.setPixmap(QPixmap(self.image))

    def resizeEvent(self, event):
        w = event.size().width()
        h = event.size().height()
        width = self.image.width()
        height = self.image.height()
        if w / h < width / height:
            new_w = w
            new_h = int(w / width * height)
        else:
            new_w = int(h / height * width)
            new_h = h
        self.view.setPixmap(
            QPixmap.fromImage(self.image).scaled(
                new_w,
                new_h
            )
        )
        self.view.adjustSize()

class GUI(QWidget):

    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)

        self.tabs = QTabWidget()
        self.tabs.setFixedWidth(350)
        self.tabs.setMinimumHeight(400)

        self.file_header = GUI_Info_FileHeader()
        self.tabs.addTab(self.file_header, "FileHeader")
        self.bit_map_core_header = GUI_Info_BitMapCoreHeader()
        self.tabs.addTab(self.bit_map_core_header, "BitMapCoreHeader")
        self.bit_map_info_header = GUI_Info_BitMapInfoHeader()
        self.tabs.addTab(self.bit_map_info_header, "BitMapInfoHeader")
        self.bit_map_v4_header = GUI_Info_BitMapV4Header()
        self.tabs.addTab(self.bit_map_v4_header, "BitMapV4Header")
        self.bit_map_v5_header = GUI_Info_BitMapV5Header()
        self.tabs.addTab(self.bit_map_v5_header, "BitMapV5Header")

        self.view = GUI_ImageView()

        layout.addWidget(self.view, 0, 0)
        layout.addWidget(self.tabs, 0, 1)

        self.disable_all_dabs()

    def disable_all_dabs(self):
        for i in range(0, 5):
            self.tabs.setTabEnabled(i, False)

    def set_all_fields(self, bmp_obj):
        self.disable_all_dabs()
        self.tabs.setTabEnabled(0, True)
        self.file_header.set_fields(bmp_obj)

        self.tabs.setTabEnabled(1, True)
        self.bit_map_core_header.set_fields(bmp_obj)
        if bmp_obj.BMInfo.Header.Size > 12:
            self.tabs.setTabEnabled(2, True)
            self.bit_map_info_header.set_fields(bmp_obj)
        if bmp_obj.BMInfo.Header.Size > 40:
            self.tabs.setTabEnabled(3, True)
            self.bit_map_v4_header.set_fields(bmp_obj)
        if bmp_obj.BMInfo.Header.Size > 108:
            self.tabs.setTabEnabled(4, True)
            self.bit_map_v5_header.set_fields(bmp_obj)
        self.view.set_image(bmp_obj)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    fin = open('input02.bmp', 'rb')
    bmp = bmp_module.BMPIMAGE(fin)

    info = GUI()
    info.set_all_fields(bmp)
    info.show()

    app.exec()