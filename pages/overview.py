  
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_fund_facts = pd.read_csv(DATA_PATH.joinpath("df_fund_facts.csv"))
df_price_perf = pd.read_csv(DATA_PATH.joinpath("df_price_perf.csv"))
#df_price_perf = df_price_perf.sort_values(by=["Year"])

def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Kim's Corner"),
                                    html.Br([]),
                                    html.P(
                                        "It’s hard to believe it’s already the beginning of March. I hope you and your families are healthy and staying warm.  Remember to Spring forward for Daylight Savings Time on March 14th.  Have you ever thought about the Purpose of our team and how we enable Lumen’s overall Purpose? Have you given much thought to how our team Makes Amazing Happen?  By now, you all should have your 2021 goals created and reviewed with your Supervisor. You should see the daily results of your contributions and understand the impact we, each one of us, have on our customers. We are the Quarterbacks of this team. The field is aligned with us like never before. We will keep calling the right plays, execute with precision, and when we drop the ball, we’ll learn from mistakes to WIN together! I am confident we will deliver another year of amazing results!",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                    html.Br([]),
                                    html.P(
                                        "\
                                            By now, you all should have your 2021 goals created and reviewed with your Supervisor.  \
                                            You should see the daily results of your contributions \
                                            and understand the impact we, each one of us, have on our customers. \
                                            We are the Quarterbacks of this team.  The field is aligned with us like never before. \
                                            We will keep calling the right plays, execute with precision, and when we drop the ball, \
                                            we’ll learn from mistakes to WIN together! \
                                            I am confident we will deliver another year of amazing results!",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(["Operations Highlights"], className="subtitle"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["Employee Engagement Index"],
                                                        style={"color": "#515151"},
                                                    )
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                            html.Div(
                                                [
                                                    html.Br([]),
                                                    html.Strong(
                                                        [
                                                            "Highlighting the results:"
                                                        ],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "As a reminder from our last survey, EEI scores saw year-over-year boosts: 62% to 69% in engagement, \
                                                            and 53% to 77% in participation.  We committed to focus on improving the following three items. \
                                                            I’ve listed a few initiatives that should improve how we’re doing.  "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["\
                                                    The rationale behind business decisions is clear to me (50%) \
                                                    "
                                                        ],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.Br([]),
                                                    html.P(
                                                        ["\
                                                    • Rolled out this Quarterly Newsletter \
                                                    "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        ["\
                                                    • Teams channel created for each workgroup to allow employees to ask “why” decisions are made \
                                                    "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Strong(
                                                        ["\
                                                    Lumen makes it easy for me to deliver the desired customer experience (59%) \
                                                    "
                                                        ],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.Br([]),
                                                    html.P(
                                                        ["\
                                                    • Partner with the Field to ensure the best MTTI and MTTR's are offered, while minimizing the number of carryovers (3% or less each day)\
                                                    "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        ["\
                                                    • Partner with IT and upstream groups to drive quality orders\
                                                    "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Strong(
                                                        ["We're Listening:"],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.Br([]),
                                                    html.P(
                                                        ["\
                                                    • Communicating job training opportunities (mandatory training on company time versus free training opportunities on your own time)\
                                                    "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        ["\
                                                    • Sharing the internal job link through the Dispatch Operations Newsletters\
                                                    "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["Looking Ahead:"],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.Br([]),
                                                    html.P(
                                                        [
                                                            "I haven’t seen any dates on the next Employee Engagement Index Survey, however, it is usually every March. \
                                                            While this survey is not mandatory, my ask of each of you is to participate.  I would love to see our highest \
                                                            participation rate ever this time.  These are anonymous, so it’s your chance to tell us what’s on your mind. \
                                                            What’s improving and more importantly, what else do we need to do to be Amazing!  "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    
                                                ],
                                                className="nine columns",
                                            ),
                                        html.Div(
                                                [
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["Percipio"],
                                                        style={"color": "#515151"},
                                                    ),
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                        html.Div(
                                                [
                                                    html.Br([]),
                                                    html.P(
                                                        [
                                                            "Our team did a great job with the Percipio training program last year \
                                                            and we want to continue to invest in you in 2021!  The training package \
                                                            for this year will have employees complete approximately 10 hours of \
                                                            training through the Percipio platform.  We've got exciting classes in our \
                                                            program, Accountability, Customer Journey, Effective Communication, Empowerment, \
                                                            Excel, PowerPoint, OneNote, Teams, Power BI, and many more. \
                                                            Your supervisor will work to clear your schedule for a class time each month. "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                ],
                                                className="nine columns",
                                            ),
                                        html.Div(
                                                [
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["Culture Pillars"],
                                                        style={"color": "#515151"},
                                                    ),
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                        html.Div(
                                                [
                                                    html.Br([]),
                                                    html.P(
                                                        [
                                                            "We’ve been talking about having a mindset of being curious,\
                                                            analytical, invested, accountable & impactful to help us do amazing things.  \
                                                            To keep this front and center every day, we’ve created a mouse pad with our culture pillars!  \
                                                            These will be shipped to everyone in the next couple of weeks. \
                                                            Some of the ways we will do this…"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.P(
                                                        ["\
                                                    •	Just ask why!\
                                                    "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        ["\
                                                    •	Use data-driven insights to make recommendations & decisions                                                    "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        ["\
                                                    •	Invest in yourself, learn new skills, try something new by doing this you’re also investing in Lumen!                                                    "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        ["\
                                                    •	Commit to holding yourself and others accountable                                                    "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        ["\
                                                    •	Busy does not equal impact. Focus your efforts on driving a positive IMPACT & helping your team & Lumen achieve their goals!                                                    "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    #html.Br([]),
                                                    html.P(
                                                        ["\
                                                    • Sharing the internal job link through the Dispatch Operations Newsletters\
                                                    "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    
                                                ],
                                                className="nine columns",
                                            ),
                                        ],
                                        className="row",
                                        style={
                                            "background-color": "#f9f9f9",
                                            "padding-bottom": "30px",
                                        },
                                    ),
                                    html.Div(
                                                [
                                                    html.Br([]),
                                                ],
                                                className="nine columns",
                                            ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        style={"margin-bottom": "35px"},
                        className="row",
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["Accomplishments & Priorities"],
                                                        style={"color": "#515151"},
                                                    )
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                            html.Div(
                                                [
                                                    html.Br([]),
                                                    html.Strong(
                                                        [
                                                            "WFA:"
                                                        ],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.Br([]),
                                                    html.P(
                                                        ["\
                                                        344 years.  That’s the combined years of Service for the WFA Forecast team,\
                                                        a total of 21 employees and 1 contractor.  Together we watch a total of 312 \
                                                        Service Areas in Q.Field.  Although we are all working in different states, cities, \
                                                        buildings and some of us have been working from home since before it was trending,\
                                                        we have never been closer to each other. \
                                                        "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.P(
                                                        ["\
                                                        2020 brought on many challenges, not only for the world but for the creative minds. \
                                                        Forecasting, although all about numbers, is more about creativity and thinking outside \
                                                        the box than it is about making the day work.  We’ve had to think creatively when the world\
                                                        starting shutting down, How do we keep our current customers’ working, now from home,\
                                                        How do we add extra services for people who are starting to work from home, \"How do we\
                                                         keep our promises and continue to be number 1 to our customers.”  Those are questions\
                                                        that were consistently running through each of our minds, as we are losing hours for our \
                                                        technicians who needed to be elsewhere during the worse of all this.  We made it through,\
                                                        adjusting to the changes and challenges and we are stronger for it.  We have learned to\
                                                        share our tech hours with our neighboring cities and towns and sometimes outside our\
                                                        field of expertise into Click Markets.  \
                                                        2021 promises to bring on new adventures for our families, our teams and work environments.  \
                                                        Looking forward to sharing with everyone the fun we are bound to have in the upcoming year."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                ],
                                                className="nine columns",
                                            ),
                                        ],
                                        className="row",
                                        style={
                                            "background-color": "#f9f9f9",
                                            "padding-bottom": "30px",
                                        },
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        style={"margin-bottom": "35px"},
                        className="row",
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(["Happy Valentines Day!"], className="subtitle"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["From Our Team"],
                                                        style={"color": "#515151"},
                                                    )
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                            html.Div(
                                                [
                                                    html.Br([]),
                                                    html.Strong(
                                                        [
                                                            "Continuous improvement means we pursue exceptional outcomes."
                                                        ],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.Br([]),
                                                    html.Br([]),
                                                    html.P(
                                                        [
                                                            "Does this look like your normal cheesecake? Of course not. Transformation leads to amazing things! Show love and sweetness to all of those around you!"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["'Cheesecake Stuffed Strawberries (No Bake Time Saver)"],
                                                        style={"color": "#515151"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "We've included a recipe from one of our team members below....."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.Img(
                                                        src='https://i.ibb.co/CHvSDvq/Picture1.png',
                                                        className="risk-reward",
                                                    ),
                                                    html.P(
                                                        [
                                                            "These cheesecake stuffed strawberries are filled with creamy cheesecake filling and dusting of graham cracker. Yield: 10 - 12 strawberries (depending on size) Prep Time: 15 minutes Cook "
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "Total Time: 15 minutes"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "Ingredients:"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "· 1 pound large strawberries"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "· 8 ounce block cream cheese, room temperature"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "· 1/4 cup powdered sugar"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "· 1 teaspoon vanilla bean paste (or extract)"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "· Graham cracker crumbs"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.Br([]),
                                                    html.P(
                                                        [
                                                            "Directions:"
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "· Rinse strawberries and cut around the top of the strawberry, leaving a nice hole to fill the strawberry with filling."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "· If the inside of your strawberry is not hollow you can use a small knife and clean out some of the inside. If you are using large strawberries, they tend to be hollow in the middle."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "· Optional: Recommend slicing a tiny bit off the bottom of the strawberries to stand upright (like you see in the picture). They can also be laid on their side."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "· Continue until all the strawberries have been prepped."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "· After the strawberries are prepped add cream cheese, powdered sugar and vanilla bean paste to the bowl of a stand mixer."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "· Mix together until smooth and fully combined."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "· Add mixture to a piping bag and fill the inside of the strawberries until the filling reaches the top of the strawberry."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "· Dip the top of the strawberry in graham cracker crumbs."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "· These are best tasting the day they are made."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                    html.P(
                                                        [
                                                            "· Optional: Feel free to add mix-ins to the cream cheese - lemon zest, flavored extract or even mini-chocolate chips. You could even dip them in chocolate after if you want more flavor."
                                                        ],
                                                        style={"color": "#7a7a7a"},
                                                    ),
                                                ],
                                                className="nine columns",
                                            ),
                                        ],
                                        className="row",
                                        style={
                                            "background-color": "#f9f9f9",
                                            "padding-bottom": "30px",
                                        },
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.H6(["Recognition"], className="subtitle"),
                                            html.Br([]),

                                            html.Div(
                                                [
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["New Hires"],
                                                        style={"color": "#515151"},
                                                    )
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                            html.Div(
                                    [
                                        html.Table(make_dash_table(df_fund_facts)),
                                    ],
                                    
                                    className="six columns",
                                ),
                            
                                            html.Div(
                                                [
                                                    html.Br([]),
                                                    
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                        ],
                                        className="row",
                                        style={
                                            "background-color": "#f9f9f9",
                                            "padding-bottom": "30px",
                                        },
                                    ),
                                ],
                                className="twelve columns",
                        )
                    ],
                    className="row",
                ),
                # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.H6([""], className="subtitle"),
                                            html.Br([]),

                                            html.Div(
                                                [
                                                    html.Br([]),
                                                    html.Strong(
                                                        ["Q1 Service Anniversaries"],
                                                        style={"color": "#515151"},
                                                    )
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                            html.Div(
                                    [
                                        html.Table(make_dash_table(df_price_perf)),
                                    ],
                                    
                                    className="six columns",
                                ),
                            
                                            html.Div(
                                                [
                                                    html.Br([]),
                                                    
                                                ],
                                                className="three columns right-aligned",
                                            ),
                                        ],
                                        className="row",
                                        style={
                                            "background-color": "#f9f9f9",
                                            "padding-bottom": "30px",
                                        },
                                    ),
                                ],
                                className="twelve columns",
                        )
                    ],
                    className="row",
                ),
            ],
            className="sub_page",
        ),
    ],
    className="page",
)
