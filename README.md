# Python GUI demos

## Introduction

There are many Python GUI frameworks. The idea of this repository is comparing
them.

There's a summary in this page and demo apps for each framework so you can
compare yourself.

## Summary

In the README file for each framework in the [demos](demos) directory you can learn more about it and see screenshots.

| Framework | Short description | Pros | Cons | Platforms[*](#platforms) |
|-----------|-------------------|------|------|--------------------------|
| [Tkinter](https://docs.python.org/3/library/tkinter.html) | Original Python GUI framework | - Included with Python<br>- Multiplatform | - Old school look and feel<br>- Non mobile friendly | w/l/m/-/-/- |
| [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)  | Modern version of Tkinter | - Compatible with Tkinter | - Modern looking<br>- Non mobile friendly | w/l/m/-/-/- |
| [ttkbootstrap](https://ttkbootstrap.readthedocs.io/)  | Tkinter with a bootstrap theme | - Compatible with Tkinter | - Modern looking<br>- Non mobile friendly | w/l/m/-/-/- |
| [pyQt](https://riverbankcomputing.com/software/pyqt/)/[pySide](https://wiki.qt.io/Qt_for_Python) | Wrappers around Qt for python. pyQt is GPL and pySide LGPL | - Well stablished<br>- Many tutorials<br>- Full library, not only GUI components | - Old school look and feel | w/l/m/-/-/- |
| [pyQt with QML](https://doc.qt.io/qtforpython/tutorials/qmlapp/qmlapplication.html)/[pySide with QML](https://wiki.qt.io/Qt_Quick) | Qt using QML | - More modern looking than traditional pyQt/pySide | - Less tutorials than traditional pyQt/pySide | w/l/m/-/-/- |
| [Kivy](https://kivy.org/) | Cross-platform GUI apps | - Mobile friendly | | w/l/m/-/i/a |
| [KivyMD](https://kivymd.readthedocs.io/) | Kivy with Google's Material Design widgets | - Modern looking | |w/l/m/-/i/a |
| [Flet](https://flet.dev/) | Flutter applications in Python | - Modern looking | - Early stages<br>- Not mobile ready yet | w/l/m/w/-/- |
| [Dash](https://plotly.com/dash/) | For dashboards | | |  -/-/-/w/-/- |
| [Streamlit](https://streamlit.io/) | For dashboards | | |  -/-/-/w/-/- |
| [PySimpleGUI](https://www.pysimplegui.org/) | Simple way of creating Python GUI applications. It's a wrapper around Tkinter, Qt, Remi or WxPython | - Simple | - Simple<br>- Old school look and feel | w/l/m/w/-/- |
| [wxPython](https://www.wxpython.org/) | Use native widgets on Windows, Macs and Linux | | | w/l/m/-/-/- |
| [PyGObject](https://pygobject.readthedocs.io/) | Bindings for GObject based libraries | | | w/l/m/-/-/- |
| [Remi](https://github.com/rawpython/remi) | GUI library for Python applications that gets rendered in web browsers | | | -/-/-/w/-/- |
| [Dear PyGui](https://dearpygui.readthedocs.io/) | GPU accelerated GUI apps | | | w/l/m/-/-/- |
| [Toga](https://toga.readthedocs.io/) | Python native, OS native, cross platform GUI toolkit, part of BeeWare | | | w/l/m/w/i/a |
| [Eel](https://github.com/python-eel/Eel) | Simple Electron-like offline HTML/JS GUI apps | - Probably not suitable for making full blown applications | | w/l/m/w/-/- |
| [Flexx](https://github.com/flexxui/flexx) | Python GUIs using web technology for rendering | | | w/l/m/w/-/- |
| [libavg](https://www.libavg.de/) | For media-centric applications | | - Last release in Apr 2021| w/l/m/-/-/- |

<a name="platforms"></a>\* Notation for platforms:

| Letter | Platform |
|--------|----------|
| w      | Windows  |
| l      | Linux    |
| m      | MacOS    |
| w      | Web      |
| i      | iOS      |
| a      | Android  |

## Console to GUI

There are some libraries that turn console programs into GUI applications. They
are not general purpose GUI frameworks, so they are out of the scope of this
project. However, for the sake of completeness, here you can find a little
comparison:

| Framework | Description | Pros | Cons |
|-----------|-------------|------|------|
| [Gooey](https://github.com/chriskiehl/Gooey) | Turn console programs into a GUI application | | |
| [Wooey](https://github.com/wooey/Wooey) | Turn console programs into a GUI application| | |
| [click-web](https://github.com/fredrik-corneliusson/click-web) | Turn click programs into a GUI applications | | |

## No longer updated

These frameworks seem to be no longer updated.

| Framework | Description | Pros | Cons |
|-----------|-------------|------|------|
| [PyForms](http://pyforms.readthedocs.io/) | For desktop, terminal and web | | - Last release in 2019 | w/l/m/w/-/- |
| [PyGUI](https://www.csse.canterbury.ac.nz/greg.ewing/python_gui/) | Cross-platform pythonic GUI API | | - Last release in 2017 |
| [Wax](https://wiki.python.org/moin/Wax) | Wrapper for wxPython | - Easier to use than wxPython | - Last release in 2006 |

## Contributing

Contributions are welcomed. Please, send pull requests. Try to follow the
conventions in the available examples. Format Python code with
[black](https://github.com/psf/black).
