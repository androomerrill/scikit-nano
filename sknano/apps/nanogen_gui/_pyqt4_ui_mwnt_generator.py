# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mwnt_generator.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MWNTGenerator(object):
    def setupUi(self, MWNTGenerator):
        MWNTGenerator.setObjectName(_fromUtf8("MWNTGenerator"))
        MWNTGenerator.resize(650, 650)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MWNTGenerator.sizePolicy().hasHeightForWidth())
        MWNTGenerator.setSizePolicy(sizePolicy)
        MWNTGenerator.setMinimumSize(QtCore.QSize(650, 650))
        MWNTGenerator.setMaximumSize(QtCore.QSize(800, 1000))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        MWNTGenerator.setFont(font)
        self.centralwidget = QtGui.QWidget(MWNTGenerator)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_19 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_2.addWidget(self.label_19)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mwnt_Ch_list_radio_button = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.mwnt_Ch_list_radio_button.setFont(font)
        self.mwnt_Ch_list_radio_button.setChecked(True)
        self.mwnt_Ch_list_radio_button.setObjectName(_fromUtf8("mwnt_Ch_list_radio_button"))
        self.mwnt_generator_button_group = QtGui.QButtonGroup(MWNTGenerator)
        self.mwnt_generator_button_group.setObjectName(_fromUtf8("mwnt_generator_button_group"))
        self.mwnt_generator_button_group.addButton(self.mwnt_Ch_list_radio_button)
        self.verticalLayout.addWidget(self.mwnt_Ch_list_radio_button)
        self.mwnt_Ch_list_widget = QtGui.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.mwnt_Ch_list_widget.setFont(font)
        self.mwnt_Ch_list_widget.setObjectName(_fromUtf8("mwnt_Ch_list_widget"))
        self.verticalLayout.addWidget(self.mwnt_Ch_list_widget)
        self.add_Ch_push_button = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_Ch_push_button.setFont(font)
        self.add_Ch_push_button.setObjectName(_fromUtf8("add_Ch_push_button"))
        self.verticalLayout.addWidget(self.add_Ch_push_button)
        self.edit_selected_Ch_push_button = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.edit_selected_Ch_push_button.setFont(font)
        self.edit_selected_Ch_push_button.setObjectName(_fromUtf8("edit_selected_Ch_push_button"))
        self.verticalLayout.addWidget(self.edit_selected_Ch_push_button)
        self.remove_selected_Ch_push_button = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.remove_selected_Ch_push_button.setFont(font)
        self.remove_selected_Ch_push_button.setObjectName(_fromUtf8("remove_selected_Ch_push_button"))
        self.verticalLayout.addWidget(self.remove_selected_Ch_push_button)
        self.clear_Ch_list_push_button = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clear_Ch_list_push_button.setFont(font)
        self.clear_Ch_list_push_button.setObjectName(_fromUtf8("clear_Ch_list_push_button"))
        self.verticalLayout.addWidget(self.clear_Ch_list_push_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout.addWidget(self.line_4)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.mwnt_wall_parameters_radio_button = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.mwnt_wall_parameters_radio_button.setFont(font)
        self.mwnt_wall_parameters_radio_button.setObjectName(_fromUtf8("mwnt_wall_parameters_radio_button"))
        self.mwnt_generator_button_group.addButton(self.mwnt_wall_parameters_radio_button)
        self.verticalLayout_9.addWidget(self.mwnt_wall_parameters_radio_button)
        self.horizontalLayout_49 = QtGui.QHBoxLayout()
        self.horizontalLayout_49.setObjectName(_fromUtf8("horizontalLayout_49"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_48 = QtGui.QHBoxLayout()
        self.horizontalLayout_48.setObjectName(_fromUtf8("horizontalLayout_48"))
        self.horizontalLayout_47 = QtGui.QHBoxLayout()
        self.horizontalLayout_47.setObjectName(_fromUtf8("horizontalLayout_47"))
        self.label_24 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_47.addWidget(self.label_24)
        self.Nwalls_spin_box = QtGui.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.Nwalls_spin_box.setFont(font)
        self.Nwalls_spin_box.setMinimum(1)
        self.Nwalls_spin_box.setProperty("value", 3)
        self.Nwalls_spin_box.setObjectName(_fromUtf8("Nwalls_spin_box"))
        self.horizontalLayout_47.addWidget(self.Nwalls_spin_box)
        self.horizontalLayout_48.addLayout(self.horizontalLayout_47)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_48.addItem(spacerItem)
        self.verticalLayout_8.addLayout(self.horizontalLayout_48)
        self.horizontalLayout_43 = QtGui.QHBoxLayout()
        self.horizontalLayout_43.setObjectName(_fromUtf8("horizontalLayout_43"))
        self.horizontalLayout_44 = QtGui.QHBoxLayout()
        self.horizontalLayout_44.setObjectName(_fromUtf8("horizontalLayout_44"))
        self.label_25 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_44.addWidget(self.label_25)
        self.min_wall_diameter_double_spin_box = QtGui.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min_wall_diameter_double_spin_box.sizePolicy().hasHeightForWidth())
        self.min_wall_diameter_double_spin_box.setSizePolicy(sizePolicy)
        self.min_wall_diameter_double_spin_box.setMinimumSize(QtCore.QSize(100, 36))
        self.min_wall_diameter_double_spin_box.setMaximumSize(QtCore.QSize(100, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.min_wall_diameter_double_spin_box.setFont(font)
        self.min_wall_diameter_double_spin_box.setDecimals(1)
        self.min_wall_diameter_double_spin_box.setMinimum(0.0)
        self.min_wall_diameter_double_spin_box.setMaximum(1000.0)
        self.min_wall_diameter_double_spin_box.setProperty("value", 0.0)
        self.min_wall_diameter_double_spin_box.setObjectName(_fromUtf8("min_wall_diameter_double_spin_box"))
        self.horizontalLayout_44.addWidget(self.min_wall_diameter_double_spin_box)
        self.horizontalLayout_43.addLayout(self.horizontalLayout_44)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_43.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_43)
        self.horizontalLayout_40 = QtGui.QHBoxLayout()
        self.horizontalLayout_40.setObjectName(_fromUtf8("horizontalLayout_40"))
        self.horizontalLayout_41 = QtGui.QHBoxLayout()
        self.horizontalLayout_41.setObjectName(_fromUtf8("horizontalLayout_41"))
        self.label_23 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_41.addWidget(self.label_23)
        self.max_wall_diameter_double_spin_box = QtGui.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_wall_diameter_double_spin_box.sizePolicy().hasHeightForWidth())
        self.max_wall_diameter_double_spin_box.setSizePolicy(sizePolicy)
        self.max_wall_diameter_double_spin_box.setMinimumSize(QtCore.QSize(100, 36))
        self.max_wall_diameter_double_spin_box.setMaximumSize(QtCore.QSize(100, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.max_wall_diameter_double_spin_box.setFont(font)
        self.max_wall_diameter_double_spin_box.setDecimals(1)
        self.max_wall_diameter_double_spin_box.setMinimum(0.1)
        self.max_wall_diameter_double_spin_box.setMaximum(9999.9)
        self.max_wall_diameter_double_spin_box.setProperty("value", 100.0)
        self.max_wall_diameter_double_spin_box.setObjectName(_fromUtf8("max_wall_diameter_double_spin_box"))
        self.horizontalLayout_41.addWidget(self.max_wall_diameter_double_spin_box)
        self.horizontalLayout_40.addLayout(self.horizontalLayout_41)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_40)
        self.horizontalLayout_45 = QtGui.QHBoxLayout()
        self.horizontalLayout_45.setObjectName(_fromUtf8("horizontalLayout_45"))
        self.horizontalLayout_46 = QtGui.QHBoxLayout()
        self.horizontalLayout_46.setObjectName(_fromUtf8("horizontalLayout_46"))
        self.label_26 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout_46.addWidget(self.label_26)
        self.wall_spacing_double_spin_box = QtGui.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wall_spacing_double_spin_box.sizePolicy().hasHeightForWidth())
        self.wall_spacing_double_spin_box.setSizePolicy(sizePolicy)
        self.wall_spacing_double_spin_box.setMinimumSize(QtCore.QSize(100, 36))
        self.wall_spacing_double_spin_box.setMaximumSize(QtCore.QSize(100, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.wall_spacing_double_spin_box.setFont(font)
        self.wall_spacing_double_spin_box.setDecimals(2)
        self.wall_spacing_double_spin_box.setMinimum(0.1)
        self.wall_spacing_double_spin_box.setMaximum(100.0)
        self.wall_spacing_double_spin_box.setProperty("value", 3.35)
        self.wall_spacing_double_spin_box.setObjectName(_fromUtf8("wall_spacing_double_spin_box"))
        self.horizontalLayout_46.addWidget(self.wall_spacing_double_spin_box)
        self.horizontalLayout_45.addLayout(self.horizontalLayout_46)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_45.addItem(spacerItem3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_45)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.horizontalLayout_49.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_7.addWidget(self.label_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.random_wall_chiralities_radio_button = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.random_wall_chiralities_radio_button.setFont(font)
        self.random_wall_chiralities_radio_button.setChecked(True)
        self.random_wall_chiralities_radio_button.setObjectName(_fromUtf8("random_wall_chiralities_radio_button"))
        self.mwnts_wall_chiral_type_button_group = QtGui.QButtonGroup(MWNTGenerator)
        self.mwnts_wall_chiral_type_button_group.setObjectName(_fromUtf8("mwnts_wall_chiral_type_button_group"))
        self.mwnts_wall_chiral_type_button_group.addButton(self.random_wall_chiralities_radio_button)
        self.verticalLayout_6.addWidget(self.random_wall_chiralities_radio_button)
        self.armchair_wall_chiralities_radio_button = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.armchair_wall_chiralities_radio_button.setFont(font)
        self.armchair_wall_chiralities_radio_button.setObjectName(_fromUtf8("armchair_wall_chiralities_radio_button"))
        self.mwnts_wall_chiral_type_button_group.addButton(self.armchair_wall_chiralities_radio_button)
        self.verticalLayout_6.addWidget(self.armchair_wall_chiralities_radio_button)
        self.zigzag_wall_chiralities_radio_button = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.zigzag_wall_chiralities_radio_button.setFont(font)
        self.zigzag_wall_chiralities_radio_button.setObjectName(_fromUtf8("zigzag_wall_chiralities_radio_button"))
        self.mwnts_wall_chiral_type_button_group.addButton(self.zigzag_wall_chiralities_radio_button)
        self.verticalLayout_6.addWidget(self.zigzag_wall_chiralities_radio_button)
        self.achiral_wall_chiralities_radio_button = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.achiral_wall_chiralities_radio_button.setFont(font)
        self.achiral_wall_chiralities_radio_button.setObjectName(_fromUtf8("achiral_wall_chiralities_radio_button"))
        self.mwnts_wall_chiral_type_button_group.addButton(self.achiral_wall_chiralities_radio_button)
        self.verticalLayout_6.addWidget(self.achiral_wall_chiralities_radio_button)
        self.chiral_wall_chiralities_radio_button = QtGui.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.chiral_wall_chiralities_radio_button.setFont(font)
        self.chiral_wall_chiralities_radio_button.setObjectName(_fromUtf8("chiral_wall_chiralities_radio_button"))
        self.mwnts_wall_chiral_type_button_group.addButton(self.chiral_wall_chiralities_radio_button)
        self.verticalLayout_6.addWidget(self.chiral_wall_chiralities_radio_button)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.horizontalLayout_49.addLayout(self.verticalLayout_7)
        self.verticalLayout_9.addLayout(self.horizontalLayout_49)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.verticalLayout_20 = QtGui.QVBoxLayout()
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.horizontalLayout_34 = QtGui.QHBoxLayout()
        self.horizontalLayout_34.setObjectName(_fromUtf8("horizontalLayout_34"))
        self.horizontalLayout_36 = QtGui.QHBoxLayout()
        self.horizontalLayout_36.setObjectName(_fromUtf8("horizontalLayout_36"))
        self.label_20 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_36.addWidget(self.label_20)
        self.mwnt_Lz_double_spin_box = QtGui.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mwnt_Lz_double_spin_box.sizePolicy().hasHeightForWidth())
        self.mwnt_Lz_double_spin_box.setSizePolicy(sizePolicy)
        self.mwnt_Lz_double_spin_box.setMinimumSize(QtCore.QSize(150, 36))
        self.mwnt_Lz_double_spin_box.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.mwnt_Lz_double_spin_box.setFont(font)
        self.mwnt_Lz_double_spin_box.setDecimals(4)
        self.mwnt_Lz_double_spin_box.setMinimum(0.1)
        self.mwnt_Lz_double_spin_box.setMaximum(100.0)
        self.mwnt_Lz_double_spin_box.setProperty("value", 1.0)
        self.mwnt_Lz_double_spin_box.setObjectName(_fromUtf8("mwnt_Lz_double_spin_box"))
        self.horizontalLayout_36.addWidget(self.mwnt_Lz_double_spin_box)
        self.horizontalLayout_34.addLayout(self.horizontalLayout_36)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem6)
        self.verticalLayout_20.addLayout(self.horizontalLayout_34)
        self.bundle_generator_check_box = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.bundle_generator_check_box.setFont(font)
        self.bundle_generator_check_box.setCheckable(True)
        self.bundle_generator_check_box.setObjectName(_fromUtf8("bundle_generator_check_box"))
        self.verticalLayout_20.addWidget(self.bundle_generator_check_box)
        self.verticalLayout_19 = QtGui.QVBoxLayout()
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.horizontalLayout_27 = QtGui.QHBoxLayout()
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        self.horizontalLayout_32 = QtGui.QHBoxLayout()
        self.horizontalLayout_32.setObjectName(_fromUtf8("horizontalLayout_32"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_32.addWidget(self.label_8)
        self.bundle_nx_spin_box = QtGui.QSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bundle_nx_spin_box.sizePolicy().hasHeightForWidth())
        self.bundle_nx_spin_box.setSizePolicy(sizePolicy)
        self.bundle_nx_spin_box.setMinimumSize(QtCore.QSize(60, 36))
        self.bundle_nx_spin_box.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.bundle_nx_spin_box.setFont(font)
        self.bundle_nx_spin_box.setReadOnly(True)
        self.bundle_nx_spin_box.setMinimum(1)
        self.bundle_nx_spin_box.setObjectName(_fromUtf8("bundle_nx_spin_box"))
        self.horizontalLayout_32.addWidget(self.bundle_nx_spin_box)
        self.horizontalLayout_27.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_33 = QtGui.QHBoxLayout()
        self.horizontalLayout_33.setObjectName(_fromUtf8("horizontalLayout_33"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_33.addWidget(self.label_16)
        self.bundle_Lx_line_edit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bundle_Lx_line_edit.sizePolicy().hasHeightForWidth())
        self.bundle_Lx_line_edit.setSizePolicy(sizePolicy)
        self.bundle_Lx_line_edit.setMinimumSize(QtCore.QSize(125, 36))
        self.bundle_Lx_line_edit.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.bundle_Lx_line_edit.setFont(font)
        self.bundle_Lx_line_edit.setReadOnly(True)
        self.bundle_Lx_line_edit.setObjectName(_fromUtf8("bundle_Lx_line_edit"))
        self.horizontalLayout_33.addWidget(self.bundle_Lx_line_edit)
        self.horizontalLayout_27.addLayout(self.horizontalLayout_33)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem7)
        self.verticalLayout_19.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_37 = QtGui.QHBoxLayout()
        self.horizontalLayout_37.setObjectName(_fromUtf8("horizontalLayout_37"))
        self.horizontalLayout_38 = QtGui.QHBoxLayout()
        self.horizontalLayout_38.setObjectName(_fromUtf8("horizontalLayout_38"))
        self.label_21 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_38.addWidget(self.label_21)
        self.bundle_ny_spin_box = QtGui.QSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bundle_ny_spin_box.sizePolicy().hasHeightForWidth())
        self.bundle_ny_spin_box.setSizePolicy(sizePolicy)
        self.bundle_ny_spin_box.setMinimumSize(QtCore.QSize(60, 36))
        self.bundle_ny_spin_box.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.bundle_ny_spin_box.setFont(font)
        self.bundle_ny_spin_box.setReadOnly(True)
        self.bundle_ny_spin_box.setMinimum(1)
        self.bundle_ny_spin_box.setObjectName(_fromUtf8("bundle_ny_spin_box"))
        self.horizontalLayout_38.addWidget(self.bundle_ny_spin_box)
        self.horizontalLayout_37.addLayout(self.horizontalLayout_38)
        self.horizontalLayout_39 = QtGui.QHBoxLayout()
        self.horizontalLayout_39.setObjectName(_fromUtf8("horizontalLayout_39"))
        self.label_22 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_39.addWidget(self.label_22)
        self.bundle_Ly_line_edit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bundle_Ly_line_edit.sizePolicy().hasHeightForWidth())
        self.bundle_Ly_line_edit.setSizePolicy(sizePolicy)
        self.bundle_Ly_line_edit.setMinimumSize(QtCore.QSize(125, 36))
        self.bundle_Ly_line_edit.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.bundle_Ly_line_edit.setFont(font)
        self.bundle_Ly_line_edit.setReadOnly(True)
        self.bundle_Ly_line_edit.setObjectName(_fromUtf8("bundle_Ly_line_edit"))
        self.horizontalLayout_39.addWidget(self.bundle_Ly_line_edit)
        self.horizontalLayout_37.addLayout(self.horizontalLayout_39)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem8)
        self.verticalLayout_19.addLayout(self.horizontalLayout_37)
        self.verticalLayout_20.addLayout(self.verticalLayout_19)
        self.horizontalLayout_12.addLayout(self.verticalLayout_20)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.verticalLayout_2.addWidget(self.line_8)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_31 = QtGui.QHBoxLayout()
        self.horizontalLayout_31.setObjectName(_fromUtf8("horizontalLayout_31"))
        self.horizontalLayout_30 = QtGui.QHBoxLayout()
        self.horizontalLayout_30.setObjectName(_fromUtf8("horizontalLayout_30"))
        self.horizontalLayout_29 = QtGui.QHBoxLayout()
        self.horizontalLayout_29.setObjectName(_fromUtf8("horizontalLayout_29"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_29.addWidget(self.label_17)
        self.element1_combo_box = QtGui.QComboBox(self.centralwidget)
        self.element1_combo_box.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.element1_combo_box.setFont(font)
        self.element1_combo_box.setObjectName(_fromUtf8("element1_combo_box"))
        self.element1_combo_box.addItem(_fromUtf8(""))
        self.element1_combo_box.addItem(_fromUtf8(""))
        self.element1_combo_box.addItem(_fromUtf8(""))
        self.element1_combo_box.addItem(_fromUtf8(""))
        self.element1_combo_box.addItem(_fromUtf8(""))
        self.horizontalLayout_29.addWidget(self.element1_combo_box)
        self.horizontalLayout_30.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_28 = QtGui.QHBoxLayout()
        self.horizontalLayout_28.setObjectName(_fromUtf8("horizontalLayout_28"))
        self.label_18 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_28.addWidget(self.label_18)
        self.element2_combo_box = QtGui.QComboBox(self.centralwidget)
        self.element2_combo_box.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.element2_combo_box.setFont(font)
        self.element2_combo_box.setObjectName(_fromUtf8("element2_combo_box"))
        self.element2_combo_box.addItem(_fromUtf8(""))
        self.element2_combo_box.addItem(_fromUtf8(""))
        self.element2_combo_box.addItem(_fromUtf8(""))
        self.element2_combo_box.addItem(_fromUtf8(""))
        self.element2_combo_box.addItem(_fromUtf8(""))
        self.horizontalLayout_28.addWidget(self.element2_combo_box)
        self.horizontalLayout_30.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_31.addLayout(self.horizontalLayout_30)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem10)
        self.verticalLayout_5.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.elements_bond_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.elements_bond_label.setFont(font)
        self.elements_bond_label.setObjectName(_fromUtf8("elements_bond_label"))
        self.horizontalLayout_14.addWidget(self.elements_bond_label)
        self.bond_double_spin_box = QtGui.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bond_double_spin_box.sizePolicy().hasHeightForWidth())
        self.bond_double_spin_box.setSizePolicy(sizePolicy)
        self.bond_double_spin_box.setMinimumSize(QtCore.QSize(150, 36))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        self.bond_double_spin_box.setFont(font)
        self.bond_double_spin_box.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.bond_double_spin_box.setReadOnly(False)
        self.bond_double_spin_box.setDecimals(3)
        self.bond_double_spin_box.setMinimum(0.5)
        self.bond_double_spin_box.setMaximum(10.0)
        self.bond_double_spin_box.setSingleStep(0.01)
        self.bond_double_spin_box.setProperty("value", 1.42)
        self.bond_double_spin_box.setObjectName(_fromUtf8("bond_double_spin_box"))
        self.horizontalLayout_14.addWidget(self.bond_double_spin_box)
        self.horizontalLayout_24.addLayout(self.horizontalLayout_14)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_24)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        spacerItem12 = QtGui.QSpacerItem(20, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem12)
        MWNTGenerator.setCentralWidget(self.centralwidget)

        self.retranslateUi(MWNTGenerator)
        self.element1_combo_box.setCurrentIndex(3)
        self.element2_combo_box.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MWNTGenerator)

    def retranslateUi(self, MWNTGenerator):
        MWNTGenerator.setWindowTitle(_translate("MWNTGenerator", "MWNT Generator", None))
        self.label_19.setText(_translate("MWNTGenerator", "Generate from...", None))
        self.mwnt_Ch_list_radio_button.setText(_translate("MWNTGenerator", "(n, m) List", None))
        self.add_Ch_push_button.setText(_translate("MWNTGenerator", "Add (n, m)", None))
        self.edit_selected_Ch_push_button.setText(_translate("MWNTGenerator", "Edit Selected", None))
        self.remove_selected_Ch_push_button.setText(_translate("MWNTGenerator", "Remove Selected", None))
        self.clear_Ch_list_push_button.setText(_translate("MWNTGenerator", "Clear List", None))
        self.mwnt_wall_parameters_radio_button.setText(_translate("MWNTGenerator", "Wall Parameters", None))
        self.label_24.setText(_translate("MWNTGenerator", "<html><head/><body><p><span style=\" font-style:italic;\">N</span><span style=\" vertical-align:sub;\">walls </span>= </p></body></html>", None))
        self.label_25.setText(_translate("MWNTGenerator", "<html><head/><body><p>Wall <span style=\" font-style:italic;\">d</span><span style=\" vertical-align:sub;\">t,min </span>= </p></body></html>", None))
        self.min_wall_diameter_double_spin_box.setSuffix(_translate("MWNTGenerator", " Å", None))
        self.label_23.setText(_translate("MWNTGenerator", "<html><head/><body><p>Wall <span style=\" font-style:italic;\">d</span><span style=\" vertical-align:sub;\">t,max </span>= </p></body></html>", None))
        self.max_wall_diameter_double_spin_box.setSuffix(_translate("MWNTGenerator", " Å", None))
        self.label_26.setText(_translate("MWNTGenerator", "<html><head/><body><p>Wall <span style=\" font-family:\'Open Sans,Helvetica Neue,Helvetica,Arial,sans-serif\'; font-size:14px; color:#333333; background-color:#f9f9f9;\">Δ</span><span style=\" font-style:italic;\">d</span><span style=\" vertical-align:sub;\">t,min </span>= </p></body></html>", None))
        self.wall_spacing_double_spin_box.setSuffix(_translate("MWNTGenerator", " Å", None))
        self.label_5.setText(_translate("MWNTGenerator", "Chiralities", None))
        self.random_wall_chiralities_radio_button.setText(_translate("MWNTGenerator", "Random", None))
        self.armchair_wall_chiralities_radio_button.setText(_translate("MWNTGenerator", "Armchair", None))
        self.zigzag_wall_chiralities_radio_button.setText(_translate("MWNTGenerator", "Zigzag", None))
        self.achiral_wall_chiralities_radio_button.setText(_translate("MWNTGenerator", "Achiral", None))
        self.chiral_wall_chiralities_radio_button.setText(_translate("MWNTGenerator", "Chiral", None))
        self.label_20.setText(_translate("MWNTGenerator", "<html><head/><body><p><span style=\" font-style:italic;\">L</span><span style=\" vertical-align:sub;\">z </span>= </p></body></html>", None))
        self.mwnt_Lz_double_spin_box.setSuffix(_translate("MWNTGenerator", " nm", None))
        self.bundle_generator_check_box.setText(_translate("MWNTGenerator", "Bundle Generator", None))
        self.label_8.setText(_translate("MWNTGenerator", "<html><head/><body><p><span style=\" font-style:italic;\">n</span><span style=\" vertical-align:sub;\">x </span>=</p></body></html>", None))
        self.label_16.setText(_translate("MWNTGenerator", "<html><head/><body><p><span style=\" font-style:italic;\">L</span><span style=\" vertical-align:sub;\">x </span>= </p></body></html>", None))
        self.label_21.setText(_translate("MWNTGenerator", "<html><head/><body><p><span style=\" font-style:italic;\">n</span><span style=\" vertical-align:sub;\">y </span>=</p></body></html>", None))
        self.label_22.setText(_translate("MWNTGenerator", "<html><head/><body><p><span style=\" font-style:italic;\">L</span><span style=\" vertical-align:sub;\">y </span>= </p></body></html>", None))
        self.label_17.setText(_translate("MWNTGenerator", "Element 1:", None))
        self.element1_combo_box.setItemText(0, _translate("MWNTGenerator", "H", None))
        self.element1_combo_box.setItemText(1, _translate("MWNTGenerator", "He", None))
        self.element1_combo_box.setItemText(2, _translate("MWNTGenerator", "B", None))
        self.element1_combo_box.setItemText(3, _translate("MWNTGenerator", "C", None))
        self.element1_combo_box.setItemText(4, _translate("MWNTGenerator", "N", None))
        self.label_18.setText(_translate("MWNTGenerator", "Element 2:", None))
        self.element2_combo_box.setItemText(0, _translate("MWNTGenerator", "H", None))
        self.element2_combo_box.setItemText(1, _translate("MWNTGenerator", "He", None))
        self.element2_combo_box.setItemText(2, _translate("MWNTGenerator", "B", None))
        self.element2_combo_box.setItemText(3, _translate("MWNTGenerator", "C", None))
        self.element2_combo_box.setItemText(4, _translate("MWNTGenerator", "N", None))
        self.elements_bond_label.setText(_translate("MWNTGenerator", "<html><head/><body><p>C-C bond =</p></body></html>", None))
        self.bond_double_spin_box.setSuffix(_translate("MWNTGenerator", " Å", None))

