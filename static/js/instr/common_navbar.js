document.write(`
    <!--nav class="navbar navbar-expand-lg  fixed-top"-->
    <nav class="navbar navbar-expand-lg fixed-top" style="background-color: #0eb6e9"> 
        <a class="navbar-brand" href="/instr/home">
            <i class="fa fa-home" aria-hidden="true" style="padding-right: 5px;"></i>Home Page
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ml-auto">

                <li class="nav-item">
                    <a class="nav-link active" href="/instr/expaper">
                        <i class="fa fa-file-text" aria-hidden="true" style="padding-right: 5px; font-weight: bold"></i>Exercise Paper
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/instr/Syndicates">
                        <i class="fa fa-users" aria-hidden="true" style="padding-right: 5px;"></i>Syndicates
                    </a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="/instr/despatches">
                            <i class="fa fa-plus-circle" aria-hidden="true" style="padding-right: 5px;"></i>Despatches
                        </a>
                </li>
                
                <li class="nav-item">
                    <a class="nav-link" href="/instr/msgs">
                            <i class="fa fa-plus-circle" aria-hidden="true" style="padding-right: 5px;"></i>Msg
                        </a>
                </li>
                
                <li class="nav-item">
                    <a class="nav-link" href="/instr/submissions">
                            <i class="fa fa-plus-circle" aria-hidden="true" style="padding-right: 5px;"></i>Submissions
                        </a>
                </li>

              <li class="nav-item">
                    <a class="nav-link" href="update_instr_password_form">
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
