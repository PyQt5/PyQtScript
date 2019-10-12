//! [0]
listWidget.addItem("Red");
listWidget.addItem("Blue");
listWidget.addItem("Green");
listWidget.addItem("Cyan");
listWidget.addItem("Yellow");
listWidget.addItem("Purple");
listWidget.addItems(["Orange", "Gray"]);
//! [0]

//! [1]
listWidget.currentRowChanged.connect(
    function(row)
    {
        listWidget.setBackgroundColor(row);
    }
);
//! [1]
