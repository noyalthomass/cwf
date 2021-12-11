import React from 'react'
import './Reporting.css'

function Reporting() {
    return (
        <>
          <div className='main'>
              <p className='reporting'>Reporting</p>
              <p className='email'>Email</p>
              <div className='box'>
              <div className='export_main'><p className='export'>Export</p></div>
              </div>
              <div className='milestone'>
                    <p className='miles'>MILESTONE</p>
              </div>
              <div className='budget'><p className='budget_sub'>BUDGET</p></div>
              <div className='metrics'><p className='metrics_sub'>METRICS</p></div>
              </div>  
              <div className='sub'>
                <div>
                    <div className='box1'>
                        
                        <div className='updates'>Milestone Updates</div>
                        <div className='subbox1'>
                        <div className='machine'>Machine8</div>
                        <div className='slicer'>Slicer BH100</div>
                        <div className='machine2'>Machine2</div>
                        <div className='packer'>Packer 5000</div>
                        <div className='bobst'>BOBST</div>
                        <div className='roto'>Roto...</div>
                        <div className='ma'>Ma...</div></div>
                        <div className='last'>Last 30 Days</div><div className='view'>View milestone</div>
                    </div>
                    
                    <div className='box2'>
                      <div className='primary'><p className="sub_primary">Primary Metrics</p></div>
                      <div><div className='value'>value</div></div>
                      
                    </div>
                    </div>
              </div>
              <div className='sub2'>
                <div><div className='box3'></div><div className='box4'></div></div>
              </div>

        </>
    )
}

export default Reporting

