import React, {useState, useEffect,Component} from 'react'
import {Link} from 'react-router-dom'
import $ from 'jquery'
import axios from 'axios'
import fondo from '../Images/background.jpg'

import Card from './Card'



class Home extends Component{
    
    
    state = {
        listado : []
    }


    actualizarListado () {
            axios.get('http://localhost:5000/obtenerListado').then((res) => {                       
            this.setState({listado : res.data})
            console.log(this.state.listado)
         })
         .catch((error) =>{
         console.log(error);
         })                
                
        }

   

    componentDidMount(){
        this.actualizarListado()
    }

     style = {
        backgroundImage: `url(${fondo})`,
        backgroundSize:'100% 100%',
       overflowY:'hidden',
       overflowX:'hidden'
    }


    
    render(){        
        
        return(
            
            <div style={this.style}>
                
                <div align ="center">

                              
                <div className="grillita" >  
                <div className="row row-cols-1 row-cols-md-3" >       
               {this.state.listado.map(list => (
                   
                   <Card
                   list = {list}
                   />
                   
               ))}
               </div>
               
               </div>
               </div>                 
            </div>
        )
    }

// function Home(){

//     const [listado,setListado] = useState (null);
    

//     //Peticion get para los episodios

//     const actualizarListado = () => {
//         axios.get('http://127.0.0.1:5000/obtenerListado').then((res) => {
//           console.log(res.data)
//           setListado(res.data)
          
//         })
//         .catch((error) =>{
//             console.log(error);
//         })
        
        
//     }
    
    

//     useEffect(() => {
//         actualizarListado();
//     }, [])

    
//     return(
//         <div className="home">
//             <h1 align="center">Episodios "The Mandalorian"</h1>

           
            
            
//         </div>
//     )
// }
}
export default Home;