window.addEventListener("load", () => {
    (($) => {
        const join_btns = $(".join-team-btn")

        join_btns.on("click", (event) => {
            event.preventDefault();
            const btnObject = event.target
            const teamName = btnObject.dataset.teamname
            const teamId = btnObject.dataset.teamid

            const agreement = confirm('Do you want to join the "' + teamName + '" ?')

            if (agreement) {
                $.ajax({
                    url : '/srv/team/join/' + teamId + '/',
                    type : 'GET',
                    success : () => {
                        // Show success message.
//                        location.reload();
                    },

                })
            }
        })
    })(django.jQuery)
});