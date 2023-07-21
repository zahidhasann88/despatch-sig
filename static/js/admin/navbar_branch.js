document.write(`
    <!--nav class="navbar navbar-expand-lg  fixed-top"-->
    <nav class="navbar navbar-expand-lg fixed-top" style="background-color: #0eb6e9"> 
        <a class="navbar-brand" href="/admin/home">
            <i class="fa fa-home" aria-hidden="true" style="padding-right: 5px;"></i>Home Page
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ml-auto">

                <li class="nav-item">
                    <a class="nav-link active" href="/admin/home">
                        <i class="fa fa-list" aria-hidden="true" style="padding-right: 5px; font-weight: bold"></i>All Users
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/admin/exercises">
                        <i class="fa fa-list" aria-hidden="true" style="padding-right: 5px;"></i>Exercises
                    </a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="/admin/courses">
                            <i class="fa fa-plus-circle" aria-hidden="true" style="padding-right: 5px;"></i>Courses
                        </a>
                </li>

              <li class="nav-item">
                    <a class="nav-link" href="update_admin_password_form">
                    <i class="fa fa-edit" aria-hidden="true" style="padding-right: 5px;"></i>Update Password</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/auth/logout">
                        <i class="fa fa-sign-out" aria-hidden="true" style="padding-right: 5px;"></i>Logout
                    </a>
                </li>
            </ul>
        </div>
    </nav>`
);
