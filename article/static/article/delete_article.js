function deleteItem(id) {
    bootbox.confirm("Are you sure?", function(result) {
        if (result) {
            document.location.href = "/articles/delete/article/" + id + "/";
        }
    });
};