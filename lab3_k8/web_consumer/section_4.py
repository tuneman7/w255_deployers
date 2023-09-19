from includes import *
from flask import Blueprint

section_4 = Blueprint('section_4', __name__)

from libraries.data_objects import data_objects as do
from libraries.mortgage_amort import Affordability as af

@section_4.route('/section_four', methods=['POST', 'GET'])
def section_four():

        res = jsonify({'htmlresponse':render_template('pages/section_content/placeholder.affordability_calc.html',)})
                
        return res

        # myaf = af()

        # form = monthly_allocation_form()
        # print(request.method)
        # if request.method == 'POST':

        #         form = monthly_allocation_form(request.form)
        #         interest_rate = float(request.form["interest_rates"].strip())
        #         downpayment_amount = float(request.form["downpayment_amt"].strip())
        #         monthly_allocation = int(request.form["monthly_allocation"].strip())
        #         print("downpayment_amount=",downpayment_amount)
        #         print("interest_rate=",interest_rate)
        #         returner= myaf.how_much_can_i_afford(monthly_allocation=monthly_allocation,
        #         down_payment_pct=downpayment_amount,
        #         interest_rate=interest_rate)

        #         print("loan_amount=",returner[1])
        #         print("monthly_allocation=",returner[2])

        #         chart_json = returner[0].configure_view(
        #             strokeWidth=0
        #         ).to_json()

        #         res = jsonify({'htmlresponse':render_template('pages/section_content/placeholder.affordability_calc.html',
        #                 form=form,
        #                 current_monthly_allocation=monthly_allocation,
        #                 current_downpayment_amount=downpayment_amount,
        #                 current_interest_rate=interest_rate,
        #                 chart_json=chart_json,)})
                        
        #         return res

        # else:
        # #print(form.monthly_allocation)
        # #print(tuple(mdo.interest_rate_tuple()))
        #         chart_json= myaf.how_much_can_i_afford(monthly_allocation=1000)[0].configure_view(
        #             strokeWidth=0
        #         ).to_json()

        #         res = make_response(render_template('pages/section_content/placeholder.affordability_calc.html',
        #                 form=form,
        #                 current_monthly_allocation="1000",
        #                 current_downpayment_amount="0.2",
        #                 current_interest_rate="0.065",
        #                 chart_json=chart_json,))

        #         return res

@section_4.route('/section_four_graph', methods=['POST', 'GET'])
def section_four_graph():
        myaf=af()
        form = monthly_allocation_form(request.form)
        interest_rate = float(request.form["interest_rates"].strip())
        downpayment_amount = float(request.form["downpayment_amt"].strip())
        monthly_allocation = int(request.form["monthly_allocation"].strip())
        current_loan_term = int(request.form["loan_term"].strip())
        print("downpayment_amount=",downpayment_amount)
        print("interest_rate=",interest_rate)
        print("monthly_allocation=",monthly_allocation)
        returner= myaf.how_much_can_i_afford(monthly_allocation=monthly_allocation,
        down_payment_pct=downpayment_amount,
        interest_rate=interest_rate,input_years=current_loan_term)

        # the method above This method returns these objects.
        #altair_object, line_graph, loan_amt, monthly_allocation, input_loan, down_payment_amount, down_payment_pct, interest_rate , amortization_schedule , output_string

        chart_json = returner[0].configure_view(
                strokeWidth=0
        ).to_json()

        chart_json1 = returner[1].configure_view(
                strokeWidth=0
        ).to_json()

        house_price = returner[4] 
        house_price = "${:,} ".format(house_price)

        amortization_schedule = returner[8]
        amortization_schedule["cume_interest"]= amortization_schedule["interest"].cumsum()
        amortization_schedule["cume_principal"]= amortization_schedule["principal"].cumsum()

        loan_cumulative_interest        = amortization_schedule["cumulative_interest"][0] 
        loan_cumulative_principal       = amortization_schedule["opening_balance"][0] 

        total_repayment_amt = loan_cumulative_interest + loan_cumulative_principal

        loan_cumulative_interest = "${:,}".format(round(loan_cumulative_interest))
        loan_cumulative_principal = "${:,}".format(round(loan_cumulative_principal))
        total_repayment_amt = "${:,}".format(round(total_repayment_amt))



        #Clean up the data.
        amortization_schedule.loc[:, "opening_balance"] ='$'+ amortization_schedule["opening_balance"].map('{:,.0f}'.format)
        amortization_schedule.loc[:, "interest"] ='$'+ amortization_schedule["interest"].map('{:,.0f}'.format)
        amortization_schedule.loc[:, "principal"] ='$'+ amortization_schedule["principal"].map('{:,.0f}'.format)
        amortization_schedule.loc[:, "period_payment"] ='$'+ amortization_schedule["period_payment"].map('{:,.0f}'.format)
        amortization_schedule.loc[:, "closing_balance"] ='$'+ amortization_schedule["closing_balance"].map('{:,.0f}'.format)
        amortization_schedule.loc[:, "cumulative_interest"] ='$'+ amortization_schedule["cumulative_interest"].map('{:,.0f}'.format)
        amortization_schedule.loc[:, "cume_interest"] ='$'+ amortization_schedule["cume_interest"].map('{:,.0f}'.format)
        amortization_schedule.loc[:, "cume_principal"] ='$'+ amortization_schedule["cume_principal"].map('{:,.0f}'.format)

        #Give it nice column names.
        amortization_schedule.columns = ["Period","Opening Principal","Period Interest", "Period Principal","Period Payment","Closing Principal","Interest Balance","Cume Interest","Cume Principal"]

        #Oranize it well.
        amortization_schedule=amortization_schedule.iloc[:,[0,4,3,2,7,8,1,5,6]]

        # dataset.columns = ["County","Date","Med List Price","30 Yr Int Rate","30 Yr Int Rate (5lag)","Active Listings"]

        #print(amortization_schedule)
        
        res = jsonify({'htmlresponse':render_template('modal/affordability.modal.html',
                form=form,
                current_monthly_allocation=monthly_allocation,
                current_downpayment_amount=downpayment_amount,
                current_interest_rate=interest_rate,
                loan_cumulative_interest = loan_cumulative_interest,
                loan_cumulative_principal = loan_cumulative_principal,
                total_repayment_amt = total_repayment_amt,
                current_loan_term=current_loan_term,
                chart_json1=chart_json1,
                house_price=house_price,
                chart_json=chart_json,
                tables=[amortization_schedule.to_html()],titles=[''])})
                
        return res
