import React, { Component } from "react";
import "./Formbuilder.css";

export default class Formbuilder extends Component {
  render() {
    return (
      <>
        <h1 className="heading">Build a beneficiary data collection form</h1>
        <div className="firstdata">
          <h1 className="mand">Mandatory</h1>
          <div className="col1">
            <p className="field1">Personal Information</p>
            <p className="dd1">Basic details, Occupation, Contact, Address</p>
          </div>

          <div className="col2">
            <p className="field1">Education History</p>
            <p className="dd1">
              Eduvcation status,school,college,Highest degree/class
            </p>
          </div>
          <div className="col3">
            <p className="field1">Financial Information</p>
            <p className="dd1">Income Details,Bank Details</p>
          </div>
          <div className="col4">
            <p className="field1">Other Details</p>
            <p className="dd1">Id image,self image,Reference image</p>
          </div>
        </div>
        <div className="secnddata">
          <h1 className="mand">Custom</h1>
          <div className="col1">
            <p className="field1">Health</p>
            <p className="dd1">Family health,personal health</p>
          </div>

          <div className="col2">
            <p className="field1">Asset Ownership</p>
            <p className="dd1">White goods,vehichle,land</p>
          </div>
          <div className="col3">
            <p className="field1">Access to Services</p>
            <p className="dd1">Electricity,data gas,water</p>
          </div>
          <div className="col5">
            <p className="field1">Other Details</p>
          </div>
        </div>
      </>
    );
  }
}
