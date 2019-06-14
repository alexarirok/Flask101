$ (function () {
    $ ("#btnsignUp").click(function()) {
        $ .ajax({
            url: "/signUp",
            data:  $("form").realize() 
            type: "POST",
            sucess: function(response) {
                console.log(response);
            }, 
            error: function(error) {
                console.log(error);
            }
        });
    });
});