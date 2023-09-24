$(document).ready(function () {
    function updateFilters() {
        var param = new URLSearchParams(window.location.search);
        var params = {};

        param.forEach(function (val, key) {
            params[key] = val;
        });

        var activeCategory = null; 
        var activeTags = [];

        $(".post-category-element.active").each(function () {
            activeCategory = $(this).data('param-value');
        });

        var selectedTag = $(".post-tags-element.active").data('param-value');
        if (selectedTag) {
            params['tag'] = selectedTag;
        } else {
            delete params['tag'];
        }

        if (activeCategory !== null) {
            params['category'] = activeCategory;
        } else {
            delete params['category'];
        }

        var searchInput = $('#search-input').val();
        if (searchInput) {
            params['search'] = searchInput;
        } else {
            delete params['search'];
        }

        var queryString = Object.keys(params)
            .map(function (key) {
                return key + '=' + params[key];
            })
            .join('&');

        $.ajax({
            type: "GET",
            url: window.location.pathname + '?' + queryString,
            success: function (data) {
                $("#featured-posts-column-container").html(data.html);
                history.pushState(null, '', window.location.pathname + '?' + queryString);
            },
        });
    }

    // Handle the click event for clearing filters
    $(document).on('click', '#clearUrl, #clearUrl2', function (e) {
        e.preventDefault();

        $(".post-category-element.active").removeClass('active');
        $(".post-tags-element.active").removeClass('active');
        $('#search-input').val('');
        updateFilters(); 
    });

    // Handle the click event for category buttons
    $(".post-category-element").on('click', function () {
        var isActive = $(this).hasClass('active');
        
        $(".post-category-element").removeClass('active');

        if (!isActive) {
            $(this).addClass('active');
        }

        updateFilters(); 
    });

    // Handle the click event for tag buttons
    $(".post-tags-element").on('click', function () {
        var isActive = $(this).hasClass('active');

        if (!isActive) {
            $(".post-tags-element").removeClass('active');
            $(this).addClass('active');
        } else {
            $(this).removeClass('active');
        }

        updateFilters(); 
    });

    $('#search-input').on('input', function () {
        updateFilters(); 
    });

    $("#blog-form").on('submit', function (e) {
        e.preventDefault(); 
        updateFilters(); 
    });

    updateFilters();
});
