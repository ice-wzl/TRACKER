import sys 
import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from DAL.addcampaignDAL import *
from DAL.addimplantDAL import *
from DAL.addlocationDAL import *
from DAL.addtargetDAL import *
from DAL.adddeploymentDAL import *
from DAL.getdeploymentDAL import *

from BLL.addcampaign import *
from BLL.addimplant import *
from BLL.addlocation import *
from BLL.addtarget import *
from BLL.adddeployment import *
from BLL.getdeployment import *


app = Flask(__name__)
    

app.secret_key = 'a_very_secret_key'  


@app.route("/", methods=['GET'])
def index():
    deployment_bll = GetDeployment(None, None, None, None, None, None, None)
    
    # Fetch all deployments via the business logic layer
    try:
        entries = deployment_bll.get_all()
    except Exception as e:
        return jsonify({"error": f"Failed to fetch deployments: {str(e)}"}), 500

    # Render the index.html with the fetched entries
    return render_template('index.html', entries=entries)


@app.route('/add_deployment', methods=['GET', 'POST'])
def add_deployment():
    deployment_bll = AddDeployment()  # Create an instance of the business logic class

    if request.method == 'POST':
        # Extract data from the form
        install_date = request.form.get('install_date')
        kill_date = request.form.get('kill_date')
        persistant = request.form.get('persistant')
        poc = request.form.get('poc')
        ip_address = request.form.get('ip_address')
        implant_port = request.form.get('implant_port')
        target_name = request.form.get('target_name')
        campaign_id = request.form.get('campaign_id')
        location_id = request.form.get('location_id')
        implant_type_id = request.form.get('implant_type_id')

        # convert entity name to id for database processing
        print(target_name)
        target_id = deployment_bll.convert_name_id(target_name)
        print(target_id)

        # Use the BLL class to add the deployment
        result = deployment_bll.add(
            install_date, kill_date, persistant, poc, ip_address, implant_port, target_id, campaign_id, location_id, implant_type_id
        )

        if result:
            flash("Deployment added successfully!", "success")
        else:
            flash("Failed to add deployment.", "error")

        return redirect(url_for('add_deployment'))

    # Fetch all deployments to display on the page
    try:
        entries = deployment_bll.get_deployment()
    except Exception as e:
        return jsonify({"error": f"Error retrieving deployments: {str(e)}"}), 500

    return render_template('add_deployment.html', entries=entries)


@app.route('/add_location', methods=['GET', 'POST'])
def add_location():
    location_bll = AddLocation()

    if request.method == 'POST':
        state = request.form.get('state')
        country = request.form.get('country')

        # Use the BLL class to add the location
        result = location_bll.add_location(state, country)

        if result:
            flash("Location added successfully!", "success")
        else:
            flash("Failed to add location.", "error")

        return redirect(url_for('add_location'))

    try:
        entries = location_bll.get_all()
    except Exception as e:
        return jsonify({"error": f"Error retrieving locations: {str(e)}"}), 500

    return render_template('add_location.html', entries=entries)


@app.route('/add_implant', methods=['GET', 'POST'])
def add_implant():
    implant_bll = AddImplant()
    if request.method == 'POST':
        implant_name = request.form.get('implant_name')
        implant_version = request.form.get('implant_version')
        implant_type = request.form.get('implant_type')
        result = implant_bll.add_implant(implant_name, implant_version, implant_type)
        if result:
            flash("Implant added successfully!", "success")
        else:
            flash("Failed to add implant.", "error")
        return redirect(url_for('add_implant'))
    try:
        entries = implant_bll.get_all()
    except Exception as e:
        return jsonify({"error": f"Error retrieving implants: {str(e)}"}), 500
    return render_template('add_implant.html', entries=entries)


@app.route('/add_campaign', methods=['GET', 'POST'])
def add_campaign():
    campaign_bll = AddCampaign()
    if request.method == 'POST':
        name = request.form.get('name')
        result = campaign_bll.add_campaign(name)
        if result:
            flash("Campaign added successfully!", "success")
        else:
            flash("Failed to add campaign.", "error")
        return redirect(url_for('add_campaign'))
    try:
        entries = campaign_bll.get_all()
    except Exception as e:
        return jsonify({"error": f"Error retrieving campaigns: {str(e)}"}), 500
    return render_template('add_campaign.html', entries=entries)


@app.route('/add_target', methods=['GET', 'POST'])
def add_target():
    target_bll = AddTarget()
    if request.method == 'POST':
        form_type = request.form.get('form_type')  # Identify which form was submitted

        if form_type == 'add':
            name = request.form.get('name')
            ip_address = request.form.get('ip_address')
            mac_address = request.form.get('mac_address')
            campaign_id = request.form.get('campaign_id')
            result = target_bll.add_target(name, ip_address, mac_address, campaign_id)
            if result:
                flash("Target added successfully!", "success")
            else:
                flash("Failed to add target.", "error")
            return redirect(url_for('add_target'))
        elif form_type == 'search':
            target_name = request.form.get('target_name')
            result = target_bll.search_target(target_name)
            if result:
                flash("Entity search results below", "success")
            else:
                flash(f"Failed to find any entity {target_name}", "error")
            return render_template('add_target.html', entries=result)
        elif form_type == 'update':
            name = request.form.get('name')
            ip_address = request.form.get('ip_address')
            mac_address = request.form.get('mac_address')
            campaign_id = request.form.get('campaign_id')
            result = target_bll.update_target(name, ip_address, mac_address, campaign_id)
            if result:
                flash("Target updated successfully!", "success")
            else:
                flash("Failed to update target", "error")
            return redirect(url_for('add_target'))
    elif request.method == "GET":       
        try:
            entries = target_bll.get_all()
        except Exception as e:
            return jsonify({"error": f"Error retrieving targets: {str(e)}"}), 500
        return render_template('add_target.html', entries=entries)
    

@app.teardown_appcontext
def close_connection(exception):
    location_bll = AddLocation()
    location_bll.close()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8081)
