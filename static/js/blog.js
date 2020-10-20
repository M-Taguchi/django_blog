<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.12.3/jquery.min.js"></script>
<script type="text/javascript">
(function($) {
    $(function () {
        $('#nav-toggle,#overlay').on('click', function() {
            $('body').toggleClass('open');
        });
        $('.scroll').perfectScrollbar();
    });
})(jQuery);
</script>