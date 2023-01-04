# REST consumer

This directory shows how to create and build an application that consumes a REST
service and shows the results in a list. Qt uses a [MVC (Model View Controller)
design
pattern](https://doc.qt.io/qtforpython/overviews/model-view-programming.html).

Notice that we need a thread to update the progress bar without halting the GUI
thread. This has been done with QThread. However, if using a real REST API,
probably the best option is using
[QNetworkAccessManager](https://doc.qt.io/qtforpython/PySide6/QtNetwork/QNetworkAccessManager.html),
which has a mechanism for updating the progress.

Install PySide with:

```bash
pip install pyside6
```

Run the application as a desktop app with:

```bash
python simple_form.py
```
