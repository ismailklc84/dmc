import dash_mantine_components as dmc
from dash import Output, Input, clientside_callback, html, dcc, page_container, State
from dash import Dash
from dash_iconify import DashIconify
import dash

app = Dash(
    __name__,
    external_stylesheets=[
        # include google fonts
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ],
)

def get_icon(icon):
    return DashIconify(icon=icon, height=16, color="#c2c7d0")


def create_home_link(label):
    return dmc.Anchor(
        label,
        size="xl",
        href="/",
        underline=False,
    )

def create_header_link(icon, href, size=22, color="indigo"):
    return dmc.Anchor(
        dmc.ThemeIcon(
            DashIconify(
                icon=icon,
                width=size,
            ),
            variant="outline",
            radius=30,
            size=36,
            color=color,
        ),
        href=href,
        target="_blank",
    )
    
app.layout =  dmc.MantineProvider(
    [
    dmc.Header(
        height=70,
        fixed=True,
        px=15,
        children=[
            dcc.Store(id="theme-store", storage_type="local"),
            dmc.Stack(
                justify="center",
                style={"height": 70},
                children=dmc.Grid(
                    children=[
                        dmc.Col(
                            [   dmc.Group([
                             dmc.MediaQuery(
                                        dmc.ActionIcon(
                                            DashIconify(
                                                icon="radix-icons:hamburger-menu",
                                                width=18,
                                            ),
                                            id="drawer-hamburger-button2",
                                            variant="outline",
                                            size=36,
                                        ),
                                        smallerThan="lg",
                                        styles={"display": "none"},
                                    ),
                                dmc.MediaQuery(
                                    create_home_link("Başlık"),
                                    smallerThan="lg",
                                    styles={"display": "none"},
                                ),
                                dmc.MediaQuery(
                                    create_home_link("BAŞ"),
                                    largerThan="lg",
                                    styles={"display": "none"},
                                ),
                                ])
                            ],
                            span="auto",
                            pt=12,pl=0
                        ),
                        dmc.Col(
                            [
                                dmc.Center(
                                    dmc.Select(
                                            id="select-component1",
                                            style={"width": 500},
                                            placeholder="Search")
                                )
                            ],
                            span=6,
                            )
                        ,
                        dmc.Col(
                            span="auto",
                            children=dmc.Group(
                                position="right",
                                spacing="xl",
                                children=[
                                    # dmc.MediaQuery(
                                    #     dmc.Select(
                                    #         id="select-component",
                                    #         style={"width": 250},
                                    #         placeholder="Search",
                                    #         nothingFound="No match found",
                                    #         searchable=True,
                                    #         clearable=True,
                                    #         # data=[
                                    #         #     {
                                    #         #         "label": component["name"],
                                    #         #         "value": component["path"],
                                    #         #     }
                                    #         #     for component in nav_data
                                    #         #     if component["name"]
                                    #         #     not in ["Home", "Not found 404"]
                                    #         # ],
                                    #         icon=DashIconify(
                                    #             icon="radix-icons:magnifying-glass"
                                    #         ),
                                    #     ),
                                    #     smallerThan="md",
                                    #     styles={"display": "none"},
                                    # ),
                                    create_header_link(
                                        "radix-icons:github-logo",
                                        "https://github.com/snehilvj/dash-mantine-components",
                                    ),
                                    create_header_link(
                                        "bi:discord", "https://discord.gg/KuJkh4Pyq5"
                                    ),
                                    dmc.ActionIcon(
                                        DashIconify(
                                            icon="gg:dark-mode", width=22
                                        ),
                                        variant="outline",
                                        radius=30,
                                        size=36,
                                        #color="yellow",
                                        id="color-scheme-toggle",
                                    ),
                                    dmc.MediaQuery(
                                        dmc.ActionIcon(
                                            DashIconify(
                                                icon="radix-icons:hamburger-menu",
                                                width=18,
                                            ),
                                            id="drawer-hamburger-button",
                                            variant="outline",
                                            size=36,
                                        ),
                                        largerThan="lg",
                                        styles={"display": "none"},
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            )
        ],
    ),
    dmc.Navbar(
        fixed=True,
        id="components-navbar",
        position={"top": 70},
        width={"base": 300},
        children=[
                html.Div(
                            [
                                dmc.NavLink(
                                    label="Clustering",
                                    icon=get_icon(icon="carbon:assembly-cluster"),
                                    childrenOffset=35,
                                    opened=True,
                                    children=[
                                        dmc.NavLink(label="KMean",
                                                    href='/kmean',
                                                    id='kmean-navbar',
                                                    icon=get_icon(icon='carbon:edge-cluster')
                                        ),
                                        dmc.NavLink(label="DBScan",
                                                    href='/dbscan',
                                                    id='dbscan-navbar', 
                                                    icon=get_icon(icon='carbon:edge-cluster')
                                        ),
                                        dmc.NavLink(label="Hierarchical",
                                                    href='/hierarchical',
                                                    icon=get_icon(icon='carbon:edge-cluster')
                                        ),
                                    ],
                                ),
                                dmc.NavLink(
                                    label="Impact Analysis",
                                    icon=get_icon(icon="carbon:assembly-cluster"),
                                    childrenOffset=35,
                                    opened=True,
                                    children=[
                                        dmc.NavLink(label="Job Connections",
                                                    href='/job_connections',
                                                    id='job-connections',
                                                    icon=get_icon(icon='carbon:edge-cluster')
                                        ),
                                        dmc.NavLink(label="Table Search",
                                                    href='/ResponsiveNavbar',
                                                    id='table-search', 
                                                    icon=get_icon(icon='carbon:edge-cluster')
                                        ),
                                    ],
                                ),
                                dmc.NavLink(
                                    label="Report Analysis",
                                    icon=get_icon(icon="carbon:assembly-cluster"),
                                    childrenOffset=35,
                                    opened=True,
                                ),
                                                    ],
                            style={'white-space': 'nowrap'},
                        ),
            dmc.ScrollArea(
                offsetScrollbars=True,
                type="scroll",
                #children=create_side_nav_content(nav_data),
            )
        ],
        style={'overflow':'hidden', 'transition': 'width 0.5s ease-in-out', 'backgroundColor':''}
    ),
    html.Div(
        dmc.Container(size="lg", pt=90, children=page_container),
                            id="wrapper",
                        ),

    ],
        theme={"colorScheme": "light"},
        id="mantine-docs-theme-provider",
        withGlobalStyles=True,
        withNormalizeCSS=True,
)

clientside_callback(
    """ function(data) { return data } """,
    Output("mantine-docs-theme-provider", "theme"),
    Input("theme-store", "data"),
)

clientside_callback(
    """
    function handle_click_sidebar_width(n_clicks, width){
      const current_width = parseInt(width.base)
      console.log(current_width)
      if (n_clicks > 0 & current_width == 300) {
       return {base: 40};
      } else {
        return {base:300};
      }
    }
    """,
    Output("components-navbar", "width"),
    Input("drawer-hamburger-button2", "n_clicks"),
    State('components-navbar','width')
)

clientside_callback(
    """function(n_clicks, data) {
        if (data) {
            if (n_clicks) {
                const scheme = data["colorScheme"] == "dark" ? "light" : "dark"
                return { colorScheme: scheme } 
            }
            return dash_clientside.no_update
        } else {
            return { colorScheme: "light" }
        }
    }""",
    Output("theme-store", "data"),
    Input("color-scheme-toggle", "n_clicks"),
    State("theme-store", "data"),
)

# noinspection PyProtectedMember
clientside_callback(
    """
    function(children) { 
        ethicalads.load();
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return null
    }
    """,
    Output("select-component", "value"),
    Input("_pages_content", "children"),
)

clientside_callback(
    """
    function(value) {
        if (value) {
            return value
        }
    }
    """,
    Output("url", "pathname"),
    Input("select-component", "value"),
)

clientside_callback(
    """function(n_clicks) { return true }""",
    Output("components-navbar-drawer", "opened"),
    Input("drawer-hamburger-button", "n_clicks"),
    prevent_initial_call=True,
)

if __name__ == "__main__":
    app.run_server()
